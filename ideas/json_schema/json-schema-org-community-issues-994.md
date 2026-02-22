# 994

**Parent:** JSON Schema — Project Ideas
**Source:** https://github.com/json-schema-org/community/issues/994
**Scraped:** 2026-02-22T23:28:47.585966

---

## GSoC 2026 - Unify the test suite

**Labels:** gsoc, Status: Accepted

## Unify the test suite

## Brief Description

In the [official test suite](https://github.com/json-schema-org/JSON-Schema-Test-Suite/), we don't manage the tests for different versions of JSON Schema very well. Each time there's a new release, we make a copy of the previous version and make updates to that copy. Because of this, we have multiple copies of most of the tests and every time we need to add a new test, we usually have to add a copy in several places.

The [annotations test suite](https://github.com/json-schema-org/JSON-Schema-Test-Suite/tree/main/annotations) takes a different approach. Tests have a `compatibility` property indicting which versions of JSON Schema the test applies to. That allows test runners to filter the tests to which one's apply to them.

The goal of this project is to collapse the per version validation tests into one test suite using a similar approach to the annotations test suite. This will allow us to manage tests in a single suite with no more copies of identical tests.

## Expected Outcomes

- A single test suite for all versions of JSON Schema
- No more copies of tests
- Tests can be easily filtered by test runners to the ones that apply to them
- Update any scripts/action in the test suite repo to use the new suite
- Update bowtie to use the new suite
- Update bowtie implementation test runners to use the new suite

## Skills Required

- Good attention to detail
- Ability to work in unfamiliar programming languages. (Updating bowtie implementation test runners.)

## Mentors

@jdesrosiers and @Julian as co-mentor


## Expected Difficulty

small

## Expected Time Commitment

90 hours

