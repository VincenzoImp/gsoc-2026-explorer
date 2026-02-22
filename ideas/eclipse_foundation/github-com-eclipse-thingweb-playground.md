# Playground Tooling

**Parent:** Eclipse Foundation — Project Ideas
**Source:** https://gitlab.eclipse.org/eclipsefdn/emo-team/gsoc-at-the-ef/-/issues/github.com/eclipse-thingweb/playground
**Scraped:** 2026-02-22T23:28:47.613397

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
