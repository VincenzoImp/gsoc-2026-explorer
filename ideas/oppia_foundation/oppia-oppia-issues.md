# "impact: high"

**Parent:** Oppia Foundation — Project Ideas
**Source:** https://github.com/oppia/oppia/issues?q=is%3Aopen+is%3Aissue+label%3A%22Impact%3A+High%22
**Scraped:** 2026-02-22T23:28:47.619918

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

**Labels:** triage needed, bug

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

## #24975: [BUG]: Try again is not Displaying

**Labels:** triage needed, bug

### Describe the bug

If you Enter wrong messeage or wrong input  Try again messeage is not displaying.

### URL of the page where the issue is observed.

https://www.oppiatestserver.org/create/FZLXbilbRDWw#/preview/1-number

### Steps To Reproduce

Go to /Creator- dashboared and click "Create Exploration"
click on Add interaction and select the Number input interaction
Click on the checkbox “Allow only input greater than or equal to zero”.
Click on “Save interaction."
In the "Add Response" pop-up, select any option from the dropdown under “if the learner’s answer …”. Write the correct answer in the content box. Add "Correct!" feedback.
Click on “Save Response
Enter a wrong number as the answer and click "Submit".

### Expected Behavior

The message "Try again" is displayed.

### Screenshots/Videos

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/c42a8d6a-66c1-4e64-b1c4-204b5b08d6c2" />

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

**Labels:** triage needed, bug

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

**Labels:** triage needed, bug

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

**Labels:** triage needed, enhancement

### Is your feature request related to a problem? Please describe.


We are currently migrating from E2E tests to Acceptance tests, however, some of the E2E tests are still not covered by Acceptance tests. So, we need to write acceptance tests covering uncovered E2E tests and delete the corresponding E2E test.

The following scenarios from E2E test `core/tests/webdriverio_desktop/userJourneys.js` are **Not Covered** in Acceptance tests:

- `should not change in an exploration`
- `should not change in exploration and collection player for guest users`
- `should show version details in the about page footer`


### Describe the solution (or solutions) you'd like

Write acceptance tests covering the scenarios above and then remove the corresponding tests from `core/tests/webdriverio_desktop/userJourneys.js`. The E2E file itself can be cleaned up or fully removed in the parent \"Fully Remove E2E tests\" issue once all of its scenarios are covered by acceptance tests.

Steps to follow:

  1. Create a new acceptance test for **exploration editor** to cover: `should not change in an exploration`. (Suggested file name: `core/tests/puppeteer-acceptance-tests/specs/exploration-editor/site-language-persists-in-exploration-editor.spec.ts`.)
  2. Create a new acceptance test for **logged-out users** to cover: `should not change in exploration and collection player for guest users`. (Suggested file name: `core/tests/puppeteer-acceptance-tests/specs/logged-out-user/site-language-persists-in-collection-player.spec.ts`.)
  3. Update the existing acceptance test `core/tests/puppeteer-acceptance-tests/specs/logged-out-user/click-all-links-in-oppia-footer.spec.ts` to cover: `should show version details in the about page footer`.
  4. Add any new acceptance test-suite(s) to `acceptance.json` (https://github.com/oppia/oppia/blob/develop/core/tests/ci-test-suite-configs/acceptance.json).
  5. Run the newly created/updated test-suite(s) locally and ensure they pass.
  6. Push the code to your repo-fork.
  7. Stress test the new/updated test-suite(s) to check for flakes. (In your Oppia repo fork, go to Actions > Stress Test Acceptance Test > Run Workflow > branch: `<YOUR_FEATURE_BRANCH_NAME>`, runs: `<ATLEAST_20>`, test-suite: `<TEST_SUITE_NAME_USED_IN_ACCEPTANCE.JSON>`.)
  8. Ensure that all jobs passes in the above workflow run.
  9. Remove the three corresponding tests from `core/tests/webdriverio_desktop/userJourneys.js` (and any other now-fully-covered tests, as per the migration sheet). Keep the file itself for now; it will be cleaned up/removed under the parent E2E removal issue.
  10. Open a PR :)
  
Other References:

