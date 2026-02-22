#!/usr/bin/env python3
"""
GSoC 2026 Organization & Project Ideas Scraper
================================================
Uses the GSoC public API to get all organizations, then fetches
each org's project ideas page and dumps the content.

Requirements:
    pip install requests beautifulsoup4 trafilatura
    pip install markdownify          # optional, improves fallback quality
    pip install playwright           # for --use-browser
    playwright install chromium      # for --use-browser

Usage:
    # Full run (HTTP only):
    python scraper.py

    # Full run with Playwright for JS-rendered pages:
    python scraper.py --use-browser

    # Scrape a single URL and print markdown:
    python scraper.py --url https://example.com/ideas
    python scraper.py --url https://example.com/ideas --use-browser

    # Step-by-step:
    python scraper.py --step orgs          # fetch org list only
    python scraper.py --step ideas         # fetch ideas (uses cached org list)

    # Filter / limit:
    python scraper.py --max-orgs 5         # test with 5 orgs
    python scraper.py --tech python        # only Python orgs
    python scraper.py --org jenkins        # only scrape matching org(s)

    # Sub-page options:
    python scraper.py --no-subpages        # skip fetching linked sub-pages
    python scraper.py --max-subpages 10    # limit sub-pages per org (0 = unlimited)
"""

import argparse
import asyncio
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime
from typing import Optional
from urllib.parse import urlparse, urljoin, quote, parse_qs

import requests
import trafilatura
from bs4 import BeautifulSoup

try:
    from markdownify import markdownify as md
    HAS_MARKDOWNIFY = True
except ImportError:
    HAS_MARKDOWNIFY = False

# ─── Config ───────────────────────────────────────────────────────────────
GSOC_API_URL = "https://summerofcode.withgoogle.com/api/program/2026/organizations/"
OUTPUT_DIR = Path(__file__).resolve().parent.parent
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}
REQUEST_DELAY = 1.0   # seconds between requests (be polite)
MAX_RETRIES = 2       # retry failed HTTP requests
RETRY_BACKOFF = 3.0   # seconds to wait before retry (doubles each attempt)
BROWSER_CONCURRENCY = 3  # parallel browser tabs


# ─── Retry helper ─────────────────────────────────────────────────────────
def fetch_with_retry(url: str, timeout: int = 15, **kwargs) -> Optional[requests.Response]:
    """Fetch a URL with retry and exponential backoff."""
    backoff = RETRY_BACKOFF
    for attempt in range(MAX_RETRIES + 1):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=timeout,
                                allow_redirects=True, **kwargs)
            resp.raise_for_status()
            return resp
        except Exception as e:
            if attempt < MAX_RETRIES:
                print(f"    Retry {attempt + 1}/{MAX_RETRIES} in {backoff:.0f}s... ({e})")
                time.sleep(backoff)
                backoff *= 2
            else:
                print(f"    Failed after {MAX_RETRIES + 1} attempts: {e}")
                return None


# ─── URL classification & markdown helpers ─────────────────────────────────
def classify_url(url: str) -> tuple:
    """
    Classify a URL and return (strategy, transformed_url).

    Strategies:
      - "github_raw": GitHub blob URL -> raw.githubusercontent.com
      - "github_wiki_raw": GitHub wiki URL -> raw wiki content
      - "gist_raw": GitHub gist -> raw gist content
      - "google_doc": Google Docs URL -> export URL
      - "github_issues": GitHub issues URL -> use gh CLI
      - "gitlab_raw": GitLab blob URL -> raw URL
      - "gitlab_issues": GitLab issues URL -> use API
      - "generic": Use trafilatura for HTML-to-markdown extraction
    """
    parsed = urlparse(url)

    # ── Google Docs ──
    if parsed.netloc == "docs.google.com" and "/document/d/" in parsed.path:
        m = re.search(r"/document/d/([a-zA-Z0-9_-]+)", parsed.path)
        if m:
            doc_id = m.group(1)
            export_url = f"https://docs.google.com/document/d/{doc_id}/export?format=html"
            return ("google_doc", export_url)

    # ── GitHub ──
    if parsed.netloc == "github.com":
        path_parts = parsed.path.strip("/").split("/")

        # Blob URLs: github.com/{owner}/{repo}/blob/{branch}/{path}
        if len(path_parts) >= 5 and path_parts[2] == "blob":
            owner = path_parts[0]
            repo = path_parts[1]
            branch = path_parts[3]
            file_path = "/".join(path_parts[4:])
            raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{file_path}"
            return ("github_raw", raw_url)

        # Wiki URLs: github.com/{owner}/{repo}/wiki/{page}
        if len(path_parts) >= 3 and path_parts[2] == "wiki":
            page = path_parts[3] if len(path_parts) > 3 else "Home"
            owner = path_parts[0]
            repo = path_parts[1]
            raw_url = f"https://raw.githubusercontent.com/wiki/{owner}/{repo}/{page}.md"
            return ("github_wiki_raw", raw_url)

        # Issues URLs: github.com/{owner}/{repo}/issues
        if len(path_parts) >= 3 and path_parts[2] == "issues":
            return ("github_issues", url)

    # ── Gists ──
    if parsed.netloc == "gist.github.com":
        raw_url = f"https://gist.githubusercontent.com{parsed.path}/raw"
        return ("gist_raw", raw_url)

    # ── GitLab ──
    if "gitlab" in parsed.netloc:
        if "/-/blob/" in parsed.path:
            raw_url = url.replace("/-/blob/", "/-/raw/")
            return ("gitlab_raw", raw_url)
        if "/-/issues" in parsed.path:
            return ("gitlab_issues", url)

    return ("generic", url)


# ─── Content quality validation ──────────────────────────────────────────

# Patterns that indicate the scraped content is not real page content.
# Each tuple is (pattern, label) — label is used for logging.
_GARBAGE_PATTERNS: list[tuple[re.Pattern, str]] = [
    # Anti-bot / challenge pages
    (re.compile(r"making sure you.re not a bot", re.I), "anti-bot challenge"),
    (re.compile(r"please wait.*while we (ensure|verify)", re.I), "anti-bot challenge"),
    (re.compile(r"checking (if the site connection is secure|your browser)", re.I), "anti-bot challenge"),
    (re.compile(r"proof.of.work", re.I), "anti-bot challenge"),
    (re.compile(r"please (enable|allow) (javascript|cookies)", re.I), "anti-bot challenge"),
    (re.compile(r"anubis.*protect the server", re.I), "anti-bot challenge"),
    (re.compile(r"verify you are human", re.I), "anti-bot challenge"),
    (re.compile(r"cloudflare.*ray id", re.I), "cloudflare challenge"),
    (re.compile(r"just a moment\.\.\.", re.I), "cloudflare challenge"),
    # Auth walls (allow whitespace/newlines between words)
    (re.compile(r"sign\s+in\s+to\s+continue", re.I | re.S), "auth wall"),
    (re.compile(r"log\s+in\s+to\s+(continue|access|your account)", re.I | re.S), "auth wall"),
    (re.compile(r"you need to (sign in|log in)", re.I), "auth wall"),
    (re.compile(r"^#?\s*sign in\s*$", re.I | re.M), "auth wall"),
    # CMS UI chrome (scraped toolbar/menu instead of content)
    (re.compile(r"(Bearbeiten|Bedienungshilfen|Dokumentenstruktur)", re.I), "CMS UI chrome"),
    (re.compile(r"Druckvorschau.*Seiteneinrichtung", re.I | re.S), "CMS UI chrome"),
    # Generic error pages
    (re.compile(r"^404\s*[-–—]?\s*(page|file)?\s*not found", re.I | re.M), "404 page"),
]


