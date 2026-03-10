# "impact: high"

**Parent:** Oppia Foundation — Project Ideas
**Source:** https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+label%3A%22Impact%3A+High%22
**Scraped:** 2026-03-10T16:58:40.307703

---

## #25255: [E2E/Acceptance CI Failure]: Acceptance (logged-in-learner/completes-the-exploration-and-decides-what-to-do-next)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

Acceptance (logged-in-learner/completes-the-exploration-and-decides-what-to-do-next)

### Did the test fail after an automatic rerun?

Test failed once, was automatically re-run, and then failed again

### Did the test fail when running on desktop, mobile, or both?

Desktop, Mobile

### Stacktrace

```shell
FAIL core/tests/puppeteer-acceptance-tests/specs/logged-in-learner/completes-the-exploration-and-decides-what-to-do-next.spec.ts (160.068 s)
  Logged-In Learner
    ✕ should be able to rate the lesson

  ● Logged-In Learner › should be able to rate the lesson

    TimeoutError: Element <div.oppia-editable-section-mask.e2e-test-state-edit-content> took too long to be clickable.
    Original Error:
    waiting for function failed: timeout 30000ms exceeded

      493 |         : selector;
      494 |     try {
    > 495 |       await this.page.waitForFunction(isElementClickable, {}, element);
          |                       ^
      496 |     } catch (error) {
      497 |       if (error instanceof Error) {
      498 |         await this.page.evaluate(isElementClickable, element, true, true);

      at new WaitTask (../../../node_modules/puppeteer/src/common/DOMWorld.ts:813:28)
      at DOMWorld.waitForFunction (../../../node_modules/puppeteer/src/common/DOMWorld.ts:728:22)
      at Frame.waitForFunction (../../../node_modules/puppeteer/src/common/FrameManager.ts:1368:28)
      at Page.waitForFunction (../../../node_modules/puppeteer/src/common/Page.ts:3358:29)
      at BaseUser.waitForElementToBeClickable (utilities/common/puppeteer-utils.ts:495:23)
          at runMicrotasks (<anonymous>)
      at BaseUser.clickOnElement (utilities/common/puppeteer-utils.ts:520:5)
      at BaseUser.clickOnElementWithSelector (utilities/common/puppeteer-utils.ts:555:5)
      at BaseUser.updateCardContent (utilities/user/exploration-editor.ts:2863:5)

Test Suites: 1 failed, 1 total
Tests:       1 failed, 1 total
Snapshots:   0 total
Time:        161.734 s
Ran all test suites matching /core\/tests\/puppeteer-acceptance-tests\/specs\/logged-in-learner\/completes-the-exploration-and-decides-what-to-do-next.spec.ts/i.
INFO     2026-03-09 23:06:12,232 shutdown.py:48] Shutting down.
Error: 3-09 23:06:12 +0000] [2971] [ERROR] Worker (pid:2975) was sent SIGTERM!
Error: 3-09 23:06:12 +0000] [3001] [ERROR] Worker (pid:3003) was sent SIGTERM!
Error: 3-09 23:06:12 +0000] [2967] [ERROR] Worker (pid:2973) was sent SIGTERM!
Error: 3-09 23:06:12 +0000] [2808] [ERROR] Worker (pid:2810) was sent SIGTERM!
INFO     2026-03-09 23:06:12,946 stub_util.py:321] Applying all pending transactions and saving the datastore
INFO     2026-03-09 23:06:12,946 stub_util.py:324] Saving search indexes
```

### Screenshots and/or Screen Recordings

N/A

### Occurrences

https://github.com/oppia/oppia/actions/runs/22862346424/job/66345183378?pr=25086

### Additional Information

The failure appears to occur when Puppeteer waits for
`oppia-edit

*[truncated]*

---

## #25245: [Feature Request]: Create website banner for Financial Literacy Campaign (Launch: April 7)

**Labels:** enhancement

### Is your feature request related to a problem? Please describe.

In preparation for the launch of the  Financial Literacy classroom, the Marketing team is planning to run a Financial Literacy campaign and would like to request a campaign banner for the Oppia website to support the launch campaign.

The campaign will begin on April 7, and the banner will be activated once the campaign goes live.

### Describe the solution (or solutions) you'd like

I have created a design sample in Figma to illustrate the layout and messaging we have in mind. Please see the link here: [https://www.figma.com/design/wAUQVHxnPslVMaPelzAgCy/Untitled?node-id=0-1&t=mLF3cMMJz271YM0n-1]

### Describe alternatives you've considered and rejected

_No response_

### Additional context

**Additional Context**

- The banner should be implemented as a site-wide banner so it is visible across the website during the campaign period.
- The banner should appear on all pages except the Donate page.
- The preferred language for this campaign is English. - We would consider translating banners into additional languages in future campaigns, but for this launch, we would like to keep it in English.

**Campaign Banner Close Behavior**
- If a user clicks the close (✕) button on the Financial Literacy Month campaign banner, the banner should be temporarily hidden but should reappear after 24 hours.

**Expected Behavior**
- When a user visits the site, the campaign banner is displayed.
- If the user clicks the ✕ close button, the banner should disappear immediately.
- The banner should remain hidden for the rest of the session or for up to 24 hours.
- After 24 hours, the banner should appear again when the user revisits the site.

---

## #25234: [CI Failure]: GitHub Actions network timeout during repository fetch

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Frontend

### Which CI step failed?

Checkout the repository so that local actions can be used

### Stacktrace

```shell
Fetching the repository
  /usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +0a873b02f907c1957b64326e755ab0b7d7a1d0d5:refs/remotes/pull/24419/merge
  Error: fatal: unable to access 'https://github.com/oppia/oppia/': Failed to connect to github.com port 443 after 132959 ms: Connection timed out
  The process '/usr/bin/git' failed with exit code 128
  Waiting 17 seconds before trying again
  /usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +0a873b02f907c1957b64326e755ab0b7d7a1d0d5:refs/remotes/pull/24419/merge
  Error: error: RPC failed; curl 56 GnuTLS recv error (-54): Error in the pull function.
  Error: fatal: protocol error: bad pack header
  The process '/usr/bin/git' failed with exit code 128
  Waiting 14 seconds before trying again
  /usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +0a873b02f907c1957b64326e755ab0b7d7a1d0d5:refs/remotes/pull/24419/merge
  Error: fatal: unable to access 'https://github.com/oppia/oppia/': Failed to connect to github.com port 443 after 133423 ms: Connection timed out
  Error: The process '/usr/bin/git' failed with exit code 128
```

### Screenshots / Screen Recordings

_No response_

### Occurrences

Once 

### Additional Information

_No response_

### Debugging document link

_No response_

---

## #25231: [BUG]: InteractionBackendDict.id uses string instead of InteractionSpecsKey, requiring unsafe cast in state editor

**Labels:** triage needed, bug

### Describe the bug

Interaction ID contracts in the frontend are too broad (string | null) instead of using InteractionSpecsKey | null. Because of this mismatch, callers need casts like as InteractionSpecsKey (for example in state editor initialization). This weakens type safety and can hide contract errors.

### URL of the page where the issue is observed.

N/A

### Steps To Reproduce

1. Open `core/templates/components/state-editor/state-editor.component.ts`.
2. Locate the call to `stateInteractionIdService.init(...)`.
3. Observe that `stateData.interaction.id` requires `as InteractionSpecsKey`.
4. Open `core/templates/domain/exploration/interaction.model.ts`.
5. Observe `InteractionBackendDict.id` is typed as `string | null` instead of `InteractionSpecsKey | null`.

### Expected Behavior

Interaction ID types should use InteractionSpecsKey | null across relevant frontend contracts so casts are not needed in callers like state editor.

### Screenshots/Videos

N/A

### What device are you using?

Desktop

### Operating System

MacOS

### What browsers are you seeing the problem on?

Chrome

### Browser version

_No response_

### Additional context

_No response_

### Tips for developers

- Cast currently appears in:
  - `core/templates/components/state-editor/state-editor.component.ts`
- Current frontend contract:
  - `core/templates/domain/exploration/interaction.model.ts`
  - `InteractionBackendDict.id` is `string | null`
- Backend reference:
  - `core/domain/state_domain.py` -> `InteractionInstanceDict.id: Optional[str]`
- Goal:
  - Introduce/use `InteractionSpecsKey | null` in frontend interaction ID contract where appropriate.
  - Remove unnecessary casts (starting with state editor).
  - Keep `null` support for uninitialized/default interaction state.
- Validation:
  - `python -m scripts.run_typescript_checks`
  - `python -m scripts.run_typescript_checks --strict_checks`

---

## #25227: [E2E/Acceptance CI Failure]: Acceptance (curriculum-admin/create-subtopic-study-guide-with-multiple-sections)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

run mobile acceptance tests to check flakiness

### Did the test fail after an automatic rerun?

Test failed once but was not automatically re-run

### Did the test fail when running on desktop, mobile, or both?

Mobile

### Stacktrace

```shell
FAIL core/tests/puppeteer-acceptance-tests/specs/curriculum-admin/create-subtopic-study-guide-with-multiple-sections.spec.ts (264.41 s)
  Curriculum Admin
    ✕ should create a study guide with multiple sections. (40335 ms)
    ✕ should add sections with workedexamples. (30134 ms)
    ✕ should preview a study guide. (30001 ms)

  ● Curriculum Admin › should create a study guide with multiple sections.

    Expected image to match or be a close match to snapshot but was 7.307546226886556% different from snapshot (73112 differing pixels).
    See diff for details: /home/runner/work/oppia/oppia/core/tests/puppeteer-acceptance-tests/curriculum-admin/create-subtopic-study-guide-with-multiple-sections/prod-mobile-screenshots/diff-snapshots/sectionContentLengthError-diff.png
    Download the artifact folder diff-snapshots from the github workflow to check the difference between the old screenshot(s) and the new one(s). To download the folder, go to "Summary" of the CI Job of the PR and find the "Artifacts" section. The artifact folder name should be something like diff-snapshots_(suite-name)_desktop_original. The diff screenshot(s) should end with "-diff".
    Please update the screenshots if the UI changed. If screenshot comparisons consistently show the same difference percentage across multiple test runs, the baseline screenshot(s) should be updated.
    To update the screenshots(s), you should run the tests in CI, download the artifact folder new-snapshots from the github workflow and use the screenshots in that folder to replace the old one(s).
    To download the folder, go to "Summary" of the CI Job of the PR and find the "Artifacts" section. The artifact folder name should be something like new-snapshots_(suite-name)_desktop_original. The new screenshot(s) should end with "-received". When replacing the screenshot(s), make sure to change the postfix "-received" to "-snap".

      1126 |         ' folder name should be something like new-snapshots_(suite-name)_desktop_original.' +
      1127 |         ' The new screenshot(s) should end with "-received". When replacing the screenshot(s), make sure to change the postfix "-received" to "-snap".';
    > 1128 |       throw new Error(errorMessage);
           |             ^
      1129 |     }
      1130 |   }
      1131 |

      at BaseUser.expectScreenshotToMatch (utilities/common/puppeteer-utils.ts:1128:13)
          at runMicrotasks (<anonymous>)
      at Object.<anonymous> (specs/curriculum-admin/create-subtopic-study-guide-with-multiple-sections.spec.ts:76:5)

  ● Curriculum Admin › should add sections with workedexamples.

    TimeoutError: Element 

### What device are you using?

Desktop

### Operating System

Windows

### What browsers are you seeing the problem on?

_No response_

### Browser version

_No response_

### Additional context

_No response_

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #25179: [E2E/Acceptance CI Failure]: Exceeded timeout of 380000 ms for a hook

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

Acceptance (topic-manager/edit-and-republish-story-with-mobile-supported-explorations)

### Did the test fail after an automatic rerun?

Test failed once and then passed after an automatic rerun

### Did the test fail when running on desktop, mobile, or both?

Desktop

### Stacktrace

```shell
FAIL core/tests/puppeteer-acceptance-tests/specs/topic-manager/edit-and-republish-story-with-mobile-supported-explorations.spec.ts (461.464 s)
  Topic Manager
    ✕ should be able to modify chapter details, preview the chapter card, add skills, and save the changes.

  ● Topic Manager › should be able to modify chapter details, preview the chapter card, add skills, and save the changes.

    thrown: "Exceeded timeout of 380000 ms for a hook.
    Use jest.setTimeout(newTimeout) to increase the timeout value, if this is a long-running test."

      34 |   let explorationId3: string | null;
      35 |
    > 36 |   beforeAll(async function () {
         |   ^
      37 |     curriculumAdmin = await UserFactory.createNewUser(
      38 |       'curriculumAdm',
      39 |       'curriculumAdmin1@example.com',

      at specs/topic-manager/edit-and-republish-story-with-mobile-supported-explorations.spec.ts:36:3
      at Object.<anonymous> (specs/topic-manager/edit-and-republish-story-with-mobile-supported-explorations.spec.ts:29:1)

Test Suites: 1 failed, 1 total
Tests:       1 failed, 1 total
Snapshots:   0 total
Time:        463.072 s
Ran all test suites matching /core\/tests\/puppeteer-acceptance-tests\/specs\/topic-manager\/edit-and-republish-story-with-mobile-supported-explorations.spec.ts/i.
INFO     2026-03-01 09:06:19,855 shutdown.py:48] Shutting down.
Error: 3-01 09:06:19 +0000] [2654] [ERROR] Worker (pid:2656) was sent SIGTERM!
Error: 3-01 09:06:19 +0000] [2831] [ERROR] Worker (pid:2837) was sent SIGTERM!
INFO     2026-03-01 09:06:20,670 stub_util.py:321] Applying all pending transactions and saving the datastore
INFO     2026-03-01 09:06:20,670 stub_util.py:324] Saving search indexes
```

