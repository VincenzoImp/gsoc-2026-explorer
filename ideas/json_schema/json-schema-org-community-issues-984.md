# 984

**Parent:** JSON Schema — Project Ideas
**Source:** https://github.com/json-schema-org/community/issues/984
**Scraped:** 2026-02-22T23:28:47.586094

---

## GSoC 2026: JSON Schema Compatibility Checker — Detect Breaking Changes Between Schema Versions

**Labels:** gsoc, Status: Accepted

**Project title**
JSON Schema Compatibility Checker — Detect Breaking Changes Between Schema Versions

**Brief Description**
<!-- 2-5+ sentences -->
JSON Schema is great at validating data, but it has no way to answer a critical question: **"Will this schema change break existing data?"**

When teams evolve their schemas in production — adding a required field, tightening a constraint, or removing an enum value — they often discover problems only after deployment. Existing data that was valid suddenly fails validation. APIs break. Incidents happen.

Other schema ecosystems solved this years ago:
- **Protobuf** has [`buf breaking`](https://buf.build/docs/breaking/) with 53 compatibility rules
- **Avro** has [Schema Registry](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html) with built-in backward/forward compatibility checking

JSON Schema has no official tool for this. The closest alternatives ([getsentry/json-schema-diff](https://github.com/getsentry/json-schema-diff), [json-schema-diff on npm](https://www.npmjs.com/package/json-schema-diff)) are self-described as "work-in-progress" with incomplete keyword coverage.

This project would create a **focused compatibility checker** — a CLI tool and library that performs a semantic **comparison of two schema versions** and reports exactly what changed and whether it's safe and whether it breaks backward or forward compatibility.

Output formats: Human-readable (CLI), machine-readable JSON (API)


**Relationship to #969:**
This proposal complements @jagpreetrahi's SchemaShift (#969). While #969 focuses on generating migration code, this project focuses purely on **detection**. As @jviotti noted in #969, combining both detection and migration "might be too much" for a single project. A focused detection tool can serve as the foundation that migration tools build upon.

In short:
- #969 focuses on migration (fixing the data).
- This Project focuses on detection (identifying the break). By separating concerns, we ensure the detection engine is lightweight, reliable, and can be used by other tools (including SchemaShift) as a dependency.


**Expected Outcomes**
- A TypeScript/JavaScript library that compares two JSON Schema versions and returns a structured compatibility report (breaking changes, warnings, safe changes)

- A CLI tool with human-readable output showing exactly what changed, where, and why it matters

- **20+ semantic compatibility rules** mapped from industry standards (`buf breaking`, `Confluent`):
  - Type changes (widening/narrowing)
  - Required field additions/removals
  - Enum value additions/removals
  - Constraint changes (`minLength`, `maxLength`, `minimum`, `maximum`, `pattern`)
  - Composition keyword changes (`allOf`, `anyOf`, `oneOf`)
  - `$ref` resolution and circular reference handling

- Documentation with compatibility matrix
- npm package published to @json-schema-org scope

### Stretch Goals (if time permits)

- **GitHub Action** for automated PR compatibility checks
- Extended draft support (2019-09, Draft-06, Draft-04)
- Performance benchmarks and optimization for large schema sets

---

**Skills Required**

- JavaScript/TypeScript proficiency
- Understanding of JSON Schema keywords across drafts (draft-07, 2019-09, 2020-12)
- Familiarity with tree traversal and comparison algorithms
- Experience writing CLI tools and test suites
- Ability to read and interpret specifications (JSON Schema spec, relevant RFCs)

---


**Mentors**

- @thclark -  as Mentor
- @jviotti  - as Co-mentor

And Open to additional TSC members or experienced contributors.

**Expected Difficulty**
Medium. I think as of.

**Expected Time Commitment**
<!-- 175 or 350 hour -->
**90 hours** (Small project)



### Why This Matters

1. **Real production need** — **Teams choose Protobuf over JSON Schema** partly because of missing compatibility tooling

2. **Existing tools are incomplete** — getsentry/json-schema-diff says "use as best-effort only"

3. **Addresses TSC-identified gap**: As noted in #969 discussion, a focused detection tool is the missing foundation for schema evolution workflows

4. **Benefits the whole ecosystem** — Every validator user, every CI pipeline, every team maintaining schemas

---

### References

- Buf breaking change detection: https://buf.build/docs/breaking/
- Confluent Schema Registry compatibility: https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html
- Existing incomplete tools:
  - https://github.com/getsentry/json-schema-diff
  - https://www.npmjs.com/package/json-schema-diff
- Related proposal: #969 (SchemaShift — complementary migration tool)
- JSON Schema canonicalization concepts: #857 (GSoC 2025, closed)

