import fs from "node:fs";
import path from "node:path";
import type {
  Organization,
  OrganizationWithIdeas,
  IdeaSubpage,
  TagCount,
} from "./types";

const DATA_DIR = path.join(process.cwd(), "..", "data");

let orgsCache: Organization[] | null = null;
let orgsWithIdeasCache: OrganizationWithIdeas[] | null = null;

export function getOrganizations(): Organization[] {
  if (orgsCache) return orgsCache;
  const raw = fs.readFileSync(
    path.join(DATA_DIR, "organizations.json"),
    "utf-8"
  );
  orgsCache = JSON.parse(raw) as Organization[];
  return orgsCache;
}

export function getOrganizationsWithIdeas(): OrganizationWithIdeas[] {
  if (orgsWithIdeasCache) return orgsWithIdeasCache;
  const raw = fs.readFileSync(
    path.join(DATA_DIR, "organizations_with_ideas.json"),
    "utf-8"
  );
  orgsWithIdeasCache = JSON.parse(raw) as OrganizationWithIdeas[];
  return orgsWithIdeasCache;
}

export function getOrganizationBySlug(
  slug: string
): Organization | undefined {
  return getOrganizations().find((o) => o.slug === slug);
}

export function getOrganizationWithIdeas(
  slug: string
): OrganizationWithIdeas | undefined {
  return getOrganizationsWithIdeas().find((o) => o.slug === slug);
}

export function getAllSlugs(): string[] {
  return getOrganizations().map((o) => o.slug);
}

export function getIdeasSlugs(): string[] {
  return getOrganizationsWithIdeas()
    .filter((o) => o.ideas_content && o.ideas_content !== "None")
    .map((o) => o.slug);
}

export function getSubpageSlugs(): Array<{ slug: string; subpage: string }> {
  return getOrganizationsWithIdeas()
    .filter((o) => o.ideas_subpages?.length > 0)
    .flatMap((o) =>
      o.ideas_subpages.map((sp) => ({ slug: o.slug, subpage: sp.slug }))
    );
}

export function getSubpage(
  orgSlug: string,
  subpageSlug: string
): { org: OrganizationWithIdeas; subpage: IdeaSubpage } | undefined {
  const org = getOrganizationWithIdeas(orgSlug);
  if (!org) return undefined;
  const subpage = org.ideas_subpages?.find((sp) => sp.slug === subpageSlug);
  if (!subpage) return undefined;
  return { org, subpage };
}

export function getTagStats(
  type: "tech" | "topic"
): TagCount[] {
  const counts = new Map<string, number>();
  const field = type === "tech" ? "tech_tags" : "topic_tags";

  for (const org of getOrganizations()) {
    for (const tag of org[field]) {
      counts.set(tag, (counts.get(tag) || 0) + 1);
    }
  }

  return Array.from(counts.entries())
    .map(([tag, count]) => ({ tag, count }))
    .sort((a, b) => b.count - a.count);
}

export function getStats() {
  const orgs = getOrganizations();
  const techTags = new Set<string>();
  const topicTags = new Set<string>();

  for (const org of orgs) {
    for (const t of org.tech_tags) techTags.add(t);
    for (const t of org.topic_tags) topicTags.add(t);
  }

  return {
    totalOrgs: orgs.length,
    totalIdeas: orgs.filter((o) => o.has_ideas).length,
    totalTechTags: techTags.size,
    totalTopicTags: topicTags.size,
  };
}
