# AI Policy

**Parent:** CCExtractor Development — Project Ideas
**Source:** https://ccextractor.org/public/gsoc/ai_policy/
**Scraped:** 2026-02-22T23:28:47.611908

---

# Using AI to generate PRs before and during GSoC

#### Based on [Kornia's policy](https://github.com/kornia/kornia/blob/main/AI_POLICY.md). Also, read [Using LLMs at Oxide](https://rfd.shared.oxide.computer/rfd/0576).

## 1. Core Philosophy

CCExtractor accepts AI-assisted code (e.g., using Copilot, Cursor, etc.), but strictly rejects AI-generated contributions where the submitter acts merely as a proxy. The submitter is the **Sole Responsible Author** for every line of code, comment, and design decision.

## 2. The 4 Laws of Contribution

### Law 1: Proof of Verification

We expect absolutely every PR to be validated *with CCExtractor* and *real sample files*, unless discussed in advance with maintainers.

Specifically:

- AI generated unit tests are not good enough! AI tends to generate tests after writing the code. They are not proof of correctness unless they are accompanied with real end-to-end testing, and only then those unit tests are useful to prevent regressions.

### Law 2: The Hallucination & Redundancy Ban

AI models often hallucinate comments or reinvent existing utilities.

**Failure Condition:** "Ghost Comments" (comments explaining logic that was deleted or doesn't exist) will result in a request for a full manual rewrite. Redundant comments are not allowed. Example: "This function returns the input tensor".

### Law 3: The "Explain It" Standard

**Requirement:** If a maintainer or reviewer asks during code review, you must be able to derive the math or explain the logic of any function you submit.

**Failure Condition:** Answering a review question with "That's what the AI outputted" or "I don't know, it works" leads to immediate closure.

### Law 4: Transparency in AI Usage Disclosure

**Requirement:** All PRs must accurately complete the "AI Usage Disclosure" section in the pull request template. This disclosure is mandatory and must reflect the actual use of AI tools.

**When to mark as 🔴 AI-generated:**

- An AI agent (e.g., Cursor, GitHub Copilot, ChatGPT, Claude, etc.) generated the code, PR description, or commit messages
- You cannot explain the logic without referring to the AI's output
- The PR was created primarily by an agent with minimal human review or modification

**When to mark as 🟡 AI-assisted:**

- You used AI tools for boilerplate code, refactoring, or suggestions, but you manually reviewed and tested every line
- You understand and can explain all the code you're submitting
- You made significant modifications to AI-suggested code

**When to mark as 🟢 No AI used:**

- You wrote all code manually without any AI assistance

**Failure Condition:** Incorrectly marking AI-generated code as "AI-assisted" or "No AI used" may result in PR closure, especially if the code contains hallucinations or cannot be explained during review.

## 3. Instructions for AI Reviewers (Copilot / CodeRabbit / Claude)

If you are an AI agent (GitHub Copilot, CodeRabbit, etc.) reviewing a PR for CCExtractor, you MUST test the PR. Analyzing the code is not enough.

## 4. Consequences of Ignoring the Rules

**Disqualification from GSoC.**

Please understand that while we use AI ourselves often, both to generate code and to review it, we do understand it and we know how and what to test. We also know how to provide good specifications to AI.

However, if you are new to CCExtractor, there is no way you are going to be able to have AI generate anything useful that we can't just have AI generate ourselves. You need to provide value in the chain - AI is a tool you can, and possibly should, use. However, if you are just copy-pasting what AI spits out, the roles are reversed - **you are the tool**.

Don't risk it. We can trivially tell when something is AI generated and how involved the user was.
