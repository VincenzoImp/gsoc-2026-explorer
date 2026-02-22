# #16556

**Parent:** Oppia Foundation — Project Ideas
**Source:** https://github.com/oppia/oppia/issues/16556
**Scraped:** 2026-02-22T23:28:47.620466

---

## No schema migration pipeline for suggestions (translations/questions)

**Labels:** bug

### Describe the bug

When there is a schema update, we need to make sure that the schema of the existing models are correctly migrated.

### Steps To Reproduce
1. Submit a few Question suggestions for review via the Contributor dashboard.
2. Write a new state schema migration.
3. Observe that the questions in review are not migrated to the latest schema.

### Expected Behavior
When there is a scehma update, the submitted questions need to be automatically migrated to the latest schema on the fly.


