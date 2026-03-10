# Playground Tooling

**Parent:** Eclipse Foundation — Project Ideas
**Source:** https://gitlab.eclipse.org/eclipsefdn/emo-team/gsoc-at-the-ef/-/issues/github.com/eclipse-thingweb/playground
**Scraped:** 2026-03-10T16:58:40.240916

---

## #31: Restructure the Eclipse Project Handbook

**Labels:** GSoC 2026, Project Idea

## **Restructure the Eclipse Project Handbook**
<!-- 
If you are interested in mentoring a project please use this template to submit your Project Idea for the GSoC programme.
The format suggested below is exactly that, a suggestion. Play with the layout, but please make sure to provide all relevant information. Please be sure to follow branding guidelines (e.g. "Eclipse Dash", not "Dash"). Links to content hosted elsewhere are fine, but bear in mind that this GitLab project and its issues will be the main point of contact for people who are not already inside your community.
-->

### **Description** 

The Eclipse Project Handbook currently rendered as a single HTML page. The current build also generates a PDF which we don't currently use.

The rendered forms are generated from a collection of files in AsciiDoc format. Each file (generally) represents one chapter of the handbook. The AsciiDoc content includes  some graphviz and PlantUML markup that generates embedded images. The current build script uses a combination of Maven and `bash` script.

As the handbook has grown in size, the decision to render it as a single HTML file makes less sense, and we'd like to explore rendering it in a more modern manner (e.g., similar to the [asciidoctor.org](https://docs.asciidoctor.org/asciidoctor/latest/) documentation with multiple pages and navigation block on the left).

Ideally, we'd like retain the ability to render the handbook as a either an ebook or a format suitable for printing hardcopies (physical books are things that we can give to our moms to impress their friends).

