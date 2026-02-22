# Project Ideas

**Parent:** JSON Schema — Project Ideas
**Source:** https://github.com/json-schema-org/community/issues?q=is%3Aopen+label%3Agsoc+sort%3Acreated-desc
**Scraped:** 2026-02-22T23:28:47.585761

---

## #1009: Developer-Friendly Schema Builder and Type Generator for JSON Schema

## **Project Title**

🚀 Developer-Friendly Schema Builder and Type Generator for JSON Schema (Node.js Ecosystem)

---

## **Brief Description**

### 📌 Problem

- JSON Schema is powerful and widely adopted.
- However, writing raw JSON Schema is:
  - Verbose
  - Repetitive
  - Hard to read for backend developers
  - Boilerplate-heavy

Developers frequently repeat patterns like:
- `"type": "string"`
- `"type": "object"`
- `"properties"`
- `"required"`

This reduces readability and slows down development.

---

### 💡 Proposed Solution

Build a **developer-friendly schema builder library** for Node.js and TypeScript that:

- Provides a clean DSL (Domain-Specific Language)
- Reduces repetition
- Improves readability
- Internally generates valid JSON Schema (Draft 2020-12 compliant)
- Optionally generates TypeScript types

The project focuses on improving developer ergonomics while remaining fully compliant with the JSON Schema specification.

---

## **Example Comparison**

### 🔹 Current JSON Schema (Verbose)

```json
{
  "type": "object",
  "required": ["name", "ingredients"],
  "properties": {
    "name": { "type": "string" },
    "ingredients": {
      "type": "array",
      "items": { "type": "string" }
    }
  }
}
```

---

### 🔹 Proposed DSL Version (Cleaner & Developer-Friendly)

```ts
const Recipe = schema.object({
  name: schema.string().required(),
  ingredients: schema.array(schema.string()).required()
})
```

---

### 🔹 Generated Output (Auto JSON Schema)

```json
{
  "type": "object",
  "required": ["name", "ingredients"],
  "properties": {
    "name": { "type": "string" },
    "ingredients": {
      "type": "array",
      "items": { "type": "string" }
    }
  }
}
```

---

## **Expected Outcomes**

### 🛠 Core Deliverables

- A schema builder library for Node.js / TypeScript
- Draft 2020-12 compliant JSON Schema generation
- Automatic TypeScript type generation

---

### 📦 Feature Support (Initial Scope)

- `object`
- `array`
- `string`
- `number`
- `boolean`
- `required`
- `enum`
- `minimum`
- `maximum`
- Basic composition:
  - `oneOf`
  - `anyOf`

---

### 🧰 Additional Deliverables

- Optional CLI tool:
  - Generate schema files
  - Export JSON Schema
  - Inspect generated schemas
- Clear documentation
- Usage examples
- Unit testing suite
- Compatibility testing with validators (e.g., Ajv)

---

## **Skills Required**

- JavaScript
- TypeScript
- Node.js
- Understanding of JSON Schema specification
- Familiarity with Ajv or similar validators
- Unit testing (Jest / Vitest)
- Basic CLI development knowledge

---

## **Mentors**

To be assigned by JSON Schema maintainers.

---

## **Expected Difficulty**

Medium to Hard

- Requires understanding of JSON Schema internals
- Requires spec compliance awareness
- Requires strong TypeScript modeling and API design

---

## **Expected Time Commitment**

350 hours

---

## #1004: Open Community Working Meeting 2026-03-16 - 13:00 PT

**Labels:** Working Meeting

---
name: Open Community Working Meeting
about: Regular Open Community Working Meetings Issue - This template is for those setting up an OCWM only.
---

# Open Community Working Meeting 2022-MM-DD - 13:00 PT

Google Meet joining info - Video call link: https://meet.google.com/raz-ptdn-ewf

