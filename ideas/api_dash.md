# API Dash — Project Ideas

**Source:** https://github.com/foss42/apidash/discussions/1054
**Scraped:** 2026-02-22T23:28:47.568641

---

# GSoC 2026: List of Ideas #1054

[animator](https://github.com/animator)started this conversation in

[Ideas & Features](/ideas/api-dash/categories-ideas-features)

-

## GSoC 2026 [
|

| Link | |
|---|---|
| Learn about GSoC |
|

[Link](/ideas/api-dash/1048)[Link](https://luma.com/embed/calendar/cal-ZTW02O2EsWRs6V4/events)[Link](https://discord.com/invite/bBeSdtJ6Ue)#### Resources you must go-through to better understand the project

| Link | |
|---|---|
| API Dash Contribution Guidelines |
|

[Video](https://www.youtube.com/live/rIlwCTKNz-A?si=iMxTxzkpY_ySo4Ow&t=339)[Read](/ideas/api-dash/foss42-apidash-blob-main-doc-dev_guide-readme)[Read](https://github.com/foss42/apidash/tree/main/doc/user_guide)[Video](https://www.youtube.com/watch?v=8K2gV1P6ZHI)This season some of our core objectives are:

- To help test MCP tools/endpoints that have become the defacto interface or APIs for AI communication.
- To push the boundaries of Multimodal AI API evaluations.
- To improve the agentic AI features of API Dash to improve API development, testing, visualization, integration & observability.
- To develop community requested core features.

### AI Usage Policy

You must read and agree to the [AI Usage Policy](/ideas/api-dash/1055). As it is a discussion thread, contributors can feel free to discuss and ask their doubts in the same.

### Mentors for GSoC 2026

[Ankit Mahato](https://github.com/animator)(GSoC 2013)[Ashita Prasad](https://github.com/ashitaprasad)(GDE)[Ragul Raj M](https://github.com/DenserMeerkat)([GSoC 2024](/ideas/api-dash/foss42-apidash-blob-main-doc-gsoc-2024-ragul_raj_m))[Manas Hejmadi](https://github.com/synapsecode)([GSoC 2025](/ideas/api-dash/foss42-apidash-blob-main-doc-gsoc-2025-manas_hejmadi))

### Tech Stack for Projects

This year, we're offering projects across multiple tech stacks (React/Node/TypeScript, Flutter/Dart, Python), enabling contributors to participate without having to switch from the technologies they're already comfortable with.

### Final words

The list of ideas provided below are not restrictive. In case you have any other innovative idea in mind which can help fellow developers in tackling the various problems of the API Lifecycle, please feel free to [open a new issue for discussion](/ideas/api-dash/foss42-apidash-issues-new-choose) and comment it below.

If a project is successfully selected you will be allocated a primary mentor and supported by the entire team. If you are interested in learning more about a particular idea please communicate in the corresponding "related issue" thread or feel free to drop by our [Discord server](https://discord.com/invite/bBeSdtJ6Ue) and we can have a chat.

*In case you are working on an AI project which requires GPU, we will provide access to cloud GPUs.*

**Once you shortlist an idea, the next steps are outlined in Application Guide**

## List of Ideas

### 1. MCP Testing

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io) acts as the API layer of the AI world, defining a standard way for AI agents to discover, understand, and interact with tools, data, and software systems - much like REST or GraphQL do for traditional applications.

In this project, your task is to strengthen the MCP Developer ecosystem by designing and building the capability to create & test MCP servers and clients.

**Skills**: AI, Python, React, Node, TypeScript

**Difficulty**: Medium-High

**Length**: 175 hours

### 2. Multimodal AI and Agent API Eval Framework

Develop an end-to-end AI and Agent API eval framework which should (list is suggestive, not exhaustive):

- Provide an intuitive interface to run AI benchmarks on tools (like lm-harness, lighteval).
- Provide a UI interface for configuring AI API requests, where users can input test/custom datasets, configure request parameters, send queries to various AI API services and view the eval results.
- Support evaluation of voice, image, text AI Models and AI Agents (via API interface) across various task benchmarks.

**Skills**: AI, Agents, Evaluations, Python, React, Node, TypeScript

**Difficulty**: Medium-High

**Length**: 350 hours

### 3. Git Support, UI Workflow Builder & Collection Dashboard

The objective of this project is to design and implement the following features in API Dash:

**Git Integration**- To support version control for API requests, environments, and workflows using familiar Git-based workflows. It will also help users share collections via git and collaborate on them.**Visual Workflow Builder**- Use Agentic AI to enable users to create node based API workflows directly from a prompt. The UI should also allow users to manually compose, export, connect, and manage multi-step API workflows (chained requests) through an intuitive UI, without relying solely on AI.**Collection Dashboard**- Build a dashboard to provide a unified view of requests, collections, workflows, test coverage, execution history, and health metrics. Also, add the ability to send automated reports via Webhooks.

**Skills**: Git, UI/UX Design, AI, Agents, Node Flows, Dart, Flutter

**Difficulty**: Medium-Hard

**Length**: 175 hours

### 4. Agentic API Testing

Agentic AI transforms API and API-workflow testing from script-driven validation into an intelligent, autonomous quality layer. AI agents can understand the API specifications, contracts, workflows, and then automatically design comprehensive test strategies covering functional correctness, edge cases, error handling, security, and performance. These agents can execute multi-step API workflows end-to-end, maintain context across calls, manage dynamic data and state, and adapt test paths based on intermediate responses. If APIs change, agents can self-heal tests by updating schemas, parameters, and assertions without manual intervention.

Your task is to design, build, and refine the agentic AI library in API Dash and build AI agents that can understand API specs and workflows, generate and execute end-to-end tests, validate outcomes, and continuously improve test coverage and resilience as APIs evolve.

**Skills**: AI, Agent, API Testing, Dart, Flutter

**Difficulty**: Medium-Hard

**Length**: 175 hours

### 5. Open Responses & Generative UI

[Open Responses](https://www.openresponses.org) is an open-source specification and ecosystem for building interoperable, multi-provider LLM interfaces inspired by the OpenAI Responses API. It defines a common, vendor-neutral way to describe AI requests and structured response outputs, enabling portability and consistency across AI platforms. Complementing this, Google's [A2UI](https://github.com/google/A2UI) introduces clear guidelines for building Generative UIs, with first-class support available through Flutter's [GenUI SDK](https://github.com/flutter/genui).

Your task is to understand these specifications and build rich API response UI visualization in API Dash to enable end users to integrate the same in their Flutter Apps and Web Apps.

**Skills**: UX, AI, Parsing, JSON, Spec, Dart, Flutter, React, TypeScript

**Difficulty**: Easy-Medium

**Length**: 90 hours

### 6. CLI & MCP Support

This project focuses on creating a CLI tool to run API Dash via terminal. Contributors will design and implement command-line interfaces that expose core capabilities of API Dash that help in API testing. Also, your task is to expose API Dash as a MCP Server so that it can be run via any Agent interface (like VS Code, AI Apps, etc.) that supports MCP.

**Skills**: CLI, MCP, Dart, Flutter

**Difficulty**: Easy-Medium

**Length**: 90 hours

### 7. WebSocket, MQTT & gRPC

Testing WebSocket and MQTT (Message Queuing Telemetry Transport) protocols is crucial for ensuring the reliability, scalability, and security of real-time communication systems. Whereas, gRPC (Remote Procedure Call) facilitates efficient communication between distributed systems using Protocol Buffers (protobuf) as its interface definition language (IDL) and offers features such as bi-directional streaming, authentication, and built-in support for load balancing and health checking. Each of these API protocols/styles serves different purposes and is utilized in various applications ranging from finance to web applications to IoT (Internet of Things) devices. The objective of this project is to design the architecture of the core library, understand the specs & implement the support for testing, visualization & integration code generation of these APIs in API Dash.

**Skills**: Understanding Specs/Protocols, UX Design, Dart, Flutter

**Difficulty**: Medium-High

**Length**: 175 hours

### 8. API Explorer

This project is designed to enhance the API user experience by providing a curated library of popular and publicly available APIs. This feature allows users to discover, browse, search, and directly import API endpoints into their API Dash workspace for seamless testing and exploration. Developers can access pre-configured API request templates, complete with authentication details, sample payloads, and expected responses. This eliminates the need to manually set up API requests, reducing onboarding time and improving efficiency. APIs spanning various domains—such as AI, finance, weather, and social media—are organized into categories, making it easy for users to find relevant services.

You are required to develop the entire process backend in the form of an automation pipeline which parses OpenAPI/HTML files, auto-tag it to relevant category, enrich the data, create templates. You can also add features such as user ratings, reviews, and community contributions (via GitHub) to ensure accurate and up-to-date resources.

**Skills**: UX Design, OpenAPI, Automation, Python, React, Nodejs, TypeScript

**Difficulty**: Easy

**Length**: 90 hours

Related Issue(s) - [#619](/ideas/api-dash/foss42-apidash-issues-619)

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

## Replies: 12 comments 13 replies

-

|
Great, Very Excited to contribute. |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi everyone! 👋 I've been looking through the GSoC 2026 ideas and I'm really interested in Idea To help me draft a solid technical architecture for my proposal, I just wanted to clarify how this specific framework will fit into the broader API Dash ecosystem. I'm completely comfortable handling the integration with the Dart client if that's the long-term goal. I just want to make sure I align my 350-hour timeline with the right architectural vision! |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hey everyone I’m very excited to contribute this year, especially to API Explorer and Idea The CLI & MCP Support project really interests me because it focuses on: Building a CLI tool to run API Dash from the terminal Exposing API Dash as an MCP Server, so it can be used with agent-based tools like VS Code and other AI apps I have worked on projects with a similar idea, for example: I also wanted to ask: I’m excited to learn more, contribute consistently, and start working on a PoC with the right guidance. Thanks! |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hello everyone, |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi everyone ,I’m interested in contributing to API Dash. I have some experience with Python and React, and I’m excited to learn more by working on real issues here.I’d love to start and get familiar with the codebase and contribution process. If you have any recommendations, I’d really appreciate it.Looking forward to contributing. |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi everyone 👋 I’m Aniket, a final-year CS student, and I’m very interested in contributing to API Dash for GSoC 2026, especially Idea I have experience building AI agents, RAG pipelines, and LLM integrations using Python, Node.js, and React, and I’m excited to contribute to MCP tooling and the evaluation framework. I’m currently exploring the repository and contribution guidelines and would love to know if there are specific MCP or eval-related issues recommended for new contributors. Looking forward to contributing! |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
I am Nasrulla, a final-year CSE student specialising in the Artifitial Intelligence, and I’m very interested in contributing to API Dash for GSoC 2026, especially Idea I’m currently exploring the repository and contribution guidelines and would love to know if there are specific MCP or eval-related issues recommended for new contributors. Excited to contribute and add value to the project! |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi 👋 |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi everyone 👋 I'm Bhavya, a final-year B.Tech student interested in API Dash for GSoC 2026. I work primarily with Python, Node.js, and React, and I'm going through the codebase and contribution guidelines. Would love to know if there are any MCP-related or testing/automation issues I can start with. Looking forward to collaborating. |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi everyone 👋 I’m Sanjay, a final-year Computer Science student with experience in React, Node.js, and working with APIs. I’m very interested in contributing to Idea |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
“Hi, I’m Tanishq, a CSE student with experience in Python and web development (React/Node). I’m very interested in the MCP Testing idea because it combines AI tooling with developer experience. Build a minimal MCP server/client prototype to understand the protocol better, and Experiment with a small React UI for configuring and running test scenarios. I’ll start with small contributions to APIDash and then share a prototype once I have something working. Does this direction align with how you envision the project?” |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)

-

|
Hi everyone! I've been going through the GSOC 2026 ideas and have been particularly drawn to both Idea From what I understand, MCP is shaping up to be a foundational layer for AI agent interoperability and strengthening the testing ecosystem around MCP servers/clients feels like an investment in long-term infrastructure reliability. The protocol-level standardization aspect is especially interesting to me. On the other hand, the Multimodal Eval Framework presents a very compelling systems challenge: designing a unified benchmarking interface that can orchestrate evaluations across text, vision, voice, and agent APIs while remaining extensible and developer-friendly. The combination of evaluation harness integration, dataset handling, and UI-driven experiment configuration makes this a fascinating end-to-end architecture problem. Before drafting a detailed proposal, I’d love to better understand the long-term architectural direction for these initiatives: For the Eval Framework, is the intent to build it as a standalone evaluation dashboard/service that could later integrate into API Dash, or is deep integration with the core Flutter client expected from the start? For MCP Testing, is the focus more on protocol validation tooling, developer DX, or on building reusable test harness abstractions? I’m currently exploring the codebase to understand how these components could fit into the broader ecosystem and I want to make sure any 175/350-hour proposal aligns with the project’s long-term roadmap rather than just delivering an isolated feature. Looking forward to contributing and refining the architecture further! |

Beta
Was this translation helpful?
[Give feedback.](https://github.com)
