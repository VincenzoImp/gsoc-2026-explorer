# Project Ideas

**Parent:** JSON Schema — Project Ideas
**Source:** https://github.com/json-schema-org/community/issues?q=is%3Aopen+label%3Agsoc+sort%3Acreated-desc
**Scraped:** 2026-03-10T16:58:40.243661

---

## #1017: JSON Schema <> APIdays Paris 2026

Hello everyone 👋

This issue is opened to begin a structured discussion on how JSON Schema should strategically show up in 2026, particularly at API-focused events such as APIdays Paris. The goal is to align early on visibility, impact, and budget considerations.

### **Option 1: Dedicated JSON Schema Track**

Hosting a dedicated track would significantly increase visibility and allow us to introduce JSON Schema to a broader audience through curated talks, ecosystem showcases, and implementer stories.

**Key considerations:**

- AV team coverage for sessions (~€2,600–€3,000)

- Merchandise

- Travel and representative expenses

- Professional photography

- Video editing and post-production

This option also creates stronger sponsorship opportunities, as we would have clearer space to showcase partners and ecosystem supporters.

### **Option 2: Shared Open Standards Booth**

Alternatively, we could participate through a shared Open Standards booth presence.

**Key considerations:**

- Representative expenses

- Merchandise

This approach is more cost-effective while still maintaining visibility, though with reduced programming control and sponsor activation opportunities.

### **Next Steps**

Discuss preferred direction (Dedicated Track vs. Booth)

Estimate total projected budget

Evaluate sponsorship strategy and funding pathways

Identify volunteers/representatives

---

## #1016: JSON Schema <> APidays India 2026

Hello everyone 👋

This issue is opened to begin a structured discussion on how JSON Schema should strategically show up in 2026, particularly at API-focused events such as APIdays India. The goal is to align early on visibility, impact, and budget considerations.

### **Option 1: Dedicated JSON Schema Track**

Hosting a dedicated track would significantly increase visibility and allow us to introduce JSON Schema to a broader audience through curated talks, ecosystem showcases, and implementer stories.

**Key considerations:**

- AV team coverage for sessions (< ~€2,600–€3,000)

- Merchandise

- Travel and representative expenses

- Professional photography

- Video editing and post-production

This option also creates stronger sponsorship opportunities, as we would have clearer space to showcase partners and ecosystem supporters.

### **Option 2: Shared Open Standards Booth**

Alternatively, we could participate through a shared Open Standards booth presence.

**Key considerations:**

- Representative expenses

- Merchandise

This approach is more cost-effective while still maintaining visibility, though with reduced programming control and sponsor activation opportunities.

### **Next Steps**

Discuss preferred direction (Dedicated Track vs. Booth)

Estimate total projected budget

Evaluate sponsorship strategy and funding pathways

Identify volunteers/representatives

---

## #1015: JSON Schema <> APIdays Munich 2026

Hello everyone 👋

This issue is opened to begin a structured discussion on how JSON Schema should strategically show up in 2026, particularly at API-focused events such as APIdays Munich. The goal is to align early on visibility, impact, and budget considerations.

### **Option 1: Dedicated JSON Schema Track**

Hosting a dedicated track would significantly increase visibility and allow us to introduce JSON Schema to a broader audience through curated talks, ecosystem showcases, and implementer stories.

**Key considerations:**

- AV team coverage for sessions (~€2,600–€3,000)

- Merchandise

- Travel and representative expenses

- Professional photography

- Video editing and post-production

This option also creates stronger sponsorship opportunities, as we would have clearer space to showcase partners and ecosystem supporters.

### **Option 2: Shared Open Standards Booth**

Alternatively, we could participate through a shared Open Standards booth presence.

**Key considerations:**

- Representative expenses

- Merchandise

This approach is more cost-effective while still maintaining visibility, though with reduced programming control and sponsor activation opportunities.

### **Next Steps**

Discuss preferred direction (Dedicated Track vs. Booth)

Estimate total projected budget

Evaluate sponsorship strategy and funding pathways

Identify volunteers/representatives

---

## #1014: JSON Schema  <> APidays London 2026

