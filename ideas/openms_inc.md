# OpenMS Inc — Project Ideas

**Source:** https://openms.de/news/gsoc2026/
**Scraped:** 2026-02-22T23:28:47.594695

---

# OpenMS Invites the Computational Mass Spectrometry Community to Join Google Summer of Code 2026!

[Google Summer of Code (GSoC) 2026](https://summerofcode.withgoogle.com) OpenMS is planning to apply as an umbrella organization and we would like to extend an invitation to other projects and groups within the computational mass spectrometry and proteomics/metabolomics communities to join us in this effort.

## GSoC Contributors

- Make sure you are
[eligible](https://summerofcode.withgoogle.com/get-started)to participate in GSoC 2026. - Review the list of themes and the projects available within. If you have specific questions about a project, our mentors are active on
[Discord](https://discord.com/invite/4TAGhqJ7s5)and we will happily assist you. - Follow our instructions below on how to submit a proposal to us.

## Submitting an Application:

- Proposal must be uploaded to the GSoC webpage before the official deadline. Ensure your CV and contact information are included in the proposal document.
- We highly recommend to get in touch with the mentors before submitting your proposal.

## AI Usage policy:

We believe that the primary goal of your participation in GSoC should be learning how to participate in open-source communities. We also believe that it is quite possible to use generative AI to be a more effective participant in our community. Therefore we do not prohibit the responsible use of AI tooling in either your contributions, or your written communications. All AI models were trained on open-source code. We like to think that they can give back a bit to the community as well. This policy comes with a number of major caveats:

### “A computer can never be held accountable”

- Ultimately the code and communication that you submit is your responsibility. Generative AI can help with language barriers, repetitive tasks, and research, but ultimately you are the contributor to the project. We will hold you responsible for any mistakes that the AI makes the same as we would for your own code and communication. You must review any product of AI before you submit it.

### If you are found submitting work that clearly hasn’t been reviewed, we reserve the right to take disciplinary action up to and including banning you from our project. It should go without saying that this would not result in your successful GSoC.

- NOTE: this is not a prohibition against making mistakes, or even missing mistakes that the AI made. You are here to learn, and mistakes happen.

### Make clear in any submission (code, communications, etc.) that you used AI tools.

- This can simply be a line in the PR description saying “Made with AI tools”. It should be clear that this isn’t meant to pass judgement on you, work made with AI tools has a very different set of typical failure modes than work done entirely by humans, it helps us to understand where mistakes may have come from.

### If we explicitly ask you to do something without AI tools, do not use them.

- Yes, we can tell. We’ve all used AI tools as well. Doing this will also result in your getting banned from our project.

### You must do your best to make sure that code produced with AI help uses consistant naming conventions and coding style.

- This doesn’t need to be hard. Have your agent load
[https://openms.de/doxygen/nightly/html/coding_conventions.html](/ideas/openms-inc/doxygen-nightly-html-coding_conventions)before writing any code, and ask it to check that it complied with all the coding conventions before code submission.

### Suggestions for using AI effectively:

-
Using an agent effectively can be challenging. Each model has specific ways that they fail, and specific limitations. Learn these before using an agent to build code.

-
The skill that an agent has in writing and understanding code is proportional to how much similar code it has seen. In our experience this means that it is much better at solving pandas dataframe formatting issues than esoteric C++ bugs.

-
Asking an agent to explain code, or program logic can be a good first step to understanding. OpenMS is a large software project, and trying to unravel how a specific piece of logic works can be daunting. Our team has internally had very good success using agents to speed up learning how a section of code works. Just keep in mind that it can be wrong sometimes.

-
Asking the agent for proof is always a good idea.


# Available Projects

## Theme A) Data Formats and Interoperability

### 1) imzML Parser in OpenMS

**Proposed Mentors:** OpenMS Team

**Skills:** C++, XML Parsing, Mass Spectrometry Imaging

**Estimated Project Length:** 350 hours | **Difficulty:** Medium

Mass spectrometry imaging (MSI) is a powerful analytical technique that enables spatial mapping of molecules in biological tissues. The imzML format is the open standard for storing MSI data, consisting of two files: an XML metadata file and a binary data file. While imzML is widely used in the MSI community, OpenMS currently lacks native support for reading and writing this format.

The goal of this project is to implement a robust imzML parser in OpenMS, enabling seamless integration of mass spectrometry imaging data into existing OpenMS workflows.

Tasks:

- Implement a C++ imzML reader that can parse both continuous and processed imzML formats.
- Implement an imzML writer to enable export of imaging data.
- Add support for common imzML metadata (coordinates, pixel size, spectrum parameters).
- Integrate the parser with existing OpenMS data structures (MSExperiment, MSSpectrum).
- Write comprehensive unit tests and validate against reference imzML datasets.
- Document the new functionality and provide usage examples.

### 2) Full Python Bindings Using Nanobind

**Proposed Mentors:** OpenMS Team

**Skills:** Python, C++, Nanobind, Cython

**Estimated Project Length:** 350 hours | **Difficulty:** Medium to Advanced

PyOpenMS provides Python bindings for OpenMS, enabling Python developers to access the powerful mass spectrometry algorithms implemented in OpenMS. Currently, these bindings are generated using Cython via the autowrap package. While functional, this approach has limitations in terms of maintenance overhead, compile times, and certain Python integration features.

Nanobind is a modern C++17 library for creating Python bindings with minimal overhead. An existing prototype demonstrates the feasibility of using nanobind for OpenMS Python bindings. This project aims to build upon this prototype to create comprehensive nanobind-based Python bindings for OpenMS.

A key deliverable of this project is a thorough evaluation comparing nanobind-based bindings against the current autowrap/Cython implementation. This evaluation should cover:

**Performance:**Binding overhead, memory usage, call latency**Build System:**Compile times, dependency management, CI/CD integration**Usability:**Python API ergonomics, documentation generation, IDE support**Maintenance:**Code complexity, debugging experience, update workflow**Compatibility:**Python version support, platform compatibility, NumPy/SciPy integration

Tasks:

- Evaluate the existing nanobind prototype and identify gaps in coverage.
- Extend the nanobind bindings to cover core OpenMS classes and algorithms.
- Implement automatic binding generation where feasible to reduce maintenance burden.
- Conduct systematic benchmarking comparing nanobind vs. autowrap/Cython bindings.
- Document advantages and disadvantages of each approach with concrete examples.
- Write unit tests ensuring feature parity with existing PyOpenMS functionality.
- Provide a recommendation report for future binding strategy based on findings.

### 3) Accelerating OpenSwathWorkflow for Large-Scale In Silico Spectral Libraries

**Proposed Mentors:** Joshua Charkow

**Skills:** C++, Algorithm Optimization, Profiling

**Estimated Project Length:** 200 hours | Difficulty: Medium

OpenSwathWorkflow is a central component of OpenMS for Data Independent Acquisition (DIA) analysis, enabling targeted extraction and scoring of chromatographic signals using spectral libraries. While OpenSwathWorkflow performs well for conventional experimental libraries, the increasing adoption of large in silico–generated spectral libraries presents substantial computational challenges. Such libraries can contain millions of precursors, leading to increased memory usage, longer runtimes, and scalability bottlenecks in candidate selection and scoring.

This project aims to analyze and improve the computational performance and scalability of OpenSwathWorkflow, with a particular focus on workflows using very large in silico spectral libraries. The goal is to identify bottlenecks, redesign performance-critical components where necessary, and introduce optimizations that enable efficient processing without compromising identification quality.

A key deliverable of this project is a systematic performance evaluation of OpenSwathWorkflow before and after optimization.

Tasks:

- Develop a comprehensive understanding for the OpenSwathWorkflow algorithm
- Develop a benchmarking dataset for profiling.
- Profile OpenSwathWorkflow to identify computational bottlenecks.
- Identify algorithmic bottlenecks and propose changes.
- Experiment with different algorithms using inspiration from other open source DIA projects.
- Validate that the optimized implementation provides comparable results to the original implementation and other DIA software tools.

## Theme B) Dependency management

### Unify development dependencies using vcpkg

**Proposed Mentors**: OpenMS Team

**Skills**: CMake, Git, Command Line, Linux, macOS, Windows

**Estimated Project Length**: 175 hours | **Difficulty**: Medium

Like many large scale software projects, OpenMS has numerous
development dependencies. Unfortunately, there is no straightforward
way to quickly and easily install all of these dependencies. Some can
be installed using various package managers such as `apt-get`

, `brew`

,
or `choco`

, while others need to be installed with a Python package
manager such as `conda`

. And finally, some dependencies need to be
compiled from source code manually.

The goal of this project is to unify dependency management using the vcpkg package manager. A successful outcome will be a simplified developer experience where only a small number of tools are required in order to set up a full OpenMS development environment. For OpenMS dependencies that are not available in vcpkg, it will be necessary to contribute a recipe to the vcpkg community using Git.

## Theme C) Visualization and results

### Interactive Proteoform-Centric Visualization and Targeted Spectrum Analysis for Top-Down Proteomics

**Proposed Mentors**: Kyowon Jeong, Tom Müller

**Skills**: Python, mass spectrometry, proteomics, data visualization, OpenMS, web development

**Estimated Project Length**: about 350 hours | Difficulty: Advanced

Top-down proteomics enables the direct analysis of intact proteoforms, providing unparalleled insight into proteoforms, distinct molecular forms of a protein arising from a single gene, including protein isoforms, truncations, and post-translational modifications. However, interpreting individual spectra and connecting observed masses to biologically meaningful proteoforms remains a major bottleneck. This project aims to develop an interactive, proteoform-centric visualization and manual analysis tool, inspired by ProSight Lite, to enable rapid interpretation of top-down mass spectrometry data at the single-spectrum level. By integrating advanced visualization with fast targeted searches, the tool will allow researchers to quickly assess truncations, modifications, and mass discrepancies for a given protein of interest. Moreover, it will include feature-level visualization of proteoform ions over m/z-retention time dimension that will allow for quick and accurate validation of proteoform quantification results. By lowering the barrier between raw spectra and biological interpretation, this project will directly support exploratory proteomics, method development, and hypothesis testing in challenging top-down datasets.

Project Goals The student will design and implement an interactive analysis module that enables: Sequence-centric visualization of proteoforms, inspired by ProSight Lite, supporting user-defined mass inputs.

Mirror plots comparing user-supplied masses or m/z values against expected theoretical masses, enabling rapid validation and interpretation.

On-demand targeted searches, where a single spectrum triggers FLASHTnT via Python bindings to identify truncations and modifications for a specified target protein.

One-spectrum, one-protein analysis workflows, optimized for fast hypothesis testing rather than large-scale database searches. Intuitive feature (m/z and mass) visualization for quantitative analysis validation, to support exact and quick comparison between theoretical feature traces of quantified proteoforms and the observed ones .
