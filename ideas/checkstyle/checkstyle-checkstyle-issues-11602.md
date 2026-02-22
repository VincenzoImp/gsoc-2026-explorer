# Convert regressions that use maven-checkstyle-plugin to CLI based

**Parent:** checkstyle — Project Ideas
**Source:** https://github.com/checkstyle/checkstyle/issues/11602
**Scraped:** 2026-02-22T23:28:47.592258

---

##  Convert regressions that use maven-checkstyle-plugin to CLI based

**Labels:** approved, miscellaneous, CI

See https://issues.apache.org/jira/browse/MCHECKSTYLE-346 .
We need to deprecate all usage of maven-checkstyle-plugin so we can start implementing backward breaking changes.

A lot of regressions use maven-checkstyle-plugin to run checkstyle on the projects and will have to be converted to using the raw CLI.
Example is anything using `checkstyle:check` via a maven command. https://github.com/checkstyle/checkstyle/search?l=Shell&q=%22checkstyle%3Acheck%22

This may be difficult for some projects as they use custom dependencies. We may have to start discussions with the project owners on how we can best do this and disable them until we can get things worked out.

breaking compatibility that plugin is rely on:
https://github.com/checkstyle/checkstyle/issues/12873