Hello everyone 👋

This issue is opened to begin a structured discussion on how JSON Schema should strategically show up in 2026, particularly at API-focused events such as APIdays London. The goal is to align early on visibility, impact, and budget considerations.

### **Option 1: Dedicated JSON Schema Track**

Hosting a dedicated track would significantly increase visibility and allow us to introduce JSON Schema to a broader audience through curated talks, ecosystem showcases, and implementer stories.

**Key considerations:**

- AV team coverage for sessions (~€2,600–€3,000)

- Merchandise

- Travel and representative expenses

- Professional photography

- Video editing and post-production

This option also creates stronger sponsorship opportunities, as we would have clearer space to showcase partners and ecosystem supporters.

### **Option 2: Shared Open Standards Booth**

Alternatively, we could participate through a shared Open Standards booth presence.

**Key considerations:**

- Representative expenses

- Merchandise

This approach is more cost-effective while still maintaining visibility, though with reduced programming control and sponsor activation opportunities.

### **Next Steps**

Discuss preferred direction (Dedicated Track vs. Booth)

Estimate total projected budget

Evaluate sponsorship strategy and funding pathways

Identify volunteers/representatives

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

## #691: Proposal to formalize the processes for Working Groups

**Labels:** Status: Do not close

### Abstract

As our community grows we'll need to establish working groups to collaborate more efficiently and empower everyone to lead initiatives. We are doing references about working groups in our (yet to be completed) [Charter](https://github.com/json-schema-org/community/pull/325) and there are no specific rules around them what slow down its adoption. 

This is my proposal for defining Working Groups for JSON Schema:

### Definition of a working group

A working group is a group of people in our community who share a common interest beyond GitHub repositories.

A working group must have, at least, one of its members appointed as its chairperson.

Anyone can create a working group. The only prerequisites are to have at least 2 founding members and the approval of the TSC.

A working group should have its own set of goals or objectives. This helps everyone in the working group to stay aligned. The goals must be public and easily accessible by anyone on the internet.

It's recommended that a working group has an associated issue where the group outlines their roadmap. In addition it will be highly recommended the usage of a [GitHub Project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project) to make it easier for others to collaborate.  It's up to the Working Group to decide the structure of the project. E.g., Kanban, Shape Up, TO-DO list, etc.

The name of the group, its members, the goals, and any other relevant information must be listed in the WORKING_GROUPS.yaml file in the community repository.

A working group has no decision power over the roadmap of the projects they may impact. It's up to the maintainers of the repositories involved to approve or reject the resulting pull requests. Therefore, it's highly recommended to either have maintainers of the impacted projects in the working group or make sure everyone is in agreement before deciding about the roadmap of the different repositories/projects.

As soon as the feature is ready, working groups will be listed in the JSON Schema website along with their description, goals, members, an anything the working group wants to include.

### Additional benefits

- Working groups become more discoverable.
- Coordinated effort across different projects/repos.
- Bounty program can also target working groups, especially for tedious tasks.
- Increased transparency of the structure of our community.

### What do you think about this proposal?

Please share your thoughts so we create together the best proposal for our project!

