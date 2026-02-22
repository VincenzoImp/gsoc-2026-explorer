"use client";

import { useCallback, useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { Building2, FileText, Lightbulb, Loader2 } from "lucide-react";
import {
  CommandDialog,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from "@/components/ui/command";
import type { SearchDocument } from "@/lib/types";
import type { FuseResult, FuseResultMatch, default as FuseType } from "fuse.js";

function extractSnippet(
  text: string,
  matchRange: readonly [number, number],
  contextChars = 60
): string {
  const [start, end] = matchRange;
  const snippetStart = Math.max(0, start - contextChars);
  const snippetEnd = Math.min(text.length, end + contextChars);
  let snippet = text.slice(snippetStart, snippetEnd).replace(/\n/g, " ");
  if (snippetStart > 0) snippet = "..." + snippet;
  if (snippetEnd < text.length) snippet = snippet + "...";
  return snippet;
}

function getMatchContext(result: FuseResult<SearchDocument>): {
  type: "org" | "ideas" | "subpage";
  contextLine: string;
} {
  const doc = result.item;

  // Sub-page documents always link to the sub-page
  if (doc.subpageSlug) {
    const contextLine = doc.description || doc.orgName || "";
    return { type: "subpage", contextLine };
  }

  const matches = result.matches || [];
  const hasIdeas = !!doc.ideasSnippet;

  const findMatch = (key: string): FuseResultMatch | undefined =>
    matches.find((m) => m.key === key);

  const nameMatch = findMatch("name");
  const taglineMatch = findMatch("tagline");
  const techMatch = findMatch("tech_tags");
  const topicMatch = findMatch("topic_tags");
  const descMatch = findMatch("description");
  const ideasMatch = findMatch("ideasSnippet");

  // Name/tagline match → show tagline, link to org
  if (nameMatch || taglineMatch) {
    return { type: "org", contextLine: doc.tagline };
  }

  // Tech tag match → show tags, link to org
  if (techMatch) {
    return {
      type: "org",
      contextLine: `Technologies: ${doc.tech_tags.join(", ")}`,
    };
  }

  // Topic tag match → show tags, link to org
  if (topicMatch) {
    return {
      type: "org",
      contextLine: `Topics: ${doc.topic_tags.join(", ")}`,
    };
  }

  // Description match → show snippet, link to org
  if (descMatch?.value && descMatch.indices?.length) {
    return {
      type: "org",
      contextLine: extractSnippet(descMatch.value, descMatch.indices[0]),
    };
  }

  // Ideas match → show snippet, link to ideas page
  if (ideasMatch?.value && ideasMatch.indices?.length && hasIdeas) {
    return {
      type: "ideas",
      contextLine: extractSnippet(ideasMatch.value, ideasMatch.indices[0]),
    };
  }

  // Fallback
  return { type: "org", contextLine: doc.tagline };
}

export function CommandSearch({
  open,
  onOpenChange,
}: {
  open: boolean;
  onOpenChange: (open: boolean) => void;
}) {
  const router = useRouter();
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<FuseResult<SearchDocument>[]>([]);
  const [searcher, setSearcher] = useState<FuseType<SearchDocument> | null>(
    null
  );
  const [loading, setLoading] = useState(false);

  // Lazy load the search index on first open
  useEffect(() => {
    if (open && !searcher) {
      setLoading(true);
      import("@/lib/search").then(({ getSearcher }) => {
        getSearcher().then((s) => {
          setSearcher(s);
          setLoading(false);
        });
      });
    }
  }, [open, searcher]);

  // Search when query changes
  useEffect(() => {
    if (!searcher || !query.trim()) {
      setResults([]);
      return;
    }
    const r = searcher.search(query, { limit: 12 });
    setResults(r);
  }, [query, searcher]);

  const handleSelect = useCallback(
    (doc: SearchDocument, type: "org" | "ideas" | "subpage") => {
      onOpenChange(false);
      setQuery("");
      if (type === "subpage") {
        router.push(`/ideas/${doc.slug}/${doc.subpageSlug}`);
      } else if (type === "ideas") {
        router.push(`/ideas/${doc.slug}`);
      } else {
        router.push(`/organizations/${doc.slug}`);
      }
    },
    [router, onOpenChange]
  );

  // Clear query on close
  const handleOpenChange = useCallback(
    (isOpen: boolean) => {
      if (!isOpen) setQuery("");
      onOpenChange(isOpen);
    },
    [onOpenChange]
  );

  // Keyboard shortcut
  useEffect(() => {
    const down = (e: KeyboardEvent) => {
      if (e.key === "k" && (e.metaKey || e.ctrlKey)) {
        e.preventDefault();
        onOpenChange(!open);
      }
    };
    document.addEventListener("keydown", down);
    return () => document.removeEventListener("keydown", down);
  }, [open, onOpenChange]);

  return (
    <CommandDialog
      open={open}
      onOpenChange={handleOpenChange}
      shouldFilter={false}
    >
      <CommandInput
        placeholder="Search organizations, ideas, technologies..."
        value={query}
        onValueChange={setQuery}
      />
      <CommandList>
        <CommandEmpty>
          {loading ? (
            <div className="flex items-center justify-center gap-2">
              <Loader2 className="h-4 w-4 animate-spin text-muted-foreground" />
              <span className="text-sm text-muted-foreground">Loading...</span>
            </div>
          ) : (
            "No results found."
          )}
        </CommandEmpty>

        {results.length > 0 && (
          <CommandGroup heading="Results">
            {results.map((r) => {
              const { type, contextLine } = getMatchContext(r);
              const Icon =
                type === "subpage"
                  ? FileText
                  : type === "ideas"
                    ? Lightbulb
                    : Building2;
              const label =
                type === "subpage"
                  ? `${r.item.name} — ${r.item.orgName}`
                  : type === "ideas"
                    ? `${r.item.name} — Ideas`
                    : r.item.name;
              const itemKey =
                type === "subpage"
                  ? `subpage-${r.item.slug}-${r.item.subpageSlug}`
                  : `${type}-${r.item.slug}`;

              return (
                <CommandItem
                  key={itemKey}
                  value={itemKey}
                  onSelect={() => handleSelect(r.item, type)}
                  className="flex items-center gap-2"
                >
                  <Icon className="h-4 w-4 shrink-0 text-muted-foreground" />
                  <div className="flex flex-col min-w-0">
                    <span className="font-medium">{label}</span>
                    <span className="text-xs text-muted-foreground line-clamp-1">
                      {contextLine}
                    </span>
                  </div>
                </CommandItem>
              );
            })}
          </CommandGroup>
        )}
      </CommandList>
    </CommandDialog>
  );
}
