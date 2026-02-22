# Kiwix — Project Ideas

**Source:** https://kiwix.org/en/google-summer-of-code/
**Scraped:** 2026-02-22T23:28:47.614968

---

-
For the full list of issues you can work on, see our GitHub repositoriesÂ

[/openZIM](https://github.com/openzim),[/offspot](https://github.com/offspot)and[/kiwix](https://github.com/kiwix)GSoC has three sets of projects, lasting ~90, ~175 and ~350 hours approximately so that people who can not work full-time (because of exams or whatnot) can still participate.

**We do not prioritize long over short projects**: the job must be done, they’re just an indication for your own comfort.A couple of project ideas are listed below to get you started:Â

## WP1 Combinator Builder

WP1 is the bot and website that provides tables like

[this one](https://en.wikipedia.org/wiki/User:WP_1.0_bot/Tables/OverallArticles)on English Wikipedia. The tables help editors determine which articles they should focus on in their WikiProjects. The website also provides tools for creating a Wikipedia âselectionâ, ie a list of articles, so that they can create a ZIM file and have a subsetted offline version of Wikipedia.There are currently multiple ways to build a selection, from simple article lists to SPARQL queries. We wish to create a âcombinatorâ builder, which allows a user to combine existing or future builders to create a final selection.

**Deliverables:**- Provide a data model for a combinator builder that integrates with the rest of the WP1 site
- Provide a UI frontend for users to create combinator builders
- Sufficient backend and frontend tests

**Skills required:**- Good understanding of Python
- Understanding of Javascript
- Understanding of Vue.js or willingness to learn

**Project length:**Small (about 90 hours of work)**Repository:**[https://github.com/openzim/wp1](https://github.com/openzim/wp1)## Hermetic Test Suite for MWoffliner

MWofflinerâs test suite currently relies heavily on live HTTP requests to Wikipedia and other MediaWiki sites, resulting in 30 minutes test runs that are flaky, resource-intensive, and unsuitable for CI/CD pipelines. This project aims to rewrite the test infrastructure to be hermeticâusing mocked responses, local test fixtures, and in-memory MediaWiki instances where needed.

**Deliverables:**Contributors will identify all external dependencies, create comprehensive mock data representing various MediaWiki configurations and edge cases, refactor tests to use dependency injection for HTTP clients, and establish patterns for future hermetic testing. The goal is reducing test runtime to under 10 minutes while improving coverage and reliability. By the end, the tests should be as hermetic as possible. A stretch goal is to separate any remaining non-hermetic tests (which need to make HTTP calls for a technical reason) to a separate e2e test target.**Skills required:**Strong testing experience (unit, integration, mocking frameworks), TypeScript/Node.js proficiency, understanding of HTTP mocking techniques (nock, MSW, or similar), experience with CI/CD systems. Familiarity with MediaWiki structure and test architecture design patterns is a plus: use the time before applications are opened to familiarize yourself with the tool.**Project Length:**Medium (150-175 hrs in total)**Repository:**[github.com/openzim/mwoffliner](https://github.com/openzim/mwoffliner)## Refactor MWoffliner Core Architecture

MWoffliner is a tool for scraping MediaWiki content into ZIM files for offline access. This project involves refactoring the codebase to improve maintainability, modularity, and performance. The current architecture has grown organically over time, leading to tight coupling between components, unclear separation of concerns, and difficulty adding new features.

**Deliverables:**Contributors will work to identify architectural pain points, design a cleaner module structure, and incrementally refactor critical paths while maintaining backward compatibility. Key areas include separating scraping logic from ZIM packaging, improving the article processing pipeline, and making the codebase more testable.**Skills required:**Strong TypeScript/Node.js experience, understanding of software architecture patterns, experience with large-scale refactoring, familiarity with MediaWiki APIs (beneficial, but youâll learn anyway). Contributors should be comfortable reading unfamiliar codebases, writing design documents, and working incrementally with extensive test coverage to prevent regressions (hard requirement).**Project length:**Long (350 hours)**Repository**:[github.com/openzim/mwoffliner](https://github.com/openzim/mwoffliner)## Testing and Reliability Engineering for Kiwix-Android

While the project already contains unit and instrumentation tests, the current testing infrastructure has several gaps: incomplete test coverage, flaky tests, missing scenario tests for critical flows (downloads, storage, restart behavior), partial or unused coverage tooling, and inconsistent CI reliability

This project focuses on building a robust, scalable, and maintainable testing ecosystem for the app. The goal is not simply âadding tests,â but establishing production-grade reliability engineering practices

**Deliverables:**By the end of the program we expect fixed flaky/failing tests; significant (and measured) increase in unit test coverage; Multiple stable instrumentation tests; a working coverage pipeline; CI improvements and reliability; a testing documentation and of course throughout the project clean, reviewable PRs**Skills required:**Kotlin, JUnit, Robolectric, Espresso / Compose Testing, MockK or Mockito, GitHub Actions and Jacoco**Project length:**Long (350 hours)**Repository**:[github.com/kiwix/kiwix-android](https://github.com/kiwix/kiwix-android) -
### Want to join?

Think hard about what you want to do, and go to the

[Google Summer of Code](https://summerofcode.withgoogle.com/)website between 16 to 31 March to register and submit your project idea(s).After reviewing all proposals, projects will be announced on 30 April. (

[full timeline](https://developers.google.com/open-source/gsoc/timeline))### Help & Tips

We want to be clear upfront that

**we will not select candidates who have never made at least**: we make our choice based on how candidates handle themselves (is the code clear, are there comments, how do they explain their choices when asked,*one*PR to our codebase*etc.*). PRs do not need to be related to the project submitted – we just need to know that you can work in a team. If we don’t know you, we can’t choose you! And if your project has “UI” in it, then it probably is a good idea to submit a mockup of what you plan to implement.(We also wrote a helpful

[guide to Writing your Google Summer of Code](/ideas/kiwix/writing-your-google-summer-of-code-application)application)Last but not least: over the years about half the contributors who did GSoC with Kiwix came up with their own project rather than one from our list â be

**bold**!### Do you have questions?

Then come and join us on ourÂ

[Slack channel](https://join.slack.com/t/kiwixoffline/shared_invite/enQtOTUyMTg4NzMxMTM4LTU0MzYyZDliYjdmMDYzYWMzNDA0MDc4MWE5OGM0ODFhYjAxNWIxMjVjZTU4MTkyODJlZWFkMmQ2YTZkYTUzZDY)!
