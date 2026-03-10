"use client";

import { useMemo, useState, useCallback } from "react";
import { useQueryState } from "nuqs";
import { Search, SlidersHorizontal, X } from "lucide-react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";
import { Checkbox } from "@/components/ui/checkbox";
import { Separator } from "@/components/ui/separator";
import { ScrollArea } from "@/components/ui/scroll-area";
import { OrgCard } from "./org-card";
import { EmptyState } from "@/components/shared/empty-state";
import type { Organization, TagCount } from "@/lib/types";

interface OrganizationsViewProps {
  organizations: Organization[];
  techTags: TagCount[];
  topicTags: TagCount[];
}

export function OrganizationsView({
  organizations,
  techTags,
  topicTags,
}: OrganizationsViewProps) {
  const [query, setQuery] = useQueryState("q", { defaultValue: "" });
  const [techFilter, setTechFilter] = useQueryState("tech", {
    defaultValue: "",
  });
  const [topicFilter, setTopicFilter] = useQueryState("topic", {
    defaultValue: "",
  });
  const [sort, setSort] = useQueryState("sort", { defaultValue: "az" });
  const [techSearch, setTechSearch] = useState("");
  const [topicSearch, setTopicSearch] = useState("");
  const [filtersOpen, setFiltersOpen] = useState(false);

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
    let result = organizations;

    // Text search
    if (query) {
      const q = query.toLowerCase();
      result = result.filter((org) => {
        const haystack =
          `${org.name} ${org.tagline} ${org.description}`.toLowerCase();
        return haystack.includes(q);
      });
    }

    // Tech filter
    if (selectedTech.size > 0) {
      result = result.filter((org) =>
        [...selectedTech].every((t) => org.tech_tags.includes(t))
      );
    }

    // Topic filter
    if (selectedTopics.size > 0) {
      result = result.filter((org) =>
        [...selectedTopics].every((t) => org.topic_tags.includes(t))
      );
    }

    // Sort
    result = [...result].sort((a, b) => {
      if (sort === "za") return b.name.localeCompare(a.name);
      return a.name.localeCompare(b.name);
    });

    return result;
  }, [organizations, query, selectedTech, selectedTopics, sort]);

  const hasActiveFilters =
    query || selectedTech.size > 0 || selectedTopics.size > 0;

  const filteredTechTags = techTags.filter((t) =>
    t.tag.toLowerCase().includes(techSearch.toLowerCase())
  );
  const filteredTopicTags = topicTags.filter((t) =>
    t.tag.toLowerCase().includes(topicSearch.toLowerCase())
  );

  const TAG_LIMIT = 50;

  const filterSidebar = (
    <div className="flex flex-col gap-4">
      <div>
        <h3 className="mb-2 text-sm font-semibold">Technologies</h3>
        <Input
          placeholder="Filter technologies..."
          value={techSearch}
          onChange={(e) => setTechSearch(e.target.value)}
          className="mb-2 h-8 text-xs"
        />
        <ScrollArea className="h-48">
          <div className="flex flex-col gap-1 pr-3">
            {filteredTechTags.slice(0, TAG_LIMIT).map(({ tag, count }) => (
              <label
                key={tag}
                className="flex cursor-pointer items-center gap-2 rounded px-1 py-0.5 text-sm hover:bg-accent"
              >
                <Checkbox
                  checked={selectedTech.has(tag)}
                  onCheckedChange={() => toggleTag(tag, "tech")}
                  className="h-3.5 w-3.5"
                />
                <span className="flex-1 truncate">{tag}</span>
                <span className="text-xs text-muted-foreground">{count}</span>
              </label>
            ))}
            {filteredTechTags.length > TAG_LIMIT && (
              <p className="px-1 py-1 text-xs text-muted-foreground">
                and {filteredTechTags.length - TAG_LIMIT} more — use the filter above
              </p>
            )}
          </div>
        </ScrollArea>
      </div>

      <Separator />

      <div>
        <h3 className="mb-2 text-sm font-semibold">Topics</h3>
        <Input
          placeholder="Filter topics..."
          value={topicSearch}
          onChange={(e) => setTopicSearch(e.target.value)}
          className="mb-2 h-8 text-xs"
        />
        <ScrollArea className="h-48">
          <div className="flex flex-col gap-1 pr-3">
            {filteredTopicTags.slice(0, TAG_LIMIT).map(({ tag, count }) => (
              <label
                key={tag}
                className="flex cursor-pointer items-center gap-2 rounded px-1 py-0.5 text-sm hover:bg-accent"
              >
                <Checkbox
                  checked={selectedTopics.has(tag)}
                  onCheckedChange={() => toggleTag(tag, "topic")}
                  className="h-3.5 w-3.5"
                />
                <span className="flex-1 truncate">{tag}</span>
                <span className="text-xs text-muted-foreground">{count}</span>
              </label>
            ))}
            {filteredTopicTags.length > TAG_LIMIT && (
              <p className="px-1 py-1 text-xs text-muted-foreground">
                and {filteredTopicTags.length - TAG_LIMIT} more — use the filter above
              </p>
            )}
          </div>
        </ScrollArea>
      </div>
    </div>
  );

  return (
    <div className="flex gap-6">
      {/* Desktop sidebar */}
      <aside className="hidden w-64 shrink-0 lg:block">
        <div className="sticky top-20">{filterSidebar}</div>
      </aside>

      {/* Main content */}
      <div className="flex-1 min-w-0">
        {/* Search + controls bar */}
        <div className="mb-4 flex flex-wrap items-center gap-2">
          <div className="relative flex-1">
            <Search className="absolute left-2.5 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
            <Input
              placeholder="Search organizations..."
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              className="h-9 pl-8"
            />
          </div>

          <select
            value={sort}
            onChange={(e) => setSort(e.target.value)}
            className="h-9 rounded-md border bg-background px-3 text-sm"
          >
            <option value="az">A → Z</option>
            <option value="za">Z → A</option>
          </select>

          {/* Mobile filter trigger */}
          <Sheet open={filtersOpen} onOpenChange={setFiltersOpen}>
            <SheetTrigger asChild>
              <Button variant="outline" size="sm" className="h-9 lg:hidden">
                <SlidersHorizontal className="mr-1 h-4 w-4" />
                Filters
                {(selectedTech.size > 0 || selectedTopics.size > 0) && (
                  <span className="ml-1 rounded-full bg-primary px-1.5 text-[10px] text-primary-foreground">
                    {selectedTech.size + selectedTopics.size}
                  </span>
                )}
              </Button>
            </SheetTrigger>
            <SheetContent side="left" className="w-80 p-4 pt-10">
              {filterSidebar}
            </SheetContent>
          </Sheet>
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

        {/* Results count */}
        <p className="mb-4 text-sm text-muted-foreground">
          Showing {filtered.length} of {organizations.length} organizations
        </p>

        {/* Grid */}
        {filtered.length > 0 ? (
          <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
            {filtered.map((org) => (
              <OrgCard key={org.slug} org={org} />
            ))}
          </div>
        ) : (
          <EmptyState />
        )}
      </div>
    </div>
  );
}
