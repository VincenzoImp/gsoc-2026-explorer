# https://gcc.gnu.org/install/

**Parent:** GNU Compiler Collection (GCC) — Project Ideas
**Source:** https://gcc.gnu.org/install/
**Scraped:** 2026-02-22T23:28:47.608973

---

The latest version of this document is always available at
[https://gcc.gnu.org/install/](https://gcc.gnu.org/install/).
It refers to the current development sources, instructions for
specific released versions are included with the sources.

This document describes the generic installation procedure for GCC as well as detailing some target specific installation instructions.

GCC includes several components that previously were separate distributions with their own installation instructions. This document supersedes all package-specific installation instructions.

*Before* starting the build/install procedure please check the
[host/target specific installation notes](https://gcc.gnu.org/specific.html).
We recommend you browse the entire generic installation instructions before
you proceed.

The installation procedure itself is broken into five steps.

Please note that GCC does not support ‘`make uninstall`’ and probably
won’t do so in the near future as this would open a can of worms. Instead,
we suggest that you install GCC into a directory of its own and simply
remove that directory when you do not need that specific version of GCC
any longer, and, if shared libraries are installed there as well, no
more binaries exist that use them.


[Return to the GCC Installation page](https://gcc.gnu.org/index.html)

Copyright © 1988-2026 Free Software Foundation, Inc.

Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3 or
any later version published by the Free Software Foundation; with no
Invariant Sections, the Front-Cover texts being (a) (see below), and
with the Back-Cover Texts being (b) (see below). A copy of the
license is included in the section entitled “[GNU
Free Documentation License](https://gcc.gnu.org/gfdl.html)”.

(a) The FSF’s Front-Cover Text is:

A GNU Manual

(b) The FSF’s Back-Cover Text is:

You have freedom to copy and modify this GNU Manual, like GNU software. Copies published by the Free Software Foundation raise funds for GNU development.

For questions related to the use of GCC,
please consult these web pages and the
[GCC manuals](https://gcc.gnu.org/onlinedocs/). If that fails,
the [gcc-help@gcc.gnu.org](mailto:gcc-help@gcc.gnu.org)
mailing list might help.
Comments on these web pages and the development of GCC are welcome on our
developer list at [gcc@gcc.gnu.org](mailto:gcc@gcc.gnu.org).
All of [our lists](https://gcc.gnu.org/lists.html)
have public archives.

Copyright (C)
[Free Software Foundation, Inc.](https://www.fsf.org)
Verbatim copying and distribution of this entire article is
permitted in any medium, provided this notice is preserved.

These pages are
[maintained by the GCC team](https://gcc.gnu.org/about.html).
Last modified 2026-01-02.
