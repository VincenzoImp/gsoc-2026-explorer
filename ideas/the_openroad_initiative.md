# The OpenROAD Initiative — Project Ideas

**Source:** https://docs.google.com/document/d/1X6xxUonxgEQ_iD5G5vFp2ZOH1vbkRSspEdYrpSf4khE/edit?usp=sharing
**Scraped:** 2026-03-10T16:58:40.229112

---

GSoC 2026 ORI Projects

ORI will offer 5-7 well-scoped GSoC 2026 projects focused on the growth, strengthening, and long-term sustainment of OpenROAD across the ORI ecosystem.

Each project will be clearly defined with measurable goals and outcomes, prioritizing direct contributions to the OpenROAD codebase, along with learning, training, tutorials and high-quality documentation.

Mentorship will be provided by experts drawn from across the ORI ecosystem, including Google, PII, ASU, Brown University, and other contributing partners.

Topics: EDA infrastructure, DevOps

Skills: C++, CMake, CI/CD, packaging, documentation

Difficulty: Hard

Size: Medium (175 hours)

Mentors: Jack, Vitor

The current build and installation process consists of several options including building from sources, using pre-built binaries with dependency packages. This project focuses on simplifying adoption through:

- Pre-built binary distributions
- A formal release cadence
- Automated release workflows
- Improved installation documentation
- End-to-end tutorial(s) (docs + video) for various installation options on supported platforms

- Simplify the current binary build pipeline and installation process robust and easy to use for all platforms including MacOS
- Implement and document a formal versioning and release process
- Integrate automated release generation into CI/CD
- Update build and installation documentation
- Create a short, reproducible “first design” tutorial showcasing various build and installation options

- Ensure the following are well supported and reliable

- Building from sources with supported packages
- Docker based installation
- Pre-built binaries and packaging options
- Align with other supported packages and flows

- Documented release process with tagged release
- Updated installation documentation
- Step-by-step onboarding tutorial(s) to guide beginners to advanced users

Topics: EDA tool development

Skills: C++ programming, algorithm design, basic knowledge of circuit theory

Difficulty: Hard

Size: Medium (175 hours)

Mentor: Martin, Jonas

- OpenROAD’s Resizer tool is a design optimizer which autonomously carries out targeted edits with the goal of improving Quality of Results and to satisfy design rules.
- The tool internally employs a library of available “moves”. Each is a localized transformation which can optimize the design while keeping the design function intact. An example of a move is buffer gate insertion, swapping the inputs on an AND gate, or adjusting the drive strength of a gate. Each move comes with heuristic criteria for its application.
- The contributor will be tasked with implementing new moves in C++ and evaluating their performance.

- Work out a proposal for one or more new moves in discussion with mentors who can provide suggestions.
- Implement said moves in C++, evaluate their performance on the provided design suite and analyze cases where enabling new moves led to design degradation. Adjust the implementation based on findings.

- One or more accepted pull requests against the OpenROAD repository with move implementation
- Data on move performance to help the OpenROAD team make a decision on whether to enable the new move by default, and at what stages in the flow

Topics: EDA tool development

Skills: C++ programming, algorithm design, knowledge on global routing

Difficulty: Hard

Size: Hard (350 hours)

Mentor: Eder

- OpenROAD’s global routing tool has two solver options, FastRoute and CUGR. FastRoute is the first global router integrated into OpenROAD, and has had several updates and enhancements over the years.
- One of the main features implemented on FastRoute was the ability to perform incremental updates on selected nets. This is important when repairing timing violations, where changes are made to a subset of the nets on the design, and only the modified nets should be rerouted.
- Recently, CUGR was added as an option to FastRoute, but it lacks some major features compared to FastRoute, including incremental capabilities.

- The contributor will be tasked with the implementation of the incremental mode on CUGR. Incremental FastRoute can be used as a reference for the implementation.

- Study CUGR data structures to understand how incremental capabilities can be introduced to the tool.
- Design a solution for the problem, describing what data structures will be added/modified.
- Implement the solution in C++, followed by thoroughly testing for correctness, efficiency and quality of results.

- Design documentation for the proposed solution.
- One or more accepted pull requests against the OpenROAD repository with the incremental CUGR implementation.
- Data on efficiency, correctness and results of the solution to show the quality of the incremental CUGR tool.

Topics: EDA Tooling

Skills:

Difficulty: Hard

Size: Hard (350 hours)

Mentor: (Google)

- Migrate OpenROAD's parallelization framework from OpenMP to Kokkos to enable portable performance across multi-core CPUs, GPUs, and heterogeneous architectures for compute-intensive placement and routing operations.

