# Processing Foundation — Project Ideas

**Source:** https://github.com/processing/Processing-Foundation-GSoC/wiki/Project-Ideas-List-(GSoC-2026)#project-ideas-list
**Scraped:** 2026-02-22T23:28:47.567922

---

## About the Processing Foundation

Our mission at the Processing Foundation is to promote software learning within the arts, artistic learning within technology-related fields, and to celebrate the diverse communities that make these fields vibrant, liberatory, and innovative. Our goal is to support people of all backgrounds in learning how to program and make creative work with code, especially those who might not otherwise have access to tools and resources. We also believe that some of the most radical futures and innovative technologies are being built by communities that have been pushed to the margins by dominant tech.

To learn more about the Processing Foundation, see our official website at [processingfoundation.org](https://processingfoundation.org/).


## Feedback & Proposal Process

Interested? Great! We're excited to read all this year's projects. Below are some essential resources for all applicants.

* [This thread on our forum](https://discourse.processing.org/t/updates-about-gsoc-2026-org-application-in-progress/47450) is the best place to ask your questions, org admins and mentors will regularly answer public questions!

* [Please carefully review the GSoC timeline and guidelines](https://opensource.googleblog.com/2025/12/shape-future-with-google-summer-of-code.html)

* Right now, project proposal applications are **not open** - we are in the process of applying as an organization. Once applications open on March 16, an applications **template** will be linked here, as well as details of the selection process. Be sure to use this template to improve your application.

* It is possible to get feedback on your proposals before you submit. The final deadline to submit proposals is March 31, and we will have a signup form to submit your drafts up to one week before. If you have a draft (even if it has parts missing! Even if it doesn't quite follow the template! Everything is OK at this stage.) ready before March 23rd, org admin(s) / mentor(s) will definitely review it. If you have a draft ready earlier, more than one round of review might be possible - but it depends on volume of requests, and is not guaranteed. We will do our best to support all applicants as well as we can!

## Important Notes

Whether your proposals focuses on one of the below ideas or a custom project, please keep the following in mind.

* Do not rely on AI in your proposal or PRs: AI use in your proposal should be clearly disclosed based on our [GSoC AI usage guideline](/ideas/processing-foundation/processing-processing-foundation-gsoc). Fully or largely AI-generated PRs may be closed, and are not in line with our [AI usage policy](https://github.com/processing/p5.js/blob/main/AI_USAGE_POLICY.md).

* PRs are not required, and PRs (and other activity in online community spaces) that consistently ignore contribution and community guidelines can actually make your proposal less likely to succeed. Before making any PR, please be sure to [read the contributor guidelines](https://p5js.org/contribute/contributor_guidelines/) carefully.

* We're especially interested in why you are interested in the idea you propose! Please include Processing or p5.js sketches you've worked on, or any other artistic or programming projects that help us understand your perspective.

## Project Ideas List

These ideas indicate important areas of work across [p5.js Web Editor](https://github.com/processing/p5.js-web-editor), [p5.js JavaScript library](https://github.com/processing/p5.js), [p5.js Reference Website](https://github.com/processing/p5.js-website), [Processing4 Java library](https://github.com/processing/processing4/), and a new implementation of Processing/p5 in Lua, [L5](https://l5lua.org/). Creative interpretations or custom projects are welcome, but keep in mind that proposals very different from the below topics will require research while writing your proposal. In proposing custom projects, be sure to review carefully existing work, and get in touch using the forum above. We expect most applications to propose 175H/Medium sized projects, though if a different scope is well justified in the proposal, larger projects would also be considered.

### Eyedropper Color Debugging in the p5.js Editor

Enable eyedropper debugging in the p5.js Web Editor, in or near the simplified console log pane. This project would require a design proposal, as well as a plan for iteration. It came up during discussion of the new p5.strands feature ([read more](https://beta.p5js.org/tutorials/intro-to-p5-strands/)), that it would be helpful to show the RGBA channel values, each in 0-1 range, when user hovers on any pixels in the canvas with the mouse. An eyedropper tool may be helpful for any type of sketch, but since it is especially important for shader programming, the focus would be on 0,1 range. It would be important to consider how to turn this debugging feature on or off to not interfere with the sketch; for example, you can review how injection is used currently by the Accessibility Settings in the editor. 

* Expected Outcomes: Improve accessibility of shader programming education resources by surfacing the most foundational debugging tool - eyedropper - in a clear and easy to use place.
* Skills/tech: Familiarity with p5.strands as a user - be sure to include at least one p5.strands in your application! JavaScript skills are required; experience with shader programming is a plus but not required.
* Mentor: Diya Solanki (proposal review supported by Claudine Chen)
* Size and Rating: 175H, Medium

### E2E Testing for the p5.js Web Editor

The [p5.js Web Editor](https://github.com/processing/p5.js-web-editor) is undergoing some current and future refactor work (eg. Typescript Migration, self-hosting support). In order to prevent silent regressions, we should enhance the existing automated test suite to include end-to-end tests to cover key front-end user-flows.

These user flows will be defined by the mentee and mentor, but the definition will be driven primarily by the mentee. The new e2e test suite should be able to be run locally by contributors, and be automatically run on every PR into ‘development’.

#### Expected Outcomes:
- New PRs into the `develop` branch of the p5.js Web Editor will automatically trigger a new test suite called `e2e`
- The test will include some integration with a test database for `users` & `projects`
- Any core user flows that have not been implemented yet are documented in a designated section in ‘Contributing’ docs & clearly defined for other contributors to pick up.

<details>
  <summary>
    Examples of core user flows could include:
  </summary>
  - Unauthenticated flow:
    - User can write code and run previews of sketches without logging in
    - User sees prompt to sign up when they try to save a sketch
    - User can download a sketch without logging in
  - Authenticated flow:
    - User can write code and run previews of sketches
    - User can save sketches, and see their changes reflected upon re-navigating to the saved sketch
    - User can edit existing sketches and save them
    - User can log out
</details>

#### Skills/tech: 
- Prior experience with testing frontend code is required. Playwright or Cypress preferred, but experience with Vitest or Jest with frontend code will satisfy the requirement.
- Ability to empathize with non-technical users & communicate technical details in non-technical language is required.
- Prior experience with the p5.js web editor is preferred.
- Some prior experience with Github Actions is preferred but not necessary and will be learned during the project.
- Interest or experience in product-management is preferred but not necessary and will be learned during the project.

**Mentor:** [Claire Peng](https://www.linkedin.com/in/pengclaire/) (proposal review supported by Claudine Chen)<br><br>
**Size and Rating:** 175H Medium

<details>
  <summary><strong>Useful links</strong></summary>

  <ul>
    <li>
      <a href="https://github.com/processing/p5.js-web-editor/blob/develop/client/index.integration.test.jsx">
        Current frontend integration test
      </a> - This current test is only a snapshot of the components on the web editor, so it does not yet cover ‘end-to-end’ user flows. Please see Playwright or Cypress documentation for examples.
    </li>
    <li>
      <a href="https://github.com/processing/p5.js-web-editor/tree/develop/.github/workflows">
        Current test workflow definitions
      </a>
    </li>
    <li>
      <a href="https://github.com/processing/p5.js-website/pull/933">
        Playwright setup example (Accessibility Testing)
      </a>
    </li>
  </ul>
</details>

### Full Texture Support for `.mtl` Files

This enhancement in the WEBGL sub-area of p5.js would increase reach and would make it easier for people to use pre-made 3D-models within their p5.js projects. Currently p5.js supports `.obj` files for 3D models with materials loaded from `.mtl` files but only vertex colors (`map_Kd`). Implementing this feature would involve proposing a new data structure capable of handling both 3D models and their associated textures, potentially multiple per model. You can review previous [discussion](https://github.com/processing/p5.js/issues/6924) and [work](https://github.com/processing/p5.js/pull/6710).

Aim: A model can have multiple materials, each with its own texture. The structure needs to: (1) Store loaded textures per material, (2) Map materials to faces/vertices, (3) Handle multiple textures per model, (4) Support other MTL texture maps (map_Ka, map_Ks, map_Ns, map_Bump, etc.), (5) Handle models with mixed materials/textures.

This would broaden access and creative possibilities, as users could use textured models from common sources, with more detailed and textured 3D models used by artists/creative technologists, and following  industry standards of supporting OBJ/MTL workflows.

* Expected Outcomes: Full Texture support for pre-made 3D-models, including visual tests. 
* Skills/tech: WEBGL,  JavaScript, Experience using p5.js 
* Mentor: Diya Solanki (proposal review supported by Claudine Chen)
* Size and Rating: 175H/300H, medium

### Continued Development of Translation Tracker

Propose an extension of the [Translation Tracker GitHub Action](https://github.com/processing/p5.js-website/tree/main/.github/actions/translation-tracker) on the p5.js reference website. This tooling supports community translation of the p5.js documentation across five languages (English, Spanish, Simplified Chinese, Korean, and Hindi).

In your proposal, focus on extending and improving this translation tracker infrastructure. What would make it easier for new contributors to start translating? Potential directions include: expanding tracking to cover all content types, creating translation stub files to lower the barrier for new translators, improving issue-to-PR workflows (such as auto-closing issues when translations are merged), building a translation progress dashboard - or your own creative ideas! The p5.js community values human translation over automation, so the goal is tooling that assists translators rather than replaces them.

* Expected Outcomes: Enhanced GitHub Action(s) and/or companion tooling in the p5.js [website repository](https://github.com/processing/p5.js-website) that improves the translation contributor experience and helps increase documentation coverage across supported languages.
* Skills/tech: JavaScript, Astro, Github Actions/Workflows; optional: JSDoc, documentation.js
* Mentor: Divyansh Srivastava (proposal reviews supported by Claire Peng)
* Size and Rating: 175H, Medium


### Extend Tests in Processing4

We would like to extend the testing ecosystem for [Processing4](https://github.com/processing/processing4) to eventually include extensive unit tests, integration tests, end-to-end tests, and visual regression tests. Tests are important to ensuring there are few regressions as we develop and maintain the codebase. What experience do you already have in developing tests for an application? Currently, Processing4 already includes both unit and visual regression tests. A strong proposal is based on and effectively extends the existing testing infrastructure. We invite you to suggest your own scope and focus, and will prioritize a realistic proposal over an ambitious one.

* Expected Outcomes: Additional tests that can run for Processing4 locally and as a part of CI/CD
* Possible Mentors: [Claudine Chen](https://mingness.github.io/)
* Skills required/preferred: Preferably, some familiarity with types of tests and writing tests in Java or another programming language. Some familiarity with Processing, so they have some idea of what we need tests for; also ideally familiarity with git and Github.
* Size and Rating: 175H, Medium/Hard

### Expanding L5: Sound, Video and Core Improvements 

L5 (L5lua.org) is a new Processing-inspired creative coding library in Lua and built on the LÖVE/Love2d framework designed for longevity and low-resource computing. This project focuses on expanding L5’s capabilities through new sound and video libraries, improving a programmer’s experience with better error messages, and achieving feature parity with Processing/p5.js core functionality.

* Expected Outcomes: Possible outcomes include building out L5sound and L5video libraries, implementing friendly error messages to improve the beginner experience, and debugging/fixing errors to achieve feature parity with Processing/p5.js. Additional work could involve improving bezier curves, adding stateful styles to push()/pop() transformation matrices, expanding input/output options (JSON), and contributing to documentation.
* Skills/tech: Experience with p5.js and/or Processing essential; Familiarity with Lua programming and the LÖVE/Love2d framework a plus but not required. Optional: experience with p5.sound.js, Processing Sound library, or audio/video programming. 
* Mentor: [Lee Tusman](https://leetusman.com/)
* Size and Rating: 175H Medium

### Code Translation between Processing Sound and p5.sound.js

Both p5.js and Processing support sound synthesis, playback, and analysis, but only p5.js does it directly in the web browser with [p5.sound.js](https://github.com/processing/p5.sound.js). An automated tool or interface for converting [Processing Sound](https://processing.org/reference/libraries/sound/index.html) to p5.sound.js and vice versa would benefit both communities: Processing Sound users could more easily share work on the web, and p5.sound.js users could more easily adapt their sketches to a wide variety of devices. We are especially excited about creative approaches to the problem of sharing sound sketches across the ecosystem even if they are not specifically translating code!

* Expected Outcomes: A possible technical outcome could be a standalone interactive webpage with user-friendly settings that helps convert Processing Sound sketches into p5.sound.js sketches, and vice versa. The community impact extends to both users of Processing Sound and p5.sound.js, and to current and future contributors!
* Possible Mentors: Kevin Stadler (proposal review supported by Lee Tusman)
* Skills: experience with both Java and JavaScript essential; optionally: some familiarity with p5.sound.js, Processing Sound, or Web Audio technologies can be a plus
* Size and Rating: 175H, Medium
