# MoganLab — Project Ideas

**Source:** https://github.com/MoganLab/GSoC-2026-MoganLab/blob/main/ideas/main.md
**Scraped:** 2026-03-10T16:58:40.274776

---

# GSoC 2026 Project Ideas with MoganLab

## Introduction
MoganLab is a nonprofit organization dedicated to building innovative, open-source tools for science and education. Our flagship project, **Mogan**, is a modern, structured editor designed for scientific and technical writing, forked from GNU TeXmacs.

For GSoC 2026, we offer exciting projects that combine deep technical challenges with real-world impact. Contributors will work on the frontier of interactive scientific software, gain mentorship from experienced developers, and become part of our global community. We look forward to collaborating with passionate students to push the boundaries of what's possible in open-source scientific tools.

## Project Ideas

### 1. Project Title: Web-Based Collaborative Editing Core
- **Description:** Mogan currently operates as a powerful desktop application. This project aims to bring its core editing experience to the web. The main technical challenge is to port the essential editing engine to run efficiently in a modern browser using technologies like WebAssembly, enabling real-time collaborative writing and editing sessions.
- **Expected Outcomes:** A functional web-based prototype capable of opening standard `.tmu` files, rendering document structure, and performing basic collaborative editing operations (e.g., concurrent text editing) in a browser. This will serve as the foundational backend for future collaborative features.
- **Recommended Skills:** Strong C++ (for understanding and porting core logic), proficiency in JavaScript/TypeScript and modern web frameworks, familiarity or strong interest in WebAssembly (Emscripten). Experience with real-time communication (WebSockets) is a plus.
- **Difficulty:** High
- **Potential Mentors:** [Darcy Shen/Email da@liii.pro]
- **Reference:** [https://research.mogan.app/research.html]

### 2. Project Title: Julia Plugin with Virtual Environment Support
- **Description:** Mogan excels at integrating computational code within documents, similar like Jupyter Notebook but with thesis-level editing support. This project focuses on deeply enhancing Mogan's support for the Julia programming language. The goal is to build a robust plugin that not only executes Julia code but also seamlessly manages Julia project environments (`Project.toml`) and packages, allowing users to reproduce computations inside the document. 
- **Expected Outcomes:**
    1.  A fully functional Julia plugin within Mogan that can execute code snippets and scripts.
    2.  Integration with Julia's package manager (Pkg) to activate and manage project-specific virtual environments from within the editor.
    3.  Basic support for resolving and loading dependencies specified in a `Project.toml` file.
    4.  Support copy and paste between Mogan to Julia. For example, one can directly copy a matrix from the math mode in mogan to Julia Session for computation and vice versa.
- **Recommended Skills:** Proficiency in the Julia programming language, understanding of Julia's package and project management system. Experience with C++ and Scheme (for plugin integration with Mogan's API) is beneficial.
- **Difficulty:** Medium
- **Potential Mentors:** [Jack Li/Email yansong@liii.pro]
- **Reference:** [https://github.com/mgubi/tm-julia]