### Screenshots and/or Screen Recordings

N/A

### Occurrences

https://github.com/oppia/oppia/actions/runs/22537631782/job/65289423681

2 March 2026

### Additional Information

_No response_

### Debugging document link

_No response_

---

## #25174: [Feature Request]: Batch Voiceover Regeneration to Avoid 60-Second Timeout

**Labels:** triage needed, enhancement

### Is your feature request related to a problem? Please describe.

Currently, voiceover regeneration for an exploration is triggered asynchronously under the following conditions:

- When an exploration is added to a published story
- When changes are made to a curated exploration
- When voiceover synthesis is explicitly triggered from the voiceover admin page

This approach has a limitation: all required voiceovers must be generated within the 60-second Gunicorn timeout limit.

In practice, generating a single voiceover takes approximately 5 seconds. As a result, when multiple contents require regeneration, the process is highly likely to exceed the Gunicorn timeout in any of the above scenarios.

### Describe the solution (or solutions) you'd like

In each of the three cases, suppose voiceovers need to be synthesized for n contents. Instead of processing all n contents in a single deferred (asynchronous) task, the task should split them into m smaller batches. Each batch would contain a limited number of contents such that its processing time remains within the 60-second timeout window.

This batching approach would prevent request timeouts while ensuring all required voiceovers are successfully regenerated.

### Describe alternatives you've considered and rejected

_No response_

### Additional context

_No response_

---

## #25172: [E2E/Acceptance CI Failure]: Acceptance (exploration-creator/preview-commonly-used-interactions)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

 Exploration Editor › should be able to preview "Continue Button" interaction and  should be able to preview "Multiple Choice" interaction

### Did the test fail after an automatic rerun?

Test failed once but was not automatically re-run

### Did the test fail when running on desktop, mobile, or both?

Desktop

### Stacktrace

```shell
FAIL core/tests/puppeteer-acceptance-tests/specs/exploration-creator/preview-commonly-used-interactions.spec.ts (529.288 s)
  Exploration Editor
    ✕ should be able to preview "Continue Button" interaction (60120 ms)
    ✕ should be able to preview "Multiple Choice" interaction (30112 ms)
    ✓ should be able to preview "Number Input" interaction (77604 ms)
    ✓ should be able to preview "Text Input" interaction (69496 ms)
    ✓ should be able to preview "Image Region" interaction (69066 ms)
    ✓ should be able to preview "Item Selection" interaction (70132 ms)
    ✓ should be able to preview "Drag and Drop Sort" interaction (86877 ms)

  ● Exploration Editor › should be able to preview "Continue Button" interaction

    TimeoutError: Element <div.oppia-editable-section-mask.e2e-test-state-edit-content> took too long to be clickable.
    Original Error:
    waiting for function failed: timeout 30000ms exceeded

      492 |         : selector;
      493 |     try {
    > 494 |       await this.page.waitForFunction(isElementClickable, {}, element);
          |                       ^
      495 |     } catch (error) {
      496 |       if (error instanceof Error) {
      497 |         await this.page.evaluate(isElementClickable, element, true, true);

      at new WaitTask (../../../node_modules/puppeteer/src/common/DOMWorld.ts:813:28)
      at DOMWorld.waitForFunction (../../../node_modules/puppeteer/src/common/DOMWorld.ts:728:22)
      at Frame.waitForFunction (../../../node_modules/puppeteer/src/common/FrameManager.ts:1368:28)
      at Page.waitForFunction (../../../node_modules/puppeteer/src/common/Page.ts:3358:29)
      at BaseUser.waitForElementToBeClickable (utilities/common/puppeteer-utils.ts:494:23)
      at BaseUser.clickOnElement (utilities/common/puppeteer-utils.ts:519:5)
      at BaseUser.clickOnElementWithSelector (utilities/common/puppeteer-utils.ts:554:5)
      at BaseUser.updateCardContent (utilities/user/exploration-editor.ts:2863:5)
      at Object.<anonymous> (specs/exploration-creator/preview-commonly-used-interactions.spec.ts:56:5)

  ● Exploration Editor › should be able to preview "Multiple Choice" interaction

    TimeoutError: Element <i.fa.fa-book.show-mobile-navbar-icon.e2e-test-mobile-options> took too long to be clickable.
    Original Error:
    waiting for function failed: timeout 30000ms exceeded

      492 |         : selector;
      493 |     try {
    > 494 |       await this.page.waitForFunction(isElementClickable, {}, element);
          |                       ^
      495 |     } catch (error) {
      496 |       if (er

*[truncated]*

---

## #25170: [BUG]: PreferencesHandler.put reads from raw self.payload instead of self.normalized_payload, bypassing schema validation

**Labels:** triage needed, bug

### Describe the bug

PreferencesHandler.put in core/controllers/profile.py reads the updates list from self.payload instead of self.normalized_payload. This means the entire PUT /preferences endpoint bypasses Oppia's schema validation framework, allowing unvalidated, untyped data (e.g. invalid language codes, arbitrary-length lists, invalid dashboard types) to be written directly to user settings in the datastore without error.
This is confirmed by PreferencesHandler being listed in HANDLER_CLASS_NAMES_WHICH_STILL_NEED_SCHEMAS in core/handler_schema_constants.py, meaning validate_and_normalize_args() does not run for this handler's PUT method.

### URL of the page where the issue is observed.

N/A

### Steps To Reproduce

1. Log in as any registered Oppia user.
2. Send a PUT request to /preferences with the following JSON body:
   {"updates": [{"update_type": "default_dashboard", "data": "INVALID_DASHBOARD_TYPE"}, {"update_type": "preferred_language_codes", "data": ["zzz", "xyz", "abc"]}]}
3. Observe that the server returns HTTP 200 with no validation error.
4. Send a GET to /preferences and observe the corrupted/invalid values were saved to the datastore.
Root cause: Line 356 of core/controllers/profile.py uses self.payload['updates'] instead of self.normalized_payload['updates'].

### Expected Behavior

The server should reject invalid values (unsupported language codes, invalid dashboard types, etc.) with a 400 InvalidInputException, consistent with how other validated handlers work. The handler should define HANDLER_ARGS_SCHEMAS for its PUT method and use self.normalized_payload instead of self.payload.

### Screenshots/Videos

_No response_

### What device are you using?

Desktop

### Operating System

MacOS

### What browsers are you seeing the problem on?

Chrome

### Browser version

_No response_

### Additional context

This is related to the ongoing schema migration effort tracked in issue #13162 ("Write schemas for handler class arguments"). PreferencesHandler is one of the handlers still missing a schema. Fixing this requires:
1. Adding HANDLER_ARGS_SCHEMAS['PUT'] to PreferencesHandler
2. Replacing self.payload with self.normalized_payload on line 356
3. Removing PreferencesHandler from HANDLER_CLASS_NAMES_WHICH_STILL_NEED_SCHEMAS in core/handler_schema_constants.py

---

## #25167: [E2E/Acceptance CI Failure]: E2E explorationImprovementsTab

**Labels:** triage needed, bug, CI breakage

### CI Test Type

E2E

### Which CI step failed?

Run E2E Test explorationImprovementsTab

### Did the test fail after an automatic rerun?

Test failed once, was automatically re-run, and then failed again

### Did the test fail when running on desktop, mobile, or both?

Desktop

### Stacktrace

```shell
INFO     2026-03-02 13:24:20,735 admin_server.py:67] Starting admin server at: http://0.0.0.0:8000
INFO     2026-03-02 13:24:21,738 instance.py:555] Detected GOOGLE_CLOUD_PROJECT=dev-project-id in environment variables
2026-03-02T13:24:22.398Z WARN @wdio/config:ConfigParser: No suite was found with name "145.0.7632.116"

Execution of 1 workers started at 2026-03-02T13:24:22.405Z

INFO     2026-03-02 13:24:22,751 instance.py:293] Instance PID: 6055

Error in "getDownloadStream". Could not download https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.9.0/selenium-server-4.9.0.jar
See more details below:
socket hang up

/home/runner/work/oppia/oppia/node_modules/selenium-standalone/lib/install.js:301
          throw new Error('Could not download ' + downloadUrl);
                ^
Error: Could not download https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.9.0/selenium-server-4.9.0.jar
    at Request.<anonymous> (/home/runner/work/oppia/oppia/node_modules/selenium-standalone/lib/install.js:301:17)
    at Object.onceWrapper (node:events:510:26)
    at Request.emit (node:events:390:28)
    at Request.emit (node:domain:475:12)
    at emitErrorNT (node:internal/streams/destroy:157:8)
    at emitErrorCloseNT (node:internal/streams/destroy:122:3)
    at processTicksAndRejections (node:internal/process/task_queues:83:21)
INFO     2026-03-02 13:24:22,858 shutdown.py:48] Shutting down.
```

### Screenshots and/or Screen Recordings

[e2e_test_retry_explorationImprovementsTab.log](https://github.com/user-attachments/files/25690990/e2e_test_retry_explorationImprovementsTab.log)

### Occurrences

Occurred in PR: #24935 

### Additional Information

_No response_

### Debugging document link

_No response_

---

## #25166: [E2E/Acceptance CI Failure]: E2E embedding test

**Labels:** triage needed, bug, CI breakage

### CI Test Type

E2E

### Which CI step failed?

Run E2E test embedding

### Did the test fail after an automatic rerun?

Test failed once, was automatically re-run, and then failed again

### Did the test fail when running on desktop, mobile, or both?

Desktop

### Stacktrace

```shell
[0-0] Error in "Embedding should display and play embedded explorations"
Error: Can't call $ on element with selector "<oppia-interactive-numeric-input>" because element wasn't found
    ��� should display and play embedded explorations �� [ /core/tests/webdriverio_desktop/embedding.js ]
[0-0] ffmpeg exited with code 255
[0-0] FAILED in chrome - /core/tests/webdriverio_desktop/embedding.js

 "spec" Reporter:
------------------------------------------------------------------
Running: chrome (v145.0.7632.116) on LINUX
Session ID: 909bef8213e8f20cce5a4ca689a825f5

�� /core/tests/webdriverio_desktop/embedding.js
Embedding
   ��� should display and play embedded explorations

1 failing (2m 2.7s)

1) Embedding should display and play embedded explorations
Error: Can't call $ on element with selector "<oppia-interactive-numeric-input>" because element wasn't found
Error: Can't call $ on element with selector "<oppia-interactive-numeric-input>" because element wasn't found


Spec Files:	 0 passed, 1 failed, 1 total (100% completed) in 00:02:08 