- [puppeteer-acceptance-tests](https://github.com/oppia/oppia/tree/develop/core/tests/puppeteer-acceptance-tests) is the base folder for acceptance tests.
- Acceptance tests: https://github.com/oppia/oppia/wiki/Acceptance-Tests

### Describe alternatives you've considered and rejected

_No response_

### Additional context

_No response_

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

**Labels:** triage needed, good first issue, enhancement, Impact: High, Work: Medium, IUJ TM.3

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

## #24925: [E2E/Acceptance CI Failure]: should have the correct tab title, available sections on landing and Sidebar should contain these items in this order from top to bottom: Profile picture, "Home" button, "Goals" button, "Progress" button (19963 ms)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

E2E

### Which CI step failed?

Acceptance (logged-in-learner/manage-classroom-progress-in-home-learner-dashboard)

### Did the test fail after an automatic rerun?

Test failed once and then passed after an automatic rerun

### Did the test fail when running on desktop, mobile, or both?

Mobile

### Stacktrace

```shell
FAIL core/tests/puppeteer-acceptance-tests/specs/logged-in-learner/manage-classroom-progress-in-home-learner-dashboard.spec.ts (1404.298 s)
  Logged-In Learner
    ✕ should have the correct tab title, available sections on landing and Sidebar should contain these items in this order from top to bottom: Profile picture, "Home" button, "Goals" button, "Progress" button (19963 ms)
    ✓ should navigate directly to math classroom (9283 ms)
    ✓ should navigate directly to the Place Values topic in the math classroom (13265 ms)
    ✓ should display in-progress and recommended lessons after starting a lesson (36363 ms)
    ✓ should not recommend any lessons if currently on last lesson (107690 ms)

  ● Logged-In Learner › should have the correct tab title, available sections on landing and Sidebar should contain these items in this order from top to bottom: Profile picture, "Home" button, "Goals" button, "Progress" button

    Expected image to match or be a close match to snapshot but was 5.53023488255872% different from snapshot (55330 differing pixels).
    See diff for details: /home/runner/work/oppia/oppia/core/tests/puppeteer-acceptance-tests/logged-in-learner/manage-classroom-progress-in-home-learner-dashboard/prod-mobile-screenshots/diff-snapshots/learnerDashboardHomeTab-diff.png
    Download the artifact folder diff-snapshots from the github workflow to check the difference between the old screenshot(s) and the new one(s). To download the folder, go to "Summary" of the CI Job of the PR and find the "Artifacts" section. The artifact folder name should be something like diff-snapshots_(suite-name)_desktop_original. The diff screenshot(s) should end with "-diff".
    Please update the screenshots if the UI changed. If screenshot comparisons consistently show the same difference percentage across multiple test runs, the baseline screenshot(s) should be updated.
    To update the screenshots(s), you should run the tests in CI, download the artifact folder new-snapshots from the github workflow and use the screenshots in that folder to replace the old one(s).
    To download the folder, go to "Summary" of the CI Job of the PR and find the "Artifacts" section. The artifact folder name should be something like new-snapshots_(suite-name)_desktop_original. The new screenshot(s) should end with "-received". When replacing the screenshot(s), make sure to change the postfix "-received" to "-snap".

      1126 |         ' folder name should be something like new-snapshots_(suite-name)_desktop_original.' +
      1127 |         ' The new screenshot(s) should end with "-received". When replacing the screenshot(s), make sure to

*[truncated]*

---

## #24924: [BUG]: Broken ARIA menu and Contrast errors in shared components (Navbar) across multiple pages

**Labels:** triage needed, bug

### Describe the bug

While using the WAVE Web Accessibility Evaluation Tool (Chrome Extension) across global routes like `/donate` and `/learner-dashboard`, I discovered two main accessibility violations originating from shared UI components, specifically within `top-navigation-bar` and `admin-navbar`:

1. **Broken ARIA menu**: Dropdown `<ul>` elements (such as "Learn", "About", "Language", and "Profile") are incorrectly assigned `role="menu"`. Since these are standard navigation links and not application menus, this breaks arrow-key keyboard navigation for screen readers. This violates WCAG 2.1.1 and 4.1.2.
2. **Very low contrast**: Several text elements and icons in the `top-navigation-bar.component.css` fail to meet the WCAG minimum contrast ratio of 4.5:1 against the white background. Specifically:
   - Language/Volunteer/Contact/Fav items (`#f2994a`, `#2d9cdb`, `#b4bbc3`, `#eb5757`)
   - Hover states (`#888`)
   - Description texts using `opacity: 0.9` which dilutes the contrast.

### URL of the page where the issue is observed.

Observed across multiple pages, including:
- https://www.oppia.org/donate
- http://localhost:8181/learner-dashboard

### Steps To Reproduce

1. Navigate to any main page on Oppia (e.g., the Learner Dashboard or Donate page).
2. Run the WAVE Chrome or Firefox Extension.
3. Open the "Details" tab in the WAVE sidebar.
4. Observe the "Errors" section showing the "Broken ARIA menu" flag pointing to the top navigation area.
5. Observe the "Contrast Errors" section showing the "Very low contrast" flag.

### Expected Behavior

- For the ARIA menu error: Remove the `role="menu"` attribute from the navigation dropdown `<ul>` elements in `top-navigation-bar.component.html` and `admin-navbar.component.html`. Standard semantic HTML handles navigation accessibility correctly.
- For the Contrast error: Update the CSS hex codes in `top-navigation-bar.component.css` to darker, WCAG AA compliant shades (e.g., changing `#2d9cdb` to a darker `#0070B8`, removing opacity rules that dilute text color, etc.) to ensure a >= 4.5:1 ratio.

### Screenshots/Videos

<img width="1918" height="1038" alt="Image" src="https://github.com/user-attachments/assets/bc369d6c-03cb-4373-bbba-5b20cf0d0545" />

<img width="1918" height="1038" alt="Image" src="https://github.com/user-attachments/assets/5d1ca0cb-90fe-433c-83b9-a0e7caf2bde6" />

### What device are you using?

Desktop

### Operating System

Linux

### What browsers are you seeing the problem on?

Chrome

### Browser version

Chromium 144.0.7559.132

### Additional context

I initially discovered these UI accessibility issues on the `/donate` page while verifying a separate server-side HTML issue (#24488). After testing other routes like `/learner-dashboard`, I confirmed it's a sitewide issue likely rooted in a shared component.

I would love to be assigned to this issue so I can track down the exact components and fix them.

### Tips for developers

Before addressing the bug, please identify wh

*[truncated]*

---

## #24920: [E2E/Acceptance CI Failure]: Acceptance (curriculum-admin/create-edit-and-delete-a-classroom)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

Run Mobile Acceptance Test curriculum-admin/create-edit-and-delete-a-classroom

### Did the test fail after an automatic rerun?

Test failed once and then passed after an automatic rerun

### Did the test fail when running on desktop, mobile, or both?

Mobile

### Stacktrace

```shell
FAIL core/tests/puppeteer-acceptance-tests/specs/curriculum-admin/create-edit-and-delete-a-classroom.spec.ts (646.457 s)
  Curriculum Admin
    ✓ should be able to create a new classroom (7909 ms)
    ✕ should be able to edit classroom information (61222 ms)
    ✓ should be able to publish classroom (14534 ms)
    ✓ should be able to enable diagnostic test for a classroom (13962 ms)
    ✓ should be able to change order of classrooms (35971 ms)
    ✓ should be able to delete a classroom (7607 ms)

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
Snapshots:   0 total
Time:        648.107 s, estimated 763 s
Ran all test suites matching /core\/tests\/puppeteer-acceptance-tests\/specs\/curriculum-admin\/create-edit-and-delete-a-classroom.spec.ts/i.
```

### Screenshots and/or Screen Recordings

[acceptance_test_curriculum-admin_create-edit-and-delete-a-classroom_mobile_original.log](https://github.com/user-attachments/files/25316855/acceptance_test_curriculum-admin_create-edit-and-delete-a-classroom_mobile_original.log)

### Occurrences

https://github.com/oppia/oppia/actions/runs/21930509067/job/63388383847

### Additional Information

_No response_

### Debugging document link

_No response_

---

## #24919: [E2E/Acceptance CI Failure]: Acceptance (exploration-creator/exploration-feedback)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

Run Desktop Acceptance Test exploration-creator/exploration-feedback Re-run Desktop Acceptance Test to check flakiness for exploration-creator/exploration-feedback Run Mobile Acceptance Test exploration-creator/exploration-feedback Re-run Mobile Acceptance Test to check flakiness for exploration-creator/exploration-feedback

### Did the test fail after an automatic rerun?

Test failed once, was automatically re-run, and then failed again

### Did the test fail when running on desktop, mobile, or both?

Desktop, Mobile

### Stacktrace

```shell
FAIL core/tests/puppeteer-acceptance-tests/specs/exploration-creator/exploration-feedback.spec.ts (124.153 s)
  Exploration Editor
    ✕ should be able to give exploration feedback

  ● Exploration Editor › should be able to give exploration feedback

    TimeoutError: Element <li.nav-item.icon.nav-list-item.e2e-test-feedback-tab> "0" took too long to be clickable.
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
      at BaseUser.navigateToFeedbackTab (utilities/user/exploration-editor.ts:2744:7)
      at specs/exploration-creator/exploration-feedback.spec.ts:38:5

Test Suites: 1 failed, 1 total
Tests:       1 failed, 1 total
Snapshots:   0 total
Time:        125.893 s
Ran all test suites matching /core\/tests\/puppeteer-acceptance-tests\/specs\/exploration-creator\/exploration-feedback.spec.ts/i.
```

### Screenshots and/or Screen Recordings

https://github.com/user-attachments/assets/5aa82721-2cce-4f04-8dd9-161130d0a530

### Occurrences

https://github.com/oppia/oppia/actions/runs/21971840472/job/63522154644

### Additional Information

_No response_

### Debugging document link

_No response_

---

## #24915: [BUG]: Pre-push hook incorrectly runs acceptance test specs in frontend unit test runner

**Labels:** triage needed, bug

### Describe the bug

The pre-push hook incorrectly attempts to run acceptance test spec files located under:

core/tests/puppeteer-acceptance-tests/specs/

using the frontend unit test runner (Karma).

This happens because scripts/run_frontend_tests.py() treats all .spec.ts files as frontend unit tests without excluding the puppeteer-acceptance-tests directory.

As a result, Karma executes 0 tests and the push fails.

### URL of the page where the issue is observed.

N/A

### Steps To Reproduce

1) Modify any acceptance test file under:
core/tests/puppeteer-acceptance-tests/specs/

2) Run:
git push

3) Observe pre-push hook failure due to Karma attempting to run acceptance specs