Thanks @fmvilas for the [inspiration](https://github.com/orgs/asyncapi/discussions/1037).

---

## #548: Define the role & responsibilities of the chairpersons

**Labels:** 👥 Team, Status: Do not close

> @Relequestual I think we should add the role&responsibilities of the Executive director/chair. An example [here](https://github.com/asyncapi/community/blob/6e8e91168fb43b23e8ab0662299430ccefc94db4/GOVERNANCE.md#L4)

_Originally posted by @benjagm in https://github.com/json-schema-org/community/issues/456#issuecomment-1748613295_

---

## #521: Let's define together what we understand by "critical" JSON Schema projects

**Labels:** ✨ Enhancement, Status: In Progress, Status: Do not close

### Objective
This issue aims to start a discussion to define together what we understand by "critical" JSON Schema projects and establish the eligibility criteria and the support provided for these projects. Currently taking advantage of and supporting projects Bowtie that are not part of the Github Organization but are critical for the whole JSON Schema Ecosystem and this issue aims to standarize this situation by find a common definition, eligibility criteria and the benefits.

### Defining Critical Projects (My proposal)
To qualify as a "critical" project, a JSON Schema project should meet the following criteria:

* **Language Agnostic**: The project should be language-agnostic, ensuring its relevance to a wide range of developers working with JSON Schema, regardless of the programming language they are using.

* **Uniqueness**: The project should offer unique and valuable functionality, avoiding direct competition with existing tools in the JSON Schema ecosystem. It should fill a gap or provide an innovative solution to a problem not adequately addressed by other projects.

* **Impact**: Critical projects should have a significant and positive impact on the entire JSON Schema ecosystem, benefiting a large user base, or addressing key challenges faced by the community.

* **Open Source**: Critical projects should be Open Source by definition.

### Support for Critical Projects (My proposal)
The support provided to critical projects will include:

* **Participation in Mentoring and Contribution Programs**: Critical projects will be eligible for mentorship programs to help onboard new contributors, and they will have access to resources and guidance to foster their growth.

* **Promotion of New Features and Updates**: We will actively assist critical projects in promoting new features and updates to ensure they reach a wider audience, including cross-promotion within the JSON Schema community and on relevant platforms.

### Process to join the List (To be defined)
For a project to get this status there should be a TSC voting process.

### Projects to consider:

* [Bowtie](https://github.com/bowtie-json-schema/bowtie/)
* [Learn JSON Schema](https://github.com/sourcemeta/learnjsonschema.com)
* [Alter Schema](https://github.com/sourcemeta/alterschema)

### Projects lists
As soon as we have consensus on definition, benefits, accessibility and the projects part of this list we'll make the list available similarly to adopters.md.

### Help us to define this together
We value your input and invite you to participate in this discussion. Please provide your feedback, suggestions, and nominations for projects that you believe meet the criteria for critical JSON Schema projects.

---

## #513: Create a Community Handbook to explain operations and processes

**Labels:** 📝 Documentation, Status: On Hold

It will be beneficial for the JSON Schema Community if we can publish a Community Handbook to explain team structure, operations and processes. This is a great example : https://about.gitlab.com/handbook/marketing/developer-relations/

**Do you think this work might require an [Architectural Decision Record (ADR)](https://github.com/json-schema-org/community/blob/main/CONTRIBUTING.md#key-architectural-decisions)? (significant or noteworthy)**

No

**Work Detail**:
- [ ] Capture feedback from the community.
- [ ] Publish the handbook.

**Any further requirements to resolve this issue**

---

## #424: Enhance public communications strategy

**Labels:** summit-results, Status: Do not close

Problem: Lack of cohesive public face / communication of our status and progress.

There is some existing planned work the improve public communications defined here: https://github.com/orgs/json-schema-org/projects/12/views/5

🚨This Issue and Roadmap Item is marked as "deferred", meaning it is low priority and should not be a focus over other items in the roadmap. However, we should identify opportunities to empower others to contribute to this task, if helpful.

@benjagm to define define success criteria, deliverables, and breakdown of tasks.

Assessed as medium impact/medium effort during our [collaborators summit 2023](https://github.com/orgs/json-schema-org/discussions/391).

---

## #423: Implement and scale the new governance model

**Labels:** summit-results, Status: Do not close

Deliverables:

- [x] Merge governance model document: https://github.com/json-schema-org/community/pull/456
- [ ] Trial run of governance process (I feel [this](https://github.com/json-schema-org/community/issues/521) would be a good candidate for doing such)
- [ ] Request feedback from those involved in the process
- [ ] Compile report and assess if revisions are needed

Assessed as medium impact/low effort during our [collaborators summit 2023](https://github.com/orgs/json-schema-org/discussions/391).

---

## #419: Report on projects financial sustainability requirements

**Labels:** summit-results, Status: Do not close

(To avoid taking credit, note, the below was written by @Julian)

The JSON Schema team is generously sponsored by a number of organizations. In some sense, Postman is a particularly notable organization in this regard, as it funds a number of developers from the team in order to be able to dedicate full-time effort to the JSON Schema ecosystem without any distraction.

Still, it is useful to ask and answer questions like "How much does development of JSON Schema cost today" in order to understand what is needed to sustain, maintain or grow development. This likely includes ensuring we understand what might happen if sponsorship of the project decreases, or more optimistically, how we could grow the project if sponsorship were to increase.

This likely includes:

* assessing the approximate combined operating expense today
  - including one level down of specificity to differentiate between "$$ spent to push the specification forward" vs "$$ spent to support implementations" -- we could perhaps address this with current contributors (speaking e.g. for myself, @Julian) by estimating the fraction of time we spend on implementation specific work vs. community-wide work
  - reviewing yearly expenses beyond salaries (e.g. hosting costs)
*  tallying the current source of funding which supports the above, and including some "gut" estimate of how stable this funding is
  - including OpenCollective funding and/or any other joint funds targeting the community
* calling out specific pieces of ongoing expense which are critical to operation of the project (e.g. maintaining the json-schema.org site)

It is very likely that we would benefit from having someone who has done this sort of calculation (e.g. as part of operations within a for-profit company, as part of a business case, or of course the best would be for a similar open source project).

So a preliminary task for this issue is likely to identify a party qualified to *ask the right questions* for the above.

The primary goal/output is to produce a deliverable which:

* can be maintained on an ongoing basis
* and which contains information about
  - how much does running the project cost today
  - where does the current funding for that cost come from today
  - how stable do we consider that funding

Once we have such a thing, the two obvious follow-on questions would be:

* Do we have a viable plan if the amount of money changes there in either direction, either for finding additional sponsors or otherwise
* How does an increase in $$ relate to any additional help we may want to bring in

Assessed as low-medium impact/low-medium effort during our [collaborators summit 2023](https://github.com/orgs/json-schema-org/discussions/391).

---

## #418: Research of existing implementations by language

**Labels:** summit-results, Status: Do not close

Problem: We do not know which languages have high quality implementations.

While members of the core team / TSC (not yet formally formed) have implementaitons in different languages, we do not know if we have "high quality" implemenations in all major languages.

Having high quality implementaitons in all major languages would improve the ecosystem. If we can identify gaps in implementations, we could then target resources to support specific languages or implementations. Overall, this would improve our ecosystem.

This item is just about the research and report, and not about making any actions or decisoions as a result of such a report.

- [ ] Decide on a list of ~10-15 programming languages or environments to assess (by some combination of popularity, TIOBE, recent publicity, commonality of use for API-adjacent or data validation-adjacent use cases, etc.)
- [ ] Compare this list against the JSON Schema [implementations page](https://json-schema.org/implementations.html)
    * [ ] Confirm this page seems correct for the programming language by searching independently for JSON Schema implementations in GitHub search, Google, etc.
    * [ ] Extract a crude "health" metric of how good support for JSON Schema is in the language based on version availability, maturity of the implementation, activity of development in the implementation and compliance with the specification (time boxed to not be fully in depth)
      - does it fail some very large number of tests
      - does it support recent versions of JSON Schema
      - does it have recent releases
      - does it have recent commits
      - does it have open security warnings
      - does its maintainer consider it production-ready (or explicitly the reverse)
      - how many open issues and pull requests does it have
      - does it implement many/all/some of the interfaces from #408
    * [ ] Document languages which *are* popular but which are deficient in their JSON Schema support
- [ ] Update any [out of date information](https://github.com/json-schema-org/website/blob/main/data/validator-libraries-modern.yml) on the implementations page on the website
- [ ] Write a blog post report for general consumptions about the method, findings, and resulting insights. (And maybe potential future work)

Assessed as high impact/low effort during our [collaborators summit 2023](https://github.com/orgs/json-schema-org/discussions/391).

---

## #415: Complete the new version of the Spec

**Labels:** summit-results, Status: In Progress

Problem: The scope the of next specification release is distributed among different issues and PRs. Some of the items have been included in milestones but not all what makes it difficult to progress with the release discussions. By identifying the pending scope and applying some project management to support the progress we hope to lighten the whole process.

Team working on this issue:
- @benjagm to project manage this work.
- @jdesrosiers and @gregdennis to write up list of work the believe still needs to be done.

Assessed as high impact/high effort during our [collaborators summit 2023](https://github.com/orgs/json-schema-org/discussions/391).

### Updated plan:
- [x] We'll create a new milestone called stable-release. We'll create a project board to enhance collaboration and transparency.
        **Milestone:** https://github.com/json-schema-org/json-schema-spec/milestone/10
        **Project Board:** https://github.com/orgs/json-schema-org/projects/15/views/1
- [ ] We'll conduct a grooming session to setup the initial spec backlog associating the issues with the new milestone.
- [ ] We'll decide if we remove the existing milestones.
- [ ] We'll decide a labelling system to identify the issues' workflow. Before, during and after an issue is added to the spec scope.
- [ ] We'll run 1 week cycles to decide the issues to focus on during that cycle. 1 session at the beginning to decide scope of the cycle and 1 session at the end to review the closed issues, and decide the issues for the next cycle. Short cycles can be done in during the OCWM.

---

## #326: Evaluate the usage of official test suite by JSON Schema implementations.

**Labels:** help wanted

**Slack Discussion:** [Link](https://json-schema.slack.com/archives/C8CQ81GKF/p1675868489424269)

**Work Summary**:
<!-- These are some suggestions to get you started, but feel free to write your own from scratch -->
Understand how JSON Schema implementations are currently using the official test suite by JSON Schema to find missing and out-of-date tests. The resulting report would be beneficial and highlight why Bowtie is so important.

**Requirements:**
1. The list of JSON Schema implementations https://json-schema.org/implementations.html#validators or the smaller list of implementations bowtie supports https://github.com/bowtie-json-schema/bowtie/tree/main/implementations.
2. Access to the GitHub repositories of each implementation.
3. Search for a reference to the official test suite repository in the implementation's GitHub repository.
4. Determine the age of the version of the test suite being referred to and write down the commit hash of the test suite.

**Expected outcome:**
* A report with information about the usage of the official test suite by JSON Implementations, including which have missing or outdated tests.
* The report will provide a comprehensive overview of the adoption of the official test suite and the importance of using Bowtie to maintain up-to-date testing.

**Do you think this work might require an [Architectural Decision Record (ADR)](https://github.com/json-schema-org/community/blob/main/CONTRIBUTING.md#key-architectural-decisions)? (significant or noteworthy)**

No

**Work Detail**:
<!-- Each item in this list may be a single Pull Request or a single PR may cover multiple  -->
- [ ] The list of JSON Schema implementations https://json-schema.org/implementations.html#validators or the smaller list of implementations bowtie supports https://github.com/bowtie-json-schema/bowtie/tree/main/implementations.
- [ ] Access to the GitHub repositories of each implementation.
- [ ] Search for a reference to the official test suite repository in the implementation's GitHub repository.
- [ ] Determine the age of the version of the test suite being referred to and write down the commit hash of the test suite.
- [ ] Create document with the results.

**Any further requirements to resolve this issue**

---

## #324: Adopt either the Contributor License Agreement (CLA) or the Developer Certificate of Origin (DCO)

**Labels:** Status: Do not close

I'm going to recommend using DCO, as it is less problematic for potential contributors.

---

## #274: Publish Project Charter on website or GitHub

**Labels:** openjsf-onboarding, Status: Do not close

Requiremnet for OpenJS Foundation onboarding.
Template provided: https://github.com/openjs-foundation/cross-project-council/blob/HEAD/PROJECT_CHARTER_TEMPLATE.md

While we are no longer a project under the OpenJS Foundation, we still feel it important to have a charter. This helps keep us focused and enables newcomers to have a clear understanding of our objectives and boundaries. The template is still useful.

---

## #183: Open Community Working Meeting 2022-06-03

**Labels:** Working Meeting, Status: Stale

<!-- Starts Here -->

📺 [See Recording](https://postman.zoom.us/rec/share/jTcXUOgjF0N5CFouqEK5uIKXHxCzN8zySQhFu9ab_n-Tc6FuBTHsrZ_AsRCJg2J3.pWzEGCNCf3sM2Yy9?startTime=1654282518000)


⏪ [Go To Previous Meeting](https://github.com/json-schema-org/community/issues/177)

## Agenda

<!-- Added from the Meeting Issue -->

```
No agenda items were set for this meeting
```

## Highlights

- @jviotti shared his project for upgrading and downgrading JSON Schemas between versions/drafts. [AlterSchema](https://github.com/jviotti/alterschema) which is designed to be langauge agnostic.

- There was a good discussion around schema version compatibility from @jdesrosiers and @awwright.

- Further discussion on vocabularies and how they could look in the future.

- A discussion on keywords that depend on other keywords

- A discussion on finite state machines, push down automata and ABNF's applicability in general and to JSON Schema. 
 
## Actions

- [x]  @Relequestual to have a backup for scheduled calls when on a holiday. 

- [ ]  @jdesrosiers to write a blog post about concerning additionalProperties, inheritence concept etc.

## Attendees

| Account           |
|:-----------------:|
| @awwright         |
| @jdesrosiers      |
| @jviotti          |
| Vipul             |
| Pranit Brahmbhatt |
| @gregsdennis      |
| @handrews         |

## Details

### Upgrading and downgrading `Schema` versions using `Alter Schema`

Alterschema is trying to solve upgrading and downgrading between JSON Schema and both OpenAPI versions. i.e how given any json schema can you upgrade it and can you also downgraded in a lossy manner. 

As it was noticed ( while working at Postman ) that people are stuck with `draft 4` and `draft 6`. We realized that people do want to upgrade but the tooling's support for older versions becoming a barrier.

---

### Fragmented ecosystem and compatibility.

Working group discussed how the ecosystem is fragmented. An example presented had to do with differences in semantic understanding while in usage the behaviour is expected with original meaning i.e of the JSON Schema specification. This leads to differences in implementation themselves i.e behaviour changes. Another is certain limitations eg. limited amount of memory leading changes in implementation and compatibility.

There is an understanding that the vocabulary system is to address those problems in the future. Also, it is understood that idea of vocabularies should be malleable where it's a collection of keywords that are defined so that defining keywords and collecting them into a group, can be called a vocabulary.

Regarding keywords that depend on other keywords, there were two points raised of resuability and usage of multiple keywords at a time and the annotation for behavior purposed of the same. The current proposal of the working group is already understood to moving in the direction of ironing it out.

---

Further Read

*[truncated]*

---

## #173: MDN/Open Web Docs case study

**Labels:** 📈 case study, Status: Stale

Contacted Florin Scholz, who cc'ed Daniel Beck.
Both responsibile in some capacity for using JSON Schmea in MDN web docs and compat data.
Both keen to collaboarate on a case study and potentially a video later.

---

## #172: Open Community Working Meeting 2022-05-06

**Labels:** Working Meeting, Status: Stale

<!-- Starts Here -->

📺 [See Recording](https://postman.zoom.us/rec/share/0-1cLt1wcUQtjZdhIL2IXRVoMI5AdoCFhb8CpW0HZIDN6HDmn4j_CMbAqZHVYvHH.5DezI8Wx1BggzEox?startTime=1651863577000)

⏪ [Go To Previous Meeting](https://github.com/json-schema-org/community/issues/164)

## Agenda

<!-- Added from the Meeting Issue -->

| Topic                                                                                                                                                                                                                                                                                                                                                                            | Owner         | Decisions/NextSteps                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Review last call's action items                                                                                                                                                                                                                                                                                                                                                  | @Relequestual | The action items were reviewed                                                                                                                                                                                     |
| JSON Schema 2020-12 patch 1 rc-0 released<br/>Feedback requested. rc-0 feedback closes 2022-05-14.<br/>Is the release process looking ok? [Spec Issue #1191](https://github.com/json-schema-org/json-schema-spec/issues/1191)                                                                                                                                                    | @Relequestual | The updates can be found at [Spec Issue #1191](https://github.com/json-schema-org/json-schema-spec/issues/1191)                                                                                                    |
| Website development progress - Johannes showed progress on the office hours call.                                                                                                                                                                                  

*[truncated]*

---