def is_valid_content(text: str, min_chars: int = 100) -> tuple[bool, str]:
    """Check if scraped content is real page content, not garbage.

    Returns (is_valid, reason). If invalid, reason describes why.
    """
    if not text or len(text.strip()) < min_chars:
        return False, "too short"

    for pattern, label in _GARBAGE_PATTERNS:
        if pattern.search(text[:2000]):  # only check the beginning
            return False, label

    return True, "ok"


# ─── Markdown link resolution & sub-page helpers ─────────────────────────

# Regex matching markdown links [text](url) but not images ![text](url)
_MD_LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)")

# File extensions for non-content resources (skip during sub-page fetch)
_NON_CONTENT_EXTENSIONS = frozenset({
    # Images
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico", ".bmp", ".tiff",
    # Media
    ".mp4", ".webm", ".mp3", ".wav", ".ogg", ".avi", ".mov",
    # Archives / binaries
    ".pdf", ".zip", ".tar", ".gz", ".bz2", ".xz", ".7z", ".rar",
    ".exe", ".dmg", ".deb", ".rpm", ".msi", ".appimage",
    # Source code (not documentation)
    ".c", ".h", ".cpp", ".hpp", ".cc", ".cxx", ".hh",
    ".py", ".pyc", ".pyo", ".pyx",
    ".js", ".ts", ".jsx", ".tsx", ".mjs", ".cjs",
    ".java", ".kt", ".kts", ".scala", ".groovy",
    ".go", ".rs", ".swift", ".m", ".mm",
    ".rb", ".php", ".pl", ".pm", ".lua", ".r",
    ".cs", ".fs", ".vb",
    ".sh", ".bash", ".zsh", ".fish", ".bat", ".ps1", ".cmd",
    ".sql", ".graphql", ".proto",
    ".css", ".scss", ".sass", ".less", ".styl",
    # Config / data files
    ".xml", ".xsl", ".xsd", ".dtd",
    ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf",
    ".cmake", ".makefile", ".gradle", ".sbt",
    ".lock", ".sum", ".mod",
    # Patches / diffs
    ".patch", ".diff",
})

# Filename patterns that are not documentation even without extensions
_NON_CONTENT_FILENAMES = frozenset({
    "cmakelists.txt", "makefile", "dockerfile", "vagrantfile",
    "gemfile", "rakefile", "procfile", ".gitignore", ".gitattributes",
    ".editorconfig", ".eslintrc", ".prettierrc",
})

# Query-string actions that indicate CMS admin/edit pages, not content
_SKIP_QUERY_ACTIONS = frozenset({
    "edit", "delete", "history", "raw", "submit", "purge", "protect",
    "unprotect", "watch", "unwatch", "render", "markpatrolled",
})

# Path segments that indicate non-content pages
_SKIP_PATH_SEGMENTS = frozenset({
    # Auth / account
    "login", "signin", "sign_in", "signup", "sign_up", "register",
    "logout", "sign_out", "oauth", "auth", "sso",
    "settings", "profile", "account",
    # Infra
    "cdn-cgi", "api", "raw", "assets", "static",
    # VCS internals
    "commit", "commits", "compare", "blame", "graphs", "network",
    "stargazers", "watchers", "forks", "contributors",
    # CI/CD
    "actions", "workflows", "runs", "checks", "pipelines",
    # Releases / packages
    "releases", "tags", "packages",
})

# Trailing path patterns that indicate non-content pages (e.g. wiki _history)
_SKIP_PATH_SUFFIXES = frozenset({
    "_history", "_edit", "_new", "_delete",
})


def is_relative_link(href: str) -> bool:
    """Check if a link is a relative path (not absolute, not anchor, not mailto)."""
    if not href:
        return False
    if href.startswith(("#", "http://", "https://", "//", "mailto:")):
        return False
    if re.match(r"^\./https?://", href):
        return False
    return True


def generate_subpage_slug(href: str, base_url: str = "") -> str:
    """Generate a URL-safe slug from a link path.

    For relative links, uses the href directly. For absolute links,
    extracts the path portion relative to the base URL.
    """
    if href.startswith(("http://", "https://", "//")):
        href_path = urlparse(href).path.strip("/")
        if base_url:
            base_path = urlparse(base_url).path.strip("/")
            if href_path.startswith(base_path + "/"):
                href_path = href_path[len(base_path) + 1:]
            elif "/" in base_path:
                parent = base_path.rsplit("/", 1)[0]
                if href_path.startswith(parent + "/"):
                    href_path = href_path[len(parent) + 1:]
        raw = href_path or urlparse(href).path.strip("/").split("/")[-1]
    else:
        raw = re.sub(r"^\./", "", href)

    raw = raw.split("#")[0].split("?")[0]
    raw = re.sub(r"\.(md|html|htm|txt|rst|wiki)$", "", raw, flags=re.IGNORECASE)
    slug = re.sub(r"[^\w]+", "-", raw).strip("-").lower()
    return slug[:80] or "subpage"


def deduplicate_slug(slug: str, seen: dict[str, int]) -> str:
    """Return a unique slug, appending -2, -3, etc. on collision."""
    if slug not in seen:
        seen[slug] = 1
        return slug
    seen[slug] += 1
    return f"{slug}-{seen[slug]}"


def resolve_markdown_links(content: str, base_url: str) -> str:
    """Resolve relative URLs in markdown links [text](url) against a base URL.

    Skips anchors (#...), already-absolute URLs, and mailto: links.
    Handles the malformed ./https:// pattern.
    """
    def _resolve(match: re.Match) -> str:
        text = match.group(1)
        href = match.group(2)

        if href.startswith(("#", "http://", "https://", "//", "mailto:")):
            return match.group(0)

        # Handle malformed ./https://... or ./http://... pattern
        cleaned = re.sub(r"^\./https?://", lambda m: m.group(0)[2:], href)
        if cleaned != href:
            return f"[{text}]({cleaned})"

        resolved = urljoin(base_url, href)
        return f"[{text}]({resolved})"

    return _MD_LINK_RE.sub(_resolve, content)


