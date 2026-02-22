import fs from "node:fs";
import path from "node:path";

interface IdeaSubpage {
  slug: string;
  title: string;
  source_url: string;
  content: string;
}

interface OrgWithIdeas {
  name: string;
  slug: string;
  tagline: string;
  description: string;
  ideas_content: string | null;
  ideas_subpages: IdeaSubpage[];
  tech_tags: string[];
  topic_tags: string[];
}

interface SearchDocument {
  slug: string;
  name: string;
  tagline: string;
  description: string;
  ideasSnippet: string;
  tech_tags: string[];
  topic_tags: string[];
  subpageSlug?: string;
  orgName?: string;
}

const DATA_DIR = path.join(__dirname, "..", "..", "data");
const OUTPUT_PATH = path.join(__dirname, "..", "public", "search-index.json");

function cleanForSearch(markdown: string, maxLen: number): string {
  let text = markdown;
  text = text.replace(/!\[([^\]]*)\]\([^)]*\)/g, "");          // images
  text = text.replace(/\[([^\]]*)\]\([^)]*\)/g, "$1");         // links -> text
  text = text.replace(/<[^>]+>/g, "");                          // HTML tags
  text = text.replace(/https?:\/\/\S+/g, "");                  // bare URLs
  text = text.replace(/[*_]{1,3}([^*_]+)[*_]{1,3}/g, "$1");   // bold/italic
  text = text.replace(/^#{1,6}\s+/gm, "");                     // heading markers
  text = text.replace(/```[\s\S]*?```/g, "");                  // code blocks
  text = text.replace(/`([^`]+)`/g, "$1");                     // inline code
  text = text.replace(/\n{3,}/g, "\n\n");                       // collapse newlines
  text = text.replace(/[ \t]+/g, " ");                          // collapse spaces
  return text.trim().slice(0, maxLen);
}

function main() {
  console.log("Generating search index...");

  const raw = fs.readFileSync(
    path.join(DATA_DIR, "organizations_with_ideas.json"),
    "utf-8"
  );
  const orgs: OrgWithIdeas[] = JSON.parse(raw);

  const index: SearchDocument[] = orgs.map((org) => {
    const mainSnippet =
      org.ideas_content && org.ideas_content !== "None"
        ? cleanForSearch(org.ideas_content, 1500)
        : "";
    const subpageTitles = (org.ideas_subpages ?? [])
      .map((sp) => sp.title)
      .join(" ");
    const ideasSnippet = subpageTitles
      ? `${mainSnippet} ${subpageTitles}`.trim()
      : mainSnippet;

    return {
      slug: org.slug,
      name: org.name,
      tagline: org.tagline,
      description: cleanForSearch(org.description, 500),
      ideasSnippet,
      tech_tags: org.tech_tags,
      topic_tags: org.topic_tags,
    };
  });

  // Add sub-page documents
  let subpageCount = 0;
  for (const org of orgs) {
    for (const sp of org.ideas_subpages ?? []) {
      index.push({
        slug: org.slug,
        subpageSlug: sp.slug,
        orgName: org.name,
        name: sp.title,
        tagline: "",
        description: cleanForSearch(sp.content, 500),
        ideasSnippet: "",
        tech_tags: [],
        topic_tags: [],
      });
      subpageCount++;
    }
  }

  fs.mkdirSync(path.dirname(OUTPUT_PATH), { recursive: true });
  fs.writeFileSync(OUTPUT_PATH, JSON.stringify(index));

  const sizeKB = (Buffer.byteLength(JSON.stringify(index)) / 1024).toFixed(0);
  console.log(
    `Search index generated: ${index.length} documents (${orgs.length} orgs, ${subpageCount} sub-pages), ${sizeKB} KB`
  );
  console.log(`Written to: ${OUTPUT_PATH}`);
}

main();
