import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft, ExternalLink, FileText } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";
import { IdeasRenderer } from "@/components/ideas/ideas-renderer";
import { IdeasToc } from "@/components/ideas/ideas-toc";
import { getOrganizationWithIdeas, getIdeasSlugs } from "@/lib/data";

interface PageProps {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  return getIdeasSlugs().map((slug) => ({ slug }));
}

export async function generateMetadata({
  params,
}: PageProps): Promise<Metadata> {
  const { slug } = await params;
  const org = getOrganizationWithIdeas(slug);
  if (!org) return { title: "Not Found" };
  return {
    title: `${org.name} — Project Ideas`,
    description: `GSoC 2026 project ideas for ${org.name}. ${org.tagline}`,
  };
}

export default async function IdeasPage({ params }: PageProps) {
  const { slug } = await params;
  const org = getOrganizationWithIdeas(slug);
  if (!org || !org.ideas_content || org.ideas_content === "None") notFound();

  return (
    <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6">
      {/* Back link */}
      <Link
        href={`/organizations/${org.slug}`}
        className="mb-6 inline-flex items-center gap-1 text-sm text-muted-foreground hover:text-foreground"
      >
        <ArrowLeft className="h-3.5 w-3.5" />
        {org.name}
      </Link>

      {/* Header */}
      <h1 className="text-3xl font-bold">{org.name} — Project Ideas</h1>
      {org.ideas_url && (
        <div className="mt-2 flex items-center gap-4">
          <Button variant="outline" size="sm" asChild>
            <a href={org.ideas_url} target="_blank" rel="noopener noreferrer">
              View Original
              <ExternalLink className="ml-1 h-3 w-3" />
            </a>
          </Button>
        </div>
      )}

      <Separator className="my-6" />

      {/* Content with TOC */}
      <div className="flex gap-8">
        <article className="min-w-0 flex-1">
          <IdeasRenderer content={org.ideas_content} ideasUrl={org.ideas_url} />

          {/* Related sub-pages */}
          {org.ideas_subpages?.length > 0 && (
            <>
              <Separator className="my-8" />
              <section>
                <h2 className="mb-4 text-xl font-semibold">Related Pages</h2>
                <ul className="space-y-2">
                  {org.ideas_subpages.map((sp) => (
                    <li key={sp.slug}>
                      <Link
                        href={`/ideas/${org.slug}/${sp.slug}`}
                        className="inline-flex items-center gap-2 text-primary hover:underline"
                      >
                        <FileText className="h-4 w-4 shrink-0" />
                        {sp.title}
                      </Link>
                    </li>
                  ))}
                </ul>
              </section>
            </>
          )}
        </article>
        <aside className="hidden w-56 shrink-0 xl:block">
          <IdeasToc content={org.ideas_content} />
        </aside>
      </div>
    </div>
  );
}