### Expected Behavior

Acceptance test specs should be excluded from the frontend unit test runner.

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

## #24914: [E2E/Acceptance CI Failure]: Timeout error in  Full-stack tests / Acceptance (exploration-creator/create-an-exploration-with-all-interactions)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

 Full-stack tests / Acceptance (exploration-creator/create-an-exploration-with-all-interactions) 

### Did the test fail after an automatic rerun?

Test failed once, was automatically re-run, and then failed again

### Did the test fail when running on desktop, mobile, or both?

Desktop

### Stacktrace

```shell
INFO     2026-02-12 07:26:53,842 module.py:830] default: "GET /internetconnectivityhandler HTTP/1.1" 200 36
[test-log] 26:55.135: Screen recording stopped for explorationEditor.
INFO     2026-02-12 07:26:55,151 module.py:830] default: "GET /third_party/generated/webfonts/fa-solid-900.woff2 HTTP/1.1" 304 -
[test-log] 26:55.719: Screenshot captured for test failure and saved as : /home/runner/work/oppia/oppia_full_stack_test_failure_screenshots/acceptance/exploration-creator_create-an-exploration-with-all-interactions-2026-02-12T07_26_55.136Z-instance-0.png
[test-log] 26:55.719: All screenshots captured for explorationEditor
[test-log] 26:55.838: Browser closed for explorationEditor.
[test-log] 26:55.838: All browsers closed.
FAIL core/tests/puppeteer-acceptance-tests/specs/exploration-creator/create-an-exploration-with-all-interactions.spec.ts (927.462 s)
  Exploration Editor
    ✓ should be able to use "Continue Button" interaction (26910 ms)
    ✓ should be able to use "Multiple Choice" interaction (35987 ms)
    ✓ should be able to use "Number Input" interaction (34276 ms)
    ✓ should be able to use "Text Input" interaction (32017 ms)
    ✓ should be able to use "Image Region" interaction (34997 ms)
    ✓ should be able to use "Item Selection" interaction (36614 ms)
    ✓ should be able to use "Drag and Drop Sort" interaction (28802 ms)
    ✓ should be able to use "Fraction Input" interaction (32427 ms)
    ✓ should be able to use "Graph Theory" interaction (106985 ms)
    ✓ should be able to use "Set Input" interaction (34788 ms)
    ✓ should be able to use "Numeric Expression" interaction (48999 ms)
    ✕ should be able to use "Algebric Expression" intreaction (67085 ms)
    ✕ should be able to use "Math Equation" interaction (40618 ms)
    ✕ should be able to use "Number With Units" interaction (40612 ms)
    ✕ should be able to use "Ratio Expression Input" interaction (40616 ms)
    ✕ should be able to use "Code Editor" interaction (40615 ms)
    ✕ should be able to use "Pencil Code Editor" interaction (40917 ms)
    ✕ should be able to use "Music Notes Input" interaction (40617 ms)
    ✕ should be able to use "World Map" interaction (40615 ms)

  ● Exploration Editor › should be able to use "Algebric Expression" intreaction

    TimeoutError: Element <div.oppia-rte-resizer.oppia-rte.e2e-test-rte.cke_editable.cke_editable_inline.cke_contents_ltr.cke_show_borders> took too long to be clickable.
    Original Error:
    waiting for function failed: timeout 30000ms exceeded

      492 |         : selector;
      493 |     try {
    > 494 |       await this.page.waitForFunction(is

*[truncated]*

---

## #24911: [BUG]: Error in Blog page

**Labels:** triage needed, bug

### Describe the bug

1. Error message shown in Blog page. The "Latest Posts” on the left, with the blog title, author name, publish time, related tags showing on each blog card are not shown. 
2. Search bar for tags is not shown.


### URL of the page where the issue is observed.

https://www.oppiatestserver.org/blog

### Steps To Reproduce

1. Select “About” -> “Blog” from the top navbar.
2. The "Latest Posts” on the left, with the blog title, author name, publish time, related tags showing on each blog card are not shown. 
3. Search bar for tags is not shown.


### Expected Behavior

The "Latest Posts” on the left, with the blog title, author name, publish time, related tags showing on each blog card should be shown.
Search bar for tags should be shown.


### Screenshots/Videos

<img width="960" height="598" alt="Image" src="https://github.com/user-attachments/assets/90b305e2-28b8-4256-acd5-cd1d5502d08b" />

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

## #24905: [CI Failure]: ModuleNotFoundError: No module named 'psutil'

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Frontend

### Which CI step failed?

Acceptance (logged-out-learner/complete-the-embedded-lesson)

### Stacktrace

```shell
Prepare all required actions
Getting action download info
Run ./.github/actions/run-a-specific-acceptance-test
Run if [[ ! "" =~ ^[a-zA-Z0-9_-]*$ ]]; then
Run set -o pipefail; VIDEO_RECORDING_IS_ENABLED=1 xvfb-run -a --server-args="-screen 0, 1920x1080x24" python -m scripts.run_acceptance_tests --skip_build --suite=logged-out-learner/complete-the-embedded-lesson --mobile --prod_env --server_log_level=info | tee acceptance_test_.log
Traceback (most recent call last):
  File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/home/runner/work/oppia/oppia/scripts/run_acceptance_tests.py", line 26, in <module>
    from scripts import build, common, servers
  File "/home/runner/work/oppia/oppia/scripts/build.py", line 31, in <module>
    from scripts import (
  File "/home/runner/work/oppia/oppia/scripts/servers.py", line 33, in <module>
    import psutil
ModuleNotFoundError: No module named 'psutil'
Error: Process completed with exit code 1.
```

### Screenshots / Screen Recordings

_No response_

### Occurrences

occurred at  : https://github.com/oppia/oppia/actions/runs/21959286869/job/63468815410?pr=24882#logs 

### Additional Information

_No response_

### Debugging document link

_No response_

---

## #24902: [BUG]: When we click on “Read more stories” in partnerships page, error message is shown.

**Labels:** triage needed, bug

### Describe the bug

When we click on “Read more stories” in partnerships page, error message is shown. 

### URL of the page where the issue is observed.

https://www.oppiatestserver.org/blog

### Steps To Reproduce

1. Click on 'Get Involved' in oppiatestserver.org page
2. Click on 'Schools and Organizations' in the navbar
3. Click on “Read more stories”.

### Expected Behavior

The error message 'Failed to get blog home page data.Error: User not found' should not show.

### Screenshots/Videos

https://github.com/user-attachments/assets/2daac6b4-1999-4a82-a488-0c08087af0a8

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

## #24899: [Feature Request]: Upgrade ElasticSearch from 8.17 to 9.X

**Labels:** triage needed, enhancement

### Is your feature request related to a problem? Please describe.

ElasticSearch we are using, 8.17, is reaching end-of-life and that, for continued support, we would need to upgrade to the latest 9.x version.

![Image](https://github.com/user-attachments/assets/eb23fea3-92bd-4290-a93c-3f88d8167c22)

### Describe the solution (or solutions) you'd like

N/A

### Describe alternatives you've considered and rejected

_No response_

### Additional context

Please take reference from this PR: https://github.com/oppia/oppia/pull/23596
especially the testing doc.

---

## #24898: [BUG]: Lesson Info page  - Learner is not able to see all the contributors of the lesson

**Labels:** triage needed, bug

### Describe the bug

Lesson Info page - When hovering over the Contributors icon, learner can see the number of contributors and the tooltip indicates multiple contributors(partial list is visible). However, the full list of contributor names is not completely visible to the learner. Some names appear truncated or hidden. As a result, the learner cannot view or click on certain contributors, which prevents them from subscribing to a specific contributor.

### URL of the page where the issue is observed.

https://www.oppiatestserver.org/explore/G8ZgSj1O4rjE?story_url_fragment=piece-of-cake&topic_url_fragment=fractionsssssssss&classroom_url_fragment=math&node_id=node_1

### Steps To Reproduce

1. Load the URL https://www.oppiatestserver.org/learner-dashboard
2. Hover on the "Learn" tab of the nav bar
3. Click on any topic
4. Click a Chapter (Preferably which has more contributors)--> Click on the Lesson info on the left bottom corner '
5. In the Pop up window hover on the contributors icon 

### Expected Behavior

All contributor names should be fully visible and clickable so learners can subscribe to a specific contributor.

### Screenshots/Videos

https://github.com/user-attachments/assets/7e797c36-5e37-43c7-a8b9-5a519dc2e3b5

### What device are you using?

Desktop

### Operating System

Windows

### What browsers are you seeing the problem on?

Chrome

### Browser version

_No response_

### Additional context

 Environment Hat: Slow Connection

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #24885: [E2E/Acceptance CI Failure]: Acceptance (logged-in-learner/manage-goals-in-learner-dashboard)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

Run Mobile Acceptance Test logged-in-learner/manage-goals-in-learner-dashboard

### Did the test fail after an automatic rerun?

Test failed once and then passed after an automatic rerun

### Did the test fail when running on desktop, mobile, or both?

Mobile

### Stacktrace

```shell
FAIL core/tests/puppeteer-acceptance-tests/specs/logged-in-learner/manage-goals-in-learner-dashboard.spec.ts (1082.474 s)
  Logged-In Learner - Manage Goals
    ✓ should display empty Goals tab with title and Add Goals button (18161 ms)
    ✓ should open add goals modal with topic checkbox and cancel (9792 ms)
    ✓ should add Place Values goal and display In Progress card (0%) (13222 ms)
    ✓ should prompt for goal removal when unchecked in modal (13331 ms)
    ✓ should return to empty state after removal (4294 ms)
    ✓ should not save checkbox selection when closing modal (7362 ms)
    ✓ should show goal card with 0% and Start button after adding goal (22072 ms)
    ✓ should expand Place Values and show all lessons with Start buttons (12539 ms)
    ✕ should highlight Goals tab in sidebar (11811 ms)

  ● Logged-In Learner - Manage Goals › should highlight Goals tab in sidebar

    Expected image to match or be a close match to snapshot but was 4.800999500249875% different from snapshot (48034 differing pixels).
    See diff for details: /home/runner/work/oppia/oppia/core/tests/puppeteer-acceptance-tests/logged-in-learner/manage-goals-in-learner-dashboard/prod-mobile-screenshots/diff-snapshots/goalsTabSidebarHighlighted-diff.png
    Download the artifact folder diff-snapshots from the github workflow to check the difference between the old screenshot(s) and the new one(s). To download the folder, go to "Summary" of the CI Job of the PR and find the "Artifacts" section. The artifact folder name should be something like diff-snapshots_(suite-name)_desktop_original. The diff screenshot(s) should end with "-diff".
    Please update the screenshots if the UI changed. If screenshot comparisons consistently show the same difference percentage across multiple test runs, the baseline screenshot(s) should be updated.
    To update the screenshots(s), you should run the tests in CI, download the artifact folder new-snapshots from the github workflow and use the screenshots in that folder to replace the old one(s).
    To download the folder, go to "Summary" of the CI Job of the PR and find the "Artifacts" section. The artifact folder name should be something like new-snapshots_(suite-name)_desktop_original. The new screenshot(s) should end with "-received". When replacing the screenshot(s), make sure to change the postfix "-received" to "-snap".

      1126 |         ' folder name should be something like new-snapshots_(suite-name)_desktop_original.' +
      1127 |         ' The new screenshot(s) should end with "-received". When replacing the screenshot(s), make sure to change the postfix "-received" to "-snap".';
   

*[truncated]*

---

## #24884: [E2E/Acceptance CI Failure]: Acceptance (practice-question-reviewer/view-contribution-stats-and-badges-earned)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

Run Desktop Acceptance Test practice-question-reviewer/view-contribution-stats-and-badges-earned

### Did the test fail after an automatic rerun?

Test failed once, was automatically re-run, and then failed again

### Did the test fail when running on desktop, mobile, or both?

Desktop, Mobile

### Stacktrace

```shell
FAIL core/tests/puppeteer-acceptance-tests/specs/practice-question-reviewer/view-contribution-stats-and-badges-earned.spec.ts (391.567 s)
  Practice Question Reviewer
    ✕ should be able to check contribution stats
    ✕ should be able to check badges earned

  ● Practice Question Reviewer › should be able to check contribution stats

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

  ● Practice Question Reviewer › should be able to check badges earned

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
      at Page.waitForFunction (../../../node_modules/puppeteer/src/common/Page.ts:3358:2

*[truncated]*

---

## #24883: [Feature Request]: Removing oppia-lightweight-root entrypoint .

**Labels:** enhancement

### Is your feature request related to a problem? Please describe.

Currently Oppia is using oppia-lightweight-root entrypoint in order to build the oppia splash page . The problem is it is acting as a blocker in the case of remove webpack project , as custom inbuild webpack which we are trying to shift to , will require only one entrypoint . 

### Describe the solution (or solutions) you'd like

Removing the entire lightweight root and making sure that the splash page  is made using the oppia-root entry point 

### Describe alternatives you've considered and rejected

_No response_

### Additional context

_No response_

---

## #24881: [E2E/Acceptance CI Failure]: Acceptance (exploration-editor/verify-statistics-and-previous-explorations)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

Run Desktop Acceptance Test exploration-editor/verify-statistics-and-previous-explorations

### Did the test fail after an automatic rerun?

Test failed once and then passed after an automatic rerun

### Did the test fail when running on desktop, mobile, or both?

Desktop

### Stacktrace

```shell
FAIL core/tests/puppeteer-acceptance-tests/specs/exploration-editor/verify-statistics-and-previous-explorations.spec.ts (289.175 s)
  Exploration Editor
    ✕ should display created explorations and their statistics on the creator dashboard after creating, playing, and rating as a logged-in user (1 ms)

  ● Exploration Editor › should display created explorations and their statistics on the creator dashboard after creating, playing, and rating as a logged-in user

    TimeoutError: Navigation timeout of 30000 ms exceeded

      at ../../../node_modules/puppeteer/src/common/LifecycleWatcher.ts:211:18
```

### Screenshots and/or Screen Recordings

https://github.com/user-attachments/assets/acce1045-f29d-4a31-a8be-bcb5bc5abbbb

### Occurrences

https://github.com/oppia/oppia/actions/runs/21726992294/job/62716902769

### Additional Information

_No response_

### Debugging document link

_No response_

---

## #24878: [CI Failure]: Lighthouse CI check failed: modern-image-formats failure for maxLength assertion

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Lighthouse CI performance

### Which CI step failed?

Lighthouse perf (shard 1)

### Stacktrace

```shell
Return code: 1
ERROR:
Checking assertions against 2 URL(s), 6 total run(s)

1 result(s) for http://localhost:8181/topic_editor/CaA00xoNbzmo :

  ✘  modern-image-formats failure for maxLength assertion
       Serve images in next-gen formats
       https://web.dev/uses-webp-images/

        expected: <=0
           found: 1
      all values: 1, 1, 1

Assertion failed. Exiting with status code 1.
assert command failed. Exiting with status code 1.

Lighthouse checks failed. More details can be found above.
Stopping GAE Development Server(name="sh", pid=3785)...
Stopping Cloud Datastore Emulator(name="sh", pid=3671)...
Stopping Firebase Emulator(name="sh", pid=3646)...
Stopping ElasticSearch Server(name="sh", pid=3497)...
Stopping Redis Server(name="sh", pid=3490)...
Error: Process completed with exit code 1.
```

### Screenshots / Screen Recordings

_No response_

### Occurrences

https://github.com/oppia/oppia/actions/runs/21903543361/job/63313273177

### Additional Information

_No response_

### Debugging document link

_No response_

---

## #24877: [BUG]: Voiceover Upload - Error message Contains Extra Information (Schema validation for 'raw_audio_file' failed)

**Labels:** triage needed, bug

### Describe the bug

Voiceover Upload - Error message Contains Extra Information:

 At 'https://www.oppiatestserver.org/createhandler/audioupload/EyJ180bShWrI' these errors are happening: Schema validation for 'raw_audio_file' failed: Audio not recognized as a mp3 file


### URL of the page where the issue is observed.

https://www.oppiatestserver.org/create/EyJ180bShWrI#/translation/Introduction

### Steps To Reproduce

1. As a voice over artist, navigate to an exploration/ translation Tab
2. Select English as Voiceover Language Code and Voiceover Language Code
3. Click "Add manual voiceover"
4. Submit a file over 5min
5. Click "Save"


### Expected Behavior

Clear message is displayed to user:
Audio files must be under 300 seconds in length. The uploaded file is 330.03 seconds long.

### Screenshots/Videos

<img width="1280" height="738" alt="Image" src="https://github.com/user-attachments/assets/aebe02c2-686c-41d1-a1aa-a4563a5907f7" />

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

## #24876: [BUG]: Remove files once Job is run on test server

**Labels:** triage needed, bug

### Describe the bug

The Beam Job and Audit Job mentioned in the PRs were created to fix a specific bug. Once these jobs are run on the test server and the bug is resolved, the corresponding files and all references to them in the codebase should be deleted, as they are no longer needed.

PR : 
- https://github.com/oppia/oppia/pull/24004
- https://github.com/oppia/oppia/pull/23575



### URL of the page where the issue is observed.

N/A

### Steps To Reproduce

N/A

### Expected Behavior

N/A

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

_No response_

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #24871: [Feature Request]: Add collapsible search panel to improve blog page layout and visual consistency

**Labels:** triage needed, enhancement

### Is your feature request related to a problem? Please describe.

On the Blog page, the search panel on the right occupies a fixed column width even when it is not actively used. This results in a large blank white space below the search bar, making the page look visually unbalanced and less aesthetic, especially when scrolling through blog posts.

This unused space gives the impression that the layout is broken or incomplete and reduces the effective content area for blog posts.

### Describe the solution (or solutions) you'd like

Introduce a collapsible search panel on the Blog page with the following behavior:
- A toggle button (e.g., “Search” / filter icon) to expand or collapse the search panel.
- When the search panel is collapsed:
  - The blog posts should expand horizontally and utilize the full available width
  - The layout should feel more content-focused and visually balanced.
- When the search panel is expanded:
  - The current two-column layout should remain intact.
  - Blog posts should align vertically, as they do now, alongside the search panel.

### Describe alternatives you've considered and rejected

_No response_

### Additional context

<img width="3014" height="1792" alt="Image" src="https://github.com/user-attachments/assets/a33528aa-5356-4f3c-8edd-a58aa699636d" />

<img width="2414" height="1450" alt="Image" src="https://github.com/user-attachments/assets/9d2b3e3f-eb6a-4059-9a77-41ae605cbadb" />

---

## #24870: [BUG]: Pagination shows confusing background circle instead of highlighting active page

**Labels:** triage needed, bug

### Describe the bug

In the blog pagination:

- A background circle appears behind the ellipsis/dots (...) instead of the active page number.
- The current page number is not clearly highlighted, which makes the pagination state confusing.
- This can mislead users into thinking the dots represent the active page.

### URL of the page where the issue is observed.

https://www.oppia.org/blog

### Steps To Reproduce

- Open https://www.oppia.org/ in a web browser.
- From the top navigation bar, click on the About dropdown menu.
- Select Blog to navigate to the blog listing page.
- Use the pagination controls to move to a page beyond Page 2 (e.g., Page 3 or later).
- Observe the pagination component and note how the background circle appears behind the ellipsis (...) instead of clearly highlighting the active page number.

### Expected Behavior

The pagination component should clearly highlight the current active page number only so users can easily understand which page they are on.

- Highlight the active page number instead of the ellipsis.
- Remove the background circle behind the dots.



### Screenshots/Videos

<img width="2306" height="1392" alt="Image" src="https://github.com/user-attachments/assets/5ef1ca08-db8c-49f8-8c2d-6acf87adf9eb" />

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

## #24859: [E2E/Acceptance CI Failure]: Acceptance (logged-out-user/sign-in-and-save-exploration-progress)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

E2E

### Which CI step failed?

Run Desktop Acceptance Test logged-out-user/sign-in-and-save-exploration-progress

### Did the test fail after an automatic rerun?

Test failed once but was not automatically re-run

### Did the test fail when running on desktop, mobile, or both?

Desktop

### Stacktrace

```shell
[test-log] 10:24.725: Checking if element <span.mat-button-wrapper> "Sign In" is clickable...
INFO     2026-02-11 01:10:24,910 module.py:830] default: "GET /third_party/generated/webfonts/fa-solid-900.woff2 HTTP/1.1" 304 -
[test-log] 10:24.933: Element (text: Sign In) clicked.
ERROR:root:Frontend error: 
Error: A network error (such as timeout, interrupted connection or unreachable host) has occurred.

    at URL: http://localhost:8181/login?return_url=%2F
