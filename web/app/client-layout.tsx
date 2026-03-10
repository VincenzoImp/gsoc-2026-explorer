"use client";

import { useState } from "react";
import { ThemeProvider } from "next-themes";
import { NuqsAdapter } from "nuqs/adapters/next/app";
import { Header } from "@/components/layout/header";
import { Footer } from "@/components/layout/footer";
import { CommandSearch } from "@/components/search/command-search";
import { BackToTop } from "@/components/shared/back-to-top";

export function ClientLayout({ children }: { children: React.ReactNode }) {
  const [searchOpen, setSearchOpen] = useState(false);

  return (
    <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
      <NuqsAdapter>
        <div className="flex min-h-dvh flex-col">
          <Header onSearchOpen={() => setSearchOpen(true)} />
          <main className="flex-1">{children}</main>
          <Footer />
        </div>
        <CommandSearch open={searchOpen} onOpenChange={setSearchOpen} />
        <BackToTop />
      </NuqsAdapter>
    </ThemeProvider>
  );
}
