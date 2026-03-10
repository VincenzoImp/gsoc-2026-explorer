import Fuse from "fuse.js";
import type { SearchDocument } from "./types";

let fuseInstance: Fuse<SearchDocument> | null = null;
let indexPromise: Promise<SearchDocument[]> | null = null;

async function loadIndex(): Promise<SearchDocument[]> {
  const resp = await fetch("/search-index.json");
  if (!resp.ok) {
    throw new Error(`Failed to load search index: ${resp.status}`);
  }
  return resp.json();
}

export async function getSearcher(): Promise<Fuse<SearchDocument>> {
  if (fuseInstance) return fuseInstance;

  if (!indexPromise) {
    indexPromise = loadIndex();
  }

  const docs = await indexPromise;

  fuseInstance = new Fuse(docs, {
    keys: [
      { name: "name", weight: 5 },
      { name: "tagline", weight: 3 },
      { name: "tech_tags", weight: 2 },
      { name: "topic_tags", weight: 2 },
      { name: "description", weight: 1 },
      { name: "ideasSnippet", weight: 0.5 },
    ],
    threshold: 0.2,
    includeMatches: true,
    includeScore: true,
    ignoreLocation: true,
    minMatchCharLength: 2,
  });

  return fuseInstance;
}