def extract_markdown_links(content: str) -> list[tuple[str, str]]:
    """Extract all markdown links as (text, url) pairs, excluding images."""
    return _MD_LINK_RE.findall(content)


def is_fetchable_subpage(href: str, base_url: str) -> bool:
    """Check if a link is a fetchable documentation sub-page on the same domain."""
    if not href or href.startswith(("#", "mailto:")):
        return False

    base_parsed = urlparse(base_url)
    resolved = urljoin(base_url, href)
    resolved_parsed = urlparse(resolved)

    # Must be same domain
    if resolved_parsed.netloc != base_parsed.netloc:
        return False

    # Skip root/homepage links (path is "/" or empty)
    if resolved_parsed.path.strip("/") == "":
        return False

    # Skip self-links
    if resolved_parsed.path == base_parsed.path:
        return False

    path_lower = resolved_parsed.path.lower()
    path_segments = [s for s in path_lower.split("/") if s]

    # Skip URLs with email addresses in path (e.g. misresolved mailto:)
    if "@" in resolved_parsed.path:
        return False

    # Skip non-content path segments (login, auth, VCS, CI, etc.)
    if _SKIP_PATH_SEGMENTS & set(path_segments):
        return False

    # Skip trailing path patterns (wiki _history, _edit, etc.)
    last_segment = path_segments[-1] if path_segments else ""
    if any(last_segment.endswith(suffix) for suffix in _SKIP_PATH_SUFFIXES):
        return False

    # Skip CMS action pages (edit, delete, history, etc.)
    query_params = parse_qs(resolved_parsed.query)
    action_values = {v.lower() for vals in query_params.get("action", []) for v in vals.split(",")}
    if action_values & _SKIP_QUERY_ACTIONS:
        return False

    # Skip non-content file extensions
    if any(path_lower.endswith(ext) for ext in _NON_CONTENT_EXTENSIONS):
        return False

    # Skip known non-documentation filenames
    if last_segment.lower() in _NON_CONTENT_FILENAMES:
        return False

    # ── Git forge heuristics (GitHub, GitLab, Gitea, etc.) ──

    is_github = base_parsed.netloc == "github.com"
    is_gitlab = "gitlab" in base_parsed.netloc

    if is_github or is_gitlab:
        # Must be same owner/repo (at least 2 common path segments)
        base_parts = base_parsed.path.strip("/").split("/")
        resolved_parts = resolved_parsed.path.strip("/").split("/")
        if len(base_parts) >= 2 and len(resolved_parts) >= 2:
            if base_parts[:2] != resolved_parts[:2]:
                return False

        # Skip user/org profile pages (github.com/username — only 1 segment)
        if len(resolved_parts) < 2:
            return False

        # Skip directory listings (/tree/) — they return just file names
        if "tree" in resolved_parts:
            return False

        # Skip pull requests (often huge diffs)
        if "pull" in resolved_parts or "pulls" in resolved_parts:
            return False

        # Skip source code blobs unless they are documentation files
        if "blob" in resolved_parts:
            doc_extensions = {".md", ".rst", ".txt", ".adoc", ".wiki", ".html", ".htm"}
            if not any(path_lower.endswith(ext) for ext in doc_extensions):
                return False

    return True


def extract_and_fetch_subpages(
    content: str,
    base_url: str,
    org_slug: str,
    max_subpages: int = 0,
) -> tuple[str, list[dict]]:
    """Extract same-domain links, fetch sub-pages, rewrite links in main content.

    Fetches both relative links and absolute same-domain links (indicating
    related content within the same site). Returns the rewritten main content
    and a list of sub-page dicts with keys: slug, title, source_url, content.

    Set max_subpages to 0 for unlimited (default).
    """
    links = extract_markdown_links(content)

    # Identify same-domain links that are fetchable
    seen_urls: set[str] = set()
    seen_slugs: dict[str, int] = {}
    # Maps original href -> (slug, title, resolved_url)
    subpage_map: dict[str, tuple[str, str, str]] = {}

    for text, href in links:
        if not href or href.startswith(("#", "mailto:")):
            continue
        resolved = urljoin(base_url, href)
        if not is_fetchable_subpage(resolved, base_url):
            continue
        normalized = urlparse(resolved)._replace(fragment="").geturl()
        if normalized in seen_urls:
            continue
        seen_urls.add(normalized)

        slug = deduplicate_slug(generate_subpage_slug(href, base_url), seen_slugs)
        title = text.strip() or slug
        subpage_map[href] = (slug, title, normalized)

    if not subpage_map:
        # No sub-pages found, still resolve remaining relative links
        rewritten = resolve_markdown_links(content, base_url)
        return rewritten, []

    items = list(subpage_map.values())
    if max_subpages > 0 and len(items) > max_subpages:
        print(f"    Limiting sub-pages from {len(items)} to {max_subpages}")
        items = items[:max_subpages]
        # Trim subpage_map to match
        allowed_slugs = {slug for slug, _, _ in items}
        subpage_map = {
            href: v for href, v in subpage_map.items() if v[0] in allowed_slugs
        }

    print(f"    Found {len(items)} relative sub-pages to fetch")

    # Fetch sub-pages
    subpages: list[dict] = []
    fetched_count = 0

    for slug, title, sub_url in items:
        print(f"      Sub-page: {title} ({sub_url})")

        sub_content = fetch_ideas_simple(sub_url)
        if sub_content:
            sub_content = resolve_markdown_links(sub_content, sub_url)
            subpages.append({
                "slug": slug,
                "title": title,
                "source_url": sub_url,
                "content": sub_content,
            })
            fetched_count += 1
            print(f"      OK ({len(sub_content)} chars)")
        else:
            # Remove from map so link won't be rewritten to internal route
            for href, v in list(subpage_map.items()):
                if v[0] == slug:
                    del subpage_map[href]
                    break
            print(f"      FAILED: no content extracted")

        time.sleep(REQUEST_DELAY)

    print(f"    Sub-pages: {fetched_count}/{len(items)} fetched")

    # Build set of successfully fetched slugs
    fetched_slugs = {sp["slug"] for sp in subpages}

    # Rewrite main content: relative links to sub-pages become internal routes,
    # other relative links become absolute
    def _rewrite(match: re.Match) -> str:
        text = match.group(1)
        href = match.group(2)

        if href in subpage_map and subpage_map[href][0] in fetched_slugs:
            slug = subpage_map[href][0]
            return f"[{text}](/ideas/{org_slug}/{slug})"

        if href.startswith(("#", "http://", "https://", "//", "mailto:")):
            return match.group(0)

        cleaned = re.sub(r"^\./https?://", lambda m: m.group(0)[2:], href)
        if cleaned != href:
            return f"[{text}]({cleaned})"

        resolved = urljoin(base_url, href)
        return f"[{text}]({resolved})"

    rewritten = _MD_LINK_RE.sub(_rewrite, content)
    return rewritten, subpages


