# Convert sevntu-checkstyle-check to ant run

**Parent:** checkstyle — Project Ideas
**Source:** https://github.com/checkstyle/checkstyle/issues/5385
**Scraped:** 2026-02-22T23:28:47.592190

---

## Convert sevntu-checkstyle-check to ant run

**Labels:** approved, miscellaneous

See https://issues.apache.org/jira/browse/MCHECKSTYLE-346 .
We need to deprecate all usage of `maven-checkstyle-plugin` so we can start implementing backward breaking changes.

We must convert our `sevntu-checkstyle-check` run to an ant run.
Specified section: https://github.com/checkstyle/checkstyle/blob/06ff5677fa5a19afe3f55078fff79ead61068a51/pom.xml#L558-L597

