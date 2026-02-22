# 965

**Parent:** JSON Schema — Project Ideas
**Source:** https://github.com/json-schema-org/community/issues/965
**Scraped:** 2026-02-22T23:28:47.586025

---

## Comprehensive test suite for `format` validation

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

