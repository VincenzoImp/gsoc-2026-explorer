"use client";

import Link from "next/link";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeSlug from "rehype-slug";
import { ExternalLink } from "lucide-react";

interface IdeasRendererProps {
  content: string;
  ideasUrl?: string;
}

function resolveHref(
  href: string,
  baseUrl?: string
): { resolved: string; isExternal: boolean } {
  if (href.startsWith("#")) {
    return { resolved: href, isExternal: false };
  }

  if (
    href.startsWith("http://") ||
    href.startsWith("https://") ||
    href.startsWith("//")
  ) {
    return { resolved: href, isExternal: true };
  }

  if (href.startsWith("mailto:")) {
    return { resolved: href, isExternal: false };
  }

  // Handle malformed ./https://... pattern
  const cleaned = href.replace(/^\.\/https?:\/\//, (match) =>
    match.slice(2)
  );
  if (cleaned !== href) {
    return { resolved: cleaned, isExternal: true };
  }

  if (baseUrl) {
    try {
      const resolved = new URL(href, baseUrl).href;
      return { resolved, isExternal: true };
    } catch {
      return { resolved: href, isExternal: false };
    }
  }

  return { resolved: href, isExternal: false };
}

export function IdeasRenderer({ content, ideasUrl }: IdeasRendererProps) {
  return (
    <div className="prose prose-neutral max-w-none dark:prose-invert prose-headings:scroll-mt-20 prose-a:text-primary prose-a:no-underline hover:prose-a:underline prose-img:rounded-lg prose-pre:bg-muted">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        rehypePlugins={[rehypeSlug]}
        components={{
          a: ({ href, children, ...props }) => {
            if (!href) {
              return <a {...props}>{children}</a>;
            }

            // Internal sub-page link (rewritten by scraper to /ideas/...)
            if (href.startsWith("/ideas/")) {
              return (
                <Link href={href} {...props}>
                  {children}
                </Link>
              );
            }

            const { resolved, isExternal } = resolveHref(href, ideasUrl);

            if (isExternal) {
              return (
                <a
                  href={resolved}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-0.5"
                  {...props}
                >
                  {children}
                  <ExternalLink className="inline h-3 w-3 shrink-0" />
                </a>
              );
            }
            return (
              <a href={resolved} {...props}>
                {children}
              </a>
            );
          },
          table: ({ children, ...props }) => (
            <div className="overflow-x-auto">
              <table {...props}>{children}</table>
            </div>
          ),
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
}