INFO     2026-03-02 13:28:13,042 shutdown.py:48] Shutting down.
Error: 3-02 13:28:13 +0000] [8449] [ERROR] Worker (pid:8460) was sent SIGTERM!
Error: 3-02 13:28:13 +0000] [8140] [ERROR] Worker (pid:8142) was sent SIGTERM!
Error: 3-02 13:28:13 +0000] [7743] [ERROR] Worker (pid:7753) was sent SIGTERM!
[datastore] Mar 02, 2026 1:28:13 PM io.netty.channel.DefaultChannelPipeline onUnhandledInboundException
```

### Screenshots and/or Screen Recordings

[e2e_test_retry_embedding.log](https://github.com/user-attachments/files/25690955/e2e_test_retry_embedding.log)

### Occurrences

Occurred in PR: 24935

### Additional Information

_No response_

### Debugging document link

_No response_

---

## #25162: [E2E/Acceptance CI Failure]: logged-out-learner/play-a-complete-community-lesson

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

re run mobile acceptance test to check flakiness

### Did the test fail after an automatic rerun?

Test failed once but was not automatically re-run

### Did the test fail when running on desktop, mobile, or both?

Mobile

### Stacktrace

```shell
FAIL core/tests/puppeteer-acceptance-tests/specs/logged-out-learner/play-a-complete-community-lesson.spec.ts (295.731 s)
  Logged-Out Learner
    ✕ should use all RTE components in the exploration

  ● Logged-Out Learner › should use all RTE components in the exploration

    TimeoutError: Element  "Done" took too long to be clickable.
    Original Error:
    waiting for function failed: timeout 30000ms exceeded

      492 |         : selector;
      493 |     try {
    > 494 |       await this.page.waitForFunction(isElementClickable, {}, element);
          |                       ^
      495 |     } catch (error) {
      496 |       if (error instanceof Error) {
      497 |         await this.page.evaluate(isElementClickable, element, true, true);

      at new WaitTask (../../../node_modules/puppeteer/src/common/DOMWorld.ts:813:28)
      at DOMWorld.waitForFunction (../../../node_modules/puppeteer/src/common/DOMWorld.ts:728:22)
      at Frame.waitForFunction (../../../node_modules/puppeteer/src/common/FrameManager.ts:1368:28)
      at Page.waitForFunction (../../../node_modules/puppeteer/src/common/Page.ts:3358:29)
      at BaseUser.waitForElementToBeClickable (utilities/common/puppeteer-utils.ts:494:23)
          at runMicrotasks (<anonymous>)
      at BaseUser.clickOnElement (utilities/common/puppeteer-utils.ts:519:5)
      at BaseUser.clickOnElementWithSelector (utilities/common/puppeteer-utils.ts:554:5)
      at BaseUser.addExplorationDescriptionContainingAllRTEComponents (utilities/user/exploration-editor.ts:6771:5)

Test Suites: 1 failed, 1 total
Tests:       1 failed, 1 total
Snapshots:   0 total
Time:        297.409 s
```

### Screenshots and/or Screen Recordings

n/a

### Occurrences

once

### Additional Information

_No response_

### Debugging document link

_No response_

---

## #25160: [E2E/Acceptance CI Failure]: TimeoutError: waiting for selector `button.e2e-test-confirm-skill-creation-button` to be hidden failed: timeout 30000ms exceeded

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

Acceptance (topic-manager/create-and-edit-questions-in-skill-dashboard)

### Did the test fail after an automatic rerun?

Test failed once and then passed after an automatic rerun

### Did the test fail when running on desktop, mobile, or both?

Desktop

### Stacktrace

```shell
t-log] 50:35.711: Started closing broswer for curriculumAdm.
[test-log] 50:35.711: Started closing broswer for superAdm.
[test-log] 50:35.711: Screen recording stopped for curriculumAdm.
[test-log] 50:35.712: Screen recording stopped for superAdm.
[test-log] 50:35.794: Error while taking screenshot for curriculumAdm: ProtocolError: Protocol error (Target.activateTarget): Target closed.
[test-log] 50:35.904: Browser closed for superAdm.
[test-log] 50:35.907: Browser closed for curriculumAdm.
[test-log] 50:35.907: All browsers closed.
FAIL core/tests/puppeteer-acceptance-tests/specs/topic-manager/create-and-edit-questions-in-skill-dashboard.spec.ts (398.238 s)
  Topic Manager
    ✕ should be able to add questions to skills using the skill editor (1 ms)
    ✕ should be able to edit questions in skills editor

  ● Topic Manager › should be able to add questions to skills using the skill editor

    TimeoutError: waiting for selector `button.e2e-test-confirm-skill-creation-button` to be hidden failed: timeout 30000ms exceeded

      611 |     await this.clickOnElementWithSelector(confirmSkillCreationButton);
      612 |     await this.waitForNetworkIdle();
    > 613 |     await this.page.waitForSelector(confirmSkillCreationButton, {
          |                     ^
      614 |       hidden: true,
      615 |     });
      616 |     await this.page.bringToFront();

      at new WaitTask (../../../node_modules/puppeteer/src/common/DOMWorld.ts:813:28)
      at DOMWorld.waitForSelectorInPage (../../../node_modules/puppeteer/src/common/DOMWorld.ts:656:22)
      at Object.internalHandler.waitFor (../../../node_modules/puppeteer/src/common/QueryHandler.ts:78:19)
      at DOMWorld.waitForSelector (../../../node_modules/puppeteer/src/common/DOMWorld.ts:511:25)
      at Frame.waitForSelector (../../../node_modules/puppeteer/src/common/FrameManager.ts:1290:47)
      at Page.waitForSelector (../../../node_modules/puppeteer/src/common/Page.ts:3222:29)
      at BaseUser.fillSkillInfoAndSubmit (utilities/user/curriculum-admin.ts:613:21)
      at BaseUser.createSkillFromSkillsDashboard (utilities/user/curriculum-admin.ts:3033:5)
      at specs/topic-manager/create-and-edit-questions-in-skill-dashboard.spec.ts:71:5

  ● Topic Manager › should be able to edit questions in skills editor

    TimeoutError: waiting for selector `button.e2e-test-confirm-skill-creation-button` to be hidden failed: timeout 30000ms exceeded

      611 |     await this.clickOnElementWithSelector(confirmSkillCreationButton);
      612 |     await this.waitForNetworkIdle();
    > 613 |     await this.page.waitForSelector(confirmSkillCreationButton, {
          |  

*[truncated]*

---

## #25157: [BUG]: translation is not done expected संख्याओं का पूर्णांकन, भाग 2

**Labels:** triage needed, bug

### Describe the bug

the hindi transalation is not done proper

### URL of the page where the issue is observed.

https://www.oppia.org/learn/math/place-values/story

### Steps To Reproduce

https://www.oppia.org/learn/math/place-values/story 
here is you can see the issue 

### Expected Behavior

5.संख्याओं का पूर्णांकन, भाग 2

### Screenshots/Videos

<img width="949" height="500" alt="Image" src="https://github.com/user-attachments/assets/6f2cc1b1-3c2a-4032-a14b-4680f6a5e0d3" />

### What device are you using?

Desktop

### Operating System

Windows

### What browsers are you seeing the problem on?

Chrome

### Browser version

_No response_

### Additional context

_No response_

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #25156: [BUG]: ExpressionChangedAfterItHasBeenCheckedError on New Learner Dashboard (Home Tab)

**Labels:** triage needed, bug

### Describe the bug

When loading the New Learner Dashboard (Home tab), an Angular runtime error appears in the browser console: ExpressionChangedAfterItHasBeenCheckedError. The error indicates that an *ngIf expression changed value (true → false) after Angular completed its change detection cycle. This happens during initial page rendering.

### URL of the page where the issue is observed.

http://localhost:8181/learner-dashboard

### Steps To Reproduce

1)Log in as a learner.

2)Go to the Admin page.

3)Grant yourself Release Coordinator rights.

4)Navigate to:
http://localhost:8181/release-coordinator

5)Enable the feature flag:
show_redesigned_learner_dashboard

6)Navigate to the Learner Dashboard.

7)Open the browser DevTools Console.

8)Refresh the page.

9)Observe the following error in the console:
ERROR Error: ExpressionChangedAfterItHasBeenCheckedError:
Expression has changed after it was checked.
Previous value: 'ngIf: true'. Current value: 'ngIf: false'.
at HomeTabComponent.html

### Expected Behavior

The New Learner Dashboard should load without any Angular runtime errors in the console.

### Screenshots/Videos

<img width="1438" height="775" alt="Image" src="https://github.com/user-attachments/assets/23431042-651a-4bc7-9428-3875d1fb7ac5" />

### What device are you using?

Desktop

### Operating System

MacOS

### What browsers are you seeing the problem on?

Chrome

### Browser version

_No response_

### Additional context

_No response_

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #25125: [E2E/Acceptance CI Failure]: Acceptance (logged-in-learner/edit-the-profile)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

logged-in-learner/edit-the-profile

### Did the test fail after an automatic rerun?

Test failed once but was not automatically re-run

### Did the test fail when running on desktop, mobile, or both?

Desktop

### Stacktrace

