# issue

**Parent:** checkstyle — Project Ideas
**Source:** https://github.com/checkstyle/checkstyle/issues/17449
**Scraped:** 2026-02-22T23:28:47.591663

---

## Add missing property examples to XDocs for Checkstyle Checks

**Labels:** approved, miscellaneous, good second issue

Checkstyle validates that all configurable properties of checks are demonstrated in the XDocs examples. However, some properties are currently missing from the examples and are temporarily suppressed in the test `XdocsExampleFileTest.java.`

This issue aims to allow new contributors to improve test coverage by adding valid <property> entries to the appropriate Xdocs example files (found under `src/xdocs-examples/resources-noncompilable/... or src/xdocs-examples/resources/...`) and removing the corresponding entry from the suppression list once the example is added.

- Add valid Xdoc example usages (i.e., in /*xml blocks) for the listed properties.
- Ensure that the test `XdocsExampleFileTest` passes without relying on suppression for the properties once they are added.
- Clean up the suppression list by removing each property from the `SUPPRESSED_PROPERTIES_BY_CHECK` map when it’s properly covered.

Preferable if single Pull Request covers whole Check.

most accurate list of suppressions to fix is at https://github.com/checkstyle/checkstyle/blob/master/src/test/java/com/puppycrawl/tools/checkstyle/internal/XdocsExampleFileTest.java#L53


example on how list looked in past:
https://github.com/checkstyle/checkstyle/blob/9a9d6137cf52fa343649e8a91f6159ed69ff766e/src/test/java/com/puppycrawl/tools/checkstyle/internal/XdocsExampleFileTest.java#L51-L56


Example of expected update: https://github.com/checkstyle/checkstyle/pull/17844

ATTENTION: please keep all examples same by java code and different only by trailing comment among all example , see all details and images at https://github.com/checkstyle/checkstyle/issues/13345

