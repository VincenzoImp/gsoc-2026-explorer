# FLARE — Project Ideas

**Source:** https://github.com/mandiant/flare-gsoc/blob/2026/doc/project-ideas.md
**Scraped:** 2026-02-22T23:28:47.581045

---

# Project Ideas
*FLARE @ Google Summer of Code 2026*

This document lists examples of projects that would be great for GSoC 2026 contributors.
The list doesn't include everything - feel free to identify your own idea and propose it!

All of our project ideas revolve around reverse engineering tools.
That is, we want to improve the lives of malware analysts through novel techniques and automation.
To succeed with any of these examples, you should have a basic familiarity with reverse engineering or a strong desire to learn.

Our tools are used by thousands of analysts to identify, describe, and stop malware.

Briefly:
- [capa](https://github.com/mandiant/capa) identifies the capabilities in executable files, such as "installs a service" or "downloads data via HTTP".
  - enhance static analysis
  - enhance dynamic analysis
- [FLOSS](https://github.com/mandiant/flare-floss) automatically deobfuscated protected strings in malware.
  - extract language specific strings (.NET, Swift, Zig, ...)
  - QUANTUMSTRAND
- [GoReSym](https://github.com/mandiant/GoReSym) is a Go symbol parser that extracts program metadata (such as CPU architecture, OS, endianness, compiler version, etc), function metadata, filename and line number metadata, and embedded structures and types.
- [XRefer](https://github.com/mandiant/xrefer) is an IDA plugin offering a custom navigation interface to examine execution paths, highlight downstream behaviors, cluster related functions, and generate Gemini-based insights into the malware's anatomy.
  - [Backend Expansion (Radare2 or Vivisect))](https://github.com/mandiant/flare-gsoc/blob/2026/doc/project-ideas.md#xrefer-backend-expansion-radare2-or-vivisect)
  - [Native Frontend Development (Binary Ninja or Ghidra)](https://github.com/mandiant/flare-gsoc/blob/2026/doc/project-ideas.md#xrefer-native-frontend-development-binary-ninja-or-ghidra)

## capa: Native Script Analysis Support

*size*: large, estimated 350 hours

*difficulty*: hard

*mentors*: [@mike-hunhoff](https://github.com/mike-hunhoff), [@Maijin](https://github.com/Maijin), [@larchchen](https://github.com/larchchen)

Current static analysis tools often struggle with scripting languages, relying on fragile regular expressions that are easily evaded. As adversaries increasingly "Live off the Land" using scripts, the need for robust, structural analysis is critical.

This project aims to extend the **capa** engine to natively support static analysis of scripting languages by integrating **Tree-sitter**. By moving beyond byte-sequence matching to Abstract Syntax Tree (AST) analysis, we can detect capabilities in interpreted languages with the same fidelity capa currently provides for PE, ELF, and .NET binaries.

**Deliverables**

* **Core Integration**: Integrate the `tree-sitter` parser library into capa's Python architecture.
* **Backend Development**: Develop a new analysis backend that traverses the AST to extract features (function calls, variable usage, structure) rather than using regex.
* **Language Support**: Implement initial support for \*Nix/Cloud languages (focusing on Bash and Python) or Windows (PowerShell).
* **Rule Verification**: Create a set of capa rules to demonstrate and test the new capability against real-world samples.

**Required Skills**

* Strong proficiency in Python3.
* Understanding of compilers, parsers, or Abstract Syntax Trees (AST).
* Familiarity with `tree-sitter` is a major plus.
* Knowledge of scripting languages (Bash, Python, or PowerShell).
* Basic understanding of Git and malware analysis concepts.

## capa: Automated Rule Generation Agent

*size*: large, estimated 350 hours

*difficulty*: medium to hard

*mentors*: [@mike-hunhoff](https://github.com/mike-hunhoff), [@Maijin](https://github.com/Maijin)

Mandiant’s [capa](https://github.com/mandiant/capa) is the industry standard for identifying capabilities in executable files. However, the volume of new malware variants and requested rules in our issue tracker often exceeds the capacity of human analysts. Keeping the ruleset up-to-date manually is challenging against the velocity of new threat techniques.

This project aims to develop an autonomous **capa agent** that functions as a "virtual contributor." The agent will automate the heavy lifting of rule creation by parsing GitHub Issues or analyzing raw samples, generating valid YAML rules using Large Language Models (LLMs), and crucially verifying them against the official capa linter and test runner before submission. The system adheres to a Human-in-the-Loop (HITL) philosophy: the agent does the engineering and testing, but human maintainers retain control over the final merge via Pull Requests.

**Deliverables**

* **Agent Core & Triggers**: Develop the agent logic using Google ADK to handle "Reactive" triggers (parsing GitHub Issues for context/samples) and "Proactive" triggers (scanning daily feeds).
* **Generation & Grounding**: Implement the LLM integration (e.g., Gemini) to write rules, using RAG or tool use (Google Search) to verify API definitions and shell commands.
* **Validation Loop**: Build a robust self-correction loop where the agent runs the `capa` linter and test runner, parsing error logs to fix syntax errors automatically *before* a human sees the code.
* **Automated PR Workflow**: Create the logic to package verified rules and submit them as formatted Pull Requests to `mandiant/capa-rules`, including test results in the PR description.

**Required Skills**

* Strong proficiency in Python.
* Experience with LLMs, Agents, or Prompt Engineering.
* Basic understanding of malware analysis and the capa rule format (YAML).
* Familiarity with Git, GitHub Actions, or CI/CD pipelines.

## capa: Enhance Static Analysis

_size_: medium to large

_difficulty_: medium

_mentors_: [@mike-hunhoff](https://github.com/mike-hunhoff)

This initiative focuses on advancing the static analysis capabilities of capa. Key research areas include improving program analysis to effectively distinguish between library/runtime code and programmer-written logic, allowing capa and similar tools to prioritize the program's most significant components. Furthermore, integrating AI at various stages of the analysis could provide significant enhancements.

**Deliverables**:

* Assess the current performance and functionality of capa
* Brainstorm and pinpoint specific areas for potential improvement
* Develop, validate, and provide documentation for all implemented enhancements
* Stretch Goal: Explore and build AI-driven analysis to bolster results

**Skill Requirements**:

* Strong proficiency in Python programming
* Fundamental knowledge of malware analysis
* Competency with tools like IDA Pro, Ghidra, Binary Ninja, or vivisect
* Practical experience using Git and GitHub


## capa: Enhance Dynamic Analysis

_size_: medium to large

_difficulty_: medium

_mentors_: [@mike-hunhoff](https://github.com/mike-hunhoff)

This project's goal is to improve capa's dynamic analysis functionality (i.e. VMRay sandbox runs). Potential improvements include filtering out sandbox noise, improving capa's extraction and matching algorithms, enhancing existing rules, etc. Applying AI analysis could also be part of this project.

**Deliverables**:

- Review and evaluate current capa functionality and performance
- Identify and brainstorm areas of improvement
- Implement, test, and document improvements
- Stretch goal: research and develop AI analysis to enhance capa results

**Required Skills**:

- Solid Python programming skills.
- Familiarity with dynamic (and static) analysis of malware.
- (Optional: Familiarity with VMRay sandbox analysis results).
- Experience with Git and GitHub.


## FLOSS: Extract Language Specific Strings (.NET, Swift, Zig, ...)

_size_: large, estimated 350 hours

_difficulty_: medium

_mentors_: [@mr-tz](https://github.com/mr-tz)

_link_: [https://github.com/mandiant/flare-floss/issues/718](https://github.com/mandiant/flare-floss/issues/718)

Various programming languages embed the constant data, like strings, used within executables in different ways. Most tools, like strings.exe, just look for printable character sequences. This doesn't work well for files compiled from Go or Rust.

Here we propose to extend FLOSS to include a framework to extract language specific strings from executables. After identifying the language, a specific extractor can use specialized logic to pull out the strings embedded into a program by the author. When possible, the extractor should indicate library and runtime-related strings. For example, the extractor may parse debug information to recognize popular third party libraries and annotate the related strings appropriately.

Today, FLOSS automatically deobfuscates protected strings found in malware. Better categorization of its output would make its users more efficient. Extracting language-specific strings would make FLOSS more useful and manifest success as the default tool used by security analysts.

**Deliverables**

- Enhance existing Go and Rust string extraction
- Develop language identification module
  - Initial focus on .NET
  - Consider also Swift, Zig, …
- Research language string embeddings and create extractor code
  - We can share existing knowledge and code to bootstrap this
- Identify strings related to runtime and library code for targeted programming languages
- Extend standard output format and render results

**Required Skills**

- Medium knowledge of Python 3
- Basic understanding of reverse engineering (focus: Windows PE files)
- Experience with .NET or Swift (internals) is a plus, but not required
- Interest in malware analysis with focus on static analysis
- Basic understanding of Git


## FLOSS: QUANTUMSTRAND

_size_: large, estimated 350 hours

_difficulty_: medium

_mentors_: [@mr-tz](https://github.com/mr-tz)

_link_: [https://github.com/mandiant/flare-floss/issues/943](https://github.com/mandiant/flare-floss/issues/943)

Extend FLOSS to use the rendering techniques pioneered by QUANTUMSTRAND.

QUANTUMSTRAND is an experiment that augments traditional strings.exe output with context to aid in malware analysis and reverse engineering. For example, we show the structure of a file alongside its strings and mute/highlight entries based on their global prevalence, library association, expert rules, and more.

FLOSS is a tool that automatically extracts obfuscated strings from malware, rendering the human-readable data in a way that enables rapid reverse engineering.

We propose to extend FLOSS to use the techniques pioneered by QUANTUMSTRAND to highlight important information while muting common and/or analytically irrelevant noise. The project will provide an opportunity to dig into the PE, ELF, and/or Mach-O file formats, finding ways to make technical details digestible. If successful, FLOSS will continue to be the tool that malware analysts turn to when triaging unknown files.

**Deliverables**

- Research
  - Review Quantumstrand functionality
  - Evaluate most useful features for integration into FLOSS
- Identify and Propose Improvements
  - Suggest improvements for the user interface and experience
  - Review and enhance string tagging databases
  - Discuss ideas with mentors and FLOSS user community
- Implementation
  - Implement improved functionality
  - Work on a GUI to interactively display FLOSS results
- Evaluation and Knowledge Sharing
  - Test improvements and gather feedback from users
  - Write blog post about experience and project achievements

**Required Skills**

- Solid knowledge of Python 3
- Basic understanding of reverse engineering / malware analysis
- Basic understanding of Git
- Experience or interest with file formats such as PE, ELF, and/or Mach-O
- Experience or interest in user interface and/or user experience design


## GoReSym: Recover Golang Structure Tags and Interface Methods in GoReSym

**Mentors:** @stevemk14ebr, @jaeyoungkimG  
**Difficulty:** Easy to Medium  
**Project Repo:** [https://github.com/mandiant/GoReSym](https://github.com/mandiant/GoReSym)  

### Description
GoReSym is a Go symbol parser that extracts program metadata, function information, and embedded structures/types from Go binaries. It is widely used by reverse engineers to analyze stripped Go binaries and reconstruct type definitions.

Currently, GoReSym recovers structure fields but fails to extract **structure tags** (e.g., `` `json:"name"` ``) and **interface method names**. These tags are critical for understanding how data is serialized (JSON, XML) and how the application interacts with databases or external APIs. The goal of this project is to implement the parsing logic required to recover these missing metadata fields and include them in GoReSym's JSON output.

### Task Details
The contributor will need to:
1.  **Analyze Existing Parsers:** Study how GoReSym currently extracts `StructField` information by looking at the code adapted from the Go runtime (specifically `objfile` and type parsing logic).
2.  **Implement Tag Extraction:** Add logic to read the tag string associated with struct fields. This involves understanding the internal memory layout of Go types.
3.  **Implement Method Name Extraction:** Add logic to recover method names for Interface types.
4.  **Update Output:** Modify the JSON serialization to include these new fields.
5.  **Testing:** specific test cases involving structs with various tags and interfaces to ensure accurate recovery across different Go versions.

### Recommended Skills
*   **Go (Golang):** Intermediate knowledge.
*   **Reverse Engineering:** Basic understanding of binary formats (PE, ELF, Mach-O) and memory layouts.
*   **Go Internals:** Familiarity with how Go stores type metadata (`moduledata`, `pclntab`) is helpful but can be learned during the project.

### Resources
*   **Issue Discussion:** [GoReSym Issue #37](https://github.com/mandiant/GoReSym/issues/37) (contains references to similar implementations).
*   **Reference Implementation:** [goretk/gore type parsing](https://github.com/goretk/gore/blob/3009b3909f08fa910e5a93d893bb66117f3628f9/type2.go#L149)

## XRefer: Backend Expansion (Radare2 or Vivisect)

_size_: large, estimated 360 hours

_difficulty_: medium

_mentors_: @m-umairx, @binjo

### Description
**XRefer** is a binary analysis tool that correlates cross-references, API traces, and LLM-generated insights to cluster functions by behavior. Currently, XRefer utilizes a robust backend abstraction layer (`xrefer_new/backend/base.py`) with implementations for IDA Pro, Ghidra, and Binary Ninja.

This project aims to democratize access to XRefer by implementing a backend for a fully open-source/free disassembly framework: **Radare2** (via r2pipe) or **Vivisect**. While Ghidra is free, it is heavy and complex to set up in automated environments. By supporting lightweight frameworks like Vivisect or Radare2, we can create a truly **standalone CLI release** of XRefer. This would allow users to install and run XRefer (e.g. via `pip`) without requiring complex setups or commercial licenses, significantly lowering the barrier to entry for students and researchers.

The core task involves mapping the target framework's API to XRefer's standardized `BackEnd` interface. This includes implementing memory reading, function enumeration, disassembly lifting (to XRefer's `Instruction` format), and cross-reference analysis.

### Deliverables
* **Functional Backend Module:** A fully implemented backend package (e.g., `xrefer_new/backend/vivisect/`) that adheres to the `BackEnd` abstract base class.
* **Core Abstraction Refinement:** As the backend abstraction layer is relatively new, the student is expected to identify and implement necessary fixes, tweaks, or extensions to the base interface (`xrefer_new/backend/base.py`) to ensure the new backend functions correctly and the abstraction remains robust.
* **CLI Integration:** A working standalone CLI version of XRefer that uses this new backend by default when no commercial tool is detected.
* **Unit Tests:** A comprehensive test suite verifying that the new backend returns data (functions, strings, xrefs) consistent with the existing IDA/Ghidra backends.
* **Documentation:** Setup guides for the standalone CLI version and dependency management.

### Required Skills
* **Python:** Advanced proficiency.
* **Reverse Engineering:** Understanding of binary file formats (PE/ELF), memory sections, and assembly (x86/x64).
* **Target Framework API:** Familiarity with **Radare2 (r2pipe)** or **Vivisect** internals is highly preferred.

## XRefer: Native Frontend Development (Binary Ninja or Ghidra)

_size_: large, estimated 360 hours

_difficulty_: medium

_mentors_: @m-umairx, @binjo

### Description
XRefer's architecture separates the analysis logic (`core/analyzer.py`) from the underlying disassembler via a backend abstraction layer. However, the current Graphical User Interface (GUI) is implemented exclusively for IDA Pro.

This project aims to build a **native frontend module** for another major platform. The candidate may choose to target either **Binary Ninja** OR **Ghidra**.

Rather than creating a generic GUI abstraction, the goal is to write a dedicated GUI module tailored specifically to the chosen platform's capabilities. This ensures the plugin feels "native" to the environment, utilizing the specific Docking API and UI toolkit of the host (Qt for Binary Ninja, Swing for Ghidra).

The student will implement a new GUI module (e.g., `xrefer_new/gui/binaryninja/` or `xrefer_new/gui/ghidra/`) that consumes the platform-agnostic analysis data produced by the XRefer core and renders it using the host's native UI widgets. This will replicate the rich experience of the IDA plugin—including cluster visualization, colored tables, and interactive navigation—directly within the chosen client.

### Deliverables
* **Native Frontend Module:** A platform-specific Python module implementing the XRefer UI, utilizing the native docking and widget APIs of the chosen tool.
* **Visual Parity:** Replication of key XRefer visual features using the host's UI primitives:
    * **Cluster Graphs:** Rendering ASCII-art or graph-based visualizations of function clusters.
    * **Context Tables:** Interactive lists of cross-references, strings, and capabilities.
    * **Status Ribbons:** Information bars displaying analysis state.
* **Interactive Navigation:** Implementation of double-click navigation and synchronization between the XRefer view and the host disassembly listing.
* **Integration:** Seamless loading of the GUI module when XRefer is started within the client.

### Required Skills
* **Python:** Strong proficiency (required for XRefer core integration).
* **Platform Specifics (Candidate must possess skills for their chosen path):**
    * **Binary Ninja Path:** Experience with **Qt (PyQt5/PySide)** and the `binaryninjaui` API.
    * **Ghidra Path:** Experience with **Java/Swing** (Ghidra's GUI toolkit) and the PyGhidra API is highly preferred.
* Experience with and access to IDA Pro are preferred, as the candidate should ideally be able to explore the IDA plugin frontend independently to replicate it on the target platform.
