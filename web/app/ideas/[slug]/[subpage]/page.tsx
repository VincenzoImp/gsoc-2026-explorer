import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft, ExternalLink } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";
import { IdeasRenderer } from "@/components/ideas/ideas-renderer";
import { IdeasToc } from "@/components/ideas/ideas-toc";
import { getSubpage, getSubpageSlugs } from "@/lib/data";

interface PageProps {
  params: Promise<{ slug: string; subpage: string }>;
}

export async function generateStaticParams() {
  return getSubpageSlugs();
}

export async function generateMetadata({
  params,
}: PageProps): Promise<Metadata> {
  const { slug, subpage } = await params;
  const result = getSubpage(slug, subpage);
  if (!result) return { title: "Not Found" };
  return {
    title: `${result.subpage.title} — ${result.org.name}`,
    description: `${result.subpage.title}. GSoC 2026 project ideas for ${result.org.name}.`,
  };
}

export default async function SubpagePage({ params }: PageProps) {
  const { slug, subpage } = await params;
  const result = getSubpage(slug, subpage);
  if (!result) notFound();

  const { org, subpage: sp } = result;

  return (
    <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6">
      {/* Breadcrumb */}
      <div className="mb-6 flex items-center gap-1 text-sm text-muted-foreground">
        <Link
          href={`/ideas/${org.slug}`}
          className="inline-flex items-center gap-1 hover:text-foreground"
        >
          <ArrowLeft className="h-3.5 w-3.5" />
          {org.name} — Project Ideas
        </Link>
      </div>

      {/* Header */}
      <h1 className="text-3xl font-bold">{sp.title}</h1>
      {sp.source_url && (
        <div className="mt-2 flex items-center gap-4">
          <Button variant="outline" size="sm" asChild>
            <a href={sp.source_url} target="_blank" rel="noopener noreferrer">
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
          <IdeasRenderer content={sp.content} ideasUrl={sp.source_url} />
        </article>
        <aside className="hidden w-56 shrink-0 xl:block">
          <IdeasToc content={sp.content} />
        </aside>
      </div>
    </div>
  );
}
