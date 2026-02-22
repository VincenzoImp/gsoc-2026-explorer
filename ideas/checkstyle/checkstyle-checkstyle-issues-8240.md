# module-info.java support

**Parent:** checkstyle — Project Ideas
**Source:** https://github.com/checkstyle/checkstyle/issues/8240
**Scraped:** 2026-02-22T23:28:47.591505

---

## Java Grammar: module-info.java support

**Labels:** discussion ongoing, antlr

Original issue https://github.com/checkstyle/checkstyle/issues/3059

We should extend our grammar to support module-info.java

- there are may be comments and Javadoc. We should validate them.
- there may be annotations. We have checks for annotations.
- we may add checks specifically for modules. For example, `ModuleName` check.