You can find these events scheduled on our **[JSON Schema Community Calendar](https://calendar.google.com/calendar/u/0/embed?src=info@json-schema.org)**.

To add the events to your Google Calendar, use the link found in the bottom right of the above calendar.
To add the events to another calendar, use the provided [ics/ical file](https://calendar.google.com/calendar/ical/info%40json-schema.org/public/basic.ics).

**Meeting accessibility**:
- We would like to record the meeting for future reference and for those who are not able to attend in person. 
- We encourage you to challenge any language or behaviour that is harmful or not inclusive during this meeting. 
- We look forward to your participation, but please consider... 
  - Remaining on mute when not speaking. 
  - Use the Zoom meeting raised hand feature to notify you wish to speak. 
- [JSON Schema Code of Conduct](https://github.com/json-schema-org/.github/blob/main/CODE_OF_CONDUCT.md)

Agenda: Compiling!

| Topic | Owner | Decision/NextStep |
| -- | -- | -- |
| Review last call's action items  | [facilitator] |
| [TOPIC] [IssuePRDiscussion] | [owner] |
<!-- | [TOPIC] [IssuePRDiscussion] | [owner] | -->

You can have a PR or an issue added to this agenda by just adding them the `agenda` label.

AOB?
If you want to discuss any other business not on the agenda, please add comments during the meeting.
If we do not complete the agenda, your discussion item will likely be rolled over to the next call.

Action items:
- [ ]

Notes:

Agenda Items rolling over:
- list

Recording: [link]

---

## #995: GSoC 2026: Enhancing the JSON Schema Community Page with Contributor Recognition and Activity Insights

## Project Title  
**Enhancing the JSON Schema Community Page with Contributor Recognition and Activity Insights**

---

## Brief Description  

The JSON Schema community page currently provides static information about the community, but it does not surface dynamic insights about contributor activity or recognize ongoing contributions across repositories.

This project proposes enhancing the community page by integrating contribution data from GitHub and presenting it in a clear, accessible dashboard. The goal is to improve transparency, recognize contributors, and strengthen community engagement—without replacing GitHub or existing communication platforms.

This idea is proposed for mentor consideration and can be refined based on feedback.

---

## Expected Outcomes  

By the end of the project, the following outcomes are expected:

- A redesigned or extended **Community page** that displays dynamic contributor information.
- A contributor listing with metrics such as:
  - Pull requests opened and merged  
  - Issues opened and closed  
  - Review activity (where applicable)
- Simple leaderboards highlighting:
  - Active contributors  
  - Reviewers  
  - First-time contributors
- Recognition indicators (e.g. badges or labels) to acknowledge consistent and impactful contributions.
- Clear links back to GitHub profiles and relevant PRs/issues.
- Clean, accessible UI consistent with the existing json-schema.org website.

---

## Skills Required  

- JavaScript (ES6+)
- React (or similar modern frontend framework)
- Git & GitHub workflow (issues, pull requests, reviews)
- GitHub REST API usage
- JSON Schema (for validating API responses)
- HTML & CSS (responsive and accessible UI)

---

## Expected Difficulty  

**Medium**

The project focuses on frontend development and API integration, without requiring complex backend infrastructure. The main challenges involve data aggregation, pagination, and presenting information in a clear and maintainable way.

---

## Expected Time Commitment  

**Medium (175–350 hours)**  
Suitable for completion within the standard GSoC coding period (10–22 weeks).

---

## Additional Notes  

- This project intentionally focuses on correctness, usability, and community impact rather than advanced performance optimizations.
- The scope can be adjusted based on mentor feedback and community priorities.
- The implementation can start with a limited set of repositories and be expanded incrementally.

---

## Mentor(s)  

**Seeking mentor(s) from the JSON Schema community**  
This project idea is open for adoption and refinement by interested mentors.

---

###  Closing Note  

This proposal is shared with the intention of contributing positively to the JSON Schema community. Feedback, suggestions, and scope adjustments from maintainers and mentors are very welcome.

---

## #994: GSoC 2026 - Unify the test suite

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

---

## #993: Intelligent Schema Migration & Modernization Assistant

**Labels:** gsoc

# GSoC 2025: Intelligent Schema Migration & Modernization Assistant

## Project Overview

Build an AI-powered tool using **LangGraph** and **MCP (Model Context Protocol)** that automates JSON Schema migration between versions, detects anti-patterns, consolidates duplicate schemas, and suggests modern best practices.

---

## Problem Statement

Organizations struggle with:
- **Manual migration** from older JSON Schema drafts (Draft-04, Draft-06, Draft-07) to modern versions (2019-09, 2020-12)
- **Schema sprawl** across microservices with duplicated and inconsistent schemas
- **Anti-patterns** that accumulate over time (overly permissive validation, missing metadata, poor structure)
- **Lack of intelligent automation** beyond basic linting
- **Technical debt** from maintaining hundreds of outdated schemas

Manual migration of complex schemas can take hours per schema, and refactoring large repositories can take weeks.

---

## Project Goals

### Core Functionality

1. **Automated Version Migration**
   - Migrate schemas between any JSON Schema draft versions
   - Handle keyword deprecations (`id` → `$id`, `definitions` → `$defs`)
   - Detect opportunities for new features (`unevaluatedProperties`, `$dynamicRef`)
   - Ensure backward compatibility

2. **Anti-Pattern Detection & Refactoring**
   - Identify common problems: overly permissive `additionalProperties`, missing descriptions, security issues
   - Suggest and apply automatic fixes
   - Integrate with existing Sourcemeta linting tools (GSoC 2025 project)
   - Provide severity classification (error/warning/info)

3. **Schema Consolidation**
   - Detect duplicate and similar schemas across repositories
   - Merge compatible schemas into canonical versions
   - Generate proper `$ref` relationships
   - Update all references automatically

4. **OpenAPI Integration**
   - Extract schemas from OpenAPI specifications
   - Migrate OpenAPI-embedded schemas
   - Remove OpenAPI-specific extensions for reusable schemas

5. **MCP Server Implementation**
   - Expose all functionality as MCP tools for reusability
   - Enable integration with AI assistants like Claude
   - Support programmatic access via MCP protocol

---

## Technical Architecture

### Technology Stack

**Core:**
- **Python 3.11+** - Primary language
- **LangGraph** - Agentic workflow orchestration
- **MCP SDK (Python)** - Tool server implementation
- **LangChain** - LLM integration for intelligent analysis

**JSON Schema:**
- **jsonschema** - Validation
- **Sourcemeta linting tools** - Integration with existing quality tools
- **json-schema-ref-parser** - Reference resolution

**AI/LLM:**
- **Claude API** (Anthropic) - Primary LLM for analysis
- **Vector embeddings** - Semantic similarity detection

### System Components

```
┌─────────────────────────────────────┐
│     User Interfaces                 │
│  (CLI, Web UI, GitHub Action)       │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│

*[truncated]*

---

## #991: GSoC 2026: Replacement for vscode-json-languageservice

**Labels:** gsoc, Status: Accepted

# Replacement for vscode-json-languageservice

## Brief Description

The goal of this project is to make a drop-in replacement for [vscode-json-languageservice](https://github.com/microsoft/vscode-json-languageservice) based on [@hyperjump/json-schema](https://github.com/hyperjump-io/json-schema).

`vscode-json-languageservice` is a language server for JSON that allows you to associate a JSON Schema with a JSON document. It uses the schema to provide useful features like code completion as well as validation. This language server is used not just in VSCode, but in many other editors and IDEs as well, so it's impact on our community is huge.

The problem is that Mircosoft doesn't seem interested in maintaining this language server. They are limited to draft-07 support and are missing support for some useful features including bundled schemas. Although it's impossible to prove, we believe that this is the biggest thing in our ecosystem restricting users from upgrading to more current versions of JSON Schema. Getting this updated could make a huge impact for the JSON Schema community.

Why not just contribute to vscode-json-languageservice? There are a couple reasons. The biggest reason is to remove our dependency on Microsoft. If our community is maintaining this project, it's easier to keep things up-to-date than if we have to depend on Microsoft. The other reason is that their implementation needs a lot of work to handle the features it's missing and I believe it would be easier to start with a fully functional validator and clone the editor features than it would be to try to improve their current validator.

## Expected Outcomes

- Support for all editor features vscode-json-languageservice supports including their custom keywords.
- Full support for draft-04 through draft-2020-12 including features not currently supported by vscode-json-languageserver (including `$id` and `$dynamicRef`).
- Support for VSCode
- **NOT IN SCOPE** -- Support for other editors including Neovim or Monaco, (But definitely a must have for later)
- **NOT IN SCOPE** -- Support for editing JSON Schema documents other than as plain JSON documents. (That's the subject of [@hyperjump/json-schema-language-tools](https://github.com/hyperjump-io/json-schema-language-tools))
- **NOT IN SCOPE** -- Supporting other media type like YAML. (But let's definitely do this later!)

**Skills Required**

- Strong knowledge of JSON Schema
- Experience with the low-level features of `@hyperjump/json-schema`. (Such as working with ASTs)
- The ability to analyze the feature set of an existing application.
- Experience working with the Language Server Protocol (LSP)
- Experience with effective testing. (Experience with TDD is a big plus)
- Willingness to pair program.

## Mentors

@jdesrosiers and @mwadams as co-mentor

## Expected Difficulty

large

## Expected Time Commitment

350 hour

---

## #990: GSOC 2026:  JSON Schema Semantic Diff and Migration Assistant

**Labels:** gsoc

### JSON Schema Semantic Diff and Migration Assistant

### Problem
At the moment, there is no standard tool that helps developers understand the semantic impact of changes made to a JSON Schema.
When schemas evolve, developers often struggle to answer important questions such as:
Is this change backward compatible?
Which existing data will fail after this change?
Which exact part of the schema is affected?
How can we safely migrate existing systems?
Currently, developers rely mostly on textual tools like git diff, which only show line-by-line differences but do not explain what those changes mean in terms of validation behaviour.
As a result, even small schema updates can introduce breaking changes that are only discovered later during testing or, in some cases, directly in production.

### Proposed Solution

This project proposes building a Schema Diff Engine that compares two versions of a JSON Schema and explains the real meaning of the changes.
Instead of treating schemas as plain text files, the tool will understand them as validation rules and analyze how those rules have changed between versions.
The goal is to provide developers with a clear and practical understanding of the impact of schema updates.

### Main Features
Breaking vs Non-breaking Detection
The tool will detect common types of changes such as:
Type changes (for example, number to string)
Changes in constraints (maxLength, minimum, etc.)
Adding or removing required fields
Each change will be classified as:
Breaking
Non-breaking
Potentially breaking
This helps developers quickly understand the risk level of a schema update.

### Affected Path Reporting

For every significant change, the tool will show the exact location in the schema where it occurred.

Example:
Breaking change at /user/age  
Type changed from number to string
This makes it easy for developers to locate and understand the issue without manually searching through large schema files.

 ### Data Impact Simulation

If sample or real data is available, the tool can validate it against both schema versions and report:
Which records will fail under the new schema
How many records are affected
This provides a practical view of the impact instead of only a theoretical analysis.

### Migration Suggestions

Based on the detected changes, the tool will suggest simple migration steps, such as:
Converting data types
Adding default values for new required fields
Adjusting constraints
These suggestions help developers update their systems in a safer and more controlled way.

### Why This Project Is Useful

This tool will make schema evolution much safer and easier for developers.
It reduces the risk of breaking APIs and data pipelines and saves time spent on manual reasoning and testing.
It can be especially useful for:
                            API development
                            OpenAPI and AsyncAPI workflows
                           Data validation systems
                           Large distributed systems




*[truncated]*

---

## #987: GSOC 2026: An official online JSONSchema repository

**Labels:** gsoc

## Project title

An official online JSONSchema repository

## Brief Description

There's pypi for python, npm for javascript, why don't we have an official repository for publishing JSONSchema?

Such a thing exists but not officially: I've spent the last 3 years building [Strands](https://strands.octue.com/) - a repository for JSONSchema. It has:
- publishing workflows for schema
- organization / team management heavily inspired by GitHub
- a fully featured [compatibility checker](https://strands.octue.com/compare) which already solves https://github.com/json-schema-org/community/issues/984
- a GitHub action for [publishing and compatibility checking](https://github.com/octue/publish-strand-version) (eg allowing you to automate version bumping and publication from GitHub, and/or fail your CI on breaking changes)
- a (basic, as yet - we're focusing on getting it right with excellent UX) [visual builder](https://strands.octue.com/builder)
- [documentation](https://docs.strands.octue.com/getting-started/get-started-with-strands)

It works beautifully, but **honestly, it should belong to the community**. I'd be willing to donate the project, which means open-sourcing:
- the stack (Django backend + NextJS frontend)
- the compatibility checker (amusingly named `version-cruzer` - an in-joke for those in the know!)
- the documentation

This project will manage that open-sourcing process and adapt the existing stack to be more cost-effective and maintainable as a community product.


## Prerequisites

- [ ] Buy-in from the JSONSchema TSC to make it an official repository on json-schema.org. **This is super important because there'll be a burden of ongoing maintenance, which I'm willing to help with, but we should discuss how that'll work before attempting this project.**
- [x] Me to check the legals of open-sourcing the compatibility checker (shouldn't be a problem but need to check).

## Steps

- _Architecture._ Currently it's a split backend/frontend architecture, which suits me well, but **for a community product we'd need to avoid the eye-watering cost of Vercel**, so we'd convert it to a monorepo and serve the main views using django-vite (following the tutorial [here](https://github.com/saaspegasus/django-vite-tailwind-starter/), which will simplify auth considerably).
- _Deployment._ Currently on GCP, I'd recommend keeping the same approach. But we'd split into a separate project outside of my commercial organization, which would be owned and administered by the TSC.
- _Technical Documentation._ A community-owned product has to have clear processes in place, can't depend on my own in-house knowledge. So the process for deployment/development needs to be documented.
- _Security review._ The app uses django-allauth and django-guardian which are extremely widely used. But, we should have a policy around 2FA requirements etc, possibly introducing more features than we have now.

## Expected Outcomes

- strands application moved from strands.octue.com 

*[truncated]*

---

## #986: Visual Test Lifecycle Explorer & Capabilities Manifest for the JSON Schema Test Suite

**Labels:** gsoc

**Visual Test Lifecycle Explorer & Capabilities Manifest for the JSON Schema Test Suite**

**Brief Description**
When I started contributing to the JSON Schema Test Suite, I struggled to understand the repository structure, how tests relate to different drafts, and why some tests are optional. This project proposes a visual, tree-based way to explore tests by draft, keyword, and lifecycle state, so new contributors can quickly understand what exists, what changed, and what is missing. The goal is to make test evolution across drafts visible and easier to manage.

**Expected Outcomes**

- A visual explorer showing tests grouped by draft and feature lifecycle
- Clear visibility into added, changed, deprecated, and optional tests
- Metadata to explain why tests are optional or environment-dependent
- CI integration to keep lifecycle information up to date on PRs
- Documentation to improve contributor onboarding

**Skills Required**

- TypeScript and React
- Familiarity of JSON Schema
- GitHub workflows and CI
- Interest in developer tooling

**Mentors**
To be determined / seeking mentors.

**Expected Difficulty**
Medium

**Expected Time Commitment**
175 hours

---

## #985: GSOC 2026 : Dependency-Level Risk Signals for the JSON Schema npm Ecosystem

**Labels:** gsoc

**OSS Dependency Risk Observatory**

This project is intended to complement the broader ecosystem observability work in #980 by focusing specifically on dependency-level, longitudinal risk signals.

**Brief Description**
Modern software ecosystems rely heavily on open-source dependencies, yet dependency risk is usually evaluated only through static vulnerability scans. This overlooks broader ecosystem health signals such as maintainer activity, release staleness, contributor diversity (bus factor), and long-term sustainability.

This project proposes a lightweight, zero-cost dependency risk observability tool focused on a curated subset of npm packages, initially targeting the JSON Schema ecosystem. Instead of building a large always-on platform, the project will implement batch-based analysis that periodically collects metadata from GitHub and the npm registry, computes interpretable risk signals, and produces static, versioned datasets and reports.

The goal is to provide maintainers and contributors with reproducible, longitudinal insights into dependency health—without requiring persistent infrastructure, paid services, or ongoing operational costs.

**Expected Outcomes**
1.Curated Dependency Dataset
- Clearly defined criteria for selecting JSON Schema–related npm packages
- Package list maintained as version-controlled metadata
2. Batch Data Collection Pipeline
- Node.js tooling to fetch metadata from:
- GitHub (commits, contributors, releases)
- npm registry (downloads, versions, dependencies)
- Designed to run periodically via GitHub Actions
3. Dependency Risk Signals (Not a Heavy “Score”)
- Maintainer activity trends
- Release cadence and staleness
- Contributor count (bus-factor proxy)
- Dependency depth and centralization indicators
- Optional: known security advisories (best-effort)
4. Time-Series Snapshots
- Periodic snapshots stored as versioned JSON/CSV files
- Enables longitudinal analysis without a database
5. Static Reports & Visualizations
- Markdown summaries and Vega-Lite charts
- Focus on trends and comparative risk signals
6. Reusable Tooling
- Modular design so other ecosystems can reuse the pipeline
- Clear documentation on extending the analysis
7. Documentation
- Methodology and assumptions
- Known limitations
- Contribution guidelines

**Skills Required**
- TypeScript / JavaScript
- Node.js
- GitHub API and package registry APIs (npm)
- Data processing and modeling
- Basic knowledge of databases (PostgreSQL / SQLite)
- DevOps and automation (GitHub Actions)
- Data visualization (Grafana, Vega-Lite, D3, or similar)

**Mentors**
TBD (Open-source maintainers from the target ecosystem / organization)

**Expected Difficulty**
Medium–Hard

**Expected Time Commitment**
350 hour

---

## #984: GSoC 2026: JSON Schema Compatibility Checker — Detect Breaking Changes Between Schema Versions

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

- **GitHub Actio

*[truncated]*

---

## #983: GSOC 2026: Enhanced Interaction and Navigation in JSON Schema Studio

**Labels:** gsoc, Status: Accepted

**Enhanced Interaction and Navigation in [JSON Schema Studio](http://studio.ioflux.org/)**

**Brief Description**
**JSON Schema Studio** is an open-source tool that visualizes JSON Schemas as interactive graphs, helping developers understand and debug complex schemas. This project was part of GSoC 2025, and we successfully released the first beta this year, receiving strong and positive feedback from the community. There remains significant scope for further improvements and feature additions.

This GSoC 2026 project focuses on improving interactivity, navigation, and rendering correctness by enhancing dependency ordering, editor synchronization, collision handling, and user-driven exploration features, including collapsible nodes, bidirectional editing, and focused graph navigation.

**Expected Outcomes**
- **Topologically sorted rendering of `$defs` dependencies**: Ensure `$defs` schemas are rendered in dependency order to handle chained and recursive references correctly.
- **Validation error navigation**: When schema validation errors occur, clicking an error highlights and scrolls to the corresponding line number in the editor.
- **Edge collision resolution**: Reduce edge overlappings to improve readability in large graphs.
- **Edge-based navigation controls**: On hovering over an edge, display navigation buttons that allow users to:
  - Focus and center the source node
  - Focus and center the target node
- **Fix handle misalignment on live edits**: Ensure node sourcehandles remain correctly positioned when schemas are edited dynamically in the editor. 
- **Distinct visualization for multi-type schemas**: Clear and intuitive rendering for nodes with multiple types (e.g. `["string", "null"]`) using visual elements such as segmented styles, badges, or patterns.
- **File upload support**: Allow users to upload JSON Schema files directly into the application for instant visualization.
- **Downloadable visualization output**: Enable exporting the visualization as an image or file for documentation and sharing.

**Skills Required**
- JavaScript/TypeScript
- Reactjs
- Understanding of visualization library ([ReactFlow](https://reactflow.dev/))
- Understanding of JSON Schema

**Mentors**
@AgniveshChaubey

**Expected Difficulty**
Small

**Expected Time Commitment**
90 hrs

---

## #982: JSON Schema Editor with Real‑Time Conflict & Suggestions

**Labels:** gsoc

# **Project Title**
Smart JSON Schema Editor with Real‑Time Conflict & AI‑Powered Suggestions

## **Brief Description**
A web‑based JSON Schema authoring tool with intelligent feedback. Users can edit JSON Schemas with real‑time semantic conflict detection, receive plain‑language explanations of constraints, and get AI‑powered suggestions for improvements, helping both beginners and experienced developers produce better, error‑free schemas.

## **Expected Outcomes**
List the key deliverables and outcomes you expect by the end of the project:
- A fully functional web application for editing JSON Schema
- Real‑time validation (syntax + semantic analysis)
- AI/LLM integration that explains schema parts and offers suggestions
- UI components that show warnings, tips, and quick‑fix actions
- Optional companion extension to detect schema files in repositories

## **Skills Required**
- Frontend: HTML, CSS, JavaScript (with editor components like Monaco)
- Backend: Python, Flask (API endpoints to analyze schemas and integrate AI)
- Basic understanding of JSON Schema standards
- Optional: Experience with AI model APIs (for suggestions & explanations)

## **Mentors**
TBD

## **Expected Difficulty**
Medium  .

## **Expected Time Commitment**
250 hours

---

## #981: GSOC 2026 : Improving Invalid and Boundary Test Case Generation in Existing JSON Schema Tooling

**Labels:** gsoc

**Project title**
Improving Invalid and Boundary Test Case Generation in Existing JSON Schema Tooling

**Brief Description**
The JSON Schema ecosystem already provides several tools for generating valid JSON instances from schemas. However, systematic generation of invalid and boundary-focused test cases remains an underexplored area, despite its importance for validator authors, tooling maintainers, and API developers.
This project aims to study existing schema-to-data tools in the ecosystem, identify concrete gaps in invalid and boundary test generation, and contribute targeted improvements to one of the existing open-source projects rather than creating a new tool. By focusing on a specific hard problem instead of reinventing existing solutions, the project seeks to strengthen the ecosystem in a practical and sustainable way.

**Expected Outcomes**
- An extension to the JSON Schema Test Suite (or a dedicated companion suite) containing comprehensive invalid and boundary test cases for core JSON Schema keywords.
- Structured test cases covering:
  - type violations
  - required property failures
  - enum/const mismatches
  - numeric boundary conditions (minimum, maximum, etc.)
  - string constraints (minLength, pattern, format, etc.)
  - array and object constraint violations

- Optional metadata tagging for test cases (e.g., constraint type, edge-case category, spec reference).
- Optional integration with Bowtie to compare validator behavior on invalid cases.
- Documentation to help implementors understand and adopt the suite.

**Skills Required**
JavaScript / TypeScript
Node.js
JSON Schema specification
Algorithms and data structures
Software testing concepts
Open-source collaboration

**Mentors**

To be discussed with maintainers of the JSON Schema community.

**Expected Difficulty**
Hard

**Expected Time Commitment**
225 hours

---

## #980: GSoC 2026: Ecosystem Observability

**Labels:** gsoc, Status: Accepted

**JSON Schema Ecosystem Observability**

**Brief Description**
An automated observability and reporting of the JSON Schema ecosystem over time (including history where possible). This is great to showcase how JSON Schema has evolved and can help us identify where the ecosystem needs more support.

**Expected Outcomes**

Regular updating graphics or dashboards with stats on the JSON Schema ecosystem.

**Skills Required**

TS/JS, Node.js, GitHub Actions, APIs, data processing.

**Mentors**
@Relequestual 

**Expected Difficulty**
Medium.

**Expected Time Commitment**
350

Additional notes.
Originally started here: https://github.com/json-schema-org/community/issues/518
Now in it's own repo.
I'm not totally clear what work has been or hasn't been done.
Need to work out a clearer picture.

---

## #979: GSOC 2026 : Enhancing UX of the JSON Schema Tooling Page with Progressive Loading and Modern Filters

**Labels:** gsoc

**Project title**
Enhancing UX of the JSON Schema Tooling Page with Progressive Loading and Modern Filters.

**Brief Description**
The Tooling section of the JSON Schema website currently contains tool categories with a large number of rows, which leads to excessive scrolling and reduced readability especially on smaller screens. Additionally, the always-visible filter panel occupies more screen space, making the UI feel boring and outdated.
This project proposes improving the overall user experience by introducing a “Load more” button for long tool tables and replacing the existing filter sidebar with a modern, icon-based filter modal. These changes aim to improve usability, user experience while preserving existing functionality and data logic.

**Expected Outcomes**
1. Reduced excessive scrolling in the Tooling section by introducing a “Load more” button for long tables
2. Improved readability and navigation, especially on small and medium screens
3. A cleaner, more modern UI by replacing the always-visible filter panel with a filter icon and modal
4. No changes to existing filtering or table logic
5. Better overall UX aligned with modern web designs
6. Glimpse of UI how would it looks:

![Image](https://github.com/user-attachments/assets/2251a5c6-b6f1-4b67-8118-25909801fadf)

**Skills Required**
Next.js
TypeScript
CSS / Tailwind CSS
Git & GitHub workflow

**Mentors**
TBD

**Expected Difficulty**
Medium

**Expected Time Commitment**
175 hours

---

## #978: GSOC 2026 : Make “Optional Tests” Machine-Selectable (Capabilities Manifest + Runner Interop)

**Labels:** gsoc

**Project Title**
Test Suite “Capabilities Manifest” for Optional/Environment-Dependent Tests

**Brief Description**

Add a machine-readable metadata layer to the JSON Schema Test Suite so that runners (including Bowtie) can automatically decide which tests apply to a given implementation or environment. The manifest would describe capabilities such as whether an implementation enables format validation, supports big integers, or uses a network-less remote resolution strategy, and runners could filter tests based on those capabilities. The work includes defining the manifest format, integrating checks into CI, and documenting how implementers can declare and consume these capabilities.

**Why It’s Needed**

The Test Suite README notes that optional/ currently conflates multiple reasons why a test is optional and that the directory structure should be made richer in the future. This makes it hard for runners and tools like Bowtie to automate test selection consistently, because they cannot tell whether a test is optional due to environment constraints, feature flags, or other factors. A capabilities layer would make that behavior explicit and easier to integrate into automated tooling.

**Expected Outcomes**

- A manifest file per dialect (for example, tests/<dialect>/manifest.json) recording test file and test-case tags, required capabilities, and brief notes or links for implementers.
- A linter/validator for the manifest, with CI checks in the Test Suite to keep metadata valid and in sync with tests.
- A JSON Schema describing the manifest itself, published alongside the suite.
- Migration of a meaningful subset of optional/ tests to use capability tags, starting with optional/format and a small number of other ambiguous categories.
- Documentation for runner authors explaining how to read the manifest and filter tests by capabilities.
- Optionally, a simple reference script or Bowtie example that demonstrates capability-based selection in practice.

**Likely Repositories Involved**

- json-schema-org/JSON-Schema-Test-Suite (manifest design, CI, and test metadata)
- bowtie-json-schema/bowtie (using the manifest for test selection and providing examples)
- json-schema-org/community (coordination and higher-level documentation)

**Skills Required**

- Familiarity with the JSON Schema Test Suite layout and contribution workflow
- JSON tooling in Python and/or Node.js for validation and CI integration
- Understanding of how format and other optional features differ across drafts and implementations

** Mentor(s)**
To be determined / seeking mentors.
​
**Expected Difficulty**
Medium.
​
**Expected Time Commitment**
Approximately 175 hours, covering the manifest design, validation tooling and CI wiring, migration of an initial set of tests, and documentation for implementers and runner authors.

---

## #977: GSOC 2026: Add Support for Reporting on the Annotation Test Suite

**Labels:** gsoc, Status: Accepted

**Project Title**
Add Support for Reporting on the Annotation Test Suite

**Brief Description**
The official JSON Schema Test Suite now includes a reasonably complete suite for **Annotations** (metadata), but Bowtie currently only supports reporting on **Validation** (boolean pass/fail).

This project aims to implement full support for running and reporting on the Annotation Test Suite. Based on the original feature request by @jdesrosiers in [Issue #2006](https://github.com/bowtie-json-schema/bowtie/issues/2006), this is a full-stack engineering challenge that requires updates across three distinct layers of Bowtie:

1.  **The UI Level:** Creating a new "Annotations" report page in the React frontend.
2.  **The Report Level:** Upgrading the internal report format to store arbitrary comparison results. Unlike validation (which is binary `valid`/`invalid`), annotations return sets of values that must be compared against an expected set.
3.  **The Protocol Level:** Updating how Bowtie’s runner talks to test harnesses to support the specific definitions of the annotation test suite.

**Expected Outcomes**
* **Protocol Update:** The Bowtie runner is capable of executing the official Annotation Test Suite against supported implementations.
* **Data Model Upgrade:** The report schema is updated to persist annotation results (sets of values) alongside standard validation results.
* **New Reporting UI:** A fully functional, interactive page on the Bowtie report site dedicated to visualizing annotation conformance.
* **Component Reusability:** Extraction of shared UI logic to ensure the new Annotation page remains consistent with the existing Validation page.

**Skills Required**
* **Python:** For updating the runner protocol and report data handling.
* **React & TypeScript:** For building the new reporting interface.
* **JSON Schema:** Understanding the specific mechanics of Annotations vs. Validation.

**Mentors**
@Julian and @AgniveshChaubey

**Expected Difficulty**
Medium

**Expected Time Commitment**
175 hours

---

## #975: GSOC 2026: Schema Documentation Generator with Examples

**Labels:** gsoc

## Schema Documentation Generator with Examples

**Brief Description**
JSON Schemas are excellent for machines but often hard for humans to read, especially for non-technical stakeholders and API consumers. While JSON Schema has strong validation tooling and educational content (like A Tour of JSON Schema and the Visualization Tool), existing documentation tools often focus on rendering schema structure and can lack schema-aware navigation and plain-language explanations for non-technical readers, similar to the experience Swagger UI provides for OpenAPI. This project proposes a `Schema Documentation Generator` that consumes JSON Schemas and produces human-friendly documentation (Markdown/HTML) with examples and plain‑language explanations of validation rules, making schemas more discoverable, understandable, and usable across teams.

**Expected Outcomes**

- **Schema-to-documentation library**  
  A TypeScript/Node.js library that converts one or more JSON Schemas into structured documentation artifacts (intermediate AST plus renderable Markdown/HTML).

- **Human-readable rule descriptions**  
  Clear, plain-language explanations of validation rules (for example, ranges, required fields), inspired by Better JSON Schema Errors but focused on documentation.

- **Example surfacing (scoped)**
Surfacing examples already present in the schema (and optionally validating them), with only very basic, best-effort examples for simple cases as a stretch goal.

- **Multi-format output**  
  Built-in support for Markdown and static HTML, with a pluggable template system (Handlebars/ETA/MDX or custom themes).

- **Static-site integrations**  
  Lightweight examples or adapters for publishing generated docs with tools like Docusaurus or Next.js.

- **Schema-aware navigation**  
  Documentation that resolves `$ref` / `$defs` and understands composition keywords (`allOf`, `anyOf`, `oneOf`), enabling cross-links and hierarchical navigation.

- **Tests and example gallery**  
  Automated tests (Vitest/Jest) covering complex schema features, plus a small gallery of real-world schemas showing before/after documentation.

**Skills Required**

- **JSON Schema**  
  Good understanding of core/validation vocabularies (draft‑07 to 2020‑12+), including `$ref`, `$defs`, composition keywords, and annotations.

- **TypeScript & Node.js**  
  Experience building and packaging CLI tools or libraries in TypeScript.

- **Schema tooling (nice to have)**  
  Familiarity with validators like Ajv, Hyperjump, or Sourcemeta for introspection and example validation.

- **Templates & text generation**  
  Ability to design template-based Markdown/HTML output and write clear, user-friendly explanatory text.

- **Testing & DX**  
  Comfortable writing automated tests for edge cases and designing intuitive APIs/CLIs.

- **Documentation & UX mindset**  
  Interest in making technical artifacts approachable, with attention to navigation and clarity.

**Context**
This idea builds naturally on 

*[truncated]*

---

## #974: GSoC 2026: CLI Tool to Generate Self-Contained, Portable, Tree-Based JSON Schema HTML Visualizer

**Labels:** gsoc

**Project title**
CLI Tool to Generate Self-Contained, Portable, Tree-Based JSON Schema HTML Visualizer

**Brief Description**
This project aims to develop a TypeScript/JavaScript-based CLI tool that takes a JSON Schema as input and generates a single, portable HTML file that visually represents the schema in an interactive, tree-based format. The generated HTML acts as a JSON Schema visualizer, allowing users to expand and collapse nodes and inspect schema properties (such as type, constraints, required fields, and descriptions) via hover interactions. 

The key value of the tool lies in producing a **fully self-contained, transferable HTML artifact** that can be **easily shared via email or common team collaboration platforms** such as **Slack** or **Microsoft Teams**, enabling non-technical users and distributed teams to review JSON Schemas in a human-readable form **without installing Node.js, TypeScript, or running any server.**

This approach is particularly valuable for **organizations** with **strict security** or **compliance policies** that **restrict uploading** internal schemas or **data** to external websites or third-party tools for visualization.

<img width="660" height="397" alt="Image" src="https://github.com/user-attachments/assets/12d8eb32-4088-4b6c-9f1b-d65ccb4ed179" />

(The above diagram is a conceptual example to illustrate the intended tree-based view and is not an actual rendered output)


**Expected Outcomes**
- A cross-platform CLI tool implemented in TypeScript/JavaScript.
- Validation of input JSON Schema before visualization generation.
- Generation of a single, dependency-free, portable HTML file.
- Interactive tree-based visualization with expandable and collapsible nodes.
- Hover-based display of detailed schema metadata (type, constraints, descriptions, required flags).
- Clear documentation and sample outputs demonstrating portability and usage.


**Skills Required**

- JavaScript / TypeScript
- Node.js and CLI tool development
- JSON Schema understanding
- HTML, CSS, and DOM manipulation
- Familiarity with tree data structures and visualization concepts (optional but helpful)

**Mentors**
  TBD

**Expected Difficulty**
   Medium

**Expected Time Commitment**
   175 - 200 hours

---

## #972: GSOC 2026 : Official Web-Based JSON Schema Playground

**Labels:** gsoc

### **Project title**

Official Web-Based JSON Schema Playground

### **Brief Description**
<!-- 2-5+ sentences -->
The JSON Schema ecosystem currently lacks a centralized, official, and feature-rich web-based playground. While third-party tools exist, they are often fragmented, limited in functionality, or not compliant with the latest specifications. This creates a barrier to entry for new users and a friction point for experienced developers.

This project aims to build the Official JSON Schema Playground, a robust, client-side web application designed to be the definitive tool for authoring, validating, and sharing JSON Schemas. It will serve as a primary learning resource, a production-grade utility for practitioners, and a reference implementation of best practices within the JSON Schema organization.

The solution will prioritize usability, performance, and correctness, offering a modern "IDE-like" experience in the browser with side-by-side editing, real-time draft-aware validation, and intelligent error reporting.

### **Expected Outcomes**
By the conclusion of this project, we will deliver a fully functional, deployed web application comprising the following key features:

**2.1. Integrated Development Environment (IDE)**
Dual-Pane Interface: A responsive, side-by-side editor layout for the JSON Schema and the JSON Instance, enabling immediate visual feedback.
Modern UX: Built with modern frontend technologies to ensure a fast, reactive, and accessible user experience.
Editor Features: Syntax highlighting, line numbers, and auto-formatting (prettier-integration) to establish a professional coding environment.

**2.2. Live, Draft-Aware Validation**
Real-Time Feedback: Instant validation of the JSON instance against the schema as the user types.
Multi-Draft Support: Full support for major JSON Schema drafts (Draft-07, 2019-09, 2020-12), with a mechanism to easily switch between them.
Standard-Compliant Engine: Integration of a robust, specification-compliant validator (e.g., Ajv) to ensure reliability.

**2.3. Human-Centric Error Reporting**
Actionable Diagnostics: Transformation of raw validation errors into structured, human-readable messages.
Visual Context: Highlighting of error locations explicitly within both the schema and the instance editors.
Remediation Guidance: (Where feasible) Providing suggestions or links to documentation for common errors.

**2.4. Interactive Schema Explorer**
Structural Visualization: An interactive tree-view visualization of the schema structure, allowing users to navigate complex nested objects and arrays.
Reference Resolution: Basic handling and visualization of internal $ref definitions to simplify understanding of modular schemas.

**2.5. Collaboration & Sharing**
Permalink Generation: A mechanism to serialize the editor state (schema + instance) into a shareable URL, facilitating collaboration and bug reproduction.
Export Capabilities: One-click export of the schema and instance as raw JSON files.



*[truncated]*

---

## #971: GSOC 2026 Proposal: SchemaFuzzer: Fixing weak Schemas with Generative Testing

**Labels:** gsoc

**Project title**
SchemaFuzzer: Fixing weak Schemas with Generative Testing

**Brief Description**
Validation tells us if our data matches a schema, but it does not tells us if the schema itself is good. While I was working on Cypress tests for the JSON schema (PR #2043), I realized how easy it is for schemas to cause silent failures. For example, a schema might accept an empty string or a 10,000-character of text as "valid" even though it breaks the UI.  So, I'm  proposing SchemaFuzzer to remove this gap. It uses property based hypothesis to try and break a schema by generating valid but nonsensical data. When it finds a weakness it reports and then suggests linter rules needed to make the schema better. 
<!-- 2-5+ sentences -->

**Expected Outcomes**
Fuzzer: A Python tool that highlights tests schemas to find where constraints (like 
minLength or maximum) are missing with the help of AI. It gives smart suggestions like "You should probably add format: password here". There can be two features for this:
1: Linter Integration: New Testability rules for the Sourcemeta linter based on the edge cases.
2. Web Dashboard: A simple react playground where we can paste a schema and see a Strength Score.

**Skills Required**
Python: For the heavy testing with hypothesis-jsonschema.
TypeScript and React - To build a clean UI for the dashboard.
Real-World Testing: Experience with Cypress or similar tools.
JSON Schema 

**Mentors** 
I've previously contributed to the website repo, hopefully it will be merged fast and would love to work with @Utkarsh-123github and @jviotti cause i see them often working to make jsonschemaorg from 0-1-100.

**Expected Difficulty**
Hard

**Expected Time Commitment**
350 hour

---

## #969: GSOC-26 : Automated JSON Schema Evolution and Data Migration CLI

**Labels:** gsoc

**Project title**
​SchemaShift:  Structural Diffing and Migrations CLI.

**Brief Description**

<!-- 2-5+ sentences -->
In production environments, schemas are never static. When a schema evolves from S_{v1} to S_{v2}, existing legacy data often becomes invalid, creating a "versioning debt" that requires manual, error-prone migration scripts.
The goal of SchemaShift is to build a CLI that actually "understands" the difference between two schemas. It shouldn't just show you a text diff; it should infer that you renamed a field or moved a property into an object, and then generate the code to fix your data automatically. It moves the community beyond simple validation and into the realm of automated data maintenance.

**Expected Outcomes**

1. ​A smart diffing engine: A tool that can look at two JSON Schemas and identify structural changes (renames, type shifts, or new constraints).

2. ​Automatic Transform Generation: The CLI should output a migration script  that moves data from the old format to the new one.

3. ​The "Safety Check": A workflow that runs the transformation and immediately validates the result against the new schema to make sure nothing got corrupted.

4. ​Interactive CLI: If the change is too complex for the tool to guess (e.g., merging two fields into one), it should ask the user what the intent was instead of just failing.

5. Support arbitrary transforms between schemas. Not only versions of the same schema  i.e. celsius to Fahrenheit.

6. Support re-usability of transformation rules. For example, if there is a transform for celsius to Fahrenheit and you have a bigger schema whose property is a celsius, can it re-use the other transform that property to Farenheit?

**Skills Required**

1. JSON Schema Internals: You need to know your way around Draft 7 and 2020-12. If you don't know the difference between anyOf and oneOf, this will be a struggle.

2. ​Language: Preference for Go, Rust, or TypeScript. We need something fast and easy to distribute as a binary.

3. Algorithm Design: Experience with tree-diffing algorithms or AST (Abstract Syntax Tree) manipulation.

4. ​Test-Driven Development: Ability to write rigorous unit tests for complex edge cases in data transformation.

**Mentors**
Any TSC or experienced community member and if possible then I am also happy to take this opportunity as a co mentor.

**Expected Difficulty**
<!-- an easy, medium or hard difficulty rating of each project -->
Hard

**Expected Time Commitment**
<!-- 175 or 350 hour -->
350 hours

---

## #968: GSoC 2026: GraphQL Schema to JSON Schema Generator for Request and Response Validation

**Labels:** gsoc

**Project title**
GSoC 2026: GraphQL Schema to JSON Schema Generator for Request and Response Validation

**Brief Description**
GraphQL schemas formally define API contracts, but many systems still rely on JSON Schema for request/response validation, documentation, and testing. This project aims to build an open-source JavaScript/TypeScript tool that converts a given GraphQL schema (SDL) into equivalent JSON Schemas for GraphQL operations (queries and mutations), covering both request variables and response payloads. The generated JSON Schemas can then be used with standard validators (e.g., AJV) for runtime validation, mock generation, and contract testing.

**Expected Outcomes**

- A reusable JavaScript/TypeScript library that parses GraphQL schemas using the official GraphQL reference implementation.
- Automatic generation of JSON Schema definitions for:
    - 	GraphQL input types (request variables)
    - 	GraphQL output types (query/mutation responses)
- CLI support to generate JSON Schema files from GraphQL SDL.
- Well-documented examples and usage guides.
- Unit tests and validation of generated schemas using a standard JSON Schema validator.


**Skills Required**
•  JavaScript / TypeScript
•  Node.js ecosystem
•  Basic understanding of GraphQL (schema, types, queries, mutations)
•  Familiarity with JSON Schema
•  Experience with AST traversal or compiler-style tooling is a plus


<img width="892" height="131" alt="Image" src="https://github.com/user-attachments/assets/6aa653cc-dca8-4b46-93a8-41a6ba24ab55" />

**Mentors**
   @jdesrosiers @Utkarsh-123github 

**Expected Difficulty**
   Medium 
(The project involves schema parsing, AST traversal, and careful semantic mapping between GraphQL and JSON Schema.)

**Expected Time Commitment**
  350 hours (Large GSoC project)

---

## #967: GSoC 2026:JSON Schema Linter & Formatter: IDE-First Developer Tooling on Standardized Rules

**Labels:** gsoc

**Project title**
JSON Schema Linter & Formatter: IDE-First Developer Tooling on Standardized Rules

**Brief Description**
Although JSON Schema linting rules and best practices exist, most developers don’t have an easy way to use them while writing schemas. Usually, feedback comes late during code reviews or CI, making it hard to catch problems early and follow best practices consistently. This project aims to bring these rules into developers’ editor, providing real-time warnings, safe fix suggestions and guidance to write better schemas from the start. _Think of it as ESLint or Prettier but for JSON Schema because who said JSON schemas can't be stylish and well behaved?😉_

**Expected Outcomes**
- A reusable library and CLI that apply existing standardized JSON Schema linting rules.
- Draft aware linting across supported JSON Schema drafts (Draft-04 through 2020-12).
- IDE integrations (e.g. VS Code) providing real-time diagnostics and fixes.
- Rule-specific autofixes where changes are safe and unambiguous.
- Formatter-style output for consistent schema structure and readability

**Skills Required**
- Node.js and Typescript
- Knowledge of JSON Schema drafts and linting concepts
- Familiarity with developer tooling such as linters and formatters

**Mentors**

**Expected Difficulty**
Medium

**Expected Time Commitment**
350 hour

---

## #965: Comprehensive test suite for `format` validation

**Labels:** gsoc, Status: Accepted

**Comprehensive test suite for `format` validation**

**Brief Description**

I it is clear by now that JSON Schema users expect `format` to validate, and do so consistently across validations. And the proposal for a [format registry](https://github.com/json-schema-org/json-schema-spec/issues/1552) will only make this more useful.

The challenge is that for implementors, properly implementing `format` validation and knowing they are doing it well is tricky, mainly when it comes to "harder" formats like `idn-hostname` and `idn-email` (see https://github.com/json-schema-org/json-schema-spec/issues/1636). As an implementor myself, I have delayed implementing `format-assertion` on [Blaze](https://github.com/sourcemeta/blaze) given this. The JSON Schema official test suite has some basic coverage of formats, but it's nowhere near to being exhaustive enough to guide a proper implementation.

My proposal (inspired by some Slack discussions with @yogyam!), is to either extend the JSON Schema Test Suite or have a new "format registry test suite" that aims to comprehensively cover, in great detail, the validation outcome needed for `format`. A very strong test suite that covers every possible edge case we can think of and fully exercises the grammar of each of the formats we support now and will support in the future.

Then all implementations can pull this test suite for properly implementing `format` and make sure they are correctly doing so. I would for sure.

**Expected Outcomes**

- A repo or extension to the JSON Schema Test Suite (not sure what we prefer?) with extensive valid/invalid tests in JSON for every supported format
- As a bonus, integrating this into Bowtie for ranking implementation compliance
- As a bonus, a basic reference implementation of the formats in their language of choice just to help prove the suite is indeed correct (sometimes you don't catch issues with it until you try to implement them!)

**Skills Required**

- Ability to properly read standards, RFCs, etc
- At least some basic understanding of formal grammars like ABNF to guide testing efforts
- Great testing skills, with an ability to detect and surface potentially tricky edge cases
- Being a big obsessed with spec-compliance and correctness 😅 

**Mentors**

I volunteer myself to guide the mentee as I also attempt my own implementations based on the new suite for Blaze (so mentee would have a chance to contribute a little bit to Blaze too if they desire), but happy to have any other TSC or experienced community member as a co-mentor!

- @jviotti 

**Expected Difficulty**

Large. Producing a test suite is not hard, but producing a correct and comprehensive one is.

**Expected Time Commitment**

350 hour

---

## #964: GSoC 2026: Call for Project Ideas and Mentors

## About Google Summer of Code
Google Summer of Code (GSoC) is a global program designed to introduce aspiring developers to open-source software development. Over 10-22 weeks, contributors work on impactful coding projects under the guidance of mentors from open-source organizations. GSoC fosters hands-on experience, professional growth, and contributions that make a real-world impact.

## Why Should You Participate in GSoC 2026?
As champions of the open-source community, we are committed to mentoring new talent and enhancing the JSON Schema ecosystem. GSoC provides a platform to realize innovative ideas, bring fresh perspectives to our projects, and welcome passionate contributors to our community.

By participating, you’ll:

- Empower the next generation of developers.
- Help build robust tools, validators, and features for JSON Schema.
- Strengthen the global open-source movement and expand our ecosystem.
- Connect with talented developers worldwide and gain fresh insights.

### How Can You Contribute?

1. **Submit a Project Idea**
    We are looking for achievable, impactful coding projects that contributors can complete within 10-22 weeks. These can include:
    
    - Developing new tools and libraries.
    - Improving validators and generators.
    - Automating workflows or enhancing front-end interfaces.
    - Expanding functionality or addressing specific challenges in JSON Schema.

2. **Become a Mentor**
    Mentors are the backbone of GSoC. Your guidance will help contributors navigate their projects and the open-source landscape effectively.

### What Makes a Great GSoC Project Idea?
A good project idea should:

- Be scoped to fit within the GSoC timeframe.
- Provide tangible benefits to the JSON Schema community.
- Offer contributors a meaningful learning experience while solving real problems.
- Encourage innovative solutions and collaboration.

### How to Submit a Project Idea
- Create an Issue: Submit your idea as an issue in our repository using the “GSoC Project Idea” template.
- Label Your Idea: Tag your issue with the label gsoc.
- Provide Detailed Information: Include the following details in your submission:
- Project Title
- Brief Description
- Expected Outcomes
- Skills Required
- Mentor(s)
- Expected Difficulty
- Expected Time Commitment
- Deadline for Submission: The timeline for submission is Friday, Jan 31st.

### What Do Mentors Do?
Mentors play a critical role in shaping the GSoC experience. Your responsibilities will include:

- Engaging Actively: Support contributors during selection, community bonding, and coding phases.
- Providing Guidance: Dedicate ~5 hours weekly, working in a team of 2+ mentors per contributor.
- Offering Feedback: Share constructive feedback and complete evaluations at each program milestone.

### How to Become a Mentor
- If you’re excited to share your expertise and shape the future of JSON Schema, let us know by adding a comment to this issue.

### Mentor eligibility criteria
- To become 

*[truncated]*

---

## #958: Open Community Working Meeting 2026-01-19 - 13:00 PT

**Labels:** Working Meeting

# Open Community Working Meeting 2026-01-19 - 13:00 PT

Google Meet joining info - Video call link: https://meet.google.com/raz-ptdn-ewf

You can find these events scheduled on our **[JSON Schema Community Calendar](https://calendar.google.com/calendar/u/0/embed?src=info@json-schema.org)**.

To add the events to your Google Calendar, use the link found in the bottom right of the above calendar.
To add the events to another calendar, use the provided [ics/ical file](https://calendar.google.com/calendar/ical/info%40json-schema.org/public/basic.ics).

**Meeting accessibility**:
- We would like to record the meeting for future reference and for those who are not able to attend in person. 
- We encourage you to challenge any language or behaviour that is harmful or not inclusive during this meeting. 
- We look forward to your participation, but please consider... 
  - Remaining on mute when not speaking. 
  - Use the Zoom meeting raised hand feature to notify you wish to speak. 
- [JSON Schema Code of Conduct](https://github.com/json-schema-org/.github/blob/main/CODE_OF_CONDUCT.md)

Agenda: Compiling!

| Topic | Owner | Decision/NextStep |
| -- | -- | -- |
| Review last call's action items  | [facilitator] |
| [TOPIC] [IssuePRDiscussion] | [owner] |
<!-- | [TOPIC] [IssuePRDiscussion] | [owner] | -->

You can have a PR or an issue added to this agenda by just adding them the `agenda` label.

AOB?
If you want to discuss any other business not on the agenda, please add comments during the meeting.
If we do not complete the agenda, your discussion item will likely be rolled over to the next call.

Action items:
- [ ]

Notes:

Agenda Items rolling over:
- list

Recording: [link]

---

## #955: Open Community Working Meeting 2025-12-15 - 13:00 PT

**Labels:** Working Meeting

---
name: Open Community Working Meeting
about: Regular Open Community Working Meetings Issue - This template is for those setting up an OCWM only.
---

# Open Community Working Meeting 2022-MM-DD - 13:00 PT

Google Meet joining info - Video call link: https://meet.google.com/raz-ptdn-ewf

You can find these events scheduled on our **[JSON Schema Community Calendar](https://calendar.google.com/calendar/u/0/embed?src=info@json-schema.org)**.

To add the events to your Google Calendar, use the link found in the bottom right of the above calendar.
To add the events to another calendar, use the provided [ics/ical file](https://calendar.google.com/calendar/ical/info%40json-schema.org/public/basic.ics).

**Meeting accessibility**:
- We would like to record the meeting for future reference and for those who are not able to attend in person. 
- We encourage you to challenge any language or behaviour that is harmful or not inclusive during this meeting. 
- We look forward to your participation, but please consider... 
  - Remaining on mute when not speaking. 
  - Use the Zoom meeting raised hand feature to notify you wish to speak. 
- [JSON Schema Code of Conduct](https://github.com/json-schema-org/.github/blob/main/CODE_OF_CONDUCT.md)

Agenda: Compiling!

| Topic | Owner | Decision/NextStep |
| -- | -- | -- |
| Review last call's action items  | [facilitator] |
| [TOPIC] [IssuePRDiscussion] | [owner] |
<!-- | [TOPIC] [IssuePRDiscussion] | [owner] | -->

You can have a PR or an issue added to this agenda by just adding them the `agenda` label.

AOB?
If you want to discuss any other business not on the agenda, please add comments during the meeting.
If we do not complete the agenda, your discussion item will likely be rolled over to the next call.

Action items:
- [ ]

Notes:

Agenda Items rolling over:
- list

Recording: [link]

---

## #951: 💡 Community Workflow proposal: Automate ADR labeling and validation workflow

**Labels:** ✨ Enhancement, Status: Triage

### Description

The current CONTRIBUTING.md mentions that ADR (Architectural Decision Records) workflow automation would be beneficial. Specifically, the document states: "(It would be great if some parts of this could be automated. Specification and full workflow required.)"

This workflow suggestion proposes automating the ADR labeling and validation process to reduce manual overhead and ensure consistency.

### Objective

Automate the ADR (Architectural Decision Records) workflow by:
1. Automatically adding `adr-required` or `adr-not-required` labels based on maintainer/contributor indicators
2. Validating that PRs with `adr-required` label include an ADR before allowing merge
3. Inheriting `adr-required` labels from associated issues to PRs
4. Auto-adding `adr-included` label when ADR is detected in PR

### Steps

1. Create GitHub Action workflow that triggers on issue/PR creation and label changes
2. Implement logic to detect ADR assertion by submitter (keywords in body, checkbox in template)
3. Add automatic label inheritance from linked issues to PRs
4. Implement ADR file detection in PRs (scan for files in docs/adr/ directory)
5. Add validation check that blocks merge if `adr-required` label exists without `adr-included`
6. Configure bot to comment on PRs requesting ADR if required label is present
7. Add workflow status checks to repository settings

### Expected Outcome

- Reduced manual effort for maintainers in tracking ADR requirements
- Consistent application of ADR policy across repositories
- Clear feedback to contributors when ADR is needed
- Automated validation ensures no significant changes are merged without proper documentation
- Improved project governance and decision tracking

### Additional Context [optional]

This directly addresses the comment in CONTRIBUTING.md about automation being desirable. Similar automation exists in other large open source projects (e.g., Kubernetes, Rust) and could be adapted for JSON Schema's needs.

The implementation could start with simple GitHub Actions and expand to more sophisticated tooling if needed. I'm willing to contribute to the specification and implementation of this workflow.

---

## #948: Open Community Working Meeting 2025-11-17 - 13:00 PT

**Labels:** Working Meeting

---
name: Open Community Working Meeting
about: Regular Open Community Working Meetings Issue - This template is for those setting up an OCWM only.
---

# Open Community Working Meeting 2022-MM-DD - 13:00 PT

Google Meet joining info - Video call link: https://meet.google.com/raz-ptdn-ewf

You can find these events scheduled on our **[JSON Schema Community Calendar](https://calendar.google.com/calendar/u/0/embed?src=info@json-schema.org)**.

To add the events to your Google Calendar, use the link found in the bottom right of the above calendar.
To add the events to another calendar, use the provided [ics/ical file](https://calendar.google.com/calendar/ical/info%40json-schema.org/public/basic.ics).

**Meeting accessibility**:
- We would like to record the meeting for future reference and for those who are not able to attend in person. 
- We encourage you to challenge any language or behaviour that is harmful or not inclusive during this meeting. 
- We look forward to your participation, but please consider... 
  - Remaining on mute when not speaking. 
  - Use the Zoom meeting raised hand feature to notify you wish to speak. 
- [JSON Schema Code of Conduct](https://github.com/json-schema-org/.github/blob/main/CODE_OF_CONDUCT.md)

Agenda: Compiling!

| Topic | Owner | Decision/NextStep |
| -- | -- | -- |
| Review last call's action items  | [facilitator] |
| [TOPIC] [IssuePRDiscussion] | [owner] |
<!-- | [TOPIC] [IssuePRDiscussion] | [owner] | -->

You can have a PR or an issue added to this agenda by just adding them the `agenda` label.

AOB?
If you want to discuss any other business not on the agenda, please add comments during the meeting.
If we do not complete the agenda, your discussion item will likely be rolled over to the next call.

Action items:
- [ ]

Notes:

Agenda Items rolling over:
- list

Recording: [link]

---

## #946: Update: Stepping down from the TSC

Hi everyone,

I just wanted to let you know that I’ll be stepping down from the TSC. Lately, I haven’t been able to give the project the time and attention it deserves, and I think it’s better to make space for others who can contribute more actively.

It’s been a real pleasure to be part of this group and to work alongside such an amazing community. I’ve learned a lot and I’ll keep cheering for the project from the sidelines. I’ll still be around, and hopefully in the future I’ll have the availability to contribute again.

Upward and onward!

Next steps:
* We need to remove all the privileges I have in all the project systems.
* Make sure all the Community operations implemented with Github Actions are not using personal tokens.

Thanks everyone!

---

- [ ] Remove from private tsc channel on slack
  - [ ] TODO: Are there other private channels that he needs to be removed from?
- [ ] Remove admin status on slack
- [ ] Remove admin status on Github org and repos
- [ ] Remove from the `/vote` bot's list of voters
-  [ ] TODO: Find all the places we list TSC members including website and markdown documents
- [ ] Remove admin status on OpenCollective
- [ ] Make sure all the Community operations implemented with Github Actions are not using personal tokens.

What other tasks need to be done? TSC members, please fill in what's missing.

---

## #945: External Request: Exploring collaboration with Json Schema

Hello everyone, we got a collaboration request from a representative at Computer Science and Engineering Society (CSES) at UC San Diego. I am bringing up this discussion because from the note, I believe it may involve some fundings (for co-hosting workshops) and active involvement of TSC members, tooling owners or active members of the community for everyone to benefit from this collaboration. However I think this could be good and an avenue to introduce JSON Schema to a wide range of people. 

Here's the note;

> Hi Json Schema Team,

> My name is [name], and I'm the Partnerships Coordinator for the Computer Science and Engineering Society (CSES) at UC San Diego. We're passionate about supporting open-source collaboration and empowering students to contribute to impactful projects.

> We would love to explore meaningful ways to collaborate with the Json Schema community this year such as:
> - Co-hosting workshops that introduce students to Json Schema's projects and development practices, and
> - Partnering on a focused student project or initiative where our members can contribute directly under the > guidance of Json Schema mentors.

> Thank you for your time and for the incredible work the Json Schema community does to advance open-source innovation. I would love to connect directly to discuss possible collaborations — happy to set up a quick Zoom call at a time that works best for you.

> Looking forward to the possibility of working together.

---

## #941: Open Community Working Meeting 2025-10-20 - 13:00 PT

**Labels:** Working Meeting

---
name: Open Community Working Meeting
about: Regular Open Community Working Meetings Issue - This template is for those setting up an OCWM only.
---

# Open Community Working Meeting 2022-MM-DD - 13:00 PT

Google Meet joining info - Video call link: https://meet.google.com/raz-ptdn-ewf

You can find these events scheduled on our **[JSON Schema Community Calendar](https://calendar.google.com/calendar/u/0/embed?src=info@json-schema.org)**.

To add the events to your Google Calendar, use the link found in the bottom right of the above calendar.
To add the events to another calendar, use the provided [ics/ical file](https://calendar.google.com/calendar/ical/info%40json-schema.org/public/basic.ics).

**Meeting accessibility**:
- We would like to record the meeting for future reference and for those who are not able to attend in person. 
- We encourage you to challenge any language or behaviour that is harmful or not inclusive during this meeting. 
- We look forward to your participation, but please consider... 
  - Remaining on mute when not speaking. 
  - Use the Zoom meeting raised hand feature to notify you wish to speak. 
- [JSON Schema Code of Conduct](https://github.com/json-schema-org/.github/blob/main/CODE_OF_CONDUCT.md)

Agenda: Compiling!

| Topic | Owner | Decision/NextStep |
| -- | -- | -- |
| Review last call's action items  | [facilitator] |
| [TOPIC] [IssuePRDiscussion] | [owner] |
<!-- | [TOPIC] [IssuePRDiscussion] | [owner] | -->

You can have a PR or an issue added to this agenda by just adding them the `agenda` label.

AOB?
If you want to discuss any other business not on the agenda, please add comments during the meeting.
If we do not complete the agenda, your discussion item will likely be rolled over to the next call.

Action items:
- [ ]

Notes:

Agenda Items rolling over:
- list

Recording: [link]

---

## #939: Open Community Working Meeting 2025-09-15 - 13:00 PT

**Labels:** Working Meeting

## Open Community Working Meeting 2025-09-15 - 13:00 PT


Google Meet joining info - Video call link: https://meet.google.com/raz-ptdn-ewf

You can find these events scheduled on our **[JSON Schema Community Calendar](https://calendar.google.com/calendar/u/0/embed?src=info@json-schema.org)**.

To add the events to your Google Calendar, use the link found in the bottom right of the above calendar.
To add the events to another calendar, use the provided [ics/ical file](https://calendar.google.com/calendar/ical/info%40json-schema.org/public/basic.ics).

**Meeting accessibility**:
- We would like to record the meeting for future reference and for those who are not able to attend in person. 
- We encourage you to challenge any language or behaviour that is harmful or not inclusive during this meeting. 
- We look forward to your participation, but please consider... 
  - Remaining on mute when not speaking. 
  - Use the Zoom meeting raised hand feature to notify you wish to speak. 
- [JSON Schema Code of Conduct](https://github.com/json-schema-org/.github/blob/main/CODE_OF_CONDUCT.md)

Agenda: Compiling!

| Topic | Owner | Decision/NextStep |
| -- | -- | -- |
| Review last call's action items  | [facilitator] |
| [TOPIC] [IssuePRDiscussion] | [owner] |
<!-- | [TOPIC] [IssuePRDiscussion] | [owner] | -->

You can have a PR or an issue added to this agenda by just adding them the `agenda` label.

AOB?
If you want to discuss any other business not on the agenda, please add comments during the meeting.
If we do not complete the agenda, your discussion item will likely be rolled over to the next call.

Action items:
- [ ]

Notes:

Agenda Items rolling over:
- list

Recording: [link]

---

## #932: Open Community Working Meeting 2025-08-18 - 13:00 PT

**Labels:** Working Meeting, Status: Stale

## Open Community Working Meeting 2025-08-18 - 13:00 PT


Google Meet joining info - Video call link: https://meet.google.com/raz-ptdn-ewf

You can find these events scheduled on our **[JSON Schema Community Calendar](https://calendar.google.com/calendar/u/0/embed?src=info@json-schema.org)**.

To add the events to your Google Calendar, use the link found in the bottom right of the above calendar.
To add the events to another calendar, use the provided [ics/ical file](https://calendar.google.com/calendar/ical/info%40json-schema.org/public/basic.ics).

**Meeting accessibility**:
- We would like to record the meeting for future reference and for those who are not able to attend in person. 
- We encourage you to challenge any language or behaviour that is harmful or not inclusive during this meeting. 
- We look forward to your participation, but please consider... 
  - Remaining on mute when not speaking. 
  - Use the Zoom meeting raised hand feature to notify you wish to speak. 
- [JSON Schema Code of Conduct](https://github.com/json-schema-org/.github/blob/main/CODE_OF_CONDUCT.md)

Agenda: Compiling!

| Topic | Owner | Decision/NextStep |
| -- | -- | -- |
| Review last call's action items  | [facilitator] |
| [TOPIC] [IssuePRDiscussion] | [owner] |
<!-- | [TOPIC] [IssuePRDiscussion] | [owner] | -->

You can have a PR or an issue added to this agenda by just adding them the `agenda` label.

AOB?
If you want to discuss any other business not on the agenda, please add comments during the meeting.
If we do not complete the agenda, your discussion item will likely be rolled over to the next call.

Action items:
- [ ]

Notes:

Agenda Items rolling over:
- list

Recording: [link]

---

## #924: Open Community Working Meeting 2025-07-21 - 13:00 PT

**Labels:** Working Meeting, Status: Stale

## Open Community Working Meeting 2025-07-21 - 13:00 PT


Google Meet joining info - Video call link: https://meet.google.com/raz-ptdn-ewf

You can find these events scheduled on our **[JSON Schema Community Calendar](https://calendar.google.com/calendar/u/0/embed?src=info@json-schema.org)**.

To add the events to your Google Calendar, use the link found in the bottom right of the above calendar.
To add the events to another calendar, use the provided [ics/ical file](https://calendar.google.com/calendar/ical/info%40json-schema.org/public/basic.ics).

**Meeting accessibility**:
- We would like to record the meeting for future reference and for those who are not able to attend in person. 
- We encourage you to challenge any language or behaviour that is harmful or not inclusive during this meeting. 
- We look forward to your participation, but please consider... 
  - Remaining on mute when not speaking. 
  - Use the Zoom meeting raised hand feature to notify you wish to speak. 
- [JSON Schema Code of Conduct](https://github.com/json-schema-org/.github/blob/main/CODE_OF_CONDUCT.md)

Agenda: Compiling!

| Topic | Owner | Decision/NextStep |
| -- | -- | -- |
| Review last call's action items  | [facilitator] |
| [Proposal: Grants process](https://github.com/json-schema-org/TSC/discussions/27) | @jdesrosiers |
<!-- | [TOPIC] [IssuePRDiscussion] | [owner] | -->

You can have a PR or an issue added to this agenda by just adding them the `agenda` label.

AOB?
If you want to discuss any other business not on the agenda, please add comments during the meeting.
If we do not complete the agenda, your discussion item will likely be rolled over to the next call.

Action items:
- [ ]

Notes:

Agenda Items rolling over:
- list

Recording: [link]

---

## #923: Community Manager Priorities: Engaging the Community

Hi all!

As I step into the role of Community Manager for the JSON Schema project, I’m excited to share my initial priorities for the next 3 months. These actions are aligned with the project’s roadmap and focus on strengthening community engagement, visibility, and contributor support. This issue will serve as a working thread to track progress, share updates, and invite collaboration.

## **Key Focus Areas (June–September 2025)**

### **Design Assets**

- [ ] Create at least 10 reusable design assets (e.g., templates for events, contributor and tooling shoutouts, release highlights, etc.).
    - [x] Create for community contributor spotlight.
    - [x] Create foe tooling spotlight.
    - [ ] Create for conference announcement (different design variations).
    - [ ] Create for speaker announcement (different design variations).
    - [x] Create for adopters and sponsors
- [x] Create a JSOn Schema cheatsheet.
    - [x] Collaborate with the community.
    - [x] Ask TSC for review
    - [x] Document all contributors so we can tag when creating the social post.
- [x] Develop and publish a monthly content theme (starting July) to guide storytelling across channels.
- [x] Highlight JSON Schema participation at API Days Munich and any upcoming conferences.
    - [ ] Post atleast twice on social media.
       - [ ] LinkedIn
       - [ ] Twitter
       - [ ] Slack

### **Contributor & Implementer Spotlights**

- [x] Launch a Contributor Spotlight series to recognize active contributors monthly.
- [x] Launch a Tooling/Implementer Spotlight to showcase ecosystem projects and their maintainers.
- [ ] Share both spotlights across newsletter, and social platforms

### Newsletter

- [ ] Launch the community newsletter

### **Mentorship & Community Growth**

- [ ] Support triage group onboarding and improve contributor documentation.

### **Community Programs & Feedback**

- [ ] Plan a lightweight community feedback form or survey to understand member needs and friction points.
- [ ] Monthly report on community efforts
- [ ] Engage actively on Slack to welcome new contributors.

Feel free to comment and I’ll continue updating this issue with progress and related links. Thanks for being here and making the JSON Schema community what it is

---

## #917: 🐛 Bug: Issue with Community meetings notification

**Labels:** 🐛 Bug, Status: In Progress

### Describe the bug

Hi everyone,

I recently discovered that the Github action that sends notifications to slack when a new community meetings is created is failing.

The expected result is:

<img width="687" alt="Image" src="https://github.com/user-attachments/assets/0aec95e9-ed29-43aa-8810-f07606ca5dfe" />

But this is what we are getting:

<img width="626" alt="Image" src="https://github.com/user-attachments/assets/26598f09-8afc-485e-a0c0-8227f3c00d6e" />

The actions is: ocwm-creator.yml


### Steps To Reproduce

.

### Expected Behavior

<img width="687" alt="Image" src="https://github.com/user-attachments/assets/671355b8-610d-4af6-aefe-422b96f6bcbb" />

### Screenshots

_No response_

### Device Information [optional]

```markdown
- OS:
- Browser:
- version:
```

### Are you working on this issue?

No

---

## #914: What is a reference implementation?

**Labels:** Status: Stale

### Context

In the last OCWM #907 , we discussed about what project to fund in the future and there was an idea to fund Reference Implementations. But what is a reference implementation?

We need to come up with a definition that clearly defines what a reference implementation is and complement it with clear eligibility criteria, commitments, and quantitative compliance data from Bowtie.

Some definitions:
- [Wikipedia](https://en.wikipedia.org/wiki/Reference_implementation)

Expectations for this issue:
- [ ] Provide definition 
- [ ] Provide the eligibility criteria: 
  - What makes those implementations different from others?
  - Can we have more than one by language?
  - Are they committed to implementing experimental capabilities?
- [ ] Define the bowtie compliance value

Next steps:
 - Agree on the criteria.
 - Highlight reference implementations.
 - Support implementations:
   - Funding.
   - Promotion.
   - Others.

---

## #907: Open Community Working Meeting 2025-05-19 - 13:00 PT

**Labels:** Working Meeting, Status: Stale

## Open Community Working Meeting 2025-05-19 - 13:00 PT


Google Meet joining info - Video call link: https://meet.google.com/raz-ptdn-ewf

You can find these events scheduled on our **[JSON Schema Community Calendar](https://calendar.google.com/calendar/u/0/embed?src=info@json-schema.org)**.

To add the events to your Google Calendar, use the link found in the bottom right of the above calendar.
To add the events to another calendar, use the provided [ics/ical file](https://calendar.google.com/calendar/ical/info%40json-schema.org/public/basic.ics).

**Meeting accessibility**:
- We would like to record the meeting for future reference and for those who are not able to attend in person. 
- We encourage you to challenge any language or behaviour that is harmful or not inclusive during this meeting. 
- We look forward to your participation, but please consider... 
  - Remaining on mute when not speaking. 
  - Use the Zoom meeting raised hand feature to notify you wish to speak. 
- [JSON Schema Code of Conduct](https://github.com/json-schema-org/.github/blob/main/CODE_OF_CONDUCT.md)

Agenda: Compiling!

| Topic | Owner | Decision/NextStep |
| -- | -- | -- |
| Review last call's action items  | [facilitator] |
| https://github.com//orgs/json-schema-org/discussions/911 - JSON Schema Financial Report (2024 and beyond) | @benjagm |
| https://github.com//orgs/json-schema-org/discussions/911#discussioncomment-13124808 - 2025 Budget Proposal | @jdesrosiers |
| Sponsoring a Community Manager https://github.com/json-schema-org/TSC/issues/25 | @benjagm |
| https://github.com/json-schema-org/TSC/issues/24 - Proposal: Stipend for important initiatives like the stable spec | @jviotti |
<!-- | [TOPIC] [IssuePRDiscussion] | [owner] | -->

You can have a PR or an issue added to this agenda by just adding them the `agenda` label.

AOB?
If you want to discuss any other business not on the agenda, please add comments during the meeting.
If we do not complete the agenda, your discussion item will likely be rolled over to the next call.

Action items:
- [ ]

Notes:

Agenda Items rolling over:
- list

Recording: [link]

---

## #897: Idea: DB Schema --> to JSON SCHEMA

**Labels:** Status: Stale

I was thinking—what if we could automatically generate JSON Schema from database schemas (SQL, PostgreSQL, MongoDB, etc.)? Instead of manually defining validation rules, we could extract constraints directly from the database, making sure APIs and data validation stay consistent.

I'm not sure this idea is good fit for standards but looking for your thoughts about it @benjagm @DhairyaMajmudar ?

---

## #896: Idea :  AI-Powered UML to JSON Schema Conversion

**Labels:** Status: Stale

Hey everyone! 

I think it would be great if we could generate JSON schemas directly from UML diagrams using AI. There are plenty of free AI models that can handle this efficiently, making schema creation much easier. I have experience in generative AI and believe this could be a valuable addition.

Would love to hear your thoughts @benjagm @DhairyaMajmudar

---

## #891: Update the Readme for GSOC 2025

**Labels:** Status: Stale

As of now, all GSoC 2025 projects have assigned mentors. However, the README file still lists one project as "looking for a mentor." Since a mentor has already been assigned, we need to update the file to provide accurate information for newcomers.

---

## #890: Open Community Working Meeting 2025-04-21 - 12:00 PT

**Labels:** Working Meeting, Status: Stale

## Open Community Working Meeting 2025-04-21 - 12:00 PT


Google Meet joining info - Video call link: https://meet.google.com/raz-ptdn-ewf

You can find these events scheduled on our **[JSON Schema Community Calendar](https://calendar.google.com/calendar/u/0/embed?src=info@json-schema.org)**.

To add the events to your Google Calendar, use the link found in the bottom right of the above calendar.
To add the events to another calendar, use the provided [ics/ical file](https://calendar.google.com/calendar/ical/info%40json-schema.org/public/basic.ics).

**Meeting accessibility**:
- We would like to record the meeting for future reference and for those who are not able to attend in person. 
- We encourage you to challenge any language or behaviour that is harmful or not inclusive during this meeting. 
- We look forward to your participation, but please consider... 
  - Remaining on mute when not speaking. 
  - Use the Zoom meeting raised hand feature to notify you wish to speak. 
- [JSON Schema Code of Conduct](https://github.com/json-schema-org/.github/blob/main/CODE_OF_CONDUCT.md)

Agenda: Compiling!

| Topic | Owner | Decision/NextStep |
| -- | -- | -- |
| Review last call's action items  | [facilitator] |
 | [TOPIC] [IssuePRDiscussion] | [owner] | 
<!-- | [TOPIC] [IssuePRDiscussion] | [owner] | -->

You can have a PR or an issue added to this agenda by just adding them the `agenda` label.

AOB?
If you want to discuss any other business not on the agenda, please add comments during the meeting.
If we do not complete the agenda, your discussion item will likely be rolled over to the next call.

Action items:
- [ ]

Notes:

Agenda Items rolling over:
- list

Recording: [link]

---

## #888: Document the JSON Schema work the TSC is performing for strategic purposes

**Labels:** Status: Stale

The key topic in today's Open Community Working Meeting has been around the constraints that the JSON Schema organisation has at the moment (with no maintainers working full time on it like before) and the various things we have going on that we might not be able to invest proper time on. We had many initiatives and ideas from where we had more resources that realistically will not happen any time soon, and we probably have to be honest about that:

A suggestion in the call was: 

- Can we take some time to zoom out and document what each of us is working on related to JSON Schema on volunteering efforts? 
- By seeing everything in one place, try to strategise (and potentially make some hard decisions) on whether the volunteering work happening right now is realistic or not, or we should more clearly start saying no to some things
- As a byproduct of the above, potentially do an org/repo cleanup to close down things we will not pursue anymore and/or aggressively simplifying certain things that have too much of a maintainability overhead 
- Finally, try to come up with a basic/minimal plan on how we can use the limited resources we have to push JSON Schema forward, potentially focusing on the highest return of investment. This might mean just going around closing lots of issues, removing code from i.e. the website, archiving some repos, etc. Whatever helps bringing in focus and simplicity given our current resources

cc @json-schema-org/tsc

---

## #886: JSON Schema GSoC 2025  - Office Hours

**Labels:** Status: Stale

# JSON Schema GSoC 2025  - Office Hours

**Meeting accessibility**:
- We would like to record the meeting for future reference and for those who are not able to attend in person. 
- We encourage you to challenge any language or behaviour that is harmful or not inclusive during this meeting. 
- We look forward to your participation, but please consider... 
  - Remaining on mute when not speaking. 
  - Use the Zoom meeting raised hand feature to notify you wish to speak. 
- [JSON Schema Code of Conduct](https://github.com/json-schema-org/.github/blob/main/CODE_OF_CONDUCT.md)

**Agenda**: 

Thanks a lot for joining JSON Schema org for this edition of GSoC!!

We'd like to invite you to the GSoC office hours sessions scheduled for next:

- March 12th 19:00 UTC
- March 26th 19:00 UTC

The sessions are perfect for connecting with maintainers and mentors, understanding the project ideas, and asking any questions you may have.

**Meet link**:  https://meet.google.com/tjq-twac-fut 

Looking forward to seeing you there!

---

## #879: GSoC 2025: Making JSON Schema Docs Easy to Read and Share

**Labels:** Status: Stale

## What's This Project About?

Have you ever tried to explain a JSON Schema to someone who's not a developer? It's pretty tough, right? This project aims to solve that problem by creating a tool that turns complex JSON Schemas into clear, easy-to-read documentation that anyone can understand. Think of it as a translator that converts technical schema definitions into human-friendly guides and explanations.

## What Will It Do?

Our tool will take your JSON Schema through a simple upload or paste process and transform it into beautiful documentation in various formats like web pages, markdown files, and PDFs, handling even the most complex schemas with ease. To make everything crystal clear, we'll convert technical constraints into plain English, provide real-world examples, create visual diagrams of connections, and highlight key rules in a way that makes sense to everyone.

You'll have complete control over the look and feel, with the ability to choose different styles, customize what information appears, add your own branding, and make the documentation match your existing style guide. The tool will fit seamlessly into your workflow by offering both command-line and programmatic access, automatically updating documentation when schemas change, and making it simple to share with your team.

## Why This Matters

This project bridges the gap between technical and non-technical team members by creating documentation everyone can understand, while saving time on manual documentation and ensuring everything stays accurate and professional-looking.

## What We'll Build

We'll create an intuitive tool with a clean interface and simple commands, supporting multiple output formats like web pages, markdown, and PDFs. The documentation will automatically generate examples, explain rules clearly, and include helpful visual diagrams when needed.

## What Skills Are Needed

The ideal candidate should understand JSON Schema well and have solid programming experience, with an eye for design and a passion for making technical concepts accessible to everyone.

## How Long Will It Take?

Overall 350-hour journey will flow naturally from building the basic converter in the first month, to adding polished templates and themes in the second month, and finally integrating it with other tools and adding the finishing touches in the third month.

## Difficulty Level

Medium-difficulty project that requires attention to detail and good design sense rather than complex technical challenges.

## Why Pick This Project?

This project solves a real problem teams face every day while providing clear value and room for growth, ultimately making JSON Schema more accessible to everyone who needs to work with data structures.

## Mentors : @benjagm 

## Future Ideas

The project can grow to include more output formats, interactive features, shared templates, and collaboration tools, making it even more valuable for teams working with JSON Schema.

## Technical Details

We'll build

*[truncated]*

---

## #830: Application for Open Community Manager Role

**Labels:** Status: Stale

Hello JSON Schema Team,

I am writing to express my interest in the Community Manager role with JSON Schema. 

Over the past six months, I have had the pleasure of contributing to the community as part of Google Season of Docs (GSoD), helping to enhance our documentation efforts. This experience has deepened my commitment to supporting and growing this community, and I am eager to contribute further as a Community Manager.
In addition to my recent work with JSON Schema, I bring experience as a Community Manager for TWMP. I developed skills in engaging with diverse audiences, managing online communities, and fostering inclusive, collaborative environments. I have also had the opportunity to mentor other tech writers, which has honed my ability to guide and support new contributors in a welcoming and productive way.

I am passionate about open-source community-building and strongly believe in creating spaces where everyone feels encouraged to share knowledge and grow together. In the past months here, I have learned more about collaboration, which makes reaching out to potential partners a doable task. 
As Community Manager, I would work to ensure a thriving and healthy environment across our platforms. From managing the JSON Schema Slack channels, organising community calls, sharing important updates, and monitoring our analytics tools, I am confident in supporting, adding value, and strengthening the JSON Schema community.

Thank you for considering my application. 

Warm regards,
Blessing Ene Anyebe.

---

## #727: Plan to Launch the Ambassadors Program

**Labels:** 🏗️ Programs, Status: In Progress, Status: Do not close

**Work Summary**:

The goal of this issue is to plan and track the launch of the JSON Schema Ambassadors Program.

### Launch Campaign for JSON Schema Ambassadors Program

#### Campaign Goals
1. **Increase Awareness**: Make the community aware of the JSON Schema Ambassadors Program.
2. **Drive Participation**: Encourage potential ambassadors to apply.
3. **Community Engagement**: Foster a sense of community and collaboration.

#### Target Audience
1. Current users of JSON Schema
2. Developers and tech enthusiasts interested in JSON Schema
3. Influencers and thought leaders in the tech community using JSON Schema
4. Organizations and tech communities that could benefit from JSON Schema

#### Key Messages
1. **Empowerment**: Become a leader in the JSON Schema community and shape its future.
2. **Visibility**: Gain recognition and visibility in the tech ecosystem.
3. **Collaboration**: Join a network of like-minded individuals and collaborate on exciting projects.
4. **Contribution**: Make meaningful contributions and drive the adoption of JSON Schema.

### Campaign Components

#### 1. **Announcement Blog Post**
- Publish a blog post on the JSON Schema website explaining the Ambassador Program.
- Share personal stories or testimonials from existing ambassadors (if any).

#### 2. **Social Media Campaign**
- **Hashtags**: #JSONSchemaAmbassador, #JSONSchema, #OpenSource
- **Channels**: Twitter, LinkedIn and Slack
- **Content**: Create a series of posts highlighting the benefits, requirements, and the application process. Include visuals like infographics and ambassador testimonials.
  - Example Post: "Join the #JSONSchemaAmbassador program and become a leader in the open-source community! Contribute, collaborate, and gain recognition. Apply now: [link]"

#### 3. **Ambassador Spotlights**
- Feature current or new ambassadors on the JSON Schema website and social media.
- Share their contributions and stories to inspire others.

#### 5. **Webinars and Online Meetups** (TBC)
- Host webinars explaining the program, its benefits, and how to apply.
- Invite current ambassadors (if any) or influential community members to speak.

### Timeline

1. **Week 1-2: Preparation**
   - Finalize blog post and social media content.
   - Coordinate with current ambassadors and community members for testimonials.
   - Schedule webinars and meetups.
   - Contact designer for swag.

2. **Week 3: Launch**
   - Publish the blog post.
   - Start the social media campaign.
   - Start online shop building.
   - Create canva design for ambassadors stoplight

3. **Week 4-6: Engagement**
   - Host the webinars and online meetups.
   - Continue social media engagement.
   - Share ambassador spotlights.
   - Complete online shop building.

4. **Week 7-8: Follow-up**
   - Monitor applications and provide updates.
   - Share additional content or testimonials if needed.
   - Engage with the community for feedback and que

*[truncated]*

---
