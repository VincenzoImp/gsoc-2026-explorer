# #991

**Parent:** JSON Schema — Project Ideas
**Source:** https://github.com/json-schema-org/community/issues/991
**Scraped:** 2026-02-22T23:28:47.585898

---

## GSoC 2026: Replacement for vscode-json-languageservice

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