INFO     2026-02-11 01:10:25,059 module.py:830] default: "POST /frontend_errors HTTP/1.1" 200 30
[test-log] 10:54.537: Test failed: Capturing screenshots...
[test-log] 10:54.538: Closing browsers for 0 users.
[test-log] 10:54.538: All browsers closed.
FAIL core/tests/puppeteer-acceptance-tests/specs/logged-out-user/sign-in-and-save-exploration-progress.spec.ts (54.578 s)
  Logged-out User
    ✕ should be able to play the exploration without signing in, sign in at any point, save progress, and clear progress

  ● Logged-out User › should be able to play the exploration without signing in, sign in at any point, save progress, and clear progress

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
      at specs/logged-out-user/sign-in-and-save-exploration-progress.spec.ts:51:25

Test Suites: 1 failed, 1 total
Tests:       1 failed, 1 total
Snapshots:   0 total
Time:        56.362 s
Ran all test suites matching /core\/tests\/puppeteer-acceptance-tests\/specs\/logged-out-user\/sign-in-and-save-exploration-progress.spec.ts/i.
INFO     2026-02-11 01:10:54,629 shutdown.py:48] Shutting down.
Error: 2-11 01:10:54 +0000] [2857] [ERROR] Worker (pid:2866) was sent SIGTERM!
Error: 2-11 01:10:54 +0000] [2853] [ERROR] Worker (pid:2863) was sent SIGTERM!
INFO     2026-02-11 01

