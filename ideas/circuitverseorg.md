# CircuitVerse.org — Project Ideas

**Source:** https://github.com/CircuitVerse/CircuitVerse/wiki/GSoC'26-Project-List
**Scraped:** 2026-03-10T16:58:40.317097

---

# CircuitVerse GSoC 2026 Project Ideas

This document presents the project ideas for CircuitVerse's participation in **Google Summer of Code (GSoC) 2026**. CircuitVerse is an open-source platform dedicated to digital logic education, and we invite motivated candidates to contribute to its continued growth and improvement. The following projects aim to enhance functionality, performance, scalability, and user experience. Candidates are also encouraged to submit original proposals aligned with the platform's long-term objectives.

Many of the ideas listed below may be **intentionally over-scoped**. This is done to provide flexibility for candidates to tailor their proposals based on interests and strengths. The final set of deliverables will be decided through discussions between mentors and selected contributors to ensure realistic goals and effective use of the GSoC timeline.

---

## Essential Information

* **Community Engagement:** Join discussions and receive updates via our [Slack Channel](https://circuitverse.org/slack).
* **Proposal Submission:** Use the official [Proposal Template](https://docs.google.com/document/d/1oeYPAuqWxeC79d-R5I9uFJywQJv4ooO4obF4pwifyTY/edit?usp=sharing) (Google Docs recommended).
* **Project Discussions:** Collaborate and refine ideas on [GitHub Discussions](https://github.com/orgs/CircuitVerse/discussions/6489).

---

## Project 1: Structured Format for Saved Circuit Data

**Duration:** 175 – 350 hours  
**Difficulty:** Hard  
**Technologies:** Ruby on Rails, JavaScript, JSON

Currently, CircuitVerse stores circuits as unstructured JSON objects where components are serialized based on placement order rather than logical hierarchy. As a result, two logically identical circuits can produce entirely different saved files. This makes the data unsuitable for advanced use cases such as Verilog generation, robust version control, circuit diffing, and large-scale machine learning or LLM-based analysis.

This project aims to design and implement a **structured, canonical data format** for saving circuits. The new format should be deterministic, logically consistent, and independent of visual layout. Circuits will be represented as ordered netlists or graph-based structures, enabling future features such as automated synthesis, AI-assisted circuit design, and semantic comparisons between circuits.

**Key Deliverables:**

* Canonical, deterministic representation of circuits
* Logical netlist-based serialization independent of placement order
* Backward compatibility with existing circuit files

**Additional Features:**

* **Human-Readable Schema:** Define a strict JSON schema for easier debugging and manual inspection.
* **Visual–Logic Separation:** Decouple logical connectivity from visual metadata (x, y coordinates, canvas layout).
* **Idempotent Converter:** Build a migration tool to convert legacy `.cv` files into the new standardized format without data loss.

**Learning Path:**

* JSON Schema design and validation
* CircuitVerse simulator internals (serialization of `CircuitElement`)
* Graph Theory: Graph isomorphism and canonical graph representations
* EDA standards such as SPICE and EDIF for inspiration

**Possible Mentors:** [JoshVarga](https://github.com/JoshVarga), [Arnabdaz](https://github.com/Arnabdaz), [Aryann Dwivedi](https://github.com/aryanndwi123)

---

## Project 2: Assignment Suite & Classroom Workflow Enhancement

**Duration:** 175 hours  
**Difficulty:** Easy  
**Technologies:** Ruby on Rails, JavaScript

This project focuses on strengthening CircuitVerse's classroom and assignment infrastructure to better support educators and students. Contributors will extend the assignment suite with multi-level classroom structures, enabling subgroup formation for collaborative projects and flexible submission workflows.

The project also includes enhancing assignments with pre-built circuit templates, integrated test cases, and auto-verification from practice sessions. Improvements to Canvas LMS integration and Learning Tools Interoperability (LTI) support will further enhance CircuitVerse's adoption in academic environments.

**Key Deliverables**

* Multi-level classroom and subgroup support
* Group and individual assignment workflows
* Pre-configured circuit assignments with test cases
* Improved Canvas LMS and LTI integration

**Learning Path:**

* Ruby on Rails via The Odin Project
* JavaScript fundamentals via MDN Web Docs
* Canvas LMS Developer APIs
* Learning Tools Interoperability (LTI)

**Possible Mentors:** [Anas Khan](https://github.com/anxkhn), [Aman Asrani](https://github.com/Asrani-Aman), [Harsh Bhadu](https://github.com/senbo1)

---

## Project 3: FSM to Circuit Synthesizer

**Duration:** 175 hours  
**Difficulty:** Medium  
**Technologies:** HTML5, CSS, JavaScript, Ruby on Rails

Finite State Machines (FSMs) are foundational concepts in digital logic and automata theory. This project aims to introduce an FSM editor within CircuitVerse that allows users to visually design FSMs and automatically synthesize them into corresponding digital circuits.

The project will support Moore and Mealy machines and can be extended to demonstrate additional computational models such as DFA, NFA, PDA, and Turing Machines. Contributors are encouraged to build upon or integrate existing open-source FSM editors.

**Expected Outcomes:**

* Visual FSM editor inside CircuitVerse
* Automatic FSM-to-circuit synthesis
* Support for Moore and Mealy machines

**Resources:**

* [http://www.cburch.com/proj/autosim/](http://www.cburch.com/proj/autosim/)
* [http://madebyevan.com/fsm/](http://madebyevan.com/fsm/)

**Possible Mentors:** [Vivek Kumar](https://github.com/092vk), [Harsh Rao](https://github.com/ThatDeparted2061)

---

## Project 4: CircuitVerse Simulator integration

**Duration:** 175 – 350 hours  
**Difficulty:** Hard  
**Technologies:** HTML5, CSS, JavaScript, Canvas API

Circuitverse.org currently uses the legacy simulator written using Jquery UI. We need to replace it with the Vuejs version and make it live on circuitverse.org

**Key Deliverables**

* Separate simulator-<version>.js and simulator-embed-<version>.js as separate output files.
* Integrate simulator session with rails session
* Implement authentication mechanism for desktop version using Tauri
* Improve circuit debugging experience

**Learning Path:**

* CircuitVerse simulator internals

**Possible Mentors:** [Nihal Rajpal](https://github.com/Nihal4777), [Arnabdaz](https://github.com/Arnabdaz), [Niladri Adhikary](https://github.com/niladrix719), [Harsh Rao](https://github.com/ThatDeparted2061)

---

## Project 5: CircuitVerse Mobile App: Feature Parity with Web Platform and Deployment Readiness

**Duration:** 175 hours  
**Difficulty:** Medium  
**Technologies:** Flutter, Dart, JavaScript

The CircuitVerse mobile application currently lacks several core features and stability compared to the web platform, which limits its effectiveness as a learning tool. This project aims to enhance the mobile application by achieving feature parity with the CircuitVerse website while improving performance, usability, and maintainability.

The primary objective is to stabilize authentication, restore and enhance the interactive book module, and resolve existing technical and UI issues. The project will ensure a consistent user experience across platforms by aligning mobile UI components with the web interface and improving accessibility.

Additionally, the project will prepare the application for production deployment by improving code quality, fixing critical bugs, and implementing scalable architecture. Support for localization and region-specific language requirements will be strengthened, including improvements to the simulator and learning modules for multilingual users.

By the end of the project, the CircuitVerse mobile application will be fully functional, reliable, and ready for public deployment, providing students worldwide with seamless access to CircuitVerse's interactive learning resources.

**Key Deliverables:**

* Implementation of core web features in the mobile application
* Stable and secure authentication system
* Fully functional interactive book module
* Improved UI consistency and accessibility
* Bug fixes and performance optimization
* Enhanced localization and multilingual support
* Production-ready deployment configuration

**Learning Outcomes:**

Participants will gain hands-on experience in:

* Flutter and Dart application development
* API integration and authentication systems
* Mobile–Web architecture and WebView integration
* Localization and internationalization techniques
* Mobile UI/UX design and accessibility standards
* Software testing, debugging, and deployment practices

**Possible Mentors:** [Hardik Sachdeva](https://github.com/hardik17771), [Yashvant Singh](https://github.com/JatsuAkaYashvant)

---

## Project 6: Enterprise & Institutional Organization Features

**Duration:** 350 hours  
**Difficulty:** Medium – Hard  
**Technologies:** Ruby on Rails, PostgreSQL, Devise, OAuth/OIDC

Currently, CircuitVerse handles users and classrooms individually. However, large universities and organizations need a way to manage multiple groups, instructors, and students under a single umbrella. This project aims to introduce an Organization layer to the platform, allowing for hierarchical management and professional-grade security features.

This will involve architecting a multi-tenant-like structure where "Org Admins" can oversee multiple classrooms and ensure seamless onboarding through Single Sign-On (SSO).

**Key Deliverables:**

* **Hierarchical Org Structure:** Ability to create an Organization and nest multiple "Groups" within it.
* **SSO Support:** OpenID Connect (OIDC) to allow students to log in using institutional credentials (e.g., Google Workspace, Microsoft Azure AD).
* **Role-Based Access Control (RBAC):** Distinct permissions for Org Admins, Group Leads, and Instructors.
* **Custom Branding (Optional):** Basic support for custom subdomains (e.g., university.circuitverse.org) and logo placement for institutional identity.

**Learning Path:**

* Multi-tenancy patterns in Ruby on Rails
* Authentication protocols (OAuth 2.0, OIDC)
* Advanced PostgreSQL indexing for organizational queries
* Security best practices for enterprise software

**Possible Mentors:**

Vedant Jain , Yashika Jotwani, Pratham

---

## Project 7: Client-Side Verilog Synthesis

**Duration:** 350 hours  
**Difficulty:** Hard  
**Technologies:** Vue.js, JavaScript/TypeScript, WebAssembly (YoWASP/YosysJS), Tauri, Rust

### Objective
This project aims to modernize the CircuitVerse synthesis pipeline. The primary goal is to **eliminate all network calls** for Verilog synthesis, enabling the **CircuitVerse Desktop version** to function entirely offline. By porting synthesis logic to the browser and moving toward a Tauri-based desktop architecture, we ensure a faster, more privacy-respecting, and robust experience for all users.


### Key Deliverables

* **Wasm Synthesis Engine (The Rewrite):** Develop a client-side layer to replace `yosys2digitaljs-server`. This involves:
    * Integrating **YoWASP** (Yosys via WebAssembly) via Web Workers.
    * Replace yosys interface from running cli program to invoking web assembly build .
* **Offline Readiness:** Ensure the entire synthesis pipeline is self-contained within the Tauri/Desktop environment without any external API or backend dependencies.

### Learning Path
* **Vue.js & State Management:** Debugging and optimizing complex reactive components.
* **WebAssembly & Tauri:** Running heavy C++ logic in a sandboxed environment and interfacing it with a Rust-based desktop framework.
* **RTL Synthesis:** Understanding the translation from HDL to gate-level netlists.
* **Graph Theory:** Applying automated layout engines to prevent "spaghetti" wiring in synthesized circuits.

### Possible Mentors

[Vivek Kumar](https://github.com/092vk), [Harsh Rao](https://github.com/ThatDeparted2061)

---

## Propose Your Own Project Idea

Candidates are encouraged to submit original project proposals. Submissions should include:

1. A clear description of the proposed concept and the problem it addresses.
2. Supporting visual materials, such as wireframes, mockups, or screenshots.
3. Identification of the intended beneficiaries (e.g., students, educators, or hardware users).
4. A detailed implementation plan outlining the approach and timeline.

Prior to submission, candidates should consult with mentors on [Slack](https://circuitverse.org/slack) or [GitHub Discussions](https://github.com/orgs/CircuitVerse/discussions/5388) to refine their proposals.

---

## Conclusion

The projects outlined above provide a foundation for meaningful contributions to CircuitVerse during GSoC 2026. Each initiative offers opportunities for skill development and collaboration within an open-source community dedicated to advancing digital logic education. Candidates may select a listed project or propose a unique idea, and we look forward to working together to enhance the platform's capabilities.
