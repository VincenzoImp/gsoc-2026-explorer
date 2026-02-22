# The Honeynet Project — Project Ideas

**Source:** https://www.honeynet.org/gsoc/gsoc-2026/google-summer-of-code-2026-project-ideas/
**Scraped:** 2026-02-22T23:28:47.618457

---

# Google Summer of Code 2026 Project Ideas

###### 17 Jan 2026

### Getting Started

This page contains a list of potential project ideas that we are keen to develop during GSoC 2026. If you would like to apply as a GSoC student, please follow these two steps to get started:

- Read through this page and identify the project ideas you find interesting. Play around with our tools!
- Join us on Discord and talk to your potential mentors on
[Discord](https://discord.gg/68B8Ru5fSU)You can also find us in[Slack](https://gsoc-slack.honeynet.org/).

If there are any questions, please don’t hesitate and get in touch! 🙂

### GSoC and The Honeynet Project

During the previous years of GSoC, the Honeynet Project’s students have created a wide range of very successful open source security projects, many of which have gone on to become the industry standard open source tools in their respective fields.

We are also always interested in hearing any ideas for additional relevant computer security and honeynet-related R&D projects (although remember that to qualify for receiving GSoC funding from Google your project deliverables need to fit in to [GSoC’s project timescales](http://developers.google.com/open-source/gsoc/faq)!). If you have a suitable and interesting project, we will always try and find the right resources to mentor it and support you.

Please note - even if you aren’t an [eligible GSoC participant](http://developers.google.com/open-source/gsoc/faq), we are also always looking for general volunteers who are enthusiastic and interested in getting involved in honeynet R&D.

Each sponsored GSoC 2026 project will have one or more mentors available to provide a guaranteed contact point to students, plus one or more technical advisors to help applicants with the technical direction and delivery of the project (often the original author of a tool or its current maintainer, and usually someone recognized as an international expert in their particular field). Our Google Summer of Code organizational administrators will also be available to all sponsored GSoC students for general advice and logistical support. We’ll also provide hosting for project infrastructure, if required.

For all questions about the Honeynet Project, the GSoC program or our projects, please contact us on [Discord](https://discord.gg/68B8Ru5fSU) (preferred)** or email us at [[email protected]](https://www.honeynet.org/cdn-cgi/l/email-protection#7404061b1e111700341c1b1a110d1a11005a1b0613). You can also find us in [Slack](https://gsoc-slack.honeynet.org/).

**Application template**

If you are considering applying to participate with us in GSoC 2026 please find our [application template here](https://honeynet.org/gsoc/gsoc-2026/application/). Use it when you are preparing your application on the official GSoC site and don’t hesitate to ask your mentors for feedback before submitting!

# GSoC 2026 Project Ideas Overview

[#1 - Improving the DICOMHawk medical honeypot](https://www.honeynet.org#improving-the-dicomhawk-medical-honeypot)[#2 - EventHorizon: the tarpit framework](https://www.honeynet.org#eventhorizon-the-tarpit-framework)[#3 - Extending the Artemis scanner](https://www.honeynet.org#extending-the-artemis-scanner)[#4 - Greedybear: Access payload files](https://www.honeynet.org#greedybear-access-payload-files)[#5 - Greedybear: Dashboard Modularization](https://www.honeynet.org#greedybear-dashboard-modularization)[#6 - Greedybear: Injection / Event Collector API](https://www.honeynet.org#greedybear-injection--event-collector-api)[#7 - IntelOwl: Integrating a Self-Deployed LLM Chatbot for Threat Intelligence](https://www.honeynet.org#intelowl-integrating-a-self-deployed-llm-chatbot-for-threat-intelligence)[#8 - IntelOwl: Integration Ecosystem & Connector Optimization](https://www.honeynet.org#intelowl-integration-ecosystem--connector-optimization)[#9 - IntelOwl: Maintenance Optimization & Architectural Refinement](https://www.honeynet.org#intelowl-maintenance-optimization--architectural-refinement)

### #1 - Improving the DICOMHawk medical honeypot

**Mentor:**Manolis Vasilomanolakis

**Project type:**Improving an existing tool

**URL:**

[https://github.com/honeynet/DICOMHawk](https://github.com/honeynet/DICOMHawk)

**Expected Project hours:**175 - 350 based on received proposal

### Project Overview

DICOMHawk is an open-source honeypot designed to emulate a vulnerable DICOM (Digital Imaging and Communications in Medicine) server to attract, log and analyze unauthorized access attempts against medical imaging systems. It provides a realistic DICOM environment with detailed logging and a web interface for monitoring interactions, helping security researchers understand how attackers probe and interact with such services in the wild.

### Goal

The GSoC project focuses on

- code improvement and debugging to make the software more robust, maintainable, and effective at capturing meaningful threat data.
- securing the honeypot itself, including hardening its deployment (e.g., through Docker and better configuration practices) so that it’s safer to run in research or production-like environments.
- general improvements to usability, monitoring, logging capabilities, and integration with threat intelligence.

Together, these efforts help evolve DICOMHawk into a more realistic, secure, and useful tool for studying attacks against healthcare infrastructure and improving defensive strategies.

### Required Skills

- Basic Linux/Command Line skills
- Docker
- Python

### #2 - EventHorizon: the tarpit framework

**Mentor:**Manolis Vasilomanolakis

**Project type:**Improving an existing tool

**URL:**

[https://github.com/honeynet/EventHorizon](https://github.com/honeynet/EventHorizon)

**Expected Project hours:**175 - 350 based on received proposal

### Project Overview

EventHorizon is an open-source multiprotocol IoT tarpit framework designed to emulate commonly abused IoT services such as Telnet, SSH, MQTT, UPnP, and CoAP in order to trap and study automated attackers. The framework focuses on keeping malicious clients engaged at the protocol level, slowing scanning and propagation activity while safely collecting measurement data. It provides a modular, containerized architecture that allows multiple protocol-aware tarpits to be deployed consistently across different environments. This GSoC project is centered on improving the framework’s capabilities, including making the codebase more robust, maintainable, and extensible for future protocol support.

### Goal

Key goals include refactoring and hardening the implementation, improving reliability and logging, and addressing edge cases discovered during real-world deployments. Additional efforts focus on enhancing deployment safety, reducing predictability to attackers, and improving overall framework usability for researchers. Together, these improvements strengthen EventHorizon as a reliable foundation for studying attacker behavior and advancing deception-based defenses for IoT systems..

### Required Skills

- Python programming and familiarity with Linux and Docker.

### #3 - Extending the Artemis scanner

**Mentor:**Krzysztof Zając

**Project type:**Improving an existing tool

**URL:**

[https://github.com/CERT-Polska/Artemis](https://github.com/CERT-Polska/Artemis)

**Expected Project hours:**175 or 350 hours

Artemis is a modular vulnerability scanner that checks multiple aspects of website security and builds easy-to-read messages to send to organizations to get the vulnerabilities fixed. Multiple national-level CSIRTs use it to improve the security of their constituencies - for example, since 2023, CERT PL has used Artemis to find and report more than a million vulnerabilities.

The goal is to improve the number and quality of detected vulnerabilities. There may be multiple ways of achieving this goal:

- Extend Artemis with modules detecting new types of vulnerabilities (for example, by integrating existing open-source tools),
- Improve Artemis in other aspects such as performance or ease of use.

The primary required skills are Python programming and familiarity with Linux and Docker. Familiarity with web security topics is also desired.

### #4 - Greedybear: Access payload files

**Mentor:**Tim Leonhard, Matteo Lodi

**Project type:**Improving an existing tool

**URL:**

[https://github.com/intelowlproject/Greedybear](https://github.com/intelowlproject/Greedybear)

**Expected Project hours:**175 - 350 based on received proposal

### Project Overview

Currently GreedyBear obtains all its data from T-Pots Elastic stack. Some data that is collected by T-Pot however is not available there. Some honeypots, like Dionaea, collect payloads that are only written to the filesystem, that is to `~/tpotce/data`

. It would be great to make those artifacts available in GreedyBear. This project might not be limited to work on GreedyBear but can also include tinkering with the configuration of T-Pot itself or even introducing changes to T-Pot.

Related issues:
[https://github.com/intelowlproject/GreedyBear/issues/558](https://github.com/intelowlproject/GreedyBear/issues/558)
[https://github.com/telekom-security/tpotce/discussions/1653](https://github.com/telekom-security/tpotce/discussions/1653)

### Goal

Have a clean and reliable way to

- access or extract payload files and other samples from T-Pot
- present them to the user in a safe manner

### Required Skills

- basic knowledge of Python, Linux and Docker
- motivation to deeply dive into both projects, GreedyBear and T-Pot, to create a stronger integration

### #5 - Greedybear: Dashboard Modularization

**Mentor:**Tim Leonhard, Matteo Lodi

**Project type:**Improving an existing tool

**URL:**

[https://github.com/intelowlproject/Greedybear](https://github.com/intelowlproject/Greedybear)

**Expected Project hours:**175 - 350 based on received proposal

### Project Overview

The GreedyBear dashboard currently displays statistics through hard coded chart components and has a fixed layout. It would benefit the project to refactor the dashboard into a flexible, configuration-driven widget system that allows easy addition and removal of dashboard components.

### Goal

Have a configuration-driven dashboard where widgets can be added or removed by editing a single configuration file, or even better, directly in the frontend for admin users.

### Required Skills

- basic knowledge of JavaScript, preferably also of React and chart libraries
- motivation to design and implement and test substantial changes to an already existing frontend

### #6 - Greedybear: Injection / Event Collector API

**Mentor:**Tim Leonhard, Matteo Lodi

**Project type:**Improving an existing tool

**URL:**

[https://github.com/intelowlproject/Greedybear](https://github.com/intelowlproject/Greedybear)

**Expected Project hours:**175 - 350 based on received proposal

### Project Overview

GreedyBear obtains all its data by pulling it from a T-Pot instance. While this will always be the main data source, it would be great to build an API where external, authenticated applications can inject data into GreedyBear’s database. This API would accept incoming event data in a specified format, process and save it. This would give honeypot developers the option to use GreedyBear as a frontend / data store.

### Goal

Have a documented and tested API endpoint that enables GreedyBear to receive event data from other sources than T-Pot in a safe and reliable manner.

### Required Skills

- basic knowledge of Python
- motivation to thoroughly design and implement an API endpoint

### #7 - IntelOwl: Integrating a Self-Deployed LLM Chatbot for Threat Intelligence

**Mentor:**Matteo Lodi, backups to be defined

**Project type:**Improving an existing tool

**URL:**

[https://github.com/intelowlproject/IntelOwl](https://github.com/intelowlproject/IntelOwl)

**Expected Project hours:**175 - 350 based on received proposal

### Project Overview

The goal of this project is to revolutionize how analysts interact with IntelOwl by integrating a cutting-edge, self-deployed LLM-based chatbot. This tool will transform static threat intelligence into a conversational experience, allowing users to query complex data using natural language.

By leveraging modern AI frameworks, the project aims to make threat investigation more intuitive, efficient, and accessible.

### Key Objectives

-
Conversational Interface Development: Utilize Python, LangChain, and ChainLit (or whatever tool is better to be used) to build a seamless chat interface capable of handling complex natural language queries (e.g., “Which campaigns are associated with this IOC?”).

-
IntelOwl Module Integration: Deeply interface the chatbot with IntelOwl’s enrichment modules, allowing the AI to trigger deeper investigations and pull real-time data when required.

-
Self-Deployed Architecture: Ensure the LLM infrastructure is self-hosted to maintain data privacy and security—a critical requirement for threat intelligence environments.

-
Adaptive Investigative Workflows: Design the system to adapt to evolving user needs, streamlining the communication between the analyst and the platform’s underlying data.


### Contributor Profile & Required Soft Skills

The LLM and AI landscape is moving at an incredible pace. To succeed in this project, we are looking for a contributor who demonstrates:

-
Proactivity: you propose creative solutions and architectural improvements to overcome technical hurdles.

-
Technical Autonomy: You are comfortable diving into dense documentation and managing your development cycles with minimal supervision.

-
High Adaptability: You stay updated with the latest open-source AI frameworks and are ready to pivot or adapt your approach as new, more efficient models or tools emerge.


### #8 - IntelOwl: Integration Ecosystem & Connector Optimization

**Mentor:**Matteo Lodi, backups to be defined

**Project type:**Improving an existing tool

**URL:**

[https://github.com/intelowlproject/IntelOwl](https://github.com/intelowlproject/IntelOwl)

**Expected Project hours:**90 - 175 based on received proposal

### Project Overview

A core strength of our platform is its ability to communicate with the broader security ecosystem. We are looking for a contributor to lead the revitalization of our “Connectors”—the vital bridges used to export and share analysis reports with external platforms.

The focus will be on ensuring seamless interoperability with industry-standard tools, specifically MISP, Yeti, and OpenCTI.

### Key Objectives

-
Comprehensive Connector Audit: Review the existing codebase for our primary connectors to identify, reproduce, and resolve reported bugs and performance bottlenecks.

-
Infrastructure Setup & Debugging: Deploy and configure local instances of the relevant open-source projects (MISP, Yeti, OpenCTI) to create a robust testing environment for end-to-end debugging.

-
Native Health Check Integration: Enhance user experience by implementing dedicated “Health Check” features. By utilizing the native APIs of external tools, you will build a diagnostic layer that allows users to instantly verify the status of their integrations.

-
Future-Proofing: Refactor existing integration logic to make future updates easier to manage as external API schemas evolve.


### Contributor Profile

The ideal candidate for this project enjoys digging into third-party documentation and has a passion for building reliable, interconnected systems. You will play a crucial role in improving the reliability of the platform for our entire user base.

#### Key expectations include:

-
Technical Research: Deep-diving into external API specifications.

-
Environment Orchestration: Willingness to set up and manage the open-source tools required for testing.

-
Proactive Communication: Working closely with mentors to standardize how data is mapped between platforms.


Github issues reference:

[https://github.com/intelowlproject/IntelOwl/issues/2737](https://github.com/intelowlproject/IntelOwl/issues/2737)[https://github.com/intelowlproject/IntelOwl/issues/2480](https://github.com/intelowlproject/IntelOwl/issues/2480)[https://github.com/intelowlproject/IntelOwl/issues/2122](https://github.com/intelowlproject/IntelOwl/issues/2122)[https://github.com/intelowlproject/IntelOwl/issues/2309](https://github.com/intelowlproject/IntelOwl/issues/2309)

### #9 - IntelOwl: Maintenance Optimization & Architectural Refinement

**Mentor:**Matteo Lodi, backups to be defined

**Project type:**Improving an existing tool

**URL:**

[https://github.com/intelowlproject/IntelOwl](https://github.com/intelowlproject/IntelOwl)

**Expected Project hours:**90 - 175 based on received proposal

### Project Overview

This project focuses on resolving core architectural bottlenecks that hinder development velocity. The primary objectives are to enhance the testing suite performance and streamline the project’s dependency graph. Currently, the project suffers from slow CI/CD cycles and frequent dependency conflicts that complicate the build process.

### Key Objectives

-
Testing Suite Optimization: Investigate and implement strategies to significantly reduce test execution time.

-
Dependency Management: Conduct a comprehensive audit of frontend and backend dependencies. The goal is to minimize the footprint by removing redundant packages, resolving version conflicts, and updating or replacing outdated libraries.

-
Analyzer & Plugin Refactor: Evaluate existing analyzers and plugins. You will be expected to identify obsolete or unecessary components and either refactor them for modern standards or replace them with more efficient alternatives. Also complete removal of an analyzer is an option.


### Contributor Expectations

As this project involves fundamental changes to the project structure, we are looking for a contributor who prioritizes:

-
Analytical Research: Proactively identifying which dependencies are “dead weight” or causing bottlenecks.

-
Iterative Development: Implementing changes in manageable increments to avoid breaking core functionality.

-
High Communication: This role requires consistent interaction with mentors to ensure structural changes align with the long-term vision of the project.


Github issues reference:

[https://github.com/intelowlproject/IntelOwl/issues/2958](https://github.com/intelowlproject/IntelOwl/issues/2958)[https://github.com/intelowlproject/IntelOwl/issues/2776](https://github.com/intelowlproject/IntelOwl/issues/2776)[https://github.com/intelowlproject/IntelOwl/issues/2737](https://github.com/intelowlproject/IntelOwl/issues/2737)