*[truncated]*

---

## #24858: [BUG]: Blog Home Page Fails to Load – "User not found" Error

**Labels:** triage needed, bug

### Describe the bug

When accessing the Blog Home Page, the system displays the error: "**Failed to get blog home page data. Error: User not found**."

### URL of the page where the issue is observed.

https://www.oppiatestserver.org/blog

### Steps To Reproduce

- Navigate to the Blog Home Page

- Observe the error message displayed

- Page content does not load

### Expected Behavior

Page content should be loaded properly



### Screenshots/Videos

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/03e60b60-7d91-42c1-82af-e234cb0d3b56" />

### What device are you using?

Desktop

### Operating System

Windows

### What browsers are you seeing the problem on?

Chrome

### Browser version

_No response_

### Additional context

Observed in Oppia Main server as well

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #24856: [BUG]: Category Drop down mismatch - Dropdown options which are available while publishing the exploration are not available in the community library page.

**Labels:** triage needed, bug

### Describe the bug

Category Drop down mismatch - Drop down options which are available while publishing the exploration are not available in the community library page to be used as a search category.

### URL of the page where the issue is observed.

https://www.oppiatestserver.org/search/find?q=&language_code=(%22en%22)

### Steps To Reproduce

1. Load the URL https://www.oppiatestserver.org/creator-dashboard
2. Click on create an exploration
3. Create an exploration successfully 
4. Save the exploration
5. Click on publish exploration
6. Observe and make a note of the categories available to choose 
7. Publish the exploration successfully 
8. Navigate to "Community library page"
9. Locate and click on the category drop down menu and look for all the drop down options available 

