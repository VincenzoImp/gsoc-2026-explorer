"use client";

import { useMemo, useState, useCallback } from "react";
import Link from "next/link";
import { useQueryState } from "nuqs";
import { Search, ArrowRight, X } from "lucide-react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { TagBadge } from "@/components/organizations/tag-badge";
import { EmptyState } from "@/components/shared/empty-state";
import type { Organization, TagCount } from "@/lib/types";

interface IdeasListProps {
  orgs: Organization[];
  techTags: TagCount[];
  topicTags: TagCount[];
}

export function IdeasList({ orgs, techTags, topicTags }: IdeasListProps) {
  const [query, setQuery] = useQueryState("q", { defaultValue: "" });
  const [techFilter, setTechFilter] = useQueryState("tech", {
    defaultValue: "",
  });
  const [topicFilter, setTopicFilter] = useQueryState("topic", {
    defaultValue: "",
  });
  const [showAllTech, setShowAllTech] = useState(false);
  const [showAllTopics, setShowAllTopics] = useState(false);

  const selectedTech = useMemo(
    () => new Set(techFilter ? techFilter.split(",") : []),
    [techFilter]
  );
  const selectedTopics = useMemo(
    () => new Set(topicFilter ? topicFilter.split(",") : []),
    [topicFilter]
  );

  const toggleTag = useCallback(
    (tag: string, type: "tech" | "topic") => {
      const setter = type === "tech" ? setTechFilter : setTopicFilter;
      const current = type === "tech" ? selectedTech : selectedTopics;
      const next = new Set(current);
      if (next.has(tag)) {
        next.delete(tag);
      } else {
        next.add(tag);
      }
      setter(next.size > 0 ? Array.from(next).join(",") : "");
    },
    [selectedTech, selectedTopics, setTechFilter, setTopicFilter]
  );

  const clearAll = useCallback(() => {
    setQuery("");
    setTechFilter("");
    setTopicFilter("");
  }, [setQuery, setTechFilter, setTopicFilter]);

  const filtered = useMemo(() => {
    let result = orgs;

    if (query) {
      const q = query.toLowerCase();
      result = result.filter((org) => {
        return (
          org.name.toLowerCase().includes(q) ||
          org.tagline.toLowerCase().includes(q) ||
          org.tech_tags.some((t) => t.toLowerCase().includes(q)) ||
          org.topic_tags.some((t) => t.toLowerCase().includes(q))
        );
      });
    }

    if (selectedTech.size > 0) {
      result = result.filter((org) =>
        [...selectedTech].every((t) => org.tech_tags.includes(t))
      );
    }

    if (selectedTopics.size > 0) {
      result = result.filter((org) =>
        [...selectedTopics].every((t) => org.topic_tags.includes(t))
      );
    }

    return result;
  }, [orgs, query, selectedTech, selectedTopics]);

  const hasActiveFilters =
    query || selectedTech.size > 0 || selectedTopics.size > 0;

  const PILL_LIMIT = 12;
  const visibleTech = showAllTech ? techTags : techTags.slice(0, PILL_LIMIT);
  const visibleTopics = showAllTopics
    ? topicTags
    : topicTags.slice(0, PILL_LIMIT);

  return (
    <>
      <div className="relative mb-4 max-w-md">
        <Search className="absolute left-2.5 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
        <Input
          placeholder="Search by name, technology, or topic..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="h-9 pl-8"
        />
      </div>

      {/* Technology filter pills */}
      <div className="mb-3">
        <h3 className="mb-1.5 text-xs font-semibold text-muted-foreground uppercase tracking-wider">
          Technologies
        </h3>
        <div className="flex flex-wrap gap-1.5">
          {visibleTech.map(({ tag }) => (
            <button
              key={tag}
              onClick={() => toggleTag(tag, "tech")}
              className={`rounded-full border px-2.5 py-0.5 text-xs font-medium transition-colors ${
                selectedTech.has(tag)
                  ? "border-blue-500 bg-blue-100 text-blue-800 dark:bg-blue-900/40 dark:text-blue-300"
                  : "border-transparent bg-muted text-muted-foreground hover:bg-accent"
              }`}
            >
              {tag}
            </button>
          ))}
          {techTags.length > PILL_LIMIT && (
            <button
              onClick={() => setShowAllTech(!showAllTech)}
              className="rounded-full px-2.5 py-0.5 text-xs font-medium text-primary hover:underline"
            >
              {showAllTech
                ? "Show less"
                : `+${techTags.length - PILL_LIMIT} more`}
            </button>
          )}
        </div>
      </div>

      {/* Topic filter pills */}
      <div className="mb-4">
        <h3 className="mb-1.5 text-xs font-semibold text-muted-foreground uppercase tracking-wider">
          Topics
        </h3>
        <div className="flex flex-wrap gap-1.5">
          {visibleTopics.map(({ tag }) => (
            <button
              key={tag}
              onClick={() => toggleTag(tag, "topic")}
              className={`rounded-full border px-2.5 py-0.5 text-xs font-medium transition-colors ${
                selectedTopics.has(tag)
                  ? "border-secondary-foreground/30 bg-secondary text-secondary-foreground"
                  : "border-transparent bg-muted text-muted-foreground hover:bg-accent"
              }`}
            >
              {tag}
            </button>
          ))}
          {topicTags.length > PILL_LIMIT && (
            <button
              onClick={() => setShowAllTopics(!showAllTopics)}
              className="rounded-full px-2.5 py-0.5 text-xs font-medium text-primary hover:underline"
            >
              {showAllTopics
                ? "Show less"
                : `+${topicTags.length - PILL_LIMIT} more`}
            </button>
          )}
        </div>
      </div>

      {/* Active filters */}
      {hasActiveFilters && (
        <div className="mb-4 flex flex-wrap items-center gap-1.5">
          {query && (
            <span className="inline-flex items-center gap-1 rounded-full bg-primary/10 px-2.5 py-0.5 text-xs font-medium text-primary">
              &quot;{query}&quot;
              <button onClick={() => setQuery("")}>
                <X className="h-3 w-3" />
              </button>
            </span>
          )}
          {[...selectedTech].map((tag) => (
            <span
              key={`tech-${tag}`}
              className="inline-flex items-center gap-1 rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800 dark:bg-blue-900/40 dark:text-blue-300"
            >
              {tag}
              <button onClick={() => toggleTag(tag, "tech")}>
                <X className="h-3 w-3" />
              </button>
            </span>
          ))}
          {[...selectedTopics].map((tag) => (
            <span
              key={`topic-${tag}`}
              className="inline-flex items-center gap-1 rounded-full bg-secondary px-2.5 py-0.5 text-xs font-medium text-secondary-foreground"
            >
              {tag}
              <button onClick={() => toggleTag(tag, "topic")}>
                <X className="h-3 w-3" />
              </button>
            </span>
          ))}
          <Button
            variant="ghost"
            size="sm"
            className="h-6 text-xs text-muted-foreground"
            onClick={clearAll}
          >
            Clear all
          </Button>
        </div>
      )}

      <p className="mb-4 text-sm text-muted-foreground">
        Showing {filtered.length} of {orgs.length} organizations
      </p>

      {filtered.length > 0 ? (
        <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {filtered.map((org) => (
            <Link
              key={org.slug}
              href={`/ideas/${org.slug}`}
              className="group flex flex-col gap-2 rounded-lg border bg-card p-4 transition-shadow hover:shadow-md"
            >
              <div className="flex items-start justify-between gap-2">
                <h3 className="font-semibold leading-tight group-hover:underline">
                  {org.name}
                </h3>
                <ArrowRight className="h-4 w-4 shrink-0 text-muted-foreground transition-transform group-hover:translate-x-0.5" />
              </div>
              {org.tagline && (
                <p className="text-sm text-muted-foreground line-clamp-2">
                  {org.tagline}
                </p>
              )}
              {org.tech_tags.length > 0 && (
                <div className="flex flex-wrap gap-1">
                  {org.tech_tags.slice(0, 3).map((tag) => (
                    <TagBadge key={tag} tag={tag} type="tech" size="sm" />
                  ))}
                  {org.tech_tags.length > 3 && (
                    <span className="inline-flex items-center rounded-full bg-muted px-2 py-0.5 text-[10px] font-medium text-muted-foreground">
                      +{org.tech_tags.length - 3}
                    </span>
                  )}
                </div>
              )}
            </Link>
          ))}
        </div>
      ) : (
        <EmptyState />
      )}
    </>
  );
}
