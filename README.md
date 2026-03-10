# GSoC 2026 Explorer

A faster way to explore [Google Summer of Code 2026](https://summerofcode.withgoogle.com/programs/2026/organizations): all participating organizations and their project ideas collected in one place, with full-text search and filtering.

**Live site:** https://gsoc-explorer.vercel.app

The project has two parts:

- a **web app** that lets you browse and search every organization and idea, and
- a **scraper** that builds the underlying dataset from the official GSoC program page and each org's ideas page.

## What's inside

- **184 organizations** accepted into GSoC 2026, each with its technologies, topics and links.
- **Project ideas** for each organization, scraped from wherever they publish them (GitHub, wikis, Google Docs, issue trackers, plain HTML pages) and normalized to Markdown.
- A **JSON dataset** for programmatic access, so the data is easy to reuse.

## Web app

The site lives in [`web/`](web/) and is a static [Next.js](https://nextjs.org/) app (App Router, React 19, TypeScript, Tailwind CSS, shadcn/radix UI). It provides:

- Client-side full-text search across organizations and ideas (powered by `fuse.js` over a prebuilt search index).
- Filtering and URL-synced query state (`nuqs`) so searches and filters are shareable.
- Per-organization and per-idea pages with rendered Markdown, syntax highlighting and a table of contents.
- Light/dark theme.

### Run it locally

```bash
cd web
npm install
npm run dev
```

Then open http://localhost:3000.

The production build regenerates the search index before compiling and emits a static export:

```bash
npm run build
```

## Scraper

The dataset is produced by [`scraper/scraper.py`](scraper/scraper.py). It queries the public GSoC API for the organization list, then fetches each org's ideas page, converting the many source formats into clean Markdown:

- GitHub blob/wiki/gist links are rewritten to raw URLs.
- Google Docs are exported to text/HTML.
- GitHub/GitLab issues are pulled via CLI/API.
- Generic HTML pages are extracted with `trafilatura` / `markdownify`.
- JS-rendered pages are handled with a Playwright headless browser (`--use-browser`).

```bash
cd scraper
pip install -r requirements.txt

python scraper.py                 # full run (HTTP only)
python scraper.py --use-browser   # include JS-rendered pages
python scraper.py --step orgs     # fetch the org list only
python scraper.py --org jenkins   # scrape a single organization
```

Run `python scraper.py --help` for the full list of options (tech filters, sub-page limits, single-URL scraping, and more).

## Repository structure

| Path | Description |
|---|---|
| [`web/`](web/) | Next.js web app (the explorer UI) |
| [`scraper/`](scraper/) | Python scraper that builds the dataset |
| [`data/`](data/) | JSON data: `organizations.json` and `organizations_with_ideas.json` |
| [`organizations/`](organizations/) | Per-organization overview pages (Markdown) |
| [`ideas/`](ideas/) | Per-organization scraped project ideas (Markdown) |

## Notes

The dataset is a snapshot of the GSoC 2026 program page and each organization's ideas at scrape time. Organizations occasionally move or update their ideas pages, so a few entries may link out to the original source rather than mirror its full content. Re-run the scraper to refresh the data.
