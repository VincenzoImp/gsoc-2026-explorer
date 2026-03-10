import { Suspense } from "react";
import type { Metadata } from "next";
import { getOrganizations, getTagStats } from "@/lib/data";
import { IdeasList } from "./ideas-list";
import { Skeleton } from "@/components/ui/skeleton";

export const metadata: Metadata = {
  title: "Project Ideas",
  description:
    "Browse all GSoC 2026 project ideas across 184 organizations.",
};

function IdeasContent() {
  const orgs = getOrganizations()
    .filter((o) => o.has_ideas)
    .sort((a, b) => a.name.localeCompare(b.name));

  const techTags = getTagStats("tech");
  const topicTags = getTagStats("topic");

  return <IdeasList orgs={orgs} techTags={techTags} topicTags={topicTags} />;
}

export default function IdeasIndexPage() {
  const orgs = getOrganizations().filter((o) => o.has_ideas);

  return (
    <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6">
      <div className="mb-6">
        <h1 className="text-2xl font-bold sm:text-3xl">Project Ideas</h1>
        <p className="mt-1 text-muted-foreground">
          {orgs.length} organizations with scraped project ideas.
          Click on any organization to view their full ideas page.
        </p>
      </div>

      <Suspense
        fallback={
          <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
            {Array.from({ length: 9 }).map((_, i) => (
              <Skeleton key={i} className="h-36 rounded-lg" />
            ))}
          </div>
        }
      >
        <IdeasContent />
      </Suspense>
    </div>
  );
}