[Finish the integration of the Kokkos library](https://www.google.com/url?q=https://github.com/The-OpenROAD-Project/OpenROAD/pull/5352&sa=D&source=editors&ust=1773159582947625&usg=AOvVaw0Q14hrAoIg0ZS9Rhme3wGA)into OpenROAD, along with Bazel build support.- Replace OpenMP #pragma omp parallel for directives with Kokkos parallel patterns
- Enable GPU acceleration for performance-critical algorithms in global placement and detailed routing
- Implement Kokkos Views to replace raw pointer-based data structures for better memory management
- Create abstraction layer allowing runtime selection of execution spaces (CPU/GPU)

- Build system integration with GPU backend support (CUDA)
- Kokkos-based implementation of global placement bin operations and density calculations
- Kokkos-based parallelization of detailed routing worker processing
- Performance benchmarking suite comparing OpenMP vs. Kokkos (CPU) vs. Kokkos (GPU) execution
- Developer documentation on Kokkos programming patterns for future contributors

Topics: EDA Tooling

Skills:

Difficulty: Hard

Size: Hard (350 hours)

Mentor: (Google)

- Complete the migration from CMake to Bazel as the primary build system to provide hermetic builds, better scalability, improved caching, and enhanced developer productivity.

- Achieve feature parity between Bazel and CMake build systems
- Migrate all tool modules currently using CMake to Bazel build definitions
- Implement platform-specific configurations for cross-compilation support
- Ensure all regression tests pass under Bazel
- Burn down the
[remaining known Github Issues](https://www.google.com/url?q=https://github.com/The-OpenROAD-Project/OpenROAD/issues?q%3Dis%253Aissue%2520state%253Aopen%2520label%253Abazel-conversion-must&sa=D&source=editors&ust=1773159582951137&usg=AOvVaw2QNC0JygXC9Af0XakKlTlz)blocking the migration.

- Complete Bazel BUILD files for all source modules replacing CMakeLists.txt functionality
- Migration guide documenting the transition from CMake to Bazel workflows
- CI/CD pipeline updates utilizing Bazel's caching and remote execution capabilities
- Performance comparison report showing build time improvements
- Proposed deprecation plan for CMake build system

Topics: EDA Tooling

Skills:

Difficulty: Hard

Size: Hard (350 hours)

Mentor: (Google), Mehdi

- Extend OpenROAD's Unified Power Format (UPF) support beyond basic power domain recognition to include comprehensive UPF standard parsing, validation, and multi-power domain design checks for advanced low-power design enablement.

- Implement full UPF 2.1/3.0 standard parsing for advanced constructs beyond basic create_power_domain
- Add support for multiple power switches per domain (currently limited to one)
- Implement comprehensive validation checks for isolation strategies, level shifters, and power switch configurations
- Add documentation for the currently empty
[limitations](https://www.google.com/url?q=https://github.com/The-OpenROAD-Project/OpenROAD/blob/5e8f15c0/src/upf/README.md%23limitations&sa=D&source=editors&ust=1773159582955532&usg=AOvVaw2VqnNHiNt_qD7UcoKjhT9X)section

- Enhanced UPF parser supporting advanced commands (supply nets, supply ports, power states)
- Validation framework checking UPF rule compliance (e.g., proper isolation cell placement, level shifter requirements)
- Comprehensive test suite with multi-voltage designs demonstrating power domain interactions
- Updated documentation with examples and resolved limitations section

Topics: DevOps, Containerization, Cross-Platform Development, CI/CD, Testing, Quality Assurance, CI/CD, Performance Engineering, Reliability

Skills: Docker, GitHub Actions, Linux/macOS/Windows development, shell scripting, Python, pytest, async programming, performance benchmarking, profiling

Difficulty: Medium

Size: Medium (175 hours)

Mentor: Jack, Vitor, Chaitanya (?)

- Improve accessibility of OpenROAD MCP through containerization and cross-platform support. Currently, setup requires manual installation. This project creates production Docker images and validates the tool across all major platforms.
- Build comprehensive testing infrastructure to ensure production readiness for v1.0 release. The project currently has basic tests but needs validation against real chip design workflows, performance benchmarking, and reliability testing at scale.
- Cross-platform: We want to cover popular coding assistants and OSes to showcase the capability of OpenROAD MCP.

- Create optimized multi-stage Dockerfiles with proper layer caching
- Publish images to GitHub Container Registry (GHCR) with automated CI/CD
- Validate and support Windows/WSL2 deployment
- Write comprehensive deployment documentation for various use cases

- Production-ready Docker images (optimized for size and build time)
- GitHub Actions workflows for automated GHCR publishing
- Cross-platform validation test suite (Ubuntu, macOS, Windows/WSL2)
- Deployment guides and troubleshooting documentation
- Implement integration tests using real ORFS flows (complete RTL-to-GDSII)
- Create performance benchmarking framework with historical tracking
- Build load testing infrastructure (validate 50+ concurrent sessions)
- Add memory profiling and leak detection
- Integration test suite covering major ORFS flows
- Performance benchmarking framework with metrics tracking over time
- Load testing infrastructure with automated regression detection
- Memory profiling tools integrated into CI pipeline

Topics: IEEE SSCS Chipathon, Documentation, Developer Experience, Knowledge Management, Generative AI (RAG), EDA Tooling

Skills: Technical writing, Markdown, MkDocs/Docusaurus, Python, embeddings/vector search, prompt engineering, GitHub Actions, basic chip design flow familiarity

Difficulty: Hard

Size: Hard (350 hours)

Mentor: Mehdi (Chipathon + OpenROAD flow repos)

- The IEEE SSCS Chipathon brings together many teams who often use OpenROAD-based flows (and related wrappers such as ORFS/OpenROAD-MCP/track-specific templates) to go from RTL to GDSII. During the competition, participants repeatedly run into the same hurdles: environment setup, tool/version mismatches, flow configuration, interpreting logs, and debugging timing/DRC/routing failures. Answers exist—but they’re scattered across GitHub repos, issues, Slack/Discord, Google Docs, and past Chipathon guidance.

- This project creates a central Chipathon Knowledge Hub and an “Ask Chipathon” chatbot that retrieves and cites canonical Chipathon/OpenROAD sources, helping participants quickly self-serve and reducing mentor/maintainer load—while making it clear that OpenROAD is the backbone of the Chipathon flow.

- A public, well-structured Chipathon Knowledge Hub site (MkDocs or Docusaurus) organized around:

- Getting Started (track-oriented)
- OpenROAD flow fundamentals
- Reference flows/templates (OpenROAD/ORFS/OpenROAD-MCP as applicable)
- Debugging playbooks (timing/DRC/routing/performance)
- Submission artifacts + checklists
- FAQ + “Seen During Chipathon” canonical answers

- A standardized Chipathon artifact map explaining where to find logs/reports/DEF/GDS/metrics and how to interpret common OpenROAD outputs.
- A contributor workflow and style guide so mentors can add or update answers during the event.
- An “Ask Chipathon” RAG chatbot (CLI required; minimal web UI optional) that:

- answers Chipathon/OpenROAD flow questions with citations to exact doc sections and/or canonical GitHub threads
- supports “related answers” / “answered before” suggestions via similarity search
- includes safe fallback behavior (asks for specific logs or points to triage steps when retrieval confidence is low)

- Automated indexing and refresh via GitHub Actions (rebuild on doc updates; optional scheduled refresh during Chipathon season).
- A small evaluation harness (30–60 Chipathon-style questions) with basic regression checks for:

- citation coverage
- groundedness (low hallucination rate)
- “no-answer” correctness when evidence is missing

- A maintainer handoff guide (how to curate sources, label canonical answers, and extend the knowledge base).

Topics: FOSSEE, EDA Tools, VLSI Design Automation, Open Source ASIC Flow, Digital Design, Physical Design

Skills: Python, C++, MakeFile, Msys, MinGW, Linux scripting, TCL, Docker, Basic VLSI design flow concepts, Familiarity with HDL, digital design, layout design, etc. Experience with KiCad / Ngspice / OpenROAD (preferred)

Difficulty: Hard

Size: Medium (175 hours)

Mentors: Sumanto Kar, Varad Patil, Shanthi Priya K., Aditya Minocha

Currently, eSim ([https://esim.fossee.in](https://www.google.com/url?q=https://esim.fossee.in/&sa=D&source=editors&ust=1773159582968226&usg=AOvVaw0j3JxS-14giaYEEmC9R17e)), developed under the FOSSEE ([https://fossee.in](https://www.google.com/url?q=https://fossee.in/&sa=D&source=editors&ust=1773159582968471&usg=AOvVaw3_0mtJkgd2fNIjJ2oEHjWm)) initiative at IIT Bombay, provides an integrated environment for schematic capture, circuit simulation, and PCB design using open-source tools like KiCad, Ngspice, Verilator, GHDL, SKY130 PDK and IHP PDK.

This project aims to integrate eSim with OpenROAD Flow Scripts (ORFS) to enable a complete open-source ASIC design pipeline. The integration will allow users to design digital circuits in eSim, generate Verilog, and automatically run the OpenROAD flow for synthesis, placement, routing, and physical design.

This will significantly enhance eSim by enabling students and researchers to explore full-chip design workflows using only open-source tools.

- Study the existing architecture of eSim and OpenROAD Flow Scripts.
- Design a workflow for exporting digital designs from eSim to the OpenROAD flow.
- Implement automated generation of necessary configuration files for ORFS.
- Create scripts to run synthesis, placement, and routing automatically.
- Integrate the flow into the eSim GUI.
- Provide example designs demonstrating the full ASIC flow.

- Automated pipeline connecting eSim designs to OpenROAD flow.
- Scripts for generating OpenROAD configuration and running ORFS.
- Example digital designs demonstrating the flow.
- Documentation and tutorials for students and educators.
- Demonstration of a complete open-source ASIC design flow using eSim and OpenROAD.