Note:
Behavioral Hat: Slow connection  

### Expected Behavior

All the drop down options available while publishing the exploration should also be made available in the community library page. 

### Screenshots/Videos

<img width="960" height="504" alt="Image" src="https://github.com/user-attachments/assets/cce2b6fc-c31f-4c1f-828f-5bc8af42db8d" />
<img width="960" height="504" alt="Image" src="https://github.com/user-attachments/assets/e4d4a0e7-6516-44e3-afed-aab804768397" />

### What device are you using?

Desktop

### Operating System

Windows

### What browsers are you seeing the problem on?

Chrome

### Browser version

_No response_

### Additional context

Note:
Behavioral Hat: Slow connection  

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #24855: Use official type hints for the Firebase Admin SDK python package

**Labels:** triage needed, enhancement

### Is your feature request related to a problem? Please describe.

The Firebase Admin SDK does not provide strong types, meaning our code fails MyPy checks with `Any` type errors. This makes it difficult for our developers to use the library consistently, correctly, and intentionally.

### Describe the solution (or solutions) you'd like

We should use the official type hint solution published by the Firebase Admin SDK: firebase/firebase-admin-python#569.

### Describe alternatives you've considered and rejected

- **[CURRENT WORKAROUND]:** Maintain a partial stub of the SDK on our own.
- The [`types-firebase-admin`](https://pypi.org/project/types-firebase-admin/) on PyPi is no longer maintained and the repository no longer exists. The most-recent publication of the package provides weaker type hints than our hand-written stubs.

### Additional context

Oppia's type stubs for the Firebase Admin SDK can be found here: https://github.com/oppia/oppia/tree/develop/stubs/firebase_admin/

---

## #24846: [E2E/Acceptance CI Failure]: Timeout error in Acceptance (logged-out-user/play-through-lesson-while-getting-feedback-and-hints)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

Acceptance (logged-out-user/play-through-lesson-while-getting-feedback-and-hints)

### Did the test fail after an automatic rerun?

Test failed once, was automatically re-run, and then failed again

### Did the test fail when running on desktop, mobile, or both?

Desktop

### Stacktrace

```shell
L core/tests/puppeteer-acceptance-tests/specs/logged-out-user/play-through-lesson-while-getting-feedback-and-hints.spec.ts (128.931 s)
  Logged-out User
    ✕ should be able to interact with different interactions,receive feedback, navigates through cards, uses hints, views previous responses, and reaches a checkpoint

  ● Logged-out User › should be able to interact with different interactions,receive feedback, navigates through cards, uses hints, views previous responses, and reaches a checkpoint

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
```

### Screenshots and/or Screen Recordings

https://github.com/user-attachments/assets/09ed3843-3519-4f8e-a8f5-7639a3621564

https://github.com/user-attachments/assets/33c462e7-438a-427b-9f0d-19553991b115

### Occurrences

https://github.com/oppia/oppia/actions/runs/21856179044?pr=24702

10 Feb 2026

### Additional Information

_No response_

### Debugging document link

_No response_

---

## #24845: [E2E/Acceptance CI Failure]: practice-question-reviewer/review-submitted-question (should be able to review the submitted questions)

**Labels:** triage needed, bug, CI breakage

### CI Test Type

Acceptance

### Which CI step failed?

  ● Practice Question Reviewer › should be able to review the submitted questions

### Did the test fail after an automatic rerun?

Test failed once, was automatically re-run, and then failed again

### Did the test fail when running on desktop, mobile, or both?

Mobile, Desktop

### Stacktrace

```shell
INFO     2026-02-09 22:31:00,419 module.py:830] default: "GET /internetconnectivityhandler HTTP/1.1" 200 36
INFO     2026-02-09 22:31:03,916 module.py:830] default: "GET /internetconnectivityhandler HTTP/1.1" 200 36
[browser-log] 31:04.011: [debug]: Document state:
  - readyState: complete
  - styleSheets loaded: 54
  - pending stylesheets: 1
  - viewport: 375x667
[browser-log] 31:04.011: [debug]: Element DIV is disabled: false
[browser-log] 31:04.012: [debug]: Element DIV is in viewport: true, true
[browser-log] 31:04.012: [debug]: Element DIV
Dimensions: 11, 242.59375, 337, 72
Center point: 179.5, 278.59375
[browser-log] 31:04.012: [debug]: Element DIV overlapping elements found: 2
Overlapping element: BUTTON (class="btn oppia-welcome-modal-button oppia-transition-200 e2e-test-dismiss-welcome-modal")
Overlapping rect: BUTTON (class="btn oppia-welcome-modal-button oppia-transition-200 e2e-test-dismiss-welcome-modal")
[browser-log] 31:04.014: [debug]: Checking overlap for DIV (class="oppia-editable-section-mask e2e-test-state-edit-content")
Overlapping elements to check: 2
[browser-log] 31:04.014: [debug]: Overlapping element BUTTON (class="btn oppia-welcome-modal-button oppia-transition-200 e2e-test-dismiss-welcome-modal")
  - Is same element: false
  - Is contained by target: false
  - Contains target: false
[browser-log] 31:04.014: [debug]: Overlapping element BUTTON (class="btn oppia-welcome-modal-button oppia-transition-200 e2e-test-dismiss-welcome-modal")
  - Is same element: false
  - Is contained by target: false
  - Contains target: false
[browser-log] 31:04.014: [debug]: Element DIV shadow elements: 0
[browser-log] 31:04.014: [debug]: Document state:
  - readyState: complete
  - styleSheets loaded: 54
  - pending stylesheets: 1
  - viewport: 375x667
[browser-log] 31:04.014: [debug]: Element DIV is disabled: false
[browser-log] 31:04.014: [debug]: Element DIV is in viewport: true, true
[browser-log] 31:04.015: [debug]: Element DIV
Dimensions: 11, 242.59375, 337, 72
Center point: 179.5, 278.59375
[browser-log] 31:04.015: [debug]: Element DIV overlapping elements found: 2
Overlapping element: BUTTON (class="btn oppia-welcome-modal-button oppia-transition-200 e2e-test-dismiss-welcome-modal")
Overlapping rect: BUTTON (class="btn oppia-welcome-modal-button oppia-transition-200 e2e-test-dismiss-welcome-modal")
[browser-log] 31:04.015: [debug]: Checking overlap for DIV (class="oppia-editable-section-mask e2e-test-state-edit-content")
Overlapping elements to check: 2
[browser-log] 31:04.015: [debug]: Overlapping element BUTTON (class="btn oppia-welcome-modal-button oppia-transition-200 e2e

*[truncated]*

---

## #24840: [BUG]: Community Library - Category drop down is not displayed properly - UI is partially cut off on page load

**Labels:** triage needed, bug

### Describe the bug

Community Library - Category drop down is not displayed properly - UI  is partially cut off on page load.

Note: Behavioural Hat: "Slow Connection"

### URL of the page where the issue is observed.

https://www.oppiatestserver.org/search/find?q=just&language_code=(%22en%22)

### Steps To Reproduce

1. Load the URL https://www.oppiatestserver.org/search/find?q=just&language_code=(%22en%22)
2. Login as a learner
3. Navigate to the community library page
4. Locate the 'category' drop down menu
5. Click on it without scrolling down the page

### Expected Behavior

Drop down UI can be made more visible or can be displayed in a better way to make the option visible to the user

### Screenshots/Videos

<img width="960" height="504" alt="Image" src="https://github.com/user-attachments/assets/a3661dbe-fcf5-4511-961a-6f67e7fbbae7" />
<img width="960" height="504" alt="Image" src="https://github.com/user-attachments/assets/e74f1185-8b87-4015-bdd2-815402e6e09e" />

### What device are you using?

Desktop

### Operating System

Windows

### What browsers are you seeing the problem on?

Chrome

### Browser version

_No response_

### Additional context

Note: Behavioural Hat: "Slow Connection"

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #24839: [BUG]: Community Library - Search results are not matching with the search term

**Labels:** triage needed, bug

### Describe the bug

Community Library - Search results are not matching with the search term. 
Exploration which are not matching with the search term is listed in the community library page.
Neither the Title of the exploration nor the goal of the exploration has the search term in it. 

### URL of the page where the issue is observed.

https://www.oppiatestserver.org/search/find?q=just&language_code=(%22en%22)

### Steps To Reproduce

1. Load the URL https://www.oppiatestserver.org/search/find?q=just&language_code=(%22en%22)
2. Login as a learner
3. Navigate to the community library page 
4. Search for an exploration by entering a key

Note: Behavioural Hat: "Slow Connection"

Exploration which are not matching with the search term is listed in the community library page.
Attaching the screen recording for reference.

### Expected Behavior

Exploration whose "Title" and/or "Goal" matching with the search term should be displayed.

### Screenshots/Videos

<!-- Failed to upload "SearchFuntionality-Irrelevant.mp4" -->

### What device are you using?

Desktop

### Operating System

Windows

### What browsers are you seeing the problem on?

Chrome

### Browser version

_No response_

### Additional context

Note: Behavioural Hat: "Slow Connection"

### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #24834: [Feature Request]: Add acceptance test for Blog Post search by body content

**Labels:** triage needed, enhancement

### Is your feature request related to a problem? Please describe.

Currently, the Acceptance Test suite for the Blog Pages (core/tests/puppeteer-acceptance-tests/specs/logged-out-user/view-and-search-blog-posts.spec.ts) covers basic functionality like tag filtering and pagination.

However, there is a missing test case for the search bar functionality. We need to verify that a user can successfully find a blog post by searching for a unique keyword that appears only in the body of the post (and not in the title). This ensures the search index is correctly parsing and retrieving the full content of the posts.

### Describe the solution (or solutions) you'd like

Update the existing acceptance test file core/tests/puppeteer-acceptance-tests/specs/logged-out-user/view-and-search-blog-posts.spec.ts to include this scenario.

The test should perform the following steps:

Create and publish a new blog post containing a unique keyword in the body.

Perform a search query using that unique keyword.

### Describe alternatives you've considered and rejected

_No response_

### Additional context

_No response_

---

## #24829: [Feature Request]: Add visual indicator for End Exploration interaction in editor preview

**Labels:** triage needed, bug

### Is your feature request related to a problem? Please describe.

Currently, the "End Exploration" interaction shows no visual representation in the exploration editor preview. When adding this interaction to a card, the interaction area appears completely empty. Unlike other interactions (Continue, Multiple Choice, etc.) that display preview UI in the editor, End Exploration leaves creators with an empty container, which can be confusing and makes it difficult to verify that the interaction was added correctly.

### Describe the solution (or solutions) you'd like
Add a visual indicator or placeholder in the editor preview for the End Exploration interaction. This could be:

- A simple text message like "End of Exploration"
-  A mock button showing "Finish" or similar
- Any visual element that makes it clear the interaction is present and functioning

### Describe alternatives you've considered and rejected
No response

### Additional context

Screenshot showing the empty interaction area:
<img width="1918" height="1037" alt="Image" src="https://github.com/user-attachments/assets/1392a084-8874-490f-8765-62d20b409052" />


### Tips for developers

Before addressing the bug, please identify which PR caused the issue (you can follow the steps [here](https://github.com/oppia/oppia/wiki/How-to-find-the-commit-which-introduced-a-bug)). If you identify the PR, comment on the issue with a link to it. If not, mention the commit hash of the oldest commit you saw the bug on (and the month and year it was made in).

Then, please leave a comment with details of the approach that you plan to take to fix the issue (see [example](https://github.com/oppia/oppia/issues/19157#issuecomment-1858788463)).

**Note:** If this is your first Oppia issue, please make sure to follow our guidelines for [choosing an issue](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#choosing-a-good-first-issue) and [setting things up](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia#setting-things-up). You will also need to show a demo of the fix working correctly on your local machine. Thanks!

---

## #24827: [Feature Request]: Making the CI checks Optimized.

**Labels:** triage needed, enhancement

### Is your feature request related to a problem? Please describe.

Currently there are almost 70 PR'S and most of the CI test checking is queued because of so many PR'S . This is causing the checking of the CI test  to take a lot of time (One of my PR'S took 18 hours just to pass all the CI checks.)



### Describe the solution (or solutions) you'd like

It is expected that even if there is large number of PR'S , the CI test should run in a well optimized manner , and not take such a long time to complete the CI check for any PR. 

### Describe alternatives you've considered and rejected

_No response_

### Additional context

_No response_

---

## #24826: Error Exploration version is not set.

**Labels:** triage needed, server errors, bug

<!--
  - Before filing a new issue, please do a quick search to check that it hasn't
  - already been filed on the [issue tracker](https://github.com/oppia/oppia/issues)._
  -->

This error occurred recently in test server:

```
Frontend error: 
Uncaught (in promise): Error: Exploration version is not set.
Error: Exploration version is not set.
    at ue.init (https://www.oppiatestserver.org/build/webpack_bundles/19.bf4156ace67342de0de2.bundle.js:1:27380)
    at https://www.oppiatestserver.org/build/webpack_bundles/19.bf4156ace67342de0de2.bundle.js:1:303850
    at e.invoke (https://www.oppiatestserver.org/build/webpack_bundles/vendors~lightweight_oppia_root~oppia_root.479abbc142614449781c.bundle.js:2995:7175)
    at Object.onInvoke (https://www.oppiatestserver.org/build/webpack_bundles/vendors~lightweight_oppia_root~oppia_root.479abbc142614449781c.bundle.js:971:1770)
    at e.invoke (https://www.oppiatestserver.org/build/webpack_bundles/vendors~lightweight_oppia_root~oppia_root.479abbc142614449781c.bundle.js:2995:7115)
    at t.run (https://www.oppiatestserver.org/build/webpack_bundles/vendors~lightweight_oppia_root~oppia_root.479abbc142614449781c.bundle.js:2995:2271)
    at https://www.oppiatestserver.org/build/webpack_bundles/vendors~lightweight_oppia_root~oppia_root.479abbc142614449781c.bundle.js:3003:2717
    at e.invokeTask (https://www.oppiatestserver.org/build/webpack_bundles/vendors~lightweight_oppia_root~oppia_root.479abbc142614449781c.bundle.js:2995:7859)
    at Object.onInvokeTask (https://www.oppiatestserver.org/build/webpack_bundles/vendors~lightweight_oppia_root~oppia_root.479abbc142614449781c.bundle.js:971:1586)
    at e.invokeTask (https://www.oppiatestserver.org/build/webpack_bundles/vendors~lightweight_oppia_root~oppia_root.479abbc142614449781c.bundle.js:2995:7780)

    at URL: https://www.oppiatestserver.org/create/<ID>/preview/Introduction
```

**Where did the error occur?** https://www.oppiatestserver.org/create/<ID>/preview/Introduction

**Which release did the error occur in?** default:3-4-9-hotfix-1

**Frequency of occurrence** Once till now.

**General instructions for contributors**
In general, the procedure for fixing server errors should be the following:

- Analyze the code in the file where the error occurred and come up with a hypothesis for the reason.
- Based on your hypothesis, determine a list of steps that reliably reproduce the issue (or confirm any repro instructions that have been provided). For example, if your hypothesis is that the issue arises due to a delay in a response from the backend server, try to change the code so that the backend server always has a delay, and see if the error then shows up 100% of the time on your local machine.
- Explain your proposed fix, the logic behind it, and any other findings/context you have on this thread. You can also link to a [debugging doc](https://docs.google.com/document/d/1qRbvKjJ0A7NPVK8g6XJNISMx_6BuepoCL7F2eIfrGqM/edit) if you prefer.
- Get your approach vali

*[truncated]*

---