```shell
FAIL core/tests/puppeteer-acceptance-tests/specs/logged-in-learner/edit-the-profile.spec.ts (233.261 s)
  Logged-In Learner
    ✓ should be able to find the preferences page (4939 ms)
    ✓ should be able to change the profile photo (7105 ms)
    ✓ should be able to edit bio (623 ms)
    ✓ should be able to change the preferred dashboard (155 ms)
    ✓ should be able to edit subject interests (1801 ms)
    ✓ should be able to add preferred audio language (1690 ms)
    ✓ should be able to change preferred exploration language (3537 ms)
    ✓ should be able to change email preferences (3170 ms)
    ✓ should be able to save all the information edited (15019 ms)
    ✓ should be able to go to their profile by clicking on their username (12106 ms)
    ✕ should be able to subscribe creators (40932 ms)

  ● Logged-In Learner › should be able to subscribe creators

    TimeoutError: Element <span.e2e-test-exploration-tile-title> "Solving problems without calcu..." took too long to be clickable.
    Original Error:
    waiting for function failed: timeout 30000ms exceeded

      492 |         : selector;
      493 |     try {
    > 494 |       await this.page.waitForFunction(isElementClickable, {}, element);
          |                       ^
      495 |     } catch (error) {
      496 |       if (error instanceof Error) {
      497 |         await this.page.evaluate(isElementClickable, element, true, true);

      at new WaitTask (../../../node_modules/puppeteer/src/common/DOMWorld.ts:813:28)
      at DOMWorld.waitForFunction (../../../node_modules/puppeteer/src/common/DOMWorld.ts:728:22)
      at Frame.waitForFunction (../../../node_modules/puppeteer/src/common/FrameManager.ts:1368:28)
      at Page.waitForFunction (../../../node_modules/puppeteer/src/common/Page.ts:3358:29)
      at BaseUser.waitForElementToBeClickable (utilities/common/puppeteer-utils.ts:494:23)
          at runMicrotasks (<anonymous>)
      at BaseUser.playLessonFromSearchResults (utilities/user/logged-out-user.ts:4523:7)
      at Object.<anonymous> (specs/logged-in-learner/edit-the-profile.spec.ts:160:5)

Test Suites: 1 failed, 1 total
Tests:       1 failed, 10 passed, 11 total
Snapshots:   0 total
Time:        234.966 s
Ran all test suites matching /core\/tests\/puppeteer-acceptance-tests\/specs\/logged-in-learner\/edit-the-profile.spec.ts/i.
INFO     2026-02-27 02:04:43,875 shutdown.py:48] Shutting down.
INFO     2026-02-27 02:04:43,888 stub_util.py:321] Applying all pending transactions and saving the datastore
INFO     2026-02-27 02:04:43,888 stub_util.py:324] Saving search indexes
Error: 2-27 02:04:43 +0000] [4937] [ERROR] Worker (pid:4939) was sent SIGTERM!
Error: 2-27 02:04:43 +0000] [4724

*[truncated]*

---

## #25115: [E2E/Acceptance CI Failure]: Acceptance (logged-in-user/manage-exploration-progress-in-learner-dashboard)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

logged-in-user/manage-exploration-progress-in-learner-dashboard

### Did the test fail after an automatic rerun?

Test failed once but was not automatically re-run

### Did the test fail when running on desktop, mobile, or both?

Desktop

### Stacktrace

```shell
FAIL core/tests/puppeteer-acceptance-tests/specs/logged-in-user/manage-exploration-progress-in-learner-dashboard.spec.ts (241.873 s)
  Logged-in User
    ✕ should navigate to the new learner dashboard

  ● Logged-in User › should navigate to the new learner dashboard

    TimeoutError: Element <div.oppia-editable-section-mask.e2e-test-state-edit-content> took too long to be clickable.
    Original Error:
    waiting for function failed: timeout 30000ms exceeded

      492 |         : selector;
      493 |     try {
    > 494 |       await this.page.waitForFunction(isElementClickable, {}, element);
          |                       ^
      495 |     } catch (error) {
      496 |       if (error instanceof Error) {
      497 |         await this.page.evaluate(isElementClickable, element, true, true);

      at new WaitTask (../../../node_modules/puppeteer/src/common/DOMWorld.ts:813:28)
      at DOMWorld.waitForFunction (../../../node_modules/puppeteer/src/common/DOMWorld.ts:728:22)
      at Frame.waitForFunction (../../../node_modules/puppeteer/src/common/FrameManager.ts:1368:28)
      at Page.waitForFunction (../../../node_modules/puppeteer/src/common/Page.ts:3358:29)
      at BaseUser.waitForElementToBeClickable (utilities/common/puppeteer-utils.ts:494:23)
          at runMicrotasks (<anonymous>)
      at BaseUser.clickOnElement (utilities/common/puppeteer-utils.ts:519:5)
      at BaseUser.clickOnElementWithSelector (utilities/common/puppeteer-utils.ts:554:5)
      at BaseUser.updateCardContent (utilities/user/exploration-editor.ts:2863:5)

Test Suites: 1 failed, 1 total
Tests:       1 failed, 1 total
Snapshots:   0 total
Time:        243.663 s
Ran all test suites matching /core\/tests\/puppeteer-acceptance-tests\/specs\/logged-in-user\/manage-exploration-progress-in-learner-dashboard.spec.ts/i.
INFO     2026-02-26 22:54:09,644 shutdown.py:48] Shutting down.
Error: 2-26 22:54:09 +0000] [9704] [ERROR] Worker (pid:9719) was sent SIGTERM!
Error: 2-26 22:54:09 +0000] [10264] [ERROR] Worker (pid:10266) was sent SIGTERM!
Error: 2-26 22:54:09 +0000] [10063] [ERROR] Worker (pid:10065) was sent SIGTERM!
Error: 2-26 22:54:09 +0000] [10229] [ERROR] Worker (pid:10231) was sent SIGTERM!
Error: 2-26 22:54:09 +0000] [9889] [ERROR] Worker (pid:9896) was sent SIGTERM!
INFO     2026-02-26 22:54:09,964 stub_util.py:321] Applying all pending transactions and saving the datastore
INFO     2026-02-26 22:54:09,965 stub_util.py:324] Saving search indexes
```

### Screenshots and/or Screen Recordings

N/A

### Occurrences

https://github.com/oppia/oppia/actions/runs/22452275553/job/65056161804?pr=24837#logs

### Additional Information

_No response_

### D

*[truncated]*

---

## #25094: [BUG]: Blog page is not accessible via sidebar in mobile view

**Labels:** triage needed, bug

### Describe the bug

The blog page cannot be accessed via the sidebar in mobile view because there is no blog button present.

### URL of the page where the issue is observed.

https://www.oppia.org

### Steps To Reproduce

1. Open Oppia in mobile view (small viewport width or device emulator)
2. Sign in as a user
3. Open the navigation menu (hamburger menu)
4. Click on the "About" section
5. Observe that there is no "Blog" option available

### Expected Behavior

The "Blog" option should be present in the mobile navigation so users can access the blog page.

### Screenshots/Videos

_No response_

### What device are you using?

Mobile

### Operating System

Android

### What browsers are you seeing the problem on?

_No response_

### Browser version

_No response_

### Additional context

_No response_

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #25093: [E2E/Acceptance CI Failure]: Acceptance (logged-in-learner/starts-from-beginning-after-completing-a-lesson)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

Starting new Acceptance Tests Server

### Did the test fail after an automatic rerun?

Test failed once, was automatically re-run, and then failed again

### Did the test fail when running on desktop, mobile, or both?

Desktop

### Stacktrace

```shell
[test-log] 11:03.531: Test failed: Capturing screenshots...
[test-log] 11:03.532: Closing browsers for 1 users.
[test-log] 11:03.532: Started closing broswer for explorationEditor.
INFO     2026-02-24 23:11:06,498 module.py:830] default: "GET /internetconnectivityhandler HTTP/1.1" 200 36
INFO     2026-02-24 23:11:10,000 module.py:830] default: "GET /internetconnectivityhandler HTTP/1.1" 200 36
INFO     2026-02-24 23:11:13,478 module.py:830] default: "GET /internetconnectivityhandler HTTP/1.1" 200 36
INFO     2026-02-24 23:11:16,996 module.py:830] default: "GET /internetconnectivityhandler HTTP/1.1" 200 36
INFO     2026-02-24 23:11:20,494 module.py:830] default: "GET /internetconnectivityhandler HTTP/1.1" 200 36
[test-log] 11:21.670: Screen recording stopped for explorationEditor.
[test-log] 11:21.822: Screenshot captured for test failure and saved as : /home/runner/work/oppia/oppia_full_stack_test_failure_screenshots/acceptance/logged-in-learner_starts-from-beginning-after-completing-a-lesson-2026-02-24T23_11_21.670Z-instance-0.png
[test-log] 11:21.822: All screenshots captured for explorationEditor
[test-log] 11:21.883: Browser closed for explorationEditor.
[test-log] 11:21.883: All browsers closed.
FAIL core/tests/puppeteer-acceptance-tests/specs/logged-in-learner/starts-from-beginning-after-completing-a-lesson.spec.ts (146.233 s)
  Logged-In User
    ✕ should be able to start lesson from beginning on revisit

  ● Logged-In User › should be able to start lesson from beginning on revisit

    TimeoutError: Element <div.oppia-editable-section-mask.e2e-test-state-edit-content> took too long to be clickable.
    Original Error:
    waiting for function failed: timeout 30000ms exceeded

      492 |         : selector;
      493 |     try {
    > 494 |       await this.page.waitForFunction(isElementClickable, {}, element);
          |                       ^
      495 |     } catch (error) {
      496 |       if (error instanceof Error) {
      497 |         await this.page.evaluate(isElementClickable, element, true, true);

      at new WaitTask (../../../node_modules/puppeteer/src/common/DOMWorld.ts:813:28)
      at DOMWorld.waitForFunction (../../../node_modules/puppeteer/src/common/DOMWorld.ts:728:22)
      at Frame.waitForFunction (../../../node_modules/puppeteer/src/common/FrameManager.ts:1368:28)
      at Page.waitForFunction (../../../node_modules/puppeteer/src/common/Page.ts:3358:29)
      at BaseUser.waitForElementToBeClickable (utilities/common/puppeteer-utils.ts:494:23)
      at BaseUser.clickOnElement (utilities/common/puppeteer-utils.ts:519:5)
      at BaseUser.clickOnElementWithSelector (utilities/common/puppeteer-utils.ts:554:5)
 

*[truncated]*

---

## #25092: [E2E/Acceptance CI Failure]: Acceptance (curriculum-admin/create-edit-and-delete-a-classroom)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

Starting new Acceptance Tests Server

### Did the test fail after an automatic rerun?

Test failed once but was not automatically re-run

### Did the test fail when running on desktop, mobile, or both?

Desktop

### Stacktrace

```shell
[test-log] 29:23.758: There are 1 classrooms present.
[test-log] 29:23.758: Closing browsers for 3 users.
[test-log] 29:23.758: Started closing broswer for curriculumAdm.
[test-log] 29:23.759: Started closing broswer for superAdm.
[test-log] 29:23.759: Started closing broswer for unknown user.
[test-log] 29:23.759: Screen recording stopped for curriculumAdm.
[test-log] 29:23.759: Screen recording stopped for unknown user.
[test-log] 29:23.841: Error while taking screenshot for curriculumAdm: ProtocolError: Protocol error (Target.activateTarget): Target closed.
[test-log] 29:23.948: Browser closed for unknown user.
[test-log] 29:23.953: Browser closed for curriculumAdm.
[test-log] 29:24.089: Screenshot captured for test failure and saved as : /home/runner/work/oppia/oppia_full_stack_test_failure_screenshots/acceptance/curriculum-admin_create-edit-and-delete-a-classroom-2026-02-24T23_29_23.759Z-instance-12.png
[test-log] 30:53.630: Screen recording stopped for superAdm.
[test-log] 30:53.714: Browser closed for superAdm.
[test-log] 30:53.714: All browsers closed.
FAIL core/tests/puppeteer-acceptance-tests/specs/curriculum-admin/create-edit-and-delete-a-classroom.spec.ts (738.544 s)
  Curriculum Admin
    ✓ should be able to create a new classroom (7871 ms)
    ✕ should be able to edit classroom information (61313 ms)
    ✓ should be able to publish classroom (14278 ms)
    ✓ should be able to enable diagnostic test for a classroom (14065 ms)
    ✓ should be able to change order of classrooms (36288 ms)
    ✓ should be able to delete a classroom (7606 ms)

  ● Curriculum Admin › should be able to edit classroom information

    TimeoutError: waiting for function failed: timeout 30000ms exceeded

      2446 |
      2447 |     // Wait for the topic to appear in the classroom before adding prerequisites.
    > 2448 |     await this.page.waitForFunction(
           |                     ^
      2449 |       (
      2450 |         topicBoxSelector: string,
      2451 |         topicNameSelector: string,

      at new WaitTask (../../../node_modules/puppeteer/src/common/DOMWorld.ts:813:28)
      at DOMWorld.waitForFunction (../../../node_modules/puppeteer/src/common/DOMWorld.ts:728:22)
      at Frame.waitForFunction (../../../node_modules/puppeteer/src/common/FrameManager.ts:1368:28)
      at Page.waitForFunction (../../../node_modules/puppeteer/src/common/Page.ts:3358:29)
      at BaseUser.addTopicToClassroom (utilities/user/curriculum-admin.ts:2448:21)
          at runMicrotasks (<anonymous>)
      at Object.<anonymous> (specs/curriculum-admin/create-edit-and-delete-a-classroom.spec.ts:111:5)

Test Suites: 1 failed, 1 total
Tests:       1 failed, 5 passed, 6 total
S

*[truncated]*

---

## #25087: [BUG]: No validation for Message text and Thread subject inside feedback.

**Labels:** triage needed, bug

### Describe the bug

when i click on CREATE EXPLORATION and navigate to feedback section when i add Message text and Thread subject there is no validation for than and no translation also.

### URL of the page where the issue is observed.

http://localhost:8181/create/85vN9avNWv3P#/feedback

### Steps To Reproduce

when i click on CREATE EXPLORATION inside creator dashboard and navigate to feedback section when i add Message text and Thread subject there is no validation for than and no translation also.

### Expected Behavior

I expect to be some validations for both inputs.

### Screenshots/Videos

https://github.com/user-attachments/assets/9f82fc2d-256f-4a68-bece-5246d6eebe2f

### What device are you using?

Desktop

### Operating System

Windows

### What browsers are you seeing the problem on?

Chrome

### Browser version

145.0.7632.117

### Additional context

_No response_

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #25067: [E2E/Acceptance CI Failure]: Element <div.oppia-editable-section-mask.e2e-test-state-edit-content> took too long to be clickable timeout 30000ms exceeded.

**Labels:** triage needed, bug, CI breakage

### CI Test Type

E2E

### Which CI step failed?

Acceptance (logged-out-learner/share-the-lesson-from-the-lesson-player)

### Did the test fail after an automatic rerun?

Test failed once, was automatically re-run, and then failed again

### Did the test fail when running on desktop, mobile, or both?

Desktop

### Stacktrace

```shell
FAIL core/tests/puppeteer-acceptance-tests/specs/logged-out-learner/share-the-lesson-from-the-lesson-player.spec.ts (171.952 s)
  Logged-Out Learner
    ✕ should be able to share the lesson using copy link
    ✕ should be able to share the lesson on Google Classroom
    ✕ should be able to share the lesson on Facebook

  ● Logged-Out Learner › should be able to share the lesson using copy link

    TimeoutError: Element <div.oppia-editable-section-mask.e2e-test-state-edit-content> took too long to be clickable.
    Original Error:
    waiting for function failed: timeout 30000ms exceeded

      492 |         : selector;
      493 |     try {
    > 494 |       await this.page.waitForFunction(isElementClickable, {}, element);
          |                       ^
      495 |     } catch (error) {
      496 |       if (error instanceof Error) {
      497 |         await this.page.evaluate(isElementClickable, element, true, true);

      at new WaitTask (../../../node_modules/puppeteer/src/common/DOMWorld.ts:813:28)
      at DOMWorld.waitForFunction (../../../node_modules/puppeteer/src/common/DOMWorld.ts:728:22)
      at Frame.waitForFunction (../../../node_modules/puppeteer/src/common/FrameManager.ts:1368:28)
      at Page.waitForFunction (../../../node_modules/puppeteer/src/common/Page.ts:3358:29)
      at BaseUser.waitForElementToBeClickable (utilities/common/puppeteer-utils.ts:494:23)
          at runMicrotasks (<anonymous>)
      at BaseUser.clickOnElement (utilities/common/puppeteer-utils.ts:519:5)
      at BaseUser.clickOnElementWithSelector (utilities/common/puppeteer-utils.ts:554:5)
      at BaseUser.updateCardContent (utilities/user/exploration-editor.ts:2863:5)

  ● Logged-Out Learner › should be able to share the lesson on Google Classroom

    TimeoutError: Element <div.oppia-editable-section-mask.e2e-test-state-edit-content> took too long to be clickable.
    Original Error:
    waiting for function failed: timeout 30000ms exceeded

      492 |         : selector;
      493 |     try {
    > 494 |       await this.page.waitForFunction(isElementClickable, {}, element);
          |                       ^
      495 |     } catch (error) {
      496 |       if (error instanceof Error) {
      497 |         await this.page.evaluate(isElementClickable, element, true, true);

      at new WaitTask (../../../node_modules/puppeteer/src/common/DOMWorld.ts:813:28)
      at DOMWorld.waitForFunction (../../../node_modules/puppeteer/src/common/DOMWorld.ts:728:22)
      at Frame.waitForFunction (../../../node_modules/puppeteer/src/common/FrameManager.ts:1368:28)
      at Page.waitForFunction (../../../node_modules/puppet

*[truncated]*

---

## #25066: [CI Failure]: Failed to run "/tmp/tmphfrngrrb/bin/pip install -r requirements.txt"

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Frontend

### Which CI step failed?

Acceptance (topic-manager/edit-the-topic)

### Stacktrace

```shell
INFO     2026-02-25 05:46:19,580 instance_factory.py:280] Using pip to install dependency libraries; pip stdout is redirected to /tmp/tmpi_kjbpvk
INFO     2026-02-25 05:46:19,594 instance_factory.py:310] Running /tmp/tmphfrngrrb/bin/pip install --upgrade pip
...
Failed to run "/tmp/tmphfrngrrb/bin/pip install -r requirements.txt"
 
i  emulators: Received SIGTERM for the first time. Starting a clean shutdown.
i  emulators: Please wait for a clean shutdown or send the SIGTERM signal again to stop right now.
i  Automatically exporting data using --export-on-exit "/home/runner/work/oppia/oppia/../firebase_emulator_cache" please wait for the export to finish...
⚠  Emulator UI has exited upon receiving signal: SIGTERM
i  Found running emulator hub for project dev-project-id at http://localhost:4400
i  Creating export directory /home/runner/work/oppia/firebase_emulator_cache
i  Exporting data to: /home/runner/work/oppia/firebase_emulator_cache
i  emulators: Received export request. Exporting data to /home/runner/work/oppia/firebase_emulator_cache.
✔  emulators: Export complete.
✔  Export complete
i  emulators: Shutting down emulators.
i  ui: Stopping Emulator UI
⚠  ui: Error stopping Emulator UI
i  auth: Stopping Authentication Emulator
i  hub: Stopping emulator hub
i  logging: Stopping Logging Emulator
ERROR:root:Portserver failed to shut down after 10 seconds.
```

### Screenshots / Screen Recordings

N/A

### Occurrences

https://github.com/oppia/oppia/actions/runs/22342787946/job/64752942698

### Additional Information

_No response_

### Debugging document link

_No response_

---

## #25060: [Feature Request]: Remove E2E test publicationAndLibrary.js

**Labels:** good first issue, enhancement, Impact: Medium, Work: Low, EUJ LO.4

### Is your feature request related to a problem? Please describe.

We are currently migrating from E2E tests to Acceptance tests; however, some of the E2E tests are still not covered by Acceptance tests. We need to write acceptance tests covering these uncovered E2E tests and delete the corresponding E2E test.

The goal is to create a new acceptance test that covers the features currently handled by the existing E2E test.

### Describe the solution (or solutions) you'd like

Write the new acceptance test and delete the existing E2E test.

**Steps to follow:**

1. Create a new acceptance test file in the appropriate directory.
2. Write the acceptance test based on the specifications found in the **WIP Doc (Internal/External Users)** linked below.
3. Add the acceptance test to [acceptance.json](https://github.com/oppia/oppia/blob/develop/core/tests/ci-test-suite-configs/acceptance.json).
4. Run the newly created test-suite locally and ensure it passes.
5. Push the code to your repo-fork.
6. **Stress test** the new test-suite to check for flakes. (In your Oppia repo fork, go to *Actions* > *Stress Test Acceptance Test* > *Run Workflow* > branch: `<YOUR_FEATURE_BRANCH_NAME>`, runs: `20`, test-suite: `<TEST_SUITE_NAME_USED_IN_ACCEPTANCE.JSON>`).
7. Ensure that all jobs pass in the above workflow run.
8. Remove the corresponding E2E test file.
9. Open a PR.

### Describe alternatives you've considered and rejected

*No response*

### Additional context

*No response*

---

### E2E Tests to be Removed

* publicationAndLibrary.js

### Acceptance Tests to be Added / Updated

* [EDITED] 🟡 LO.4. Play through a lesson (WIP External Users)
    - Add first step in the acceptance test.
    - Make required changes in setup.
### Documentation References

* **[WIP Doc (Internal Users)](https://docs.google.com/spreadsheets/d/1DIZ0_Gmf9uhjTbhuDpA495PTjYZW9ZE97r6urS-iXwg/edit?gid=888982708)** 
* [WIP Doc (External Users)](https://docs.google.com/spreadsheets/d/1IrxN13IC5xwWdAFnGMu_4p3FU1ADL4QO-eLZIuTowIA/edit?gid=888982708#gid=888982708)
* **Puppeteer Acceptance Tests Folder:** [[GitHub Link](https://github.com/oppia/oppia/tree/develop/core/tests/puppeteer-acceptance-tests)](https://github.com/oppia/oppia/tree/develop/core/tests/puppeteer-acceptance-tests)
* **Acceptance Test Wiki:** [[GitHub Wiki](https://github.com/oppia/oppia/wiki/Acceptance-Tests)](https://github.com/oppia/oppia/wiki/Acceptance-Tests)


> [!IMPORTANT]
> **If you want to claim this issue, strictly follow the instructions below:**
>
> 1. Read the guidance (if you haven't already):  
>    https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue  
> 2. As this issue is simple, no need to explain how you’ll fix it — just provide proof you can complete it.  
> 3. Run:
>    ```
>    VIDEO_RECORDING_IS_ENABLED=1 python -m scripts.run_acceptance_test --suite=<SUITE>
>    ```
>    Recordings will be saved in `../oppia_full_stack_test_video_recordings`.  
>    Link all rec

*[truncated]*

---

## #25058: [BUG]: Creator should not be able to add manager without exploration title.

**Labels:** triage needed, bug

### Describe the bug

When a creator tries to share an exploration without a title, they should be blocked. However, it seems they are not.

Note: While fixing this bug, acceptance test "LC.9. Delete lesson creator’s user profile" should also be fixed from [WIP doc](https://docs.google.com/spreadsheets/d/1DIZ0_Gmf9uhjTbhuDpA495PTjYZW9ZE97r6urS-iXwg/edit?gid=888982708#gid=888982708&range=J144:K144).

So, this issue covers
- [ ] Fixing the issue
- [ ] Fixing the acceptance test LC.9.

### URL of the page where the issue is observed.

/create/<EXP_ID>

### Steps To Reproduce

1. Navigate to creator dashboard
2. Click on "Create Exploration"
3. Close welcome modal
4. Navigate to settings tab.
5. Click "Edit" button next to managers.
6. Insert a valid username (a user with given username should exists).
8. Press "tab" key (or get focus out of user name input).
9. "Save" button is enabled.

### Expected Behavior

In step 9, the "Save" button should be disabled, and a error should be shown that creator needs to add title before they can share.

### Screenshots/Videos

_No response_

### What device are you using?

Desktop

### Operating System

Linux

### What browsers are you seeing the problem on?

_No response_

### Browser version

_No response_

### Additional context

_No response_

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #25052: [E2E/Acceptance CI Failure]: Acceptance (blog-post-writer/create-and-edit-blog-post)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

E2E

### Which CI step failed?

run desktop tests

### Did the test fail after an automatic rerun?

Test failed once but was not automatically re-run

### Did the test fail when running on desktop, mobile, or both?

Desktop

### Stacktrace

```shell
[test-log] 06:14.052: Element .e2e-test-save-blog-post-content is visible.
[test-log] 06:14.157: Checking if element  "DONE" is clickable...
[test-log] 06:14.243: Element (selector: .e2e-test-save-blog-post-content) clicked.
[test-log] 06:14.252: Element .e2e-test-save-blog-post-content is hidden.
[test-log] 06:17.284: Page rendered fully.
[test-log] 06:17.287: Element .e2e-test-blog-card-preview-button is visible.
[test-log] 06:17.392: Checking if element  "PREVIEW" is clickable...
[test-log] 06:17.458: Element (selector: .e2e-test-blog-card-preview-button) clicked.
[test-log] 06:17.471: Element .e2e-test-modal-header is visible.
INFO     2026-02-25 03:06:17,492 module.py:830] default: "GET /assetsdevhandler/blog_post/h6nXMXrMmWGc/assets/thumbnail/banner.jpeg HTTP/1.1" 200 56619
WARNING:root:Invalid URL requested: http://localhost:8181/assetsdevhandler/user//assets/image/profile_picture.webp?v=26596.600000000093
INFO     2026-02-25 03:06:17,497 module.py:830] default: "GET /assetsdevhandler/user//assets/image/profile_picture.webp?v=26596.600000000093 HTTP/1.1" 404 5943
[test-log] 06:23.186: Test failed: Capturing screenshots...
[test-log] 06:23.195: Element .e2e-test-profile-dropdown is visible.
[test-log] 06:23.300: Checking if element <li.nav-item.e2e-test-profile-dropdown.oppia-navbar-clickable-dropdown.profile-dropdown.pfl.dropdown> "blogPostWriter Creator Dashboa..." is clickable...
[browser-log] 06:53.303: [debug]: Document state:
  - readyState: complete
  - styleSheets loaded: 35
  - pending stylesheets: 0
  - viewport: 383x682
[browser-log] 06:53.304: [debug]: Element LI is disabled: false
[browser-log] 06:53.304: [debug]: Element LI is in viewport: true, true
[browser-log] 06:53.305: [debug]: Element LI
Dimensions: 295.5, 0, 87.5, 56
Center point: 339.5, 28
[browser-log] 06:53.305: [debug]: Element LI overlapping elements found: 2
Overlapping element: MAT-ICON (class="mat-icon notranslate material-icons mat-icon-no-color")
Overlapping rect: MAT-ICON (class="mat-icon notranslate material-icons mat-icon-no-color")
[browser-log] 06:53.305: [debug]: Checking overlap for LI (class="nav-item e2e-test-profile-dropdown oppia-navbar-clickable-dropdown profile-dropdown pfl dropdown")
Overlapping elements to check: 2
[browser-log] 06:53.305: [debug]: Overlapping element MAT-ICON (class="mat-icon notranslate material-icons mat-icon-no-color")
  - Is same element: false
  - Is contained by target: false
  - Contains target: false
[browser-

*[truncated]*

---

## #25051: [Feature Request]: Remove E2E test contributorAdminDashoard.js

**Labels:** good first issue, enhancement, Impact: Medium, Work: Medium, IUJ TC.1, IUJ QC.1

### Is your feature request related to a problem? Please describe.

We are currently migrating from E2E tests to Acceptance tests; however, some of the E2E tests are still not covered by Acceptance tests. We need to write acceptance tests covering these uncovered E2E tests and delete the corresponding E2E test.

The goal is to create a new acceptance test that covers the features currently handled by the existing E2E test.

### Describe the solution (or solutions) you'd like

Write the new acceptance test and delete the existing E2E test.

**Steps to follow:**

1. Create a new acceptance test file in the appropriate directory.
2. Write the acceptance test based on the specifications found in the **WIP Doc (Internal/External Users)** linked below.
3. Add the acceptance test to [acceptance.json](https://github.com/oppia/oppia/blob/develop/core/tests/ci-test-suite-configs/acceptance.json).
4. Run the newly created test-suite locally and ensure it passes.
5. Push the code to your repo-fork.
6. **Stress test** the new test-suite to check for flakes. (In your Oppia repo fork, go to *Actions* > *Stress Test Acceptance Test* > *Run Workflow* > branch: `<YOUR_FEATURE_BRANCH_NAME>`, runs: `20`, test-suite: `<TEST_SUITE_NAME_USED_IN_ACCEPTANCE.JSON>`).
7. Ensure that all jobs pass in the above workflow run.
8. Remove the corresponding E2E test file.
9. Open a PR.

### Describe alternatives you've considered and rejected

*No response*

### Additional context

*No response*

---

### E2E Tests to be Removed

* contributorAdminDashboard.js

### Acceptance Tests to be Added / Updated

* [EDITED] 🟡 QC.1. Manage contributors' question review/submission rights. (WIP Internal Users)
* [EDITED] 🟡 TC.1. Manage contributors' translation review rights. (WIP Internal Users)
### Documentation References

* **WIP Doc (Internal Users):** [[Spreadsheet Link](https://docs.google.com/spreadsheets/d/1DIZ0_Gmf9uhjTbhuDpA495PTjYZW9ZE97r6urS-iXwg/edit?gid=888982708&authuser=2)](https://docs.google.com/spreadsheets/d/1DIZ0_Gmf9uhjTbhuDpA495PTjYZW9ZE97r6urS-iXwg/edit?gid=888982708)
* [WIP Doc (External Users)](https://docs.google.com/spreadsheets/d/1IrxN13IC5xwWdAFnGMu_4p3FU1ADL4QO-eLZIuTowIA/edit?gid=888982708#gid=888982708)
* **Puppeteer Acceptance Tests Folder:** [[GitHub Link](https://github.com/oppia/oppia/tree/develop/core/tests/puppeteer-acceptance-tests)](https://github.com/oppia/oppia/tree/develop/core/tests/puppeteer-acceptance-tests)
* **Acceptance Test Wiki:** [[GitHub Wiki](https://github.com/oppia/oppia/wiki/Acceptance-Tests)](https://github.com/oppia/oppia/wiki/Acceptance-Tests)


> [!IMPORTANT]
> **If you want to claim this issue, strictly follow the instructions below:**
>
> 1. Read the guidance (if you haven't already):  
>    https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue  
> 2. As this issue is simple, no need to explain how you’ll fix it — just provide proof you can complete it.  
> 3. Run:
>    ```
>    VIDEO_RECORD

*[truncated]*

---

## #25031: [BUG]: Backend coverage checks fail when jobs merge different commits from develop

**Labels:** bug

### Describe the bug

In [this backend test run on CI](https://github.com/oppia/oppia/actions/runs/22294254567/attempts/1?pr=25020), the coverage checks fail because between the jobs that run the tests and the job that checks coverage, the develop branch changed, so the coverage check job merged different code from develop than the test runner jobs.

### URL of the page where the issue is observed.

https://github.com/oppia/oppia/actions/runs/22294254567/attempts/1?pr=25020

### Steps To Reproduce

This is hard to reproduce on oppia/oppia, but in a testing repo, you can create a similar set of backend test CI jobs and merge changes to the backend code under test between the test runs and the coverage check. You'll likely need to build in a delay to the backend test runner jobs so you have time to update develop.

### Expected Behavior

Even if the tests have to run on a slightly older version of our code, they shouldn't fail just because develop changes while the tests are running.

### Screenshots/Videos

_No response_

### What device are you using?

Desktop

### Operating System

Other

### What browsers are you seeing the problem on?

_No response_

### Browser version

_No response_

### Additional context

Two possible solutions:

1. Stop merging from develop for backend tests. I think we used to do this. Downside is any flake fixes won't automatically get incorporated.
2. Create a job that runs before the test-running jobs. This setup job only grabs the SHA of the HEAD of develop and stores it as an artifact. Then all subsequent jobs merge the feature branch into this SHA instead of into develop. This lets us still incorporate new fixes from develop while also ensuring that all jobs run off of the same code.

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #25026: [BUG]: Remove Existing Translation error . 

**Labels:** triage needed, bug

### Describe the bug

When a second logged in user tries to edit a exploration which is assigned to a story , during publishing the story the error is coming . 

### URL of the page where the issue is observed.

http://localhost:8181/create/<exp_id>

### Steps To Reproduce

Prerequisite have 2 logged in user and user A is curriculum admin 

1) With the help of user A make a exploration make edits to the exploration. 
2) The user a should make user b as the manager of the exploration . 
3) User A  should then publish the exploration l. 
4) User A should assign themselves as the curriculum admin
5) User A  should make new math classroom . 
6) They should then make a new story for  any topic , and add the exploration as one of the chapters of the story. 
7) User B should go to the exploration through their webpage . 
8) User B should then edit the exploration . 
9) User B when saving the changes , a warning will be shown with a pop up which will give three options : 
  a) Remove Existing translation b) Mark Translation as stale c) Leave as is 
10) Click on any of the options 
11) Try to publish the exploration . 
12) The stack trace is produced 

### Expected Behavior

It is expected that the story is uploaded succesfully . 

### Screenshots/Videos

(NOTE : The video starts directly from step 8 onwards. )

https://github.com/user-attachments/assets/9f606828-843c-4038-b19d-b0d70b1e2ae9

### What device are you using?

Desktop

### Operating System

Linux, Windows

### What browsers are you seeing the problem on?

Chrome

### Browser version

_No response_

### Additional context

**This issue was seen when I was testing the 3.4.9 release  locally .** 

The stack trace is given below : 
```
ERROR:root:

KeyError: Exception raised

Stack Trace:
Traceback (most recent call last):
  File "/tmp/tmp448rbo1o/lib/python3.10/site-packages/webapp2.py", line 604, in dispatch
    return method(*args, **kwargs)
  File "/home/meeth/oppia/core/controllers/acl_decorators.py", line 2205, in test_can_save
    return handler(self, exploration_id, **kwargs)
  File "/home/meeth/oppia/core/controllers/editor.py", line 266, in put
    exp_services.update_exploration(
  File "/home/meeth/oppia/core/domain/exp_services.py", line 2038, in update_exploration
    models_to_put = compute_models_to_put_when_saving_new_exp_version(
  File "/home/meeth/oppia/core/domain/exp_services.py", line 2143, in compute_models_to_put_when_saving_new_exp_version
    new_voiceover_models = voiceover_services.compute_voiceover_related_change(
  File "/home/meeth/oppia/core/domain/voiceover_services.py", line 312, in compute_voiceover_related_change
    language_accent_codes = language_code_to_language_accent_mapping[
KeyError: 'en'

URL requested: http://localhost:8181/createhandler/data/T1NQEEUjkrRN
Request method: PUT
Handler class name: ExplorationHandler
Traceback (most recent call last):
  File "/tmp/tmp448rbo1o/lib/python3.10/site-packages/webapp2.py", line 604, in dispatch
    return meth

*[truncated]*

---

## #25024: [E2E/Acceptance CI Failure]: should be able to edit classroom information

**Labels:** triage needed, bug, CI breakage

### CI Test Type

E2E

### Which CI step failed?

Acceptance (curriculum-admin/create-edit-and-delete-a-classroom)

### Did the test fail after an automatic rerun?

Test failed once but was not automatically re-run

### Did the test fail when running on desktop, mobile, or both?

Mobile

### Stacktrace

```shell
● Curriculum Admin › should be able to edit classroom information

    TimeoutError: waiting for function failed: timeout 30000ms exceeded

      2446 |
      2447 |     // Wait for the topic to appear in the classroom before adding prerequisites.
    > 2448 |     await this.page.waitForFunction(
           |                     ^
      2449 |       (
      2450 |         topicBoxSelector: string,
      2451 |         topicNameSelector: string,

      at new WaitTask (../../../node_modules/puppeteer/src/common/DOMWorld.ts:813:28)
      at DOMWorld.waitForFunction (../../../node_modules/puppeteer/src/common/DOMWorld.ts:728:22)
      at BaseUser.addTopicToClassroom (utilities/user/curriculum-admin.ts:2448:21)
      at Object.<anonymous> (specs/curriculum-admin/create-edit-and-delete-a-classroom.spec.ts:111:5)
```

### Screenshots and/or Screen Recordings

[acceptance_test_curriculum-admin_create-edit-and-delete-a-classroom_mobile_original.log](https://github.com/user-attachments/files/25484777/acceptance_test_curriculum-admin_create-edit-and-delete-a-classroom_mobile_original.log)

### Occurrences

3 occurrence I think.

https://github.com/oppia/oppia/actions/runs/22257693646/job/64427374261

### Additional Information

_No response_

### Debugging document link

_No response_

---

## #25022: [BUG]: Button is not properly translated on Homepage in Turkish language

**Labels:** triage needed, bug

### Describe the bug

On the homepage, when switching language to Türkçe, the button labeled 'Explore Oppia Classrooms' is not properly translated. 

### URL of the page where the issue is observed.

https://www.oppia.org/

### Steps To Reproduce

1. Go to the Oppia Homepage
2. At the top right, click on the language selector and select Türkçe from the dropdown.
3. The button labeled 'Explore Oppia Classrooms' is not translated, but is still in English.

### Expected Behavior

I expect the button labeled 'Explore Oppia Classrooms' to be translated to the relevant language (Türkçe/Turkish).

### Screenshots/Videos

<img width="1523" height="910" alt="Image" src="https://github.com/user-attachments/assets/120275c1-642b-4c1c-844d-d5a2274f90fd" />

### What device are you using?

Desktop

### Operating System

Windows

### What browsers are you seeing the problem on?

Firefox

### Browser version

147.0.4 (Firefox)

### Additional context

_No response_

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #25021: [E2E/Acceptance CI Failure]: Acceptance (voiceover-submitter/create-delete-and-update-status-of-voiceovers-of-the-explorations)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

Run Mobile Acceptance Test

### Did the test fail after an automatic rerun?

Test failed once but was not automatically re-run

### Did the test fail when running on desktop, mobile, or both?

Mobile

### Stacktrace

```shell
FAIL core/tests/puppeteer-acceptance-tests/specs/voiceover-submitter/create-delete-and-update-status-of-voiceovers-of-the-explorations.spec.ts (282.12 s)
  Voiceover Submitter
    ✕ should see content for voiceover in exploration language
    ✕ should see correct accessibility labels in the voiceover translation tab
    ✕ should be able to add and remove voiceovers to explorations
    ✕ should not be able to upload a non-audio file
    ✕ should not be able to upload audio file larger than 5 minutes
    ✕ should be able to mark/unmark voiceover as stale

  ● Voiceover Submitter › should see content for voiceover in exploration language

    TimeoutError: Element <h3.e2e-test-voice-artists-settings-container.e2e-test-voice-artists-header> "Voice Artists" took too long to be clickable.
    Original Error:
    waiting for function failed: timeout 30000ms exceeded

      492 |         : selector;
      493 |     try {
    > 494 |       await this.page.waitForFunction(isElementClickable, {}, element);
          |                       ^
      495 |     } catch (error) {
      496 |       if (error instanceof Error) {
      497 |         await this.page.evaluate(isElementClickable, element, true, true);

      at new WaitTask (../../../node_modules/puppeteer/src/common/DOMWorld.ts:813:28)
      at DOMWorld.waitForFunction (../../../node_modules/puppeteer/src/common/DOMWorld.ts:728:22)
      at Frame.waitForFunction (../../../node_modules/puppeteer/src/common/FrameManager.ts:1368:28)
      at Page.waitForFunction (../../../node_modules/puppeteer/src/common/Page.ts:3358:29)
      at BaseUser.waitForElementToBeClickable (utilities/common/puppeteer-utils.ts:494:23)
          at runMicrotasks (<anonymous>)
      at BaseUser.clickOnElement (utilities/common/puppeteer-utils.ts:519:5)
      at BaseUser.clickOnElementWithSelector (utilities/common/puppeteer-utils.ts:554:5)
      at BaseUser.addVoiceoverArtistsToExploration (utilities/user/voiceover-admin.ts:241:7)
```

### Screenshots and/or Screen Recordings

https://github.com/user-attachments/assets/ea6298af-bd41-45f6-9813-a0eb98f8ecf0

### Occurrences

https://github.com/Mohak51234/oppia/actions/runs/22255264867/job/64385473046

### Additional Information

_No response_

### Debugging document link

_No response_

---

## #25016: [WIKI]: Fix broken Pillow installation link in Troubleshooting wiki page

**Labels:** triage needed, bug

### Describe the bug

The [Troubleshooting Wiki page](https://github.com/oppia/oppia/wiki/Troubleshooting) contains a broken reference for resolving Pillow/zlib installation errors.

Location: > Wiki Page: Troubleshooting
Section: Installation Issues (or macOS specific section)
Broken Link: https://github.com/python-pillow/Pillow/issues/3438

Proposed Fix:
Update the Wiki link to point to the official Pillow documentation: https://pillow.readthedocs.io/en/stable/installation.html#building-from-source

I would like to be assigned this to update the Wiki.

### URL of the page where the issue is observed.

https://github.com/oppia/oppia/wiki/Troubleshooting

### Steps To Reproduce

Navigate to the Oppia GitHub home page.

On the top bar of sections, navigate to Wiki.

Scroll down to the "MacOS" section or click on the link at the top of the page [Command cc failed with exit status 1](https://github.com/oppia/oppia/wiki/Troubleshooting#command-cc-failed-with-exit-status-1)

Locate and click the link under the reference: https://github.com/python-pillow/Pillow/issues/3438.

Observe that GitHub displays a "404 Not Found" page.

### Expected Behavior

Expected Behaviour:
The link on the Troubleshooting wiki page should direct the user to a valid, official resource for resolving Pillow and zlib installation dependencies. This ensures that new developers, particularly those on macOS, can successfully complete their local environment setup without encountering broken documentation.

### Screenshots/Videos

_No response_

### What device are you using?

Desktop

### Operating System

MacOS

### What browsers are you seeing the problem on?

Safari

### Browser version

_No response_

### Additional context

_No response_

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #25015: [DEVDOC]: Fix broken OpenSSF security link in security.md

**Labels:** triage needed, bug

### Describe the bug

While reviewing the security documentation, I found that the link to the OpenSSF Secure Software Development Fundamentals Course is broken (404).
[Secure Software Development Fundamentals course](https://github.com/ossf/secure-sw-dev-fundamentals/blob/main/secure_software_development_fundamentals.md)

### URL of the page where the issue is observed.

https://github.com/oppia/oppia/blob/develop/.github/SECURITY.md

### Steps To Reproduce

Go to the Oppia repository on GitHub.

Open the file oppia/.github/SECURITY.md

Scroll down to the "References"  section.

Click on the link for "OpenSSF Secure Software Development Fundamentals."

Observe that the link leads to a 404 GitHub error page.

### Expected Behavior

The link should direct the user to the active "Developing Secure Software" training content provided by OpenSSF. This allows contributors to learn the necessary security protocols for working on the Oppia codebase.

### Screenshots/Videos

_No response_

### What device are you using?

Desktop

### Operating System

MacOS

### What browsers are you seeing the problem on?

Safari

### Browser version

_No response_

### Additional context

_No response_

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #25008: core.utils.ValidationError Invalid character _ in the collection title: Mosin_es_testing URL requested

**Labels:** triage needed, server errors, bug

<!--
  - Before filing a new issue, please do a quick search to check that it hasn't
  - already been filed on the [issue tracker](https://github.com/oppia/oppia/issues)._
  -->

This error occurred recently in test server:

```
 core.utils.ValidationError: Invalid character _ in the collection title: Mosin_es_testing URL requested: https://www.oppiatestserver.org/collection_editor_handler/data/0E1alYUpdbqY Request method: PUT Handler class name: EditableCollectionDataHandler Traceback (most recent call last): File "/layers/google.python.pip/pip/lib/python3.10/site-packages/webapp2.py", line 604, in dispatch return method(*args, **kwargs) File "/workspace/core/controllers/acl_decorators.py", line 567, in test_can_edit return handler(self, collection_id, **kwargs) File "/workspace/core/controllers/collection_editor.py", line 135, in put collection_services.update_collection( File "/workspace/core/domain/collection_services.py", line 1282, in update_collection _save_collection(committer_id, collection, commit_message, change_list) File "/workspace/core/domain/collection_services.py", line 982, in _save_collection collection.validate(strict=False) File "/workspace/core/domain/collection_domain.py", line 1314, in validate utils.require_valid_name( File "/workspace/core/utils.py", line 836, in require_valid_name raise ValidationError( core.utils.ValidationError: Invalid character _ in the collection title: Mosin_es_testing
at .require_valid_name ( /workspace/core/utils.py:836 )
at .validate ( /workspace/core/domain/collection_domain.py:1314 )
at ._save_collection ( /workspace/core/domain/collection_services.py:982 )
at .update_collection ( /workspace/core/domain/collection_services.py:1282 )
at .put ( /workspace/core/controllers/collection_editor.py:135 )
at .test_can_edit ( /workspace/core/controllers/acl_decorators.py:567 )
at .dispatch ( /layers/google.python.pip/pip/lib/python3.10/site-packages/webapp2.py:604 ) 
```

**Where did the error occur?** Add the page the error occurred on.

**Which release did the error occur in?** `auto-ad8f48e `

**Frequency of occurrence** Once

**General instructions for contributors**
In general, the procedure for fixing server errors should be the following:

- Analyze the code in the file where the error occurred and come up with a hypothesis for the reason.
- Based on your hypothesis, determine a list of steps that reliably reproduce the issue (or confirm any repro instructions that have been provided). For example, if your hypothesis is that the issue arises due to a delay in a response from the backend server, try to change the code so that the backend server always has a delay, and see if the error then shows up 100% of the time on your local machine.
- Explain your proposed fix, the logic behind it, and any other findings/context you have on this thread. You can also link to a [debugging doc](https://docs.google.com/document/d/1qRbvKjJ0A7NPVK8g6XJNISMx_6BuepoCL7F2eIfrGqM/edit) if you prefer.
- Get your approa

*[truncated]*

---

## #25007: core.utils.ValidationError Cannot reference a private exploration within a public collection

**Labels:** triage needed, server errors, bug

<!--
  - Before filing a new issue, please do a quick search to check that it hasn't
  - already been filed on the [issue tracker](https://github.com/oppia/oppia/issues)._
  -->

This error occurred recently in test server:

```
 core.utils.ValidationError: Cannot reference a private exploration within a public collection, exploration ID: <ID> URL requested: https://www.oppiatestserver.org/collection_editor_handler/publish/<ID> Request method: PUT Handler class name: CollectionPublishHandler Traceback (most recent call last): File "/layers/google.python.pip/pip/lib/python3.10/site-packages/webapp2.py", line 604, in dispatch return method(*args, **kwargs) File "/workspace/core/controllers/acl_decorators.py", line 2494, in test_can_publish_collection return handler(self, collection_id, **kwargs) File "/workspace/core/controllers/collection_editor.py", line 239, in put collection_services.validate_exps_in_collection_are_public(collection) File "/workspace/core/domain/collection_services.py", line 940, in validate_exps_in_collection_are_public raise utils.ValidationError( core.utils.ValidationError: Cannot reference a private exploration within a public collection, exploration ID: epcC7WT1KbvH
at .validate_exps_in_collection_are_public ( /workspace/core/domain/collection_services.py:940 )
at .put ( /workspace/core/controllers/collection_editor.py:239 )
at .test_can_publish_collection ( /workspace/core/controllers/acl_decorators.py:2494 )
at .dispatch ( /layers/google.python.pip/pip/lib/python3.10/site-packages/webapp2.py:604 ) 
```

**Where did the error occur?** Add the page the error occurred on.

**Which release did the error occur in?** `auto-ad8f48e `

**Frequency of occurrence** Occurred once.

**General instructions for contributors**
In general, the procedure for fixing server errors should be the following:

- Analyze the code in the file where the error occurred and come up with a hypothesis for the reason.
- Based on your hypothesis, determine a list of steps that reliably reproduce the issue (or confirm any repro instructions that have been provided). For example, if your hypothesis is that the issue arises due to a delay in a response from the backend server, try to change the code so that the backend server always has a delay, and see if the error then shows up 100% of the time on your local machine.
- Explain your proposed fix, the logic behind it, and any other findings/context you have on this thread. You can also link to a [debugging doc](https://docs.google.com/document/d/1qRbvKjJ0A7NPVK8g6XJNISMx_6BuepoCL7F2eIfrGqM/edit) if you prefer.
- Get your approach validated by an Oppia team member.
- Make a PR that fixes the issue.

---

## #25006: ValueError min() arg is an empty sequence

**Labels:** triage needed, server errors, bug

<!--
  - Before filing a new issue, please do a quick search to check that it hasn't
  - already been filed on the [issue tracker](https://github.com/oppia/oppia/issues)._
  -->

This error occurred recently in test server:

```
Error message from worker: Traceback (most recent call last):
  File "apache_beam/runners/common.py", line 1498, in apache_beam.runners.common.DoFnRunner.process
  File "apache_beam/runners/common.py", line 685, in apache_beam.runners.common.SimpleInvoker.invoke_process
  File "/layers/google.python.pip/pip/lib/python3.10/site-packages/apache_beam/transforms/core.py", line 2162, in <lambda>
  File "/opt/apache/beam-venv/beam-venv-worker-sdk-0-0/lib/python3.10/site-packages/core/jobs/batch_jobs/contributor_admin_stats_jobs.py", line 655, in transform_translation_review_stats
    first_contribution_date = min(
ValueError: min() arg is an empty sequence

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.10/site-packages/apache_beam/runners/worker/sdk_worker.py", line 313, in _execute
    response = task()
  File "/usr/local/lib/python3.10/site-packages/apache_beam/runners/worker/sdk_worker.py", line 387, in <lambda>
    lambda: self.create_worker().do_instruction(request), request)
  File "/usr/local/lib/python3.10/site-packages/apache_beam/runners/worker/sdk_worker.py", line 659, in do_instruction
    return getattr(self, request_type)(
  File "/usr/local/lib/python3.10/site-packages/apache_beam/runners/worker/sdk_worker.py", line 697, in process_bundle
    bundle_processor.process_bundle(instruction_id))
  File "/usr/local/lib/python3.10/site-packages/apache_beam/runners/worker/bundle_processor.py", line 1274, in process_bundle
    input_op_by_transform_id[element.transform_id].process_encoded(
  File "/usr/local/lib/python3.10/site-packages/apache_beam/runners/worker/bundle_processor.py", line 237, in process_encoded
    self.output(decoded_value)
  File "apache_beam/runners/worker/operations.py", line 568, in apache_beam.runners.worker.operations.Operation.output
  File "apache_beam/runners/worker/operations.py", line 570, in apache_beam.runners.worker.operations.Operation.output
  File "apache_beam/runners/worker/operations.py", line 260, in apache_beam.runners.worker.operations.SingletonElementConsumerSet.receive
  File "apache_beam/runners/worker/operations.py", line 263, in apache_beam.runners.worker.operations.SingletonElementConsumerSet.receive
  File "apache_beam/runners/worker/operations.py", line 951, in apache_beam.runners.worker.operations.DoOperation.process
  File "apache_beam/runners/worker/operations.py", line 952, in apache_beam.runners.worker.operations.DoOperation.process
  File "apache_beam/runners/common.py", line 1500, in apache_beam.runners.common.DoFnRunner.process
  File "apache_beam/runners/common.py", line 1609, in apache_beam.runners.common.DoFnRunner._reraise_augmented
  File "apache_beam/runners/common.py", l

*[truncated]*

---

## #25002: [BUG]: Installation script strictly requires Python 3.10.16 and fails on other 3.10 patches

**Labels:** triage needed, bug

### Describe the bug

[install_third_party_libs.py](https://github.com/user-attachments/files/25459338/install_third_party_libs.py)
Currently, scripts/install_third_party_libs.py raises an exception if the Python version is not exactly 3.10.16. This makes it difficult for contributors using other stable patches like 3.10.12 to set up the project. The script should allow the 3.10.x family but warn users if they aren't on .16.

### URL of the page where the issue is observed.

N/A

### Steps To Reproduce

Ensure you have a version of Python 3.10 installed that is not 3.10.16 (e.g., Python 3.10.12).

Navigate to the root of the Oppia repository.

Run the command: python3 -m scripts.install_third_party_libs.

Observe that the script terminates with an Exception: No suitable python version found error, even though Python 3.10 is being used.

### Expected Behavior

The script should recognize that any version in the Python 3.10.x family is acceptable for development, or at least allow it to proceed with a warning.

### Screenshots/Videos

_No response_

### What device are you using?

Desktop

### Operating System

Linux

### What browsers are you seeing the problem on?

Firefox

### Browser version

_No response_

### Additional context

_No response_

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #24976: [BUG]: Tags do not appear in Preview Summary

**Labels:** bug

### Describe the bug

When adding one or more tags in the Exploration Editor > Settings, the tags are not displayed in the Preview Summary page after clicking the Preview Summary button.

Although the tags are successfully entered in the Settings section, they do not appear in the preview card as expected. This prevents users from verifying whether the tags were correctly added before saving or publishing.

### URL of the page where the issue is observed.

N/A

### Steps To Reproduce

1. Open the **Exploration Editor**.
2. Go to **Settings**.
3. Add one or more tags.
4. Click on **Preview Summary**.

### Expected Behavior

The Preview Summary Card should display all tags entered by the user.

### Screenshots/Videos

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/8d87a269-caab-4da5-b3fd-e7153d5e58ec" />

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/10b8535c-0ccb-4b85-8b0b-18b0e01191e8" />

### What device are you using?

Desktop

### Operating System

Windows

### What browsers are you seeing the problem on?

Chrome

### Browser version

_No response_

### Additional context

_No response_

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #24972: [Flake]: Acceptance (site-moderator/check-recent-commits)

<img width="1422" height="833" alt="Image" src="https://github.com/user-attachments/assets/3fa62891-6bef-47db-a6d0-1d1e86c5a34d" />

<img width="837" height="416" alt="Image" src="https://github.com/user-attachments/assets/79212bd4-c91a-4590-b30c-8db3e094845d" />

CI Test Type : Acceptance

CI Test failed on : mobile, desktop

Occurrences :  in PR #20153

---

## #24970: Exception User with ID not found.

**Labels:** triage needed, server errors, bug

<!--
  - Before filing a new issue, please do a quick search to check that it hasn't
  - already been filed on the [issue tracker](https://github.com/oppia/oppia/issues)._
  -->

This error occurred recently in test server:

```
Exception: Exception raised

Stack Trace: 
Traceback (most recent call last):
  File "/layers/google.python.pip/pip/lib/python3.10/site-packages/webapp2.py", line 604, in dispatch
    return method(*args, **kwargs)
  File "/workspace/core/controllers/acl_decorators.py", line 2652, in test_can_perform
    return handler(self, **kwargs)
  File "/workspace/core/controllers/tasks.py", line 230, in post
    email_manager.send_flag_exploration_email(
  File "/workspace/core/domain/email_manager.py", line 1585, in send_flag_exploration_email
    reporter_username = user_services.get_username(reporter_id)
  File "/workspace/core/domain/user_services.py", line 1552, in get_username
    return get_usernames([user_id], strict=True)[0]
  File "/workspace/core/domain/user_services.py", line 1599, in get_usernames
    non_system_users_settings = get_users_settings(
  File "/workspace/core/domain/user_services.py", line 343, in get_users_settings
    raise Exception('User with ID \'%s\' not found.' % user_id)
Exception: User with ID <ID> not found.

URL requested: http://oppiatestserver.appspot.com/task/email/flagexplorationemailhandler
Request method: POST
Handler class name: FlagExplorationEmailHandler
Traceback (most recent call last):
  File "/layers/google.python.pip/pip/lib/python3.10/site-packages/webapp2.py", line 604, in dispatch
    return method(*args, **kwargs)
  File "/workspace/core/controllers/acl_decorators.py", line 2652, in test_can_perform
    return handler(self, **kwargs)
  File "/workspace/core/controllers/tasks.py", line 230, in post
    email_manager.send_flag_exploration_email(
  File "/workspace/core/domain/email_manager.py", line 1585, in send_flag_exploration_email
    reporter_username = user_services.get_username(reporter_id)
  File "/workspace/core/domain/user_services.py", line 1552, in get_username
    return get_usernames([user_id], strict=True)[0]
  File "/workspace/core/domain/user_services.py", line 1599, in get_usernames
    non_system_users_settings = get_users_settings(
  File "/workspace/core/domain/user_services.py", line 343, in get_users_settings
    raise Exception('User with ID \'%s\' not found.' % user_id)
Exception: User with ID <ID> not found.
```

**Where did the error occur?** http://oppiatestserver.appspot.com/task/email/flagexplorationemailhandler

**Which release did the error occur in?** Occurred in 3.4.9, 3.5.0 and 3.4.9-hotfix-1

**Frequency of occurrence** Occurred 708 times, first seen on Jan 19 and last seen Feb 19.

**General instructions for contributors**
In general, the procedure for fixing server errors should be the following:

- Analyze the code in the file where the error occurred and come up with a hypothesis for the reason.
- Based on your hypothesis, determine a list

*[truncated]*

---

## #24968: [Feature Request]: Remove unused interactions

**Labels:** triage needed, enhancement

### Is your feature request related to a problem? Please describe.

We have identified that the below interaction is no longer in use and is not required .
To reduce unnecessary complexity in the codebase, this interaction should be completely removed.

- [ ] pencilcode
- [ ] music notes
- [ ] codemirror,
- [ ] graph
- [ ] interactive map

### Describe the solution (or solutions) you'd like

This would involve deleting the interaction files, removing its registration/configuration, cleaning up any related tests, and ensuring there are no leftover references.

### Describe alternatives you've considered and rejected

_No response_

### Additional context

_No response_

---

## #24953: [BUG]: 'Add Item' button label in 'Set Input' interaction has no character limit, causing error

**Labels:** bug

### Describe the bug

When entering an excessively large amount of text in the "Label for the 'Add Item' button" field within the "Set Input" interaction, the system does not enforce any character limit. As a result, attempting to save the interaction causes an error.

There is no validation or feedback informing the user about a maximum allowed length before saving.

### URL of the page where the issue is observed.

N/A

### Steps To Reproduce

1. Go to /creator-dashboard and click on "Create Exploration".
2. Click on “Add Interaction”, select the "Math" tab, and select the "Set Input" interaction.
3. Paste a very large text (e.g., 1,000,000,000 characters) in the box under "Label for the 'Add Item' button".
4. Click on “Save interaction".

### Expected Behavior

The system should enforce a character limit for this field and the limit should be clearly indicated to the user.

### Screenshots/Videos

<img width="1894" height="902" alt="Image" src="https://github.com/user-attachments/assets/f49dd69a-e131-400f-ba1b-082744f873cb" />

### What device are you using?

Desktop

### Operating System

Windows

### What browsers are you seeing the problem on?

Chrome

### Browser version

_No response_

### Additional context

_No response_

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #24946: [E2E/Acceptance CI Failure]:  Visual regression in goalsTabMobileView (Logged-In Learner)

**Labels:** bug, Impact: Low -- ONLY DO IF GOOD FIRST ISSUE, Work: Medium, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

Acceptance (logged-in-learner/interact-with-goals-in-learner-dashboard)

### Did the test fail after an automatic rerun?

Test failed once and then passed after an automatic rerun

### Did the test fail when running on desktop, mobile, or both?

Desktop

### Stacktrace

```shell
ebar_btn--active> "Goals" is clickable...
[test-log] 31:51.919: Element (selector: .e2e-test-goals-section) clicked.
[test-log] 31:51.922: Element .e2e-test-goals-section-container is visible.
[test-log] 31:54.940: Page rendered fully.
[test-log] 31:54.943: Element .e2e-test-goals-section-container is visible.
[test-log] 32:00.323: Test failed: Capturing screenshots...
[test-log] 32:00.324: Started closing broswer for loggedInUser1.
[test-log] 32:00.324: Screen recording stopped for loggedInUser1.
[test-log] 32:00.325: Error while taking screenshot for loggedInUser1: Error: Protocol error (Target.activateTarget): Session closed. Most likely the page has been closed.
[test-log] 32:00.427: Browser closed for loggedInUser1.
[test-log] 32:00.427: Closing browsers for 1 users.
[test-log] 32:00.427: Started closing broswer for superAdm.
[test-log] 32:00.427: Screen recording stopped for superAdm.
[test-log] 32:00.427: Browser closed for superAdm.
[test-log] 32:00.427: All browsers closed.
FAIL core/tests/puppeteer-acceptance-tests/specs/logged-in-learner/interact-with-goals-in-learner-dashboard.spec.ts (1066.924 s)
  Logged-In Learner
    ✓ should start and complete Chapter 1, then show updated progress (33%) (50596 ms)
    ✓ should complete Chapter 2 and update progress to 66% (34420 ms)
    ✓ should complete final chapter and move goal to Completed section (39552 ms)
    ✕ should display correctly on mobile viewport (19377 ms)

  ● Logged-In Learner › should display correctly on mobile viewport

    Expected image to match or be a close match to snapshot but was 5.43248375812094% different from snapshot (13588 differing pixels).
    See diff for details: /home/runner/work/oppia/oppia/core/tests/puppeteer-acceptance-tests/logged-in-learner/interact-with-goals-in-learner-dashboard/prod-mobile-screenshots/diff-snapshots/goalsTabMobileView-diff.png
    Download the artifact folder diff-snapshots from the github workflow to check the difference between the old screenshot(s) and the new one(s). To download the folder, go to "Summary" of the CI Job of the PR and find the "Artifacts" section. The artifact folder name should be something like diff-snapshots_(suite-name)_desktop_original. The diff screenshot(s) should end with "-diff".
    Please update the screenshots if the UI changed. If screenshot comparisons consistently show the same difference percentage across multiple test runs, the baseline screenshot(s) should be updated.
    To update the screenshots(s), you should run the tests in CI, download the artifact folder new-snapshots from the github workflow and use the screenshots in that folder to replace the old one(s).


*[truncated]*

---

## #24943: [BUG]: Next Lesson button is white on the lesson completion page

**Labels:** bug

### Describe the bug

Next Lesson button is white on the lesson completion page. 

### URL of the page where the issue is observed.

https://www.oppiatestserver.org/explore/G8ZgSj1O4rjE?topic_url_fragment=fractionsssssssss&classroom_url_fragment=math&story_url_fragment=piece-of-cake&node_id=node_1

### Steps To Reproduce

1. As a learner navigate to Fraction - What is a Fraction Lesson
2. Complete the lesson
3. Observe

### Expected Behavior

The next right button is not an empty white square, it is either an arrow or a thumbnail of the next lesson

### Screenshots/Videos

<img width="710" height="591" alt="Image" src="https://github.com/user-attachments/assets/6397325f-7072-4e6c-9c9e-c946ba9eead1" />

### What device are you using?

Desktop

### Operating System

MacOS

### What browsers are you seeing the problem on?

_No response_

### Browser version

_No response_

### Additional context

_No response_

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #24938: [Feature Request]: Migrate remaining userJourneys.js tests to acceptance

**Labels:** good first issue, enhancement, Work: Medium, Work: Low, EUJ IP.1, IUJ LC.1, EUJ LO.13

### Is your feature request related to a problem? Please describe.

We are currently migrating from E2E tests to Acceptance tests; however, some of the E2E tests are still not covered by Acceptance tests. We need to write acceptance tests covering these uncovered E2E tests and delete the corresponding E2E test.

The goal is to create a new acceptance test that covers the features currently handled by the existing E2E test.

### Describe the solution (or solutions) you'd like

Write the new acceptance test and delete the existing E2E test.

**Steps to follow:**

1. Create a new acceptance test file in the appropriate directory.
2. Write the acceptance test based on the specifications found in the **WIP Doc (Internal/External Users)** linked below.
3. Add the acceptance test to [acceptance.json](https://github.com/oppia/oppia/blob/develop/core/tests/ci-test-suite-configs/acceptance.json).
4. Run the newly created test-suite locally and ensure it passes.
5. Push the code to your repo-fork.
6. **Stress test** the new test-suite to check for flakes. (In your Oppia repo fork, go to *Actions* > *Stress Test Acceptance Test* > *Run Workflow* > branch: `<YOUR_FEATURE_BRANCH_NAME>`, runs: `20`, test-suite: `<TEST_SUITE_NAME_USED_IN_ACCEPTANCE.JSON>`).
7. Ensure that all jobs pass in the above workflow run.
8. Remove the corresponding E2E test file.
9. Open a PR.

### Describe alternatives you've considered and rejected

*No response*

### Additional context

*No response*

---

### E2E Tests to be Removed

* userJourney.js

### Acceptance Tests to be Added / Updated

* [EDITED] IP.1. Learn about the organization (WIP External Users)
* [EDITED] LO.13. View a collection (WIP External Users)
* [EDITED] LC.1. Create a basic exploration. (WIP Internal Users)

### Documentation References

* **WIP Doc (Internal Users):** [[Spreadsheet Link](https://docs.google.com/spreadsheets/d/1DIZ0_Gmf9uhjTbhuDpA495PTjYZW9ZE97r6urS-iXwg/edit?gid=888982708&authuser=2)](https://docs.google.com/spreadsheets/d/1DIZ0_Gmf9uhjTbhuDpA495PTjYZW9ZE97r6urS-iXwg/edit?gid=888982708)
* [WIP Doc (External Users)](https://docs.google.com/spreadsheets/d/1IrxN13IC5xwWdAFnGMu_4p3FU1ADL4QO-eLZIuTowIA/edit?gid=888982708#gid=888982708)
* **Puppeteer Acceptance Tests Folder:** [[GitHub Link](https://github.com/oppia/oppia/tree/develop/core/tests/puppeteer-acceptance-tests)](https://github.com/oppia/oppia/tree/develop/core/tests/puppeteer-acceptance-tests)
* **Acceptance Test Wiki:** [[GitHub Wiki](https://github.com/oppia/oppia/wiki/Acceptance-Tests)](https://github.com/oppia/oppia/wiki/Acceptance-Tests)


> [!IMPORTANT]
> **If you want to claim this issue, strictly follow the instructions below:**
>
> 1. Read the guidance (if you haven't already):  
>    https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue  
> 2. As this issue is simple, no need to explain how you’ll fix it — just provide proof you can complete it.  
> 3. Run:
>    ```
>    VIDEO_RECORDING_IS_

*[truncated]*

---

## #24933: [Feature Request]: Use new translation opportunity structure for all user-generated content in curated curriculum

**Labels:** enhancement

### Is your feature request related to a problem? Please describe.

The translation infrastructure built in https://github.com/oppia/oppia/issues/22793 should be extended to cover all entities with user-generated content in our curated curriculum.

### Describe the solution (or solutions) you'd like

TDD: https://docs.google.com/document/d/1cFJ6weoOWPopLFpRf2lw4RRPPNFVJ4QVLqdxb_WsLyY/edit?

### Describe alternatives you've considered and rejected

See TDD

### Additional context

_No response_

---

## #24932: [Feature Request]: Remove E2E test topicAndStoryEditor.js

**Labels:** good first issue, enhancement, Impact: High, Work: Medium, IUJ TM.3

### Is your feature request related to a problem? Please describe.

We are currently migrating from E2E tests to Acceptance tests, however, some of the E2E tests are still not covered by Acceptance tests. So, we need to write acceptance tests covering uncovered E2E tests and delete the corresponding E2E test.

Acceptance test(s) for "TM.3. Create, delete and edit stories and chapters" (e.g. Save chapters with mobile-supported explorations, Edit and preview a chapter) need to be created or updated to cover the features currently covered by E2E test "topicAndStoryEditor".



### Describe the solution (or solutions) you'd like

Write or update the acceptance test(s) for TM.3 (Create, delete and edit stories and chapters) to cover the scenarios in topicAndStoryEditor.js, and delete the existing E2E test (wipeout).

Steps to follow:

  1. Update the existing acceptance test for TM.3: `core/tests/puppeteer-acceptance-tests/specs/topic-manager/create-delete-and-edit-the-stories-and-chapters.spec.ts` (test-suite name in acceptance.json: `topic-manager/create-delete-and-edit-the-stories-and-chapters`).
  2. Write/add the new steps based on TM.3. Create, delete and edit stories and chapters from [CUJ v3 Sheet (Internal)](https://docs.google.com/spreadsheets/d/1DIZ0_Gmf9uhjTbhuDpA495PTjYZW9ZE97r6urS-iXwg/edit?gid=103504248#gid=103504248).
  3. No new entry in acceptance.json is needed (the test-suite is already registered).
  4. Extend the spec to cover the missing scenarios from topicAndStoryEditor.js (e.g. same exploration for two chapters → warning, reorder chapters, prerequisite/acquired skill validation, delete prerequisite and acquired skill) as needed.
  5. Run newly created/updated test-suite locally and ensure it passes.
  6. Push the code to your repo-fork.
  7. Stress test the new test-suite to check for flakes. (In your Oppia repo fork, go to Actions > Stress Test Acceptance Test > Run Workflow > branch: <YOUR_FEATURE_BRANCH_NAME>, runs: <ATLEAST_20>, test-suite: <TEST_SUITE_NAME_USED_IN_ACCEPTANCE.JSON>.)
  8. Ensure that all jobs passes in the above workflow run.
  9. Remove E2E test, topicAndStoryEditor.js.
  10. Open a PR :)

Other References:

[puppeteer-acceptance-tests](https://github.com/oppia/oppia/tree/develop/core/tests/puppeteer-acceptance-tests) is the base folder for acceptance tests.
Acceptance tests: https://github.com/oppia/oppia/wiki/Acceptance-Tests


### Describe alternatives you've considered and rejected

_No response_

### Additional context

_No response_

---

## #24931: [E2E/Acceptance CI Failure]: Acceptance (logged-out-learner/give-feedback-on-the-lesson-from-the-lesson-player)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

run desktop tests

### Did the test fail after an automatic rerun?

Test failed once but was not automatically re-run

### Did the test fail when running on desktop, mobile, or both?

Desktop

### Stacktrace

```shell
ERROR:root:Frontend error: 
Error: A network error (such as timeout, interrupted connection or unreachable host) has occurred.

    at URL: http://localhost:8181/login?return_url=%2F
INFO     2026-02-13 02:16:44,864 module.py:830] default: "POST /frontend_errors HTTP/1.1" 200 30
[test-log] 17:14.465: Test failed: Capturing screenshots...
[test-log] 17:14.468: Closing browsers for 0 users.
[test-log] 17:14.468: All browsers closed.
FAIL core/tests/puppeteer-acceptance-tests/specs/logged-out-learner/give-feedback-on-the-lesson-from-the-lesson-player.spec.ts (55.541 s)
  Logged-Out Learner
    ✕ should be able to give feedback from the navbar

  ● Logged-Out Learner › should be able to give feedback from the navbar

    TimeoutError: Navigation timeout of 30000 ms exceeded

      662 |       await this.clickOnElementWithText(selector);
      663 |     }
    > 664 |     await navigationPromise;
          |     ^
      665 |   }
      666 |
      667 |   /**

      at ../../../node_modules/puppeteer/src/common/LifecycleWatcher.ts:211:18
      at FrameManager.waitForFrameNavigation (../../../node_modules/puppeteer/src/common/FrameManager.ts:239:19)
      at Frame.waitForNavigation (../../../node_modules/puppeteer/src/common/FrameManager.ts:795:12)
      at Page.waitForNavigation (../../../node_modules/puppeteer/src/common/Page.ts:1833:12)
      at BaseUser.clickAndWaitForNavigation (utilities/common/puppeteer-utils.ts:664:5)
      at BaseUser.signInWithEmail (utilities/common/puppeteer-utils.ts:366:5)
      at BaseUser.signUpNewUser (utilities/common/puppeteer-utils.ts:373:5)
      at Function.Object.<anonymous>.UserFactory.createNewUser (utilities/common/user-factory.ts:308:5)
      at specs/logged-out-learner/give-feedback-on-the-lesson-from-the-lesson-player.spec.ts:53:25

Test Suites: 1 failed, 1 total
Tests:       1 failed, 1 total
Snapshots:   0 total
Time:        57.378 s
Ran all test suites matching /core\/tests\/puppeteer-acceptance-tests\/specs\/logged-out-learner\/give-feedback-on-the-lesson-from-the-lesson-player.spec.ts/i.
INFO     2026-02-13 02:17:14,558 shutdown.py:48] Shutting down.
Error: 2-13 02:17:14 +0000] [2982] [ERROR] Worker (pid:2986) was sent SIGTERM!
Error: 2-13 02:17:14 +0000] [2970] [ERROR] Worker (pid:2975) was sent SIGTERM!
INFO     2026-02-13 02:17:15,193 stub_util.py:321] Applying all pending transactions and saving the datastore
INFO     2026-02-13 02:17:15,193 stub_util.py:324] Saving search indexes
                                                            
ERROR:root:Portserver failed to shut down after 10 seconds.
Traceback (mo

*[truncated]*

---