Our use of cross references across chapters may require adjustment (there's a lot of cross references, so this may be a painstaking chore). There may be other examples of naive use of AsciiDoc features that we'd welcome help remediating.

### **Links to Eclipse Project** 

- [Eclipse Dash](https://projects.eclipse.org/projects/technology.dash)
- [Eclipse Project Handbook in GitLab](https://gitlab.eclipse.org/eclipse/technology/dash/org.eclipse.dash.handbook)

### **Expected outcomes** 

- Document (content) updates as required
- Updated (or new) automated build that produces the handbook in chapter format and in PDF/ebook format

Note that replacement of the Maven-based build is an acceptable outcome.

Hint: We think that [Antora](https://docs.antora.org) plays a role in the solution.

### **Skills required/preferred** 

- Familiarity with AsciiDoc and asciidoctor.org will be a tremendous asset

### **Project size** 
We think that this is a 90 hour project. But feel free to convince us otherwise.

### **Possible mentors:** 
[Wayne Beaton](https://projects.eclipse.org/projects/technology.dash/PL/wbeaton)

Hint: don't try to figure out how to contact me directly. This is an open source project. An important part of engaging in open source is to ask questions and work in the open. Ask your questions on this issue. Working in the open is hard. But I believe in you.

### **Rating** 

W

*[truncated]*

---

## #30: Support for using an SBOM as input

**Labels:** GSoC 2026, Project Idea

## **Support for using an SBOM as input**

### **Description** 

The Eclipse Dash License Tool is a Java-based utility used by Eclipse committers to identify the licenses of project dependencies and verify them against the Eclipse Foundation’s IP policy. Currently, the tool relies on specific ecosystem inputs (like Maven `pom.xml`, Gradle lockfiles, or NPM `package-lock.json`) to identify dependencies.

This project aims to generalise the tool’s input capabilities by implementing support for Software Bill of Materials (SBOM) files in CycloneDX and SPDX formats. The student will extend the tool to parse these industry-standard formats, extract dependency identifiers (pURLs, GAVs, NPM IDs, etc.), and perform the license check. Furthermore, the tool should be able to output an "enriched" version of the original SBOM, populated with the license information and review status discovered during the check.

### **Links to Eclipse Project** 
- [Eclipse Dash](https://projects.eclipse.org/projects/technology.dash)
- [Eclipse Dash License Tool](https://github.com/eclipse-dash/dash-licenses)
- This feature is discussed in [Issue 191](https://github.com/eclipse-dash/dash-licenses/issues/191)

### **Expected outcomes** 

- Implement parsers for CycloneDX (JSON/XML) and SPDX (JSON/Tag-Value) that extract a list of dependencies for the Dash Tool to process.
- Integrate the extracted data into the existing Dash License Tool licence identification workflow.
- Add a feature to generate an updated SBOM file that merges the original data with the discovered license information.
- Add new command-line arguments (e.g., `--sbom-input` and `--sbom-output`) to support this workflow.
- Provide comprehensive unit tests and user documentation for the new features.
- Be open and transparent (e.g., discuss implementation ideas using issues and public discussion channels; contribute code as pull requests)

### **Skills required/preferred** 

- Basic understanding with Java (the tool is written in Java).
- Understanding of dependency management (GAVs, PURLs, etc.).
- Some familiarity with SBOM standards (CycloneDX and SPDX).

### **Project size** 

175 or 350 hours (The scope is flexible; a 175-hour project could focus on one format like CycloneDX, while 350 hours would cover both formats and the enrichment/output features).

### **Possible mentors:** 

[Wayne Beaton](https://projects.eclipse.org/projects/technology.dash/PL/wbeaton)

**Do not email maintainers to ask questions about this project. Do not ask for hints or tips on how to "win" this project.** Open source depends on openness and transparency. So, step one is: be open and transparent. If you have questions, ask them either as a comment on this issue, on [Issue 191](https://github.com/eclipse-dash/dash-licenses/issues/191), or start a [discussion](https://github.com/eclipse-dash/dash-licenses/discussions).

### **Rating** 

Medium

### **Hints**

- Plan on using standard libraries like `cyclonedx-core-java` and `spdx-j

*[truncated]*

---

## #29: Getting Eclipse ThreadX "Getting Started" restarted

**Labels:** GSoC 2026, Project Idea

**Description** 

The goal of this project is to build a set of new "Getting Started" demos and samples showcasing [Eclipse ThreadX](https://threadx.io) and its companion components (NetX Duo, FileX, GUIX, and USBX). The code will target specific evaluation boards from major silicon vendors.

Eclipse ThreadX is the world's first and only Real-Time Operating System (RTOS) certified for safety-critical applications. Deployed in over 12 billion devices since 1997, it is still going strong. From 2109 to 2023, ThreadX was known as Microsoft Azure RTOS. During that time, Microsoft worked with its silicon partners (Microship, NXP, Renesas, and STMicroelectronics) to provide hardware enablement and developer tooling support. Microsoft contributed Azure RTOS and the ThreadX trademarks to the Eclipse Foundation in November 2023. Since then, the Eclipse Foundation and the Eclipse ThreadX project team have been working together to create a true open source ecosystem around the project. 

The Azure RTOS team at Microsoft built and maintained [a repository named _Getting Started_](https://github.com/eclipse-threadx/getting-started), which contained sample code pre-configured to run on popular evaluation boards from Microsoft's partners. Since the transition to Eclipse, this repository has been mostly untouched. The applications it contains showcase integration to Microsoft Azure IoT, which is not a goal of the Eclipse ThreadX project. 

In 2024, the Eclipse ThreadX team started [a new repository called IoT DevKit](https://github.com/eclipse-threadx/iot-devkit/) to replace Getting Started. For the time being, this repository is focused on the AZ3166 board from MXChip only, since Microsoft donated hundreds of those boards to Eclipse.   

***Practical goals***

- Build a set of clean, empty starter applications targeting several popular evaluation boards
- Taking inspiration from IoT DevKit, build samples and demonstrations leveraging the hardware features of the boards (sensors, buttons, screen, WiFi, Bluetooth, etc.)
- Ensure the samples and demos can be built and run using CMake or the IDEs provided by the selected board's vendors (example: STM32CubeIDE and STM32CubeIDE for VS Code in the case of STMicroelectronics.
- Nice-to-have: Some video content showcasing the work above!

**Links to Eclipse Project**
 
- [GitHub organisation](https://github.com/eclipse-threadx)
- [Eclipse ThreadX](https://github.com/eclipse-threadx/threadx)
- [Eclipse ThreadX NetXDuo](https://github.com/eclipse-threadx/netxduo)
- [Eclipse ThreadX USBX](https://github.com/eclipse-threadx/usbx)
- [Eclipse ThreadX FileX](https://github.com/eclipse-threadx/filex)
- [Eclipse ThreadX GUIX](https://github.com/eclipse-threadx/guix)


**Expected outcomes**

- A fresh set of samples and demos targeting at least two distinct evaluation boards
- Documentation describing how to keep the samples and demos up-to-date when vendors release SDK updates
- Some video content (optional)

**Skills required/pr

*[truncated]*

---

## #28: [Eclipse Thingweb] Nodejs on embedded boards in Web of Things

**Labels:** GSoC 2026, Project Idea

## Description

The [Web of Things](https://www.w3.org/WoT/) (WoT) aims to enhance interoperability and usability across diverse Internet of Things (IoT) platforms by leveraging standard web technologies. Central to this is the [Thing Description](https://www.w3.org/TR/wot-thing-description11/) (TD), a standardized metadata model that describes the capabilities and interfaces of IoT devices, enabling seamless integration and interaction.

The Eclipse Thingweb project provides open-source tools and libraries for WoT development. In particular, the node-wot project is a powerful NodeJs-based Web of Things (WoT) runtime, allowing applications to consume (use) and expose (create) IoT devices using standardized Thing Descriptions (TDs). However, its current implementation is designed for regular server/edge devices and is not optimized for resource-constrained microcontrollers like the Raspberry Pi Pico.

This project aims to port node-wot to the [Raspberry Pi Pico 2 ](https://www.raspberrypi.com/products/raspberry-pi-pico-2/) by adapting its execution model to run efficiently on constrained hardware. The project will also explore performance optimizations and implement a UDP-based socket to enhance support for CoAP-based protocols, commonly used in low-power IoT scenarios.

Students will not need to re-write the whole runtime but they can use off-shelf solutions like: [Kalumajs](https://kalumajs.org/). 

#### Practical goals

1. Deploy a simple node-wot application to Pico 2
    - Implement an IoT sensor in Javascript, expose a Thing Description using Node-wot 
    - Verify that everything works using a node-wot desktop application. 
2. Reduce node-wot bundle size by removing the dependency from AJV. 
    - Find innovative ways to support JSONSchema validation in the embedded board (pre-compile schemas or implement a lightweight validation library).
3. Support CoAP:
    - Introduce a UDP-based transport layer to support CoAP interactions
4. Port node-wot to other JS-enabled boards:
    - As an optional step students can decide to evaluate other boards

## Links to Eclipse Project

- [Thingweb - EF](https://projects.eclipse.org/projects/iot.thingweb)
- [Thingweb - node-wot](https://github.com/eclipse-thingweb/node-wot)
- [Thingweb - website](https://thingweb.io/)

## Expected Outcomes
- Updates to node-wot code base to make it more friendly for the embedded world.
- Documentation and tutorials about how to develop node-wot applications for Raspberry Pico and possibly other boards.

## Skills required/preferred

This project is ideal for embedded systems and IoT enthusiasts with experience in:

- JavaScript/TypeScript (Node.js)
- Microcontroller programming (C/C++ for RP2040, MicroPython, or Espruino)
- Networking (CoAP, UDP, MQTT, HTTP on embedded devices)

## Project Size

175 hours

## Possible Mentors

- [Ege Korkan](https://projects.eclipse.org/projects/iot.thingweb/PL/ekorkan)
- [Cristiano Aguzzi](https://projects.eclipse.org/projects/iot.thingwe

*[truncated]*

---

## #27: [Eclipse 4diac] Test Suite for Type Management Refactorings in 4diac IDE

**Labels:** GSoC 2026, Project Idea

## **Test Suite for Type Management Refactorings in 4diac IDE**

### **Description** 
The Type Management component in 4diac IDE provides refactorings such as rename/move/copy/delete for FB types, SubApp types, and data types, plus follow-up updates (e.g., reconnect pins, update instances, repair broken connections). This code is complex (EMF model edits + Eclipse LTK refactoring + workspace resources) and currently lacks dedicated automated regression tests.
This project will implement a comprehensive JUnit 5 test suite that programmatically executes core refactorings and validates model + resource correctness (including undo/redo), enabling safer maintenance and future refactoring work in 4diac IDE.

### **Links to Eclipse Project** 
 [Project](https://eclipse.dev/4diac/)

 [Repository](https://github.com/eclipse-4diac/4diac-ide)

### **Expected outcomes** 
- New automated test coverage for org.eclipse.fordiac.ide.typemanagement.refactoring (rename/move/copy/delete + critical follow-up edits).

- A small reusable “refactoring test framework” inside the 4diac test bundles.

- Test data projects/fixtures that reproduce realistic refactoring scenarios.

- Developer documentation for maintaining and extending the suite.

- An infrastrucuture for “before/after” refactoring scenarios: load input .sys/.fbt/.subapp resources into an Eclipse test workspace, execute the refactoring, and assert correctness by comparing the resulting files and relevant EMF model state against expected output fixtures.

### **Skills required/preferred** 
- Java (comfortable), JUnit 5

- Basic Eclipse platform knowledge (workspace/resources, plug-in tests)

- EMF/GEF basics helpful (model edits and commands)

- Interest in software quality/testing

### **Project size** 
175/350 hours

175h: rename (including transitive renaming) + move + basic delete scenarios + undo/redo

350h: plus copy refactoring, connection-repair/struct refactoring


### **Possible mentors:** 
[Michael Oberlehner](mailto:michael.oberlehner@jku.at)

### **Rating** 
Medium

---

## #26: [Eclipse Thingweb] Enhancing TD Directories with MCP-driven Capabilities

**Labels:** GSoC 2026, Project Idea

### **Description** 

Our Thing Description Directory Domus can manage TDs of devices in the field. The users are expected to use our REST API to add, update, delete and query TDs. We want to make it easy for AI Agents to interact with our TDD via the Model Context Protocol. In addition to managing TDs, we want the users to be able make interactions with the devices, leveraging a new interface exposed to MCP. This way, it will be possible to make more complex queries such as giving the average temperature of all Things in a certain location, i.e. mixing static knowledge in TDs with dynamic data from the physical world.

#### Strongly Recommended Preparation for the Project

* Reading the specification https://www.w3.org/TR/wot-discovery/#exploration-directory-api 
* Testing the Domus TDD API project linked below
* Reading the MCP documentation: https://modelcontextprotocol.io/docs/getting-started/intro
* Experimenting with MCP libraries (not just with chat software like Claude). See https://modelcontextprotocol.io/docs/sdk 

### **Links to Eclipse Project** 

* [Website](https://thingweb.io/)
* [Eclipse Project Page](https://projects.eclipse.org/projects/iot.thingweb)
* [Repository relevant for the GSoC project](https://github.com/eclipse-thingweb/domus-tdd-api )


### **Expected outcomes** 

* TDs managed by the TDD can be used by AI Agents via MCP
* TDD can interact with Things by sending messages over the protocol they support

### **Skills required/preferred** 

* **Required:** Proficiency in Python
* **Required:** REST API Design
* **Preferred:** Previous experience with SPARQL
* **Required:** Good understanding of MCP Architecture
* **Strongly Recommended:** Familiarity with the Web of Things (WoT) architecture.

### **Project size** 

175 hours

### **Possible mentors:** 

- [Christian Glomb](https://projects.eclipse.org/projects/iot.thingweb/CM/cglomb)
- [Ege Korkan](https://projects.eclipse.org/projects/iot.thingweb/PL/ekorkan)
- [Cristiano Aguzzi](https://projects.eclipse.org/projects/iot.thingweb/PL/caguzzi)
- [Daniel Peintner](https://projects.eclipse.org/projects/iot.thingweb/CM/dpeintner)


### **Rating** 
Medium

### **Overall Rules**

1. We deeply value previous interactions with the community. Community interactions include but are not limited to:
  - Chatting with the community on [Discord](https://discord.gg/RJNYJsEgnb) and/or [Telegram](https://t.me/nodewot)
  - Showing something you are doing with WoT components: Example
  - Doing substantial Pull Requests in our repositories that are merged by the maintainers. The Pull Request does not have to be related to a project idea we have provided.
2. We appreciate applicants who used similar technologies before and can demonstrate that (repositories, screenshots, designs, documentation)
3. Please do your chat-level interactions in a group so that everybody sees your involvement. Limit your one-to-one interactions to specific questions that can only be answered by them.
4. Each proje

*[truncated]*

---

## #25: [Eclipse EdiTDor] Web of Things in VS Code

**Labels:** GSoC 2026, Project Idea

## **Web of Things in VS Code**

### **Description** 

Our td-code extension for VS Code allows developers to access basic tooling for Thing Descriptions. Meanwhile, we have other projects that provide tooling for the browser or Node.js environments. We want to bring them under one roof in td-code where EdiTDor project is leveraged like a Swagger viewer (e.g. https://marketplace.visualstudio.com/items?itemName=Arjun.swagger-viewer) for TDs while other tools linked below can be used via the command palette. All these tools should work seamlessly without the developers leaving the VS Code environment. Examples of workflows:
- Send requests to IoT devices via the rendered EdiTDor window
- Transform TDs into different formats like AsyncAPI, OpenAPI
- Do advanced validations of TDs
- Generate request code for IoT devices

### **Links to Eclipse Project** 

* [Website](https://thingweb.io/)
* [Eclipse Project Page](https://projects.eclipse.org/projects/iot.thingweb)
* [td-code](https://github.com/eclipse-thingweb/td-code)
* [EdiTDor](https://github.com/eclipse-editdor/editdor)
* [Playground Tooling](https://gitlab.eclipse.org/eclipsefdn/emo-team/gsoc-at-the-ef/-/issues/github.com/eclipse-thingweb/github.com/eclipse-thingweb/playground)
* [TD Tools ](https://github.com/eclipse-thingweb/td-tools/tree/main/node)

### **Expected outcomes** 

* More capability for the vs-code as mentioned in the description
* EdiTDor npm package

### **Skills required/preferred** 
* **Required:** Strong proficiency in TypeScript and Modern JavaScript (ES6+)
* **Strongly Recommended:** Familiarity with the Web of Things (WoT) architecture.

### **Project size** 
350 hours

### **Possible mentors:** 

- [Ege Korkan](https://projects.eclipse.org/projects/iot.thingweb/PL/ekorkan)
- [Ricardo Silva](https://projects.eclipse.org/projects/iot.editdor/CM/techinaco)
- [Cristiano Aguzzi](https://projects.eclipse.org/projects/iot.thingweb/PL/caguzzi)
- [Daniel Peintner](https://projects.eclipse.org/projects/iot.thingweb/CM/dpeintner)


You can reach out to the mentors through Telegram or Discord linked above.

### **Rating** 
medium

### Project-specific Instructions

Make sure to try out td-code in your vs code and EdiTDor in your browser

### **Overall Rules**

1. We deeply value previous interactions with the community. Community interactions include but are not limited to:
  - Chatting with the community on [Discord](https://discord.gg/RJNYJsEgnb) and/or [Telegram](https://t.me/nodewot)
  - Showing something you are doing with WoT components: Example
  - Doing substantial Pull Requests in our repositories that are merged by the maintainers. The Pull Request does not have to be related to a project idea we have provided.
2. We appreciate applicants who used similar technologies before and can demonstrate that (repositories, screenshots, designs, documentation)
3. Please do your chat-level interactions in a group so that everybody sees your involvement. Limit your one-to-one interactions to specific questions that can only be answered by them.
4. Each project idea has some specifi

*[truncated]*

---

## #24: [Eclipse Thingweb] WoT Bindings for Agent Communications and Smart Home

**Labels:** GSoC 2026, Project Idea

## **WoT Bindings for Agent Communications and Smart Home**

### **Description** 

The W3C Web of Things (WoT) architecture provides a standardized way to describe and interact with Things using Thing Descriptions (TDs). node-wot is one of the most widely used runtime implementations of the WoT architecture in JavaScript/TypeScript.

Currently, node-wot  supports a limited set of protocol bindings (e.g., HTTP, CoAP, MQTT, OPC UA, WebSockets). However, the IoT ecosystem is rapidly evolving, and new communication standards and interaction models are gaining adoption, such as:
- Matter (smart home interoperability)
- MCP (Model Context Protocol)
- UTCP
- A2A (Agent-to-Agent communication)
- Other emerging or domain-specific protocols

Without bindings for these protocols, developers must build custom integrations that bypass the WoT abstraction layer, reducing interoperability and reuse.

The main goal of this project is to design, implement, and document new node-wot bindings.

### **Links to Eclipse Project** 

* [Website](https://thingweb.io/)
* [Eclipse Project Page](https://projects.eclipse.org/projects/iot.thingweb)
* [node-wot](https://github.com/eclipse-thingweb/node-wot)
* Binding Mechanism: https://www.w3.org/TR/wot-thing-description-2.0/#bindings 

### **Expected outcomes** 

* Evaluation of Matter, MCP, UTCP, A2A, and similar protocols against the WoT interaction model
* Binding specifications on how WoT concepts (Properties, Actions, Events) map to each protocol’s communication primitives
* node-wot binding packages following reusable, modular bindings following node-wot extension patterns
* Examples demonstrating usage with sample Things and Consumers

### **Out of Scope**

- Redefinition of the WoT standard
- Low-level protocol implementation from scratch
- Closed-spec protocols

### **Target audience**

- IoT developers using node-wot
- Smart home and Matter ecosystem developers
- Researchers and early adopters working on agent-based systems
- Standards bodies and open-source contributors

### **Skills required/preferred** 

* **Required:** Affinity to read and understand protocol specifications
* **Required:** Strong proficiency in TypeScript and Modern JavaScript (ES6+)
* **Strongly Recommended:** Familiarity with the Web of Things (WoT) architecture.
* **Preferred:** Understanding of how internet-layer protocols work

### **Project size** 
350 hours

### **Possible mentors:** 

[Ege Korkan](https://projects.eclipse.org/projects/iot.thingweb/PL/ekorkan)
[Cristiano Aguzzi](https://projects.eclipse.org/projects/iot.thingweb/PL/caguzzi)
[Daniel Peintner](https://projects.eclipse.org/projects/iot.thingweb/CM/dpeintner)
[Jan Romann](https://projects.eclipse.org/projects/iot.thingweb/CM/jromannojt)

### **Overall Rules**

1. We deeply value previous interactions with the community. Community interactions include but are not limited to:
  - Chatting with the community on [Discord](https://discord.gg/RJNYJsEgnb) and/or [Telegram](https://t

*[truncated]*

---

## #23: [Eclipse Thingweb] node-wot Online Playground

**Labels:** GSoC 2026, Project Idea

## **node-wot Online Playground**

### **Description** 

The goal of this project is to lower the barrier to entry for the Web of Things (WoT) by creating a browser-based "Playground" for node-wot. Currently, developers must install Node.js, set up a local environment, and configure dependencies to start experimenting with WoT. We want to eliminate this friction by creating an online environment—similar to CodePen or StackBlitz—where users can write, run, and interact with Web Things directly in their browser.
This is a significant architectural challenge that involves adapting the [node-wot browser bundle](https://github.com/eclipse-thingweb/node-wot/tree/master/packages/browser-bundle) to communicate with browser-defined Things. The student will build a web application that features:

- Code Editor: A primary view using a web-based editor (e.g., Monaco Editor) where users define the logic of an exposed Thing.
- Runtime Environment: A mechanism to run this code in the browser (e.g., via Web Workers).
- Interaction View: A secondary view to interact with the simulated Thing. This could be a custom client script or an automatic UI rendered by the UI-WoT library.

Key Architectural Challenge: Browser Bindings. A core objective is enabling communication between the "Virtual Thing" and the "Client" within the browser constraints. The student must investigate and implement one of the following approaches:

- In-Memory "Mock" Binding: Creating a virtual protocol binding that routes messages between the Thing and Client within the browser memory. This is easier to implement but limits the Thing to the local tab (it cannot be accessed by external tools).
- WebRTC Binding: Implementing a binding based on WebRTC. This allows the Thing to generate a valid Thing Description (TD) that can be shared with others, enabling true peer-to-peer interaction between different browsers/computers.

This project is ideal for a student interested in browser runtimes, web protocols, and advanced TypeScript application architecture.

### **Links to Eclipse Project** 

* [Website](https://thingweb.io/)
* [Eclipse Project Page](https://projects.eclipse.org/projects/iot.thingweb)
* [node-wot](https://github.com/eclipse-thingweb/node-wot)
* [ui-wot](https://github.com/eclipse-thingweb/ui-wot)

### **Expected outcomes** 
* A fully functional web application acting as a WoT Playground.
* Integration of a code editor (Monaco or CodeMirror) with TypeScript support/intellisense for `node-wot` APIs.
* Implementation of a "Browser Binding" (Mock, WebRTC, MQTT over WebSockets, or Websockets) allowing the `node-wot` core to function inside a browser environment without Node.js APIs.
* Integration with **UI-WoT** to automatically render controls based on the Thing Description generated in the editor.
* Documentation on how to use the playground and examples of "Virtual Things".

### **Skills required/preferred** 

* **Required:** Strong proficiency in TypeScript and Modern JavaScript (ES

*[truncated]*

---

## #22: [Eclipse 4diac] Extending the IO Layer of 4diac FORTE

**Labels:** GSoC 2026, Project Idea

## **Project Idea Name**
<!-- 
If you are interested in mentoring a project please use this template to submit your Project Idea for the GSoC programme.
The format suggested below is exactly that, a suggestion. Play with the layout, but please make sure to provide all relevant information. Please be sure to follow branding guidelines (e.g. "Eclipse Dash", not "Dash"). Links to content hosted elsewhere are fine, but bear in mind that this GitLab project and its issues will be the main point of contact for people who are not already inside your community.
-->

### **Description** 
Recent changes to the IO layer in 4diac FORTE have established a solid foundation for supporting fieldbus and hardware bus systems. At present, 4diac FORTE supports several IO buse systems, including Embrick, Revolution Pi, WAGO K-Bus, and a generic GPIO chip layer for Linux-based systems.

Building on this foundation, we aim to further enhance the IO layer with a focus on improved usability and extensibility, as well as support for a broader range of bus systems. Planned additions include:

- Modbus
- I2C
- The new generation of LEGO Mindstorms (e.g., SPIKE)

### **Links to Eclipse Project** 
Both to the [Eclipse 4diac](https://eclipse.dev/4diac/) and [Project Repository](https://github.com/eclipse-4diac/4diac-forte).

### **Expected outcomes** 

- List of usability issues
- List of potential improvements
- IO Layer improvements
- Documentation of results
- At least one bus implementation

### **Skills required/preferred** 
Good C++ experience, knowledge of design patterns, and basic understanding of IO and field bus systems.

### **Project size** 
175 hours or 350 hours (scope can be adjusted)

### **Possible mentors:** 
[Michael Oberlehner](mailto:michael.oberlehner@jku.at)

### **Rating** 
Hard

---

## #21: [Eclipse 4diac] Improving the Usability of the 4diac IDE's State Machine Editor

**Labels:** GSoC 2026, Project Idea

## **[Eclipse 4diac] Improving the Usability of the 4diac IDE's State Machine Editor**
<!-- 
If you are interested in mentoring a project please use this template to submit your Project Idea for the GSoC programme.
The format suggested below is exactly that, a suggestion. Play with the layout, but please make sure to provide all relevant information. Please be sure to follow branding guidelines (e.g. "Eclipse Dash", not "Dash"). Links to content hosted elsewhere are fine, but bear in mind that this GitLab project and its issues will be the main point of contact for people who are not already inside your community.
-->

### **Description** 
Over the last years, the several graphical editors in 4diac IDE were reworked to make them more usable and to reduce the number of user interactions. These are, for example, the FB network editor or the FB interface editor. One editor that didn't get the full treatment is the state machine editor.With this project, we would like to explore what issues we have in this editor and how we can improve the usability of this editor. Topics of a potential project are:

 - identify usability issues
 - group them regarding implementation effort
 - fix usability issues
 - document results

### **Links to Eclipse Project** 
Both to the [Eclipse 4diac](https://eclipse.dev/4diac/) and [Project Repository](https://github.com/eclipse-4diac/4diac-ide).

### **Expected outcomes** 
  - List of usability issues and potential improvements
  - **Improved editor**
  - Documentation of results 

### **Skills required/preferred** 
Strong programming skills in Java and knowledge of Eclipse GEF Classic are required.

### **Project size** 
175 hours or 350 hours (scope can be adjusted)

### **Possible mentors:** 
[Alois Zoitl](mailto:alois.zoitl@gmx.at)

### **Rating** 
Medium to hard

---

## #1: Adding a new project idea in our brand new GSoC project

**Labels:** GSoC 2026, Project Idea

## **Adding a new project idea in our brand new GSoC project**

### **Description** 

  In this project you'll learn how to submit a new project idea in our brand new GSoC project. 

### **Relevant Links**

- [Link to the GitLab GSoC for EF project](https://gitlab.eclipse.org/eclipsefdn/emo-team/gsoc-at-the-ef) 

- [Link to submit a new project idea](https://gitlab.eclipse.org/eclipsefdn/emo-team/gsoc-at-the-ef/-/issues/new?issuable_template=GSoC_projectidea)

### **Expected outcomes** 

  After completing this project you'll be able to submit a project idea for GSoC at the EF by yourself.

### **Skills required/preferred** 

  Basic computer skills and 5-10 minutes for each project idea submitted.

### **Project size** 

  5 minutes

### **Possible mentors:** 

  [EMO](https://gitlab.eclipse.org/eclipsefdn/emo-team/gsoc-at-the-ef/-/issues/github.com/eclipse-thingweb/emo@Ecipse-foundation.org)

### **Rating** 

  Easy :smile:

---