def fetch_raw_markdown(url: str) -> Optional[str]:
    """Fetch a URL expected to return raw markdown directly."""
    resp = fetch_with_retry(url)
    if not resp:
        return None

    content = resp.text.strip()
    if len(content) < 50:
        return None
    # Check we didn't get an HTML error page
    if content.lstrip().startswith("<!DOCTYPE") or content.lstrip().startswith("<html"):
        return None
    return content


def fetch_google_doc(export_url: str, original_url: str = None) -> Optional[str]:
    """Fetch a Google Doc via its export URL (HTML or plain text)."""
    print(f"    Fetching Google Doc export...")
    resp = fetch_with_retry(export_url, timeout=30)
    if resp:
        result = html_to_markdown(resp.text, url=original_url)
        if result and len(result.strip()) > 100:
            return result

    # Fallback: plain text export
    txt_url = export_url.replace("format=html", "format=txt")
    resp = fetch_with_retry(txt_url, timeout=30)
    if resp:
        text = resp.text.strip()
        if len(text) > 100:
            return text

    return None


def fetch_github_issues(url: str) -> Optional[str]:
    """Fetch GitHub issues using the gh CLI."""
    parsed = urlparse(url)
    path_parts = parsed.path.strip("/").split("/")
    if len(path_parts) < 3:
        return None

    owner, repo = path_parts[0], path_parts[1]

    # Single issue: github.com/{owner}/{repo}/issues/{number}
    if len(path_parts) >= 4 and path_parts[3].isdigit():
        issue_num = path_parts[3]
        print(f"    Fetching issue #{issue_num} via gh CLI...")
        try:
            result = subprocess.run(
                ["gh", "issue", "view", issue_num, "--repo", f"{owner}/{repo}",
                 "--json", "title,body,labels"],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                data = json.loads(result.stdout)
                content = f"## {data.get('title', 'Untitled')}\n\n"
                labels = [l.get("name", "") for l in data.get("labels", [])]
                if labels:
                    content += f"**Labels:** {', '.join(labels)}\n\n"
                content += data.get("body", "") + "\n"
                if len(content.strip()) > 100:
                    return content
        except Exception as e:
            print(f"    gh issue view failed: {e}")
        return None

    # Multiple issues: extract label from query string
    label = None
    if parsed.query:
        m = re.search(r'label[:%]3A["\s]*([^"&]+)', parsed.query)
        if not m:
            m = re.search(r'label_name[^=]*=([^&]+)', parsed.query)
        if m:
            label = m.group(1).replace("+", " ").replace("%20", " ").strip('"')

    print(f"    Fetching issues from {owner}/{repo}" +
          (f" (label: {label})" if label else "") + " via gh CLI...")

    cmd = ["gh", "issue", "list", "--repo", f"{owner}/{repo}", "--state", "open",
           "--json", "title,body,labels,number", "--limit", "50"]
    if label:
        cmd.extend(["--label", label])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            print(f"    gh issue list failed: {result.stderr.strip()}")
            return None

        issues = json.loads(result.stdout)
        if not issues and label:
            # Retry without label filter
            print(f"    No issues with label '{label}', trying without filter...")
            cmd_no_label = ["gh", "issue", "list", "--repo", f"{owner}/{repo}",
                           "--state", "open", "--json", "title,body,labels,number", "--limit", "50"]
            result = subprocess.run(cmd_no_label, capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                issues = json.loads(result.stdout)

        if not issues:
            return None

        content = ""
        for issue in issues:
            title = issue.get("title", "Untitled")
            number = issue.get("number", "")
            body = issue.get("body", "").strip()
            labels = [l.get("name", "") for l in issue.get("labels", [])]

            content += f"## #{number}: {title}\n\n"
            if labels:
                content += f"**Labels:** {', '.join(labels)}\n\n"
            if body:
                if len(body) > 3000:
                    body = body[:3000] + "\n\n*[truncated]*"
                content += body + "\n\n"
            content += "---\n\n"

        return content.strip() if len(content.strip()) > 100 else None

    except Exception as e:
        print(f"    gh CLI failed: {e}")
        return None


def fetch_gitlab_content(url: str) -> Optional[str]:
    """Fetch content from GitLab - raw blobs or issues via API."""
    parsed = urlparse(url)

    # GitLab blob -> raw
    if "/-/blob/" in parsed.path:
        raw_url = url.replace("/-/blob/", "/-/raw/")
        print(f"    Trying GitLab raw URL...")
        content = fetch_raw_markdown(raw_url)
        if content:
            return content

    # GitLab issues -> API
    if "/-/issues" in parsed.path:
        m = re.match(r"https?://([^/]+)/(.+?)/-/issues", url)
        if m:
            host = m.group(1)
            project_path = quote(m.group(2), safe="")
            label = None
            m_label = re.search(r"label_name[^=]*=([^&]+)", parsed.query)
            if m_label:
                label = m_label.group(1).replace("%20", " ").replace("+", " ")

            api_url = f"https://{host}/api/v4/projects/{project_path}/issues?state=opened&per_page=50"
            if label:
                api_url += f"&labels={quote(label)}"
            print(f"    Trying GitLab API...")
            resp = fetch_with_retry(api_url)
            if resp:
                try:
                    issues = resp.json()
                    if issues:
                        content = ""
                        for issue in issues:
                            content += f"## #{issue.get('iid', '')}: {issue.get('title', 'Untitled')}\n\n"
                            labels = issue.get("labels", [])
                            if labels:
                                content += f"**Labels:** {', '.join(labels)}\n\n"
                            body = issue.get("description", "").strip()
                            if body:
                                if len(body) > 3000:
                                    body = body[:3000] + "\n\n*[truncated]*"
                                content += body + "\n\n"
                            content += "---\n\n"
                        return content.strip() if len(content.strip()) > 100 else None
                except Exception as e:
                    print(f"    GitLab API parse failed: {e}")

    # Fallback: fetch HTML
    resp = fetch_with_retry(url)
    if resp:
        return html_to_markdown(resp.text, url=url)
    return None


def html_to_markdown(html: str, url: str = None) -> Optional[str]:
    """
    Extract main content from HTML and convert to clean markdown.
    Primary: trafilatura. Fallback: BS4 + markdownify.
    """
    # Primary: trafilatura
    try:
        result = trafilatura.extract(
            html,
            output_format="markdown",
            include_links=True,
            include_tables=True,
            include_images=False,
            include_formatting=True,
            include_comments=False,
            favor_recall=True,
            url=url,
        )
        if result and len(result.strip()) > 100:
            return result.strip()
    except Exception as e:
        print(f"    Trafilatura extraction failed: {e}")

    # Fallback: BS4 + markdownify
    if HAS_MARKDOWNIFY:
        try:
            soup = BeautifulSoup(html, "html.parser")
            for tag in soup(["script", "style", "nav", "footer", "header", "aside", "noscript"]):
                tag.decompose()

            main = (
                soup.find("main")
                or soup.find("article")
                or soup.find('[role="main"]')
                or soup.find("div", class_=re.compile(r"content|main|post|entry|wiki", re.I))
                or soup.find("div", id=re.compile(r"content|main|post|entry|wiki", re.I))
            )

            target = main if (main and len(main.get_text(strip=True)) > 200) else (soup.find("body") or soup)
            result = md(str(target), heading_style="ATX", bullets="-", strip=["img"])

            if result and len(result.strip()) > 100:
                result = re.sub(r"\n{3,}", "\n\n", result)
                return result.strip()
        except Exception as e:
            print(f"    Markdownify fallback failed: {e}")

    return None


# ─── Step 1: Fetch organizations from API ─────────────────────────────────
def fetch_organizations() -> list:
    """Fetch all GSoC 2026 organizations from the public API."""
    print("Fetching organizations from GSoC API...")
    print(f"  URL: {GSOC_API_URL}")

    resp = requests.get(GSOC_API_URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()

    data = resp.json()

    # The API may return a list directly or a paginated response
    if isinstance(data, list):
        orgs = data
    elif isinstance(data, dict):
        orgs = data.get("results", data.get("organizations", []))
        # Handle pagination
        next_url = data.get("next")
        while next_url:
            print(f"  Fetching next page...")
            resp = requests.get(next_url, headers=HEADERS, timeout=30)
            resp.raise_for_status()
            page_data = resp.json()
            if isinstance(page_data, dict):
                orgs.extend(page_data.get("results", page_data.get("organizations", [])))
                next_url = page_data.get("next")
            else:
                orgs.extend(page_data)
                break
    else:
        print(f"  WARNING: Unexpected API response type: {type(data)}")
        print(f"  Response preview: {str(data)[:500]}")
        orgs = []

    print(f"  Found {len(orgs)} organizations\n")
    return orgs


def process_org(org: dict) -> dict:
    """Normalize org data from the API response."""
    return {
        "name": org.get("name", org.get("title", "Unknown")),
        "slug": org.get("slug", org.get("id", "")),
        "tagline": org.get("tagline", org.get("short_description", "")),
        "description": org.get("description", ""),
        "ideas_url": org.get("ideas_link", org.get("ideas_url", org.get("ideas_list", ""))),
        "website_url": org.get("website_url", org.get("url", "")),
        "irc_channel": org.get("irc_channel", ""),
        "contact_email": org.get("contact_email", ""),
        "mailing_list": org.get("mailing_list", ""),
        "tech_tags": org.get("tech_tags", org.get("technologies", [])),
        "topic_tags": org.get("topic_tags", org.get("topics", [])),
        "category": org.get("category", ""),
        "gsoc_page": f"https://summerofcode.withgoogle.com/programs/2026/organizations/{org.get('slug', org.get('id', ''))}",
    }


# ─── Step 2: Fetch ideas pages ───────────────────────────────────────────
def fetch_ideas_simple(url: str) -> Optional[str]:
    """Try to fetch an ideas page and convert to clean markdown."""
    strategy, target_url = classify_url(url)

    # ── Strategy-specific fetchers ──

    # Raw markdown (GitHub blob/wiki/gist, GitLab blob)
    # NOTE: links are NOT resolved here — extract_and_fetch_subpages() handles
    # both sub-page detection (on raw relative links) and link resolution.
    if strategy in ("github_raw", "github_wiki_raw", "gist_raw", "gitlab_raw"):
        content = fetch_raw_markdown(target_url)
        if content:
            return content
        print(f"    Raw markdown unavailable, trying HTML extraction...")

    # Google Docs export
    if strategy == "google_doc":
        content = fetch_google_doc(target_url, original_url=url)
        if content:
            return content
        return None

    # GitHub Issues via gh CLI
    if strategy == "github_issues":
        content = fetch_github_issues(url)
        if content:
            return content
        return None

    # GitLab (raw fallback or issues API)
    if strategy == "gitlab_issues":
        content = fetch_gitlab_content(url)
        if content:
            return content
        return None

    # ── Generic: fetch HTML and extract markdown ──
    resp = fetch_with_retry(url)
    if not resp:
        return None

    # Early check: reject garbage HTML before expensive extraction
    # (trafilatura can strip anti-bot markers, so check raw HTML first)
    valid, reason = is_valid_content(resp.text)
    if not valid:
        print(f"    Content rejected ({reason})")
        return None

    # Try trafilatura + markdownify
    result = html_to_markdown(resp.text, url=url)
    if not result:
        # Final fallback: plain text extraction
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header", "aside", "noscript"]):
            tag.decompose()
        main = (
            soup.find("main")
            or soup.find("article")
            or soup.find('[role="main"]')
            or soup.find("div", class_=re.compile(r"content|main|post|entry|wiki", re.I))
            or soup.find("div", id=re.compile(r"content|main|post|entry|wiki", re.I))
        )
        if main and len(main.get_text(strip=True)) > 200:
            result = main.get_text(separator="\n", strip=True)
        else:
            body = soup.find("body")
            result = (body or soup).get_text(separator="\n", strip=True)
        result = re.sub(r"\n{3,}", "\n\n", result).strip()

    # Validate content quality — reject garbage (challenge pages, auth walls, etc.)
    valid, reason = is_valid_content(result)
    if not valid:
        print(f"    Content rejected ({reason})")
        return None

    return result


async def _extract_page_content(page, url: str) -> Optional[str]:
    """Extract markdown/text content from a loaded browser page."""
    html_content = await page.content()

    result = html_to_markdown(html_content, url=url)
    if not result:
        soup = BeautifulSoup(html_content, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()
        main = (
            soup.find("main") or soup.find("article") or soup.find('[role="main"]')
        )
        text = (main or soup.find("body") or soup).get_text(separator="\n", strip=True)
        text = re.sub(r"\n{3,}", "\n\n", text)
        if len(text.strip()) > 100:
            result = text.strip()

    return result


async def _fetch_one_browser(context, name: str, url: str) -> tuple:
    """Fetch a single URL in a browser tab. Returns (name, result_or_None)."""
    page = await context.new_page()
    try:
        # For Google Docs, use the published/preview version instead of the editor
        if "docs.google.com" in url and "/document/d/" in url:
            m = re.search(r"/document/d/([a-zA-Z0-9_-]+)", url)
            if m:
                doc_id = m.group(1)
                url = f"https://docs.google.com/document/d/{doc_id}/preview"

        wait_until = "domcontentloaded" if "docs.google.com" in url else "networkidle"
        await page.goto(url, wait_until=wait_until, timeout=30000)
        await asyncio.sleep(2)

        # First extraction attempt
        result = await _extract_page_content(page, url)

        # If content looks like a challenge/interstitial page, wait for it to resolve
        if result:
            valid, reason = is_valid_content(result)
            if not valid and reason in ("anti-bot challenge", "cloudflare challenge"):
                print(f"    Challenge page detected, waiting for resolution...")
                # Wait up to 20 seconds for the challenge to complete,
                # polling every 2 seconds for a URL change or new content
                original_url = page.url
                for attempt in range(10):
                    await asyncio.sleep(2)
                    current_url = page.url
                    if current_url != original_url:
                        # Page redirected after challenge — re-extract
                        await asyncio.sleep(1)
                        result = await _extract_page_content(page, current_url)
                        break
                    # Check if content changed (challenge resolved in-place)
                    new_result = await _extract_page_content(page, url)
                    if new_result:
                        new_valid, _ = is_valid_content(new_result)
                        if new_valid:
                            result = new_result
                            break

        # Scroll to load lazy content
        for _ in range(12):
            try:
                prev = await page.evaluate("document.body.scrollHeight")
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                await asyncio.sleep(0.4)
                curr = await page.evaluate("document.body.scrollHeight")
                if curr == prev:
                    break
            except Exception:
                break

        # Final extraction after scrolling (may have loaded more content)
        final_result = await _extract_page_content(page, url)
        if final_result and len(final_result) > len(result or ""):
            result = final_result

        # Final validation
        if result:
            valid, reason = is_valid_content(result)
            if valid:
                print(f"    OK ({len(result)} chars)")
                return (name, result)
            else:
                print(f"    FAILED: content rejected ({reason})")
                return (name, None)
        else:
            print(f"    FAILED: no content extracted")
            return (name, None)

    except Exception as e:
        print(f"    ERROR: {e}")
        return (name, None)
    finally:
        await page.close()


async def fetch_ideas_browser(urls: list) -> dict:
    """
    Fetch ideas pages using Playwright with parallel tabs.
    """
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("  Playwright not installed. Run: pip install playwright && playwright install chromium")
        return {}

    results = {}

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent=HEADERS["User-Agent"],
            viewport={"width": 1280, "height": 720},
        )

        # Process in batches of BROWSER_CONCURRENCY
        for batch_start in range(0, len(urls), BROWSER_CONCURRENCY):
            batch = urls[batch_start:batch_start + BROWSER_CONCURRENCY]
            for name, url in batch:
                idx = urls.index((name, url)) + 1
                print(f"  [{idx}/{len(urls)}] {name}")
                print(f"           {url}")

            tasks = [_fetch_one_browser(context, name, url) for name, url in batch]
            batch_results = await asyncio.gather(*tasks)

            for name, content in batch_results:
                if content:
                    results[name] = content

            await asyncio.sleep(0.5)

        await browser.close()

    return results


# Minimum content lines to consider "good enough" — below this, browser retry is attempted
SHORT_CONTENT_THRESHOLD = 100


def fetch_all_ideas(
    orgs: list,
    use_browser: bool = False,
    fetch_subpages: bool = True,
    max_subpages: int = 0,
) -> list:
    """Fetch project ideas for all organizations."""
    total = len(orgs)
    print(f"Fetching project ideas pages for {total} organizations...\n")

    browser_needed = []
    fetched = 0
    skipped = 0

    for i, org in enumerate(orgs):
        url = org.get("ideas_url", "")
        org_slug = org.get("slug", sanitize_filename(org["name"]))
        if not url:
            print(f"  [{i+1}/{total}] {org['name']}: — no ideas URL")
            org["ideas_content"] = None
            org["ideas_subpages"] = []
            skipped += 1
            continue

        print(f"  [{i+1}/{total}] {org['name']}")
        print(f"           {url}")

        # Try simple HTTP fetch first
        content = fetch_ideas_simple(url)

        if content:
            fetched += 1
            lines = content.count("\n") + 1
            print(f"    OK ({len(content)} chars, {lines} lines)")

            # Extract and fetch relative sub-pages
            if fetch_subpages:
                rewritten, subpages = extract_and_fetch_subpages(
                    content, url, org_slug, max_subpages
                )
                org["ideas_content"] = rewritten
                org["ideas_subpages"] = subpages
                if subpages:
                    print(f"    Extracted {len(subpages)} sub-pages")
            else:
                org["ideas_content"] = resolve_markdown_links(content, url)
                org["ideas_subpages"] = []

            # If content is short and browser is available, queue for retry
            if use_browser and lines < SHORT_CONTENT_THRESHOLD:
                browser_needed.append((org["name"], url))
                print(f"    -> short content, queued for browser retry")
        else:
            org["ideas_content"] = None
            org["ideas_subpages"] = []
            if use_browser:
                browser_needed.append((org["name"], url))
                print(f"    -> queued for browser")
            else:
                print(f"    FAILED (try --use-browser)")

        time.sleep(REQUEST_DELAY)

    # Browser-fetch remaining
    if browser_needed:
        print(f"\n{'─'*40}")
        print(f"Browser-fetching {len(browser_needed)} pages ({BROWSER_CONCURRENCY} parallel tabs)...\n")
        browser_results = asyncio.run(fetch_ideas_browser(browser_needed))

        for org in orgs:
            if org["name"] in browser_results:
                new_content = browser_results[org["name"]]
                old_content = org.get("ideas_content") or ""
                old_lines = old_content.count("\n") + 1 if old_content else 0
                new_lines = new_content.count("\n") + 1

                if new_lines > old_lines:
                    if old_content:
                        print(f"  UPGRADED {org['name']}: {old_lines} -> {new_lines} lines")
                    if not old_content:
                        fetched += 1
                    # Extract sub-pages for browser-upgraded content
                    browser_url = org.get("ideas_url", "")
                    org_slug = org.get("slug", sanitize_filename(org["name"]))
                    if fetch_subpages and browser_url:
                        rewritten, subpages = extract_and_fetch_subpages(
                            new_content, browser_url, org_slug, max_subpages
                        )
                        org["ideas_content"] = rewritten
                        org["ideas_subpages"] = subpages
                    else:
                        org["ideas_content"] = new_content
                        org["ideas_subpages"] = org.get("ideas_subpages", [])

    print(f"\n  Summary: {fetched} fetched, {skipped} no URL, {total - fetched - skipped} failed")
    return orgs


# ─── Single URL scraping ─────────────────────────────────────────────────
def scrape_single_url(url: str, use_browser: bool = False) -> Optional[str]:
    """Scrape a single URL and return markdown content."""
    strategy, _ = classify_url(url)
    print(f"  URL: {url}")
    print(f"  Strategy: {strategy}")

    # Try HTTP first
    content = fetch_ideas_simple(url)
    if content:
        lines = content.count("\n") + 1
        print(f"  HTTP: {len(content)} chars, {lines} lines")
        if not use_browser or lines >= SHORT_CONTENT_THRESHOLD:
            return content
        print(f"  Short content, trying browser...")

    if use_browser:
        print(f"  Fetching with browser...")
        browser_results = asyncio.run(fetch_ideas_browser([("url", url)]))
        browser_content = browser_results.get("url")
        if browser_content:
            new_lines = browser_content.count("\n") + 1
            old_lines = content.count("\n") + 1 if content else 0
            print(f"  Browser: {len(browser_content)} chars, {new_lines} lines")
            if new_lines > old_lines:
                return browser_content
            print(f"  Browser result not better, keeping HTTP result")

    return content


# ─── Step 3: Save results ────────────────────────────────────────────────
def sanitize_filename(name: str) -> str:
    return re.sub(r"[^\w\s-]", "", name).strip().replace(" ", "_").lower()[:80]


def save_results(orgs: list, output_dir: Path):
    """Save all results to disk in multiple formats."""
    output_dir.mkdir(parents=True, exist_ok=True)
    orgs_dir = output_dir / "organizations"
    orgs_dir.mkdir(exist_ok=True)
    ideas_dir = output_dir / "ideas"
    # Clean stale ideas files from previous runs
    if ideas_dir.exists():
        shutil.rmtree(ideas_dir)
    ideas_dir.mkdir(exist_ok=True)
    data_dir = output_dir / "data"
    data_dir.mkdir(exist_ok=True)

    print(f"\nSaving results to {output_dir}/\n")

    # 1. Master JSON (metadata only, no content blobs)
    master = []
    for org in orgs:
        entry = {k: v for k, v in org.items()
                 if k not in ("ideas_content", "ideas_subpages")}
        entry["has_ideas"] = bool(org.get("ideas_content"))
        master.append(entry)

    master_path = data_dir / "organizations.json"
    with open(master_path, "w", encoding="utf-8") as f:
        json.dump(master, f, indent=2, ensure_ascii=False)
    print(f"  {master_path} (metadata)")

    # 2. Full JSON (with ideas content)
    full_path = data_dir / "organizations_with_ideas.json"
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(orgs, f, indent=2, ensure_ascii=False)
    print(f"  {full_path} (full data)")

    # 3. Individual markdown files
    for org in orgs:
        fname = sanitize_filename(org["name"])

        # Org overview
        with open(orgs_dir / f"{fname}.md", "w", encoding="utf-8") as f:
            f.write(f"# {org['name']}\n\n")
            if org.get("tagline"):
                f.write(f"> {org['tagline']}\n\n")
            if org.get("tech_tags"):
                f.write(f"**Technologies:** {', '.join(org['tech_tags'])}\n")
            if org.get("topic_tags"):
                f.write(f"**Topics:** {', '.join(org['topic_tags'])}\n")
            if org.get("category"):
                f.write(f"**Category:** {org['category']}\n")
            f.write(f"**Website:** {org.get('website_url', 'N/A')}\n")
            f.write(f"**Ideas:** {org.get('ideas_url', 'N/A')}\n")
            f.write(f"**GSoC Page:** {org.get('gsoc_page', 'N/A')}\n\n")
            if org.get("description"):
                f.write(f"## Description\n\n{org['description']}\n\n")

        # Ideas dump (main content)
        if org.get("ideas_content"):
            with open(ideas_dir / f"{fname}.md", "w", encoding="utf-8") as f:
                f.write(f"# {org['name']} — Project Ideas\n\n")
                f.write(f"**Source:** {org.get('ideas_url', 'N/A')}\n")
                f.write(f"**Scraped:** {datetime.now().isoformat()}\n\n---\n\n")
                f.write(org["ideas_content"])
                f.write("\n")

            # Sub-page files in ideas/{org_slug}/ directory
            subpages = org.get("ideas_subpages", [])
            if subpages:
                subpages_dir = ideas_dir / fname
                subpages_dir.mkdir(exist_ok=True)
                for sp in subpages:
                    sp_path = subpages_dir / f"{sp['slug']}.md"
                    with open(sp_path, "w", encoding="utf-8") as f:
                        f.write(f"# {sp['title']}\n\n")
                        f.write(f"**Parent:** {org['name']} — Project Ideas\n")
                        f.write(f"**Source:** {sp['source_url']}\n")
                        f.write(f"**Scraped:** {datetime.now().isoformat()}\n\n---\n\n")
                        f.write(sp["content"])
                        f.write("\n")

    ideas_count = sum(1 for o in orgs if o.get("ideas_content"))
    subpages_count = sum(len(o.get("ideas_subpages", [])) for o in orgs)
    print(f"  {orgs_dir}/ ({len(orgs)} files)")
    print(f"  {ideas_dir}/ ({ideas_count} files, {subpages_count} sub-pages)")

    # 4. README with inline summary table
    readme_path = output_dir / "README.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(f"# GSoC 2026 — Project Ideas\n\n")
        f.write(f"All **{len(orgs)}** organizations participating in "
                f"[Google Summer of Code 2026](https://summerofcode.withgoogle.com/programs/2026/organizations), "
                f"with their project ideas scraped and collected in one place.\n\n")
        f.write(f"**{ideas_count}** out of {len(orgs)} ideas pages successfully scraped.\n\n")
        f.write(f"| # | Organization | Tech | Ideas |\n")
        f.write(f"|---|---|---|---|\n")
        sorted_orgs = sorted(orgs, key=lambda o: o.get("name", "").lower())
        for i, org in enumerate(sorted_orgs, 1):
            fname = sanitize_filename(org["name"])
            safe_name = org["name"].replace("|", "\\|")
            name_link = f"[{safe_name}](organizations/{fname}.md)"
            techs = ", ".join(t.replace("|", "\\|") for t in org.get("tech_tags", [])[:4])
            if org.get("ideas_content"):
                ideas_link = f"[Ideas](ideas/{fname}.md)"
            elif org.get("ideas_url"):
                ideas_link = f"[Link]({org['ideas_url']})"
            else:
                ideas_link = "—"
            f.write(f"| {i} | {name_link} | {techs} | {ideas_link} |\n")
        f.write(f"\n---\n\n")
        f.write(f"## How this data was collected\n\n")
        f.write(f"A Python scraper queries the GSoC public API, then fetches each org's ideas page:\n\n")
        f.write(f"- GitHub blob/wiki/gist URLs are converted to raw URLs for clean Markdown\n")
        f.write(f"- Google Docs are exported as HTML/text\n")
        f.write(f"- GitHub/GitLab issues are fetched via CLI/API\n")
        f.write(f"- HTML pages are extracted via trafilatura or markdownify\n")
        f.write(f"- Playwright headless browser handles JS-rendered pages\n\n")
        f.write(f"See [`scraper/`](scraper/) for the source code.\n\n")
        f.write(f"## Repository structure\n\n")
        f.write(f"| Path | Description |\n")
        f.write(f"|---|---|\n")
        f.write(f"| [`organizations/`](organizations/) | Overview of each org (tech, topics, links) |\n")
        f.write(f"| [`ideas/`](ideas/) | Scraped project ideas for each org |\n")
        f.write(f"| [`data/`](data/) | JSON data for programmatic access |\n")
        f.write(f"| [`scraper/`](scraper/) | Scraper source code and requirements |\n")

    print(f"  {readme_path}")


# ─── Main ─────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="GSoC 2026 Organizations & Project Ideas Scraper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scraper.py                           # full run (HTTP only)
  python scraper.py --use-browser             # full run with Playwright
  python scraper.py --url https://example.com # scrape single URL
  python scraper.py --url URL --use-browser   # single URL with browser
  python scraper.py --org jenkins             # re-scrape matching org(s)
  python scraper.py --tech python             # only Python orgs
  python scraper.py --max-orgs 5              # test with 5
  python scraper.py --step orgs               # only fetch org list
  python scraper.py --step ideas              # only fetch ideas (needs cached orgs)
  python scraper.py --no-subpages             # skip linked sub-pages
  python scraper.py --max-subpages 10         # limit sub-pages per org
        """,
    )
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR), help="Output directory")
    parser.add_argument("--step", choices=["orgs", "ideas", "all"], default="all")
    parser.add_argument("--max-orgs", type=int, help="Limit number of orgs")
    parser.add_argument("--tech", type=str, help="Filter by technology tag")
    parser.add_argument("--topic", type=str, help="Filter by topic tag")
    parser.add_argument("--org", type=str, help="Filter by org name (substring match)")
    parser.add_argument("--use-browser", action="store_true",
                        help="Use Playwright for JS-rendered pages")
    parser.add_argument("--orgs-file", type=str, help="Load orgs from file (skip API)")
    parser.add_argument("--url", type=str,
                        help="Scrape a single URL and print markdown (no GSoC API needed)")
    parser.add_argument("--no-subpages", action="store_true",
                        help="Skip fetching linked sub-pages (faster runs)")
    parser.add_argument("--max-subpages", type=int, default=0,
                        help="Max sub-pages to fetch per org (0 = unlimited, default: 0)")
    args = parser.parse_args()

    # ── Single URL mode ──
    if args.url:
        print(f"\n{'═'*60}")
        print(f"  Single URL Scrape")
        print(f"{'═'*60}\n")

        content = scrape_single_url(args.url, use_browser=args.use_browser)
        if content:
            print(f"\n{'─'*60}")
            print(f"Result ({content.count(chr(10)) + 1} lines):")
            print(f"{'─'*60}\n")
            print(content)
        else:
            print("\nNo content extracted.")
            sys.exit(1)
        return

    output_dir = Path(args.output_dir)

    print(f"\n{'═'*60}")
    print(f"  GSoC 2026 Scraper")
    print(f"{'═'*60}")
    print(f"  Output:  {output_dir}")
    print(f"  Time:    {datetime.now().isoformat()}")
    print(f"  Browser: {'yes' if args.use_browser else 'no (HTTP only)'}")
    print(f"{'═'*60}\n")

    # ── Load / fetch organizations ──
    orgs = None

    if args.step in ("orgs", "all"):
        raw_orgs = fetch_organizations()
        orgs = [process_org(o) for o in raw_orgs]
    elif args.orgs_file:
        with open(args.orgs_file, "r", encoding="utf-8") as f:
            orgs = json.load(f)
        print(f"Loaded {len(orgs)} orgs from {args.orgs_file}")
    else:
        cache = output_dir / "data" / "organizations.json"
        if not cache.exists():
            cache = output_dir / "organizations.json"
        if cache.exists():
            with open(cache, "r", encoding="utf-8") as f:
                orgs = json.load(f)
            print(f"Loaded {len(orgs)} orgs from cache ({cache})")
        else:
            print("No cached org list found. Run with --step orgs first, or omit --step.")
            sys.exit(1)

    # ── Apply filters ──
    if args.tech:
        tech = args.tech.lower()
        orgs = [o for o in orgs if any(tech in t.lower() for t in o.get("tech_tags", []))]
        print(f"Filtered by tech '{args.tech}': {len(orgs)} orgs")

    if args.topic:
        topic = args.topic.lower()
        orgs = [o for o in orgs if any(topic in t.lower() for t in o.get("topic_tags", []))]
        print(f"Filtered by topic '{args.topic}': {len(orgs)} orgs")

    if args.org:
        org_filter = args.org.lower()
        orgs = [o for o in orgs if org_filter in o.get("name", "").lower()
                or org_filter in o.get("slug", "").lower()]
        print(f"Filtered by org '{args.org}': {len(orgs)} orgs")

    if args.max_orgs:
        orgs = orgs[:args.max_orgs]
        print(f"Limited to {args.max_orgs} orgs")

    if not orgs:
        print("No organizations to process!")
        sys.exit(0)

    # ── Fetch ideas ──
    if args.step in ("ideas", "all"):
        orgs = fetch_all_ideas(
            orgs,
            use_browser=args.use_browser,
            fetch_subpages=not args.no_subpages,
            max_subpages=args.max_subpages,
        )

    # ── Save ──
    save_results(orgs, output_dir)

    print(f"\n{'═'*60}")
    print(f"  Done! {len(orgs)} organizations processed.")
    ideas = sum(1 for o in orgs if o.get("ideas_content"))
    print(f"  Ideas pages scraped: {ideas}/{len(orgs)}")
    print(f"  Output: {output_dir}/")
    print(f"{'═'*60}\n")


if __name__ == "__main__":
    main()
