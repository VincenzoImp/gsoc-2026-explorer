# Upgrade XML logger to XML 1.1

**Parent:** checkstyle — Project Ideas
**Source:** https://github.com/checkstyle/checkstyle/issues/5168
**Scraped:** 2026-02-22T23:28:47.592322

---

## Upgrade XML logger to XML 1.1

**Labels:** approved

Identified at https://github.com/checkstyle/checkstyle/pull/5163#issuecomment-333160165 ,

I have created the issue with maven-checkstyle-plugin at https://issues.apache.org/jira/browse/MCHECKSTYLE-342  still open and blocking our upgrade.

We need to upgrade our XML output to 1.1 to support escaping non-printable characters like hex 0x01 and 0x02 found in openjdk projects.

Before we can upgrade though, we must have maven-checkstyle-plugin ugpgrade their support of this as they won't accept the newer version of XML.
> [ERROR] Failed to execute goal org.apache.maven.plugins:maven-checkstyle-plugin:2.17:check (default-cli) on project postgresql: Unable to read Checkstyle results xml: /pipeline/source/pgjdbc/pgjdbc/target/checkstyle-result.xml: only 1.0 is supported as <?xml version not '1.1' (position: START_DOCUMENT seen <?xml version="1.1"... @1:19) -> [Help 1]

