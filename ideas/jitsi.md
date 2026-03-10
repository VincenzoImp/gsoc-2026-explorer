# Jitsi — Project Ideas

**Source:** https://github.com/jitsi/gsoc-ideas/blob/master/2026/README.md
**Scraped:** 2026-03-10T16:58:40.241297

---

# Projects for GSoC 2026

Here's the list of project ideas for GSoC 2026! Click on the title for a more detailed description.

* [Chat Moderation & Editing](/ideas/jitsi/chat-moderation-editing)
* [Jitsi Videobridge JavaScript client](/ideas/jitsi/jvb-js)
* [Virtual Backgrounds, take 2](/ideas/jitsi/virtual-backgrounds-ng)
* [E2EE: Replace olm with vodozemac](/ideas/jitsi/e2ee-vodozemac)
* [Tracing calls through backend components](/ideas/jitsi/tracing-backend)
* [External API without iframe](/ideas/jitsi/external-api-no-iframe)
* [External API with non-serialized postMessages](/ideas/jitsi/external-api-structured-clone)
* [Inject external streams via iframe API](/ideas/jitsi/inject-external-streams)
* [PTZ camera support via WebRTC constraints](/ideas/jitsi/ptz-camera-support)
* [Ultrasound experiments with ggwave (part 2)](/ideas/jitsi/ultrasound-ggwave)
* [Rewrite Jibri to use iframe API](/ideas/jitsi/jibri-iframe-api)
* [Document Picture-in-Picture for browser meetings](/ideas/jitsi/document-pip-browser)

# Interested in applying for a project?

Jitsi GSoC’26 Application Guidelines
==========================================

Welcome! We are thrilled you’re interested in contributing to Jitsi. To ensure a healthy environment for our mentors and to find the best long-term collaborators, we have a strict set of engagement rules for 2026.
Our Goal: We are looking for people, not patches. We value your struggle, your questions, and your unique coding style more than a "perfect" AI-generated fix.

**1. The "Human Fingerprint" Policy (AI Usage)**
   
We acknowledge that LLMs (ChatGPT, Gemini, Claude) are part of the modern workflow. However, GSoC is a mentorship program for humans.

Allowed: Using AI as a learning aid to overcome the initial "steep curve" of the project, IDE auto-completion (LSPs), or explaining complex documentation.

Forbidden: Submitting code or proposals generated primarily by AI.

The Penalty: If we detect "Uncanny Valley" code (code that works but you cannot explain the design trade-offs for), your application will be immediately rejected. If discovered during the program, you will be removed.

**2. Technical Gatekeeping**
   
If you plan to start contributing to the project, please take a look at the [contribution guidelines](https://jitsi.github.io/handbook/docs/dev-guide/dev-guide-contributing/) and only submit valid PRs.

To protect mentor bandwidth, we apply the following "Hard Filters" to all Pull Requests (PRs):

The "GSoC" Prefix: Every PR submitted by an applicant must include GSoC: at the beginning of the title (e.g., GSoC: Fix memory leak in JitsiConference). PRs without this prefix will not be attributed to GSoC applicants.

The Build Rule: If your PR does not compile or pass our CI/CD linting, it will be closed without review.

The "Real Repro" Rule: Every bug fix must include steps for reproduction. A "dummy" fix with no proof of a local run is a "No-Go."

Concurrency Limit: You may have a maximum of 3 active PRs at any time. Focus on quality, not quantity.

**3. Community & Communication**
   
Please use the [Jitsi Community forum](https://community.jitsi.org/) to post your questions and connect with fellow aspirants for GSoC'26.

No "Introduction" Posts: Do not create new posts just to introduce yourself. Find existing GSoC'26 threads where community members and mentors are already active. Engaging in an established conversation shows you have done your research.

Talk First: Do not submit a large PR without a linked discussion thread where a mentor has given you the "green light."

Be Patient: Repeatedly pinging mentors for reviews will decrease your chances of selection.

Protect Your Ideas: Do not post your detailed technical approach or proposal drafts on the public forum. This prevents plagiarism and ensures we can evaluate your original work. Discussion on the forum should be about understanding the problem, not revealing your unique solution.

**How We Evaluate You (The Rubric)**

Please make sure to list all merged PRs in your profile but we don't just count the number of merged PRs. We use a weighted rubric to rank candidates:

Depth of Insight: Did you ask "Why?" Did you suggest a better way to do things?

Independence: Can you set up your local environment and run tests without hand-holding?

Communication: Are you helping others in the Jitsi community? Are you easy to talk to?

The Proposal: Is it a unique technical plan, or a generic AI-generated template?
