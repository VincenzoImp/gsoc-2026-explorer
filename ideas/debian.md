# Debian — Project Ideas

**Source:** https://wiki.debian.org/SummerOfCode2026/Projects
**Scraped:** 2026-02-22T23:28:47.577886

---

Contents

-
[Approved Projects](https://wiki.debian.org#Approved_Projects)-
[Attack Of The Clones: Fight Back Using Code Duplication Detection from Security Patches](https://wiki.debian.org#SummerOfCode2026.2FApprovedProjects.2FAttackOfTheClonesFightBack.Attack_Of_The_Clones:_Fight_Back_Using_Code_Duplication_Detection_from_Security_Patches) -
[DebNet: Visualising the Bus Factor – Graph Analysis of Debian's Infrastructure](https://wiki.debian.org#SummerOfCode2026.2FApprovedProjects.2FDebNet:_Visualising_the_Bus_Factor_.2BIBM_Graph_Analysis_of_Debian.27s_Infrastructure.DebNet:_Visualising_the_Bus_Factor_.2BIBM_Graph_Analysis_of_Debian.27s_Infrastructure) -
[Debusine: debuginfod server](https://wiki.debian.org#SummerOfCode2026.2FApprovedProjects.2FDebusineDebuginfodServer.Debusine:_debuginfod_server) -
[Debusine: git-first development](https://wiki.debian.org#SummerOfCode2026.2FApprovedProjects.2FDebusineGitFirstDevelopment.Debusine:_git-first_development) -
[Debusine: live log streaming](https://wiki.debian.org#SummerOfCode2026.2FApprovedProjects.2FDebusineLiveLogStreaming.Debusine:_live_log_streaming) -
[Debusine: replace archive-wide reports in UDD](https://wiki.debian.org#SummerOfCode2026.2FApprovedProjects.2FDebusineReplaceUDDWorkers.Debusine:_replace_archive-wide_reports_in_UDD) -
[Debusine: usability and papercuts](https://wiki.debian.org#SummerOfCode2026.2FApprovedProjects.2FDebusineUsabilityAndPapercuts.Debusine:_usability_and_papercuts) -
[Improving Salsa CI](https://wiki.debian.org#SummerOfCode2026.2FApprovedProjects.2FImprovingSalsaCI.Improving_Salsa_CI) -
[Linux Livepatching](https://wiki.debian.org#SummerOfCode2026.2FApprovedProjects.2FLinuxLivePatching.Linux_Livepatching)

-
-
[Unapproved Projects with confirmed mentors](https://wiki.debian.org#Unapproved_Projects_with_confirmed_mentors)

The main page is at [SummerOfCode2026](/ideas/debian/summerofcode2026).


# Approved Projects


## Attack Of The Clones: Fight Back Using Code Duplication Detection from Security Patches

The clone attack where identical copies of vulnerable code are embedded across multiple executables is a distribution wide security problem. The current approach necessitates extensive tracking of code duplication and individual patching or recompiling of each affected binary, significantly increasing the complexity and overhead of security updates. As a result, ensuring timely remediation across all instances of the code becomes challenging, leaving systems more susceptible to prolonged exposure to vulnerabilities.

The goal of this project is to automate the detection of code duplication in the archive by using security patches, converting these patches into loose regex patterns, and then scanning the archive for security‑related code duplication.

**Confirmed Mentor**: Bastien Roucaries**How to contact the mentor:**[rouca+gsoc2025@debian.org](mailto:rouca+gsoc2025@debian.org)**Confirmed co-mentors:**Arnaud Valence (associate professor ESIA, Laval, France)**Difficulty level**: Medium**Project size:**350 hours (large), but useful progress can be made in 175 hours if needed**Deliverables of the project**: A proof a concept that will write attack of clone report for security team**Desirable skills**: python, git**What the intern will learn:**how to write good documentation, HTTP api, writing automatic report (template), finding bibliography, AI if needed, python programming**Application tasks:**- Extract patch metadata from debian security tracker. May need to standardization of patch annotation and writing a custom parser
- Research way to transform patch to loosely code signature using limited regex (re2) that could be used by codesearch.debian.net
- Use codesearch.debian.net to find code duplication in the archive
- write report about attack of clone found

**Related projects:**[https://hal.science/hal-05334923v1/document](https://hal.science/hal-05334923v1/document)**AI usage policy:**: We will not accept applications written using LLMs, and we expect accepted students to write code themselves, not via an LLM.


## DebNet: Visualising the Bus Factor – Graph Analysis of Debian's Infrastructure

**Description of the project:**Debian has more than 70.000 packages in the archives, which are all held together by a decentralised community of a few thousand volunteers.[?](https://wiki.debian.org/DebNet)DebNet aims to visualise the resilience of the archive by modelling the archive as a graph. You will collaborate with mentors to define specific KPIs (e.g. Bus Factor, Centrality, ...) to evaluate archive health. The goal is to identify critical packages that are abandoned or rely on too few maintainers which need more support. You will build a FastAPI application to provide all analysed data through HTTP endpoints. This project offers the chance to actively shape how we detect single points of failure within the distribution.**Confirmed Mentor**: Christian Kastner, Arian Ott**How to contact the mentor:**Christian Kastner <[ckk@debian.org](mailto:ckk@debian.org)>, Arian Ott <[arian.ott@ieee.org](mailto:arian.ott@ieee.org)>**Confirmed co-mentors:**Debian AI Team <[debian-ai@lists.debian.org](mailto:debian-ai@lists.debian.org)>**Difficulty level**: Hard**Project size:**350h**Deliverables of the project**: FastAPI backend (which does all the analytics etc.)**Desirable skills**:- Foundational knowledge of Graph Theory
- Python programming
- Basic knowledge of SQL

**What the intern will learn:**- Using Graph theory to analyse the debian archive
- Building secure and performant FastAPI applications

**Application tasks:**Solve the tasks from this repo:[https://salsa.debian.org/Arian-Ott/debnet-application-tasks](https://salsa.debian.org/Arian-Ott/debnet-application-tasks)**Related projects:**None (maybe UDD?)**AI usage Policy:**We will not accept applications written using LLMs, and we expect accepted students to write code themselves, not via an LLM.

[[SummerOfCode2026/ApprovedProjects/DebNet: Visualising the Bus Factor – Graph Analysis of Debian's Infrastructure]](https://wiki.debian.org/SummerOfCode2026/ApprovedProjects/DebNet%3A%20Visualising%20the%20Bus%20Factor%20%E2%80%93%20Graph%20Analysis%20of%20Debian%27s%20Infrastructure)

[[edit]](https://wiki.debian.org/SummerOfCode2026/ApprovedProjects/DebNet%3A%20Visualising%20the%20Bus%20Factor%20%E2%80%93%20Graph%20Analysis%20of%20Debian%27s%20Infrastructure?action=edit&backto=SummerOfCode2026%2FProjects)


## Debusine: debuginfod server

**Description of the project:** Debusine provides Debian developers and maintainers with a way to host package repositories. We would like to [support debug symbol packages](https://salsa.debian.org/freexian-team/debusine/-/issues/957) as well, serving them in a way that’s compatible with debuginfod(8). This would make it easy for users of those packages to provide meaningful backtraces in the event of crashes.

**Confirmed Mentor**: Colin Watson**How to contact the mentor:**[cjwatson@debian.org](mailto:cjwatson@debian.org)**Confirmed co-mentors:**None confirmed, but other people from the[Debusine team](https://freexian-team.pages.debian.net/debusine/reference/development-team-organization.html#current-team-organization)can help if needed.**Difficulty level**: Hard**Project size:**175 hours (medium)**Deliverables of the project**:Debusine transforms

`*-dbgsym`packages into suitable artifacts with individual elements broken out.Debusine’s archive views have

`buildid/*`endpoints compatible with debuginfod(8).`gdb`can fetch debug symbols from such repositories, and Debusine documents how to configure it to do so.

**Desirable skills**: Competent Python, basic Django and/or SQL, and the ability to read C/C++ well enough to analyze the details of what debuginfod(8) does (writing C/C++ is unlikely to be required).**What the intern will learn:**How`gdb`finds debug symbols. How a real-world repository hosting system works, and how to extend it with new features.**Application tasks:**Pick a

[Quick fix](https://salsa.debian.org/freexian-team/debusine/-/issues?sort=created_date&state=opened&label_name%5B%5D=Quick%20fix&first_page_size=100)issue from our list and try to fix it, including full test coverage for your changes.Look at

[debuginfod(8)’s web API documentation](https://manpages.debian.org/stable/debuginfod/debuginfod.8.en.html#WEBAPI)and the`elf_classify`function in[debuginfod.cxx](https://sourceware.org/git/?p=elfutils.git;a=blob;f=debuginfod/debuginfod.cxx). Prepare an initial high-level summary of what would need to be extracted from incoming debug symbol packages in order to handle the`/buildid/BUILDID/debuginfo`` endpoint.

**AI usage policy:**We will not accept applications written using LLMs, and we expect accepted students to write code themselves, not via an LLM.


## Debusine: git-first development

**Description of the project:** Many people are much more familiar with git than with Debian source package tools; even Debian developers often find the latter to be a bit of a maze. The [dgit](https://manpages.debian.org/testing/dgit/dgit.1.en.html) maintainers have been working for some time on allowing contributors to use git directly for their uploads, and [tag2upload](/ideas/debian/tag2upload) allows people to upload simply by pushing the right kind of signed tag.

However, Debusine doesn’t integrate well with this yet. Members of the Debusine and dgit teams have had some [productive design discussions](https://salsa.debian.org/freexian-team/debusine/-/issues/815), and we would like to turn some of those into reality.

**Confirmed Mentor**: Colin Watson**How to contact the mentor:**[cjwatson@debian.org](mailto:cjwatson@debian.org)**Confirmed co-mentors:**None confirmed, but other people from the[Debusine team](https://freexian-team.pages.debian.net/debusine/reference/development-team-organization.html#current-team-organization)can help if needed.**Difficulty level**: Medium**Project size:**350 hours (large), but useful progress can be made in 175 hours if needed**Deliverables of the project**:Debusine has a new

[artifact](https://freexian-team.pages.debian.net/debusine/explanation/concepts.html#artifacts)category representing a source package version in a git repository, and a new[task](https://freexian-team.pages.debian.net/debusine/explanation/concepts.html#tasks)to turn those into traditional source packages as needed.- Debusine can send an outgoing webhook to notify the tag2upload manager when a workflow completes.
- (Optional, depending on the student:) Work with the dgit team to design a system to add additional metadata to signed tags to specify testers. The mentor can help with cross-project communication.
(Stretch goal:) Tie this all together using some kind of

`git debpush`configuration that requests that a git tag be tested by Debusine before pushing it to the Debian archive.

**Desirable skills**: Solid understanding of git’s data model. Competent Python. The ability to read Perl and shell scripts well enough to find answers to questions in dgit’s source code.**What the intern will learn:**How typical git workflows correspond to the Debian archive. Webhooks and other aspects of typical web service design. Running a cross-functional project.**Application tasks:**Pick a

[Quick fix](https://salsa.debian.org/freexian-team/debusine/-/issues?sort=created_date&state=opened&label_name%5B%5D=Quick%20fix&first_page_size=100)issue from our list and try to fix it, including full test coverage for your changes.Explain how a git tag gets from

`git debpush`to the Debian archive.

**AI usage policy:**We will not accept applications written using LLMs, and we expect accepted students to write code themselves, not via an LLM.


## Debusine: live log streaming

**Description of the project:** Debusine allows viewing logs for tasks after they have been completed, but it should also [allow viewing logs of tasks that are in progress](https://salsa.debian.org/freexian-team/debusine/-/issues/854).

**Confirmed Mentor**: Stefano Rivera**How to contact the mentor:**[stefanor@debian.org](mailto:stefanor@debian.org)**Confirmed co-mentors:**None confirmed, but other people from the[Debusine team](https://freexian-team.pages.debian.net/debusine/reference/development-team-organization.html#current-team-organization)can help if needed.**Difficulty level**: Medium to hard**Project size:**175 hours (medium); this project can be split into multiple stages**Deliverables of the project**:- Debusine workers incrementally collect output from tasks as they run, and send it to the server which stores that output in a suitable backend database.
- (Stretch goal:) The Debusine web UI shows streaming output from running tasks.

**Desirable skills**: Python systems programming, Python async programming, websocket communication, Redis and/or PostgreSQL, Django application development. For later stages, HTML+CSS+[?](https://wiki.debian.org/JavaScript)JavaScript development without[?](https://wiki.debian.org/JavaScript)JavaScript frameworks.**What the intern will learn:**Development practices for a medium-sized real-world software development platform. Systems design architecture, with care for latency and scalability. Web user interface design.**Application tasks:**Pick a

[Quick fix](https://salsa.debian.org/freexian-team/debusine/-/issues?sort=created_date&state=opened&label_name%5B%5D=Quick%20fix&first_page_size=100)issue from our list and try to fix it, including full test coverage for your changes.- Write a "producer" command line tool that runs a program and streams its output to Redis.
- Write a "consumer" command line tool that takes output streamed to Redis and writes it on its output. Ideally, while one producer is running, one could start multiple consumers and see the same output streaming on both.

**Additional details:**- Development would have multiple milestones. The first two would be required for successful completion of the project, and the remaining two would count towards rewarding user-visible bragging rights:
- Worker-side, collecting relevant output on the worker code and sending it back to the server via the websocket interface
- Server-side, collecting incoming output from workers and dispatching it to an appropriate Redis structure or a PostgreSQL table
- Server-side, providing a view to make incoming output lines available to code on the browser side
- Browser-side, subscribing to updates and viewing them streaming on the page


- Development would have multiple milestones. The first two would be required for successful completion of the project, and the remaining two would count towards rewarding user-visible bragging rights:
**AI usage policy:**We will not accept applications written using LLMs, and we expect accepted students to write code themselves, not via an LLM.


## Debusine: replace archive-wide reports in UDD

**Description of the project:** The Ultimate Debian Database (UDD) gathers data about many aspects of Debian in a single database, which in turn is used to provide many useful reports to Debian contributors. Some of its tables (e.g. Lintian analysis or information about new upstream versions) import their data from workers that the UDD maintainers run. This overlaps heavily with Debusine: we already need to run Lintian on packages uploaded to Debusine, we can store results in a collection for regression analysis, and we maintain our own worker farm. It seems worth consolidating these and having Debusine generate the necessary data in a way that can be imported by UDD.

We would not expect a student to replace all the uses of external workers in UDD, but we would like to establish a pattern that can be used for the future.

**Confirmed Mentor**: Stefano Rivera**How to contact the mentor:**[stefanor@debian.org](mailto:stefanor@debian.org)**Confirmed co-mentors:**Raphaël Hertzog ([hertzog@debian.org](mailto:hertzog@debian.org))**Difficulty level**: Medium (but the student will need to do some design work)**Project size:**175 hours (medium)**Deliverables of the project**:Debusine has a mechanism to regularly run a

[workflow](https://freexian-team.pages.debian.net/debusine/explanation/concepts.html#workflows)to keep Lintian analyses of Debian unstable and experimental up to date in a[debian:qa-results](https://freexian-team.pages.debian.net/debusine/reference/collections/specs/qa-results.html)collection.- Debusine has a suitable API endpoint to allow UDD to query current Lintian analyses in bulk.
- (Stretch goal:) UDD uses this new API endpoint and can retire its Lintian worker.

**Desirable skills**: Competent Python, and basic Django and/or SQL.**What the intern will learn:**Debusine workflow design. How the plumbing behind Debian’s QA systems works.**Application tasks:**Pick a

[Quick fix](https://salsa.debian.org/freexian-team/debusine/-/issues?sort=created_date&state=opened&label_name%5B%5D=Quick%20fix&first_page_size=100)issue from our list and try to fix it, including full test coverage for your changes.- Investigate how UDD’s Lintian importer works and prepare a brief report on the information it needs.

**AI usage policy:**We will not accept applications written using LLMs, and we expect accepted students to write code themselves, not via an LLM.


## Debusine: usability and papercuts

**Description of the project:** Debusine is now usable by Debian developers and maintainers to perform a variety of QA-related experiments and to host package repositories. However, we have often needed to focus mainly on feature development, and there are plenty of areas where the system is not as usable as we would like. Many of these are relatively small and self-contained tasks that would be ideal for an enthusiastic student to try.

**Confirmed Mentor**: Stefano Rivera**How to contact the mentor:**[stefanor@debian.org](mailto:stefanor@debian.org)**Confirmed co-mentors:**None confirmed, but other people from the[Debusine team](https://freexian-team.pages.debian.net/debusine/reference/development-team-organization.html#current-team-organization)can help if needed.**Difficulty level**: Easy to medium, depending on issue selection**Project size:**This project can be split into many small pieces and so can be any of 90 (small), 175 (medium), or 350 (large) hours depending on student availability.**Deliverables of the project**:- Improvements to the usability of Debusine, scope to be defined with the student.

**Desirable skills**: Web application development, preferably in Python with Django. Debian packaging skills are helpful in order to properly understand the problem domain, but can also be taught as we go along.**What the intern will learn:**Development practices for a medium-sized real-world software development platform. Web user interface design. How the pieces of preparing high-quality changes to sets of Debian packages fit together.**Application tasks:****AI usage policy:**We will not accept applications written using LLMs, and we expect accepted students to write code themselves, not via an LLM.


## Improving Salsa CI

**Description of the project:** Salsa CI is a custom-built continuous integration framework that is used in the Debian Gitlab instance (Salsa) and helps Debian maintainers manage tens of thousands projects. The Salsa CI pipeline emulates the Debian build process and runs several Debian quality tests, helping to detect issues **before** packages are uploaded to the Debian archive. When new source code triggers a Salsa CI pipeline, several different jobs run to build and test it automatically. Salsa CI checks to see whether the to-be-uploaded packages build on multiple architectures, runs autopkgtest test suites to try to identify potential regressions, and checks for common errors with our custom linter, lintian, among other tests. There are different ways to improve Salsa CI that could benefit from the work of a GSoC student.

**Confirmed Mentor**: Santiago Ruano Rincón**How to contact the mentor:**[santiago@debian.org](mailto:santiago@debian.org)/ santiago @ irc.oftc.net**Confirmed co-mentors:**Emmanuel Arias <[eamanu@debian.org](mailto:eamanu@debian.org)>**Difficulty level**: Medium**Project size:**175 (medium) or 350 (large), depending on student's availability**Deliverables of the project**: Fix issues reported against Salsa CI (see below). Specially issues labeled as "Nice-to-have", "Accepting MRs".**Desirable skills**: Awareness of the Gitlab CI/CD support. Collaborative work relying on 'git' and asynchronous-remote tools. Basic knowledge of Debian packaging.**What the intern will learn:**Debian Release process, Debian package building, Debian CI process, Basic QA of Debian packages. Development on a collaborative small team, inside a large community (Debian).**Application tasks:**Pick issues from here (

[https://salsa.debian.org/salsa-ci-team/pipeline/-/issues/?sort=created_asc&state=opened&first_page_size=20=](https://salsa.debian.org/salsa-ci-team/pipeline/-/issues/?sort=created_asc&state=opened&first_page_size=20=), discuss with the team and aim to fix them. Example of priority issues:[https://salsa.debian.org/salsa-ci-team/pipeline/-/issues/318](https://salsa.debian.org/salsa-ci-team/pipeline/-/issues/318)(to minimise the changes of introducing regressions when doing a MR against the pipeline)[https://salsa.debian.org/salsa-ci-team/pipeline/-/issues/498](https://salsa.debian.org/salsa-ci-team/pipeline/-/issues/498)(to make it possible to have runners different to the instance shared runner) More resources:[https://salsa.debian.org/salsa-ci-team/pipeline/](https://salsa.debian.org/salsa-ci-team/pipeline/)[https://about.gitlab.com/blog/2023/09/19/debian-customizes-ci-tooling-with-gitlab/](https://about.gitlab.com/blog/2023/09/19/debian-customizes-ci-tooling-with-gitlab/)

**AI usage policy:**We will not accept applications written using LLMs, and we expect accepted students to write code themselves, not via an LLM.


## Linux Livepatching

**Description of the project:** Evaluate if it's possible to rely on klp-build and clang-extract to bootstrap linux livepatching in Debian. There has been a first attemp to support linux livepatching in Debian, relying on kpatch. However, starting with trixie, kpatch does no longer support the kernel, which prevents us to continue using this approach. SUSE's klp-build overcomes the difficulties found with kpatch, but we need to confirm it's actually possible to package and use it. Also, Debian currently lacks a standardized workflow to build, distribute and publish livepatches for its kernels. The goal of this project is not only package and evaluate klp-build, but also explore and propose a solution about how linux livepatches could built, packaged and made available to Debian users in a controlled, safety and reproducible way.

**Confirmed Mentor**: Emmanuel Arias**How to contact the mentor:**[eamanu@debian.org](mailto:eamanu@debian.org)**Confirmed co-mentors:**Santiago Ruano Rincón <[santiago@debian.org](mailto:santiago@debian.org)>**Difficulty level**: Medium to Hard**Project size:**350 hour (large)**Deliverables of the project**:- Packaging of clang-extract and klp-build
- Study of support of the debian kernel by klp-build.
- Proposal of a mechanism to release Kernel patches.

**Desirable skills**: C Language knowledge. Linux Kernel knowledge desirable. Basic knowledge about Debian packaging. Competent Python. Collaborative work relying on 'git' and asynchronous tools.**What the intern will learn:**- How Linux livepatching works.
- Debian Packaging.
- Development on a collaborative small team, inside a large community (Debian).

**Application tasks:**Finish the linux-livepatching Intent to Package (ITP) bug (

[https://bugs.debian.org/1070494](https://bugs.debian.org/1070494)), and for that, the student will need to:Package clang-extract (

[https://bugs.debian.org/1117623](https://bugs.debian.org/1117623)) and klp-build.- Confirm that klp-build is useful for the current Debian Linux Kernels.
- Propose a distributable Linux Kernel livepatch format to Debian users.
- Propose a mechanism to release Kernel patches.


**More resources:****AI usage policy:**We will not accept applications written using LLMs, and we expect accepted students to write code themselves, not via an LLM.

To add a new project proposal, please enter a WikiName in one of the boxes below (the contents will be used as a wiki page name, please **avoid spaces**) and hit the button! Then, fill in the template, and drop us a line on the debian-outreach mailing-list.

**Please note that below projects aren't approved yet. Please don't apply for non-approved projects. The list of approved projects is available above. **


# Unapproved Projects with confirmed mentors
