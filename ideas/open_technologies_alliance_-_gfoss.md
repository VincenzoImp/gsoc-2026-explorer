# Open Technologies Alliance - GFOSS — Project Ideas

**Source:** https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas
**Scraped:** 2026-02-22T23:28:47.624684

---

# Google Summer of Code 2026 proposed ideas

[Μετάβαση στην πλοήγηση](https://ellak.gr#mw-head)

[Πήδηση στην αναζήτηση](https://ellak.gr#searchInput)

Contributors interested to participate should check which of the following projects fits their interests and skills.

**Τo communicate with the mentors and ask questions about the projects, students should subscribe to this** [list](https://lists.ellak.gr/gsoc-developers/listinfo.html) **and post relevant questions. Please follow the Proposal Template**

For practical information, developers should visit this ** page**.



**VS Code pluggin for CScout**[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=1) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=1)]

#### Brief Explanation[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=2) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=2)]

The objective of the proposed project is to create a Visual Studio Code plugin for accessing the functionality of the CScout source code analyzer and refactoring browser for collections of C programs.

CScout can process workspaces of multiple projects (a project is defined as a collection of C source files that are linked together) mapping the complexity introduced by the C preprocessor back into the original C source code files. CScout takes advantage of modern hardware (fast processors and large memory capacities) to analyze C source code beyond the level of detail and accuracy provided by current compilers and linkers. The analysis CScout performs takes into account the identifier scopes introduced by the C preprocessor and the C language proper scopes and namespaces. CScout has already been applied on projects of tens of thousands of lines to millions of lines, like the Linux and FreeBSD kernels and the Apache web server.

Having VSCode act as a front-end to CScout’s existing batch analysis will work as follows.

- Trigger explicit runs (command palette / tasks), not on-save analysis.
- Present results as:
- Navigable diagnostics
- Cross-reference views (definitions, uses, dependencies)
- Refactoring previews as diffs
- Project-wide facts (identifier scopes, file coupling, macro effects) that are otherwise buried in textual reports


This will offer the following advantages

- Lower adoption barrier: developers are far more likely to try CScout if results appear inside their editor instead of via reports or bespoke UIs.
- Natural fit for whole-program analysis: VS Code already supports long-running, cancellable tasks with progress reporting.
- Superior comprehension UX: jump-to-definition, peek views, code lenses, and diff previews make CScout’s semantic information immediately actionable.
- Safer refactoring workflow: preview-first refactorings reduce fear of large, semantics-preserving transformations.
- Separation of concerns: keeps CScout as a standalone engine while the plugin handles visualization and navigation.
- Research leverage: enables realistic user studies (e.g., acceptance of large-scale refactorings, tolerance of latency).
- Longevity and reuse: the same backend can serve CLI, CI, and IDE use; the plugin becomes a thin, replaceable shell.

Thus the plugin will combine CScout’s strengths (macro-aware parsing, precise identifier resolution, and whole-system reasoning) that are hard to appreciate via static reports and tricky to use through the existing rudimentary web front-end. The VSCode plugin combines two open source software projects to provide immediate developer value.

#### Expected Results[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=3) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=3)]

A VS Code plugin that can act as an interface to CScout

#### Duration of the Project[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=4) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=4)]

Large Project – 350 hrs

#### Related Repositories[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=5) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=5)]

[https://github.com/dspinellis/cscout](https://github.com/dspinellis/cscout)

#### Knowledge Prerequisites[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=6) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=6)]

Typescript, C/C++, VS Code API

#### Mentors[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=7) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=7)]

Diomidis Spinellis

**OpenTRIM**[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=8) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=8)]

#### Brief Explanation[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=9) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=9)]

OpenTRIM is an open-source code for simulating the passage of energetic ions through materials and calculating the associated modifications and damage that they cause to these materials. It is based on the kinetic Monte-Carlo method and employs the Binary Collision Approximation to describe the interaction between ions and target atoms. OpenTRIM comprises a set of C++ libraries, a command-line program for executing simulations in batch mode, and a Qt-based graphical user interface for configuring, running, and evaluating simulations. Several parts of the codebase require improvements and extensions.

#### Expected Results[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=10) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=10)]

Real-time 3D visualization tool for simulated ion tracks

Python bindings for running simulations and retrieving results directly from Python

#### Duration of the Project[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=11) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=11)]

Large Project – 350 hrs

#### Related Repositories[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=12) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=12)]

[https://github.com/ir2-lab/OpenTRIM](https://github.com/ir2-lab/OpenTRIM)

#### Knowledge Prerequisites[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=13) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=13)]

C++

Python (optional)

OpenGL (optional)

#### Mentors[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=14) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=14)]

George Apostolopoulos

Michail Axiotis

Eleni Mitsi

**Open-Source AI Framework for Thermal Satellite Payload Data Analysis**[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=15) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=15)]

#### Brief Explanation[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=16) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=16)]

This project aims to develop a general-purpose open-source AI framework for extracting high-level semantic information from thermal sensor payloads onboard satellites. The framework will support multiple application scenarios such as nighttime cloud detection and thermal event or anomaly monitoring on land and sea.

The project focuses on building a reusable pipeline covering dataset creation and augmentation from real and synthetic thermal imagery, model training and benchmarking, and advanced analysis tools such as uncertainty quantification and explainability. The goal is to provide a practical and reproducible platform for thermal remote sensing applications in Earth observation and small satellite programs.

#### Expected Results[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=17) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=17)]

Modular AI pipeline for thermal satellite data processing

Dataset extraction, preprocessing and labeling workflows

Baseline and benchmarked ML/DL models

Uncertainty quantification methods

Explainability tools

Public open-source releases with documentation

#### Duration of the Project[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=18) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=18)]

Large Project – 350 hrs

#### Related Repositories[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=19) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=19)]

[https://github.com/Orion-AI-Lab](https://github.com/Orion-AI-Lab)

[https://github.com/Orion-AI-Lab/TIRAuxCloud](https://github.com/Orion-AI-Lab/TIRAuxCloud)

#### Knowledge Prerequisites[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=20) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=20)]

Python

Machine Learning / Deep Learning (PyTorch or similar)

Image processing fundamentals

Geospatial / satellite imagery familiarity

Interest in remote sensing and explainable AI

#### Mentors[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=21) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=21)]

Christos Chronis

Alexis Apostolakis

Simon Vellas

**Command & Data Handling Software for Open-Source CubeSat FlatSat Testbed**[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=22) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=22)]

#### Brief Explanation[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=23) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=23)]

The CubeSat FlatSat testbed is a ground-based platform for deploying and testing onboard AI algorithms, end-to-end processing pipelines, and avionics software/hardware. It supports onboard processing validation and serves as a development platform for university student projects and future open-source CubeSat missions.

#### Expected Results[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=24) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=24)]

C&DH flight software on STM32 with FreeRTOS

Inter-subsystem communication using CSP over CAN

NASA cFS-inspired modular architecture

Zenoh middleware for high-bandwidth payload data

Unit tests and integration tests

Architecture documentation and developer guides

Public open-source release on GitHub

#### Duration of the Project[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=25) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=25)]

Large Project – 350 hrs

#### Related Repositories[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=26) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=26)]

[https://github.com/omega-space-group](https://github.com/omega-space-group)

[https://github.com/omega-space-group/orion-cubesat-testbed](https://github.com/omega-space-group/orion-cubesat-testbed)

#### Knowledge Prerequisites[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=27) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=27)]

Python and C

Embedded systems development

FreeRTOS

CAN bus & networking protocols

STM32 toolchain familiarity

Interest in satellite systems and flight software

#### Mentors[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=28) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=28)]

Christos Chronis

Simon Vellas



**Fine-tuning AI transcription models for Greek Municipal Councils**[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=29) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=29)]

#### Brief Explanation[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=30) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=30)]

OpenCouncil has accumulated hundreds of hours of Greek municipal council recordings with human-corrected transcriptions and utterance-level timestamps. Greek municipal speech presents unique challenges: regional accents, domain-specific legal and administrative terminology, multiple speakers, and varying audio quality. This project will fine-tune Whisper (or similar open-source speech recognition models) on our dataset to significantly improve transcription accuracy for Greek municipal contexts. The contributor will preprocess training data, experiment with fine-tuning approaches, evaluate model performance against our current pipeline, and deploy the improved model to production. Success means measurably better transcription quality — especially for technical terms and speaker identification.

OpenCouncil is a civic tech platform that makes Greek municipal council proceedings accessible to citizens through AI-powered transcription, summarization, and search. We have established partnerships with 10+ municipalities across Greece, providing both real-world data and direct validation channels for this project. Our existing dataset of human-corrected transcriptions is a unique resource that makes this fine-tuning project feasible and impactful. The resulting model will be open-sourced and can benefit the entire Greek-speaking NLP community.

#### Expected Results[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=31) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=31)]

A preprocessed, validated training dataset of Greek municipal speech with utterance-level alignments, ready for model fine-tuning and future research use. A fine-tuned Whisper model that demonstrates measurable improvement in Word Error Rate (WER) over the baseline, particularly on domain-specific terminology (legal, administrative), regional accents, and multi-speaker segments. An evaluation framework with benchmarks and test sets for ongoing quality measurement of Greek municipal transcription. Production integration of the fine-tuned model into OpenCouncil's transcription pipeline, validated on real council meetings from our 10+ municipal partners. Documentation of the fine-tuning methodology, dataset preparation process, and results — contributing to the broader Greek NLP and open-source speech recognition community.

#### Duration of the Project[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=32) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=32)]

Large Project – 350 hrs

#### Related Repositories[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=33) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=33)]

[https://github.com/schemalabz/opencouncil](https://github.com/schemalabz/opencouncil)

#### Knowledge Prerequisites[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=34) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=34)]

Python, Machine Learning, PyTorch/TensorFlow, Speech Recognition, Greek language required

#### Mentors[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=35) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=35)]

Andreas Kouloumos (andreas@opencouncil.gr), Christos Porios (christos@opencouncil.gr)





**Municipal Budget and Technical Program Visualization Tool**[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=36) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=36)]

#### Brief Explanation[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=37) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=37)]

All 332 Greek municipalities publish annual budgets (προϋπολογισμοί) and technical programs (τεχνικά προγράμματα) as PDFs — hundreds of pages of financial data and infrastructure projects that citizens struggle to understand. This project will build a standalone tool that processes these PDFs, extracts structured data, and presents it through an accessible interface. Users will be able to search projects, track spending over time, compare municipalities, and visualize budget allocations. The tool will handle the varied PDF formats used across municipalities and be deployable for all 332 Greek municipalities with minimal configuration.

This tool addresses a fundamental transparency gap in Greek local government. While budget data is technically public, it is practically inaccessible to citizens due to its format and complexity. OpenCouncil's network of 10+ municipal partners provides immediate access to real budget documents for development and testing, and a clear path to adoption across Greece. The tool will be fully open-source and designed for reuse by other civic tech initiatives. This project complements OpenCouncil's core mission of making municipal governance transparent and accessible.

#### Expected Results[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=38) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=38)]

1. PDF processing pipeline: Build robust extraction system that handles various PDF formats and structures, validate data quality 2.Data model and API: Design database schema, create API endpoints, implement search and comparison features 3. User interface and deployment: Build accessible frontend for exploring budgets and projects, deploy for multiple municipalities, write documentation

#### Duration of the Project[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=39) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=39)]

Large Project – 350 hrs

#### Related Repositories[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=40) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=40)]

[https://github.com/schemalabz/opencouncil](https://github.com/schemalabz/opencouncil)

#### Knowledge Prerequisites[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=41) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=41)]

Python, PDF processing, Data extraction, PostgreSQL, Next.js/React, Data visualization, greek language required

#### Mentors[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=42) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=42)]

Andreas Kouloumos (andreas@opencouncil.gr), Christos Porios (christos@opencouncil.gr)



**GlossAPI: Needs-Driven Evolution of the Dataset Production Pipeline for Greek Language Data**[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=43) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=43)]

#### Brief Explanation[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=44) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=44)]

This project focuses on improving the GlossAPI dataset production pipeline by addressing practical limitations and gaps that emerge as new datasets are processed and published.

As the scope and volume of Greek-language datasets handled by GlossAPI continue to grow, the pipeline must evolve to remain maintainable, reliable, and adaptable to new use cases. The contributor will work on the reconstruction and evolution of parts of the pipeline, guided by operational needs encountered during dataset ingestion, processing, and publication.

The work will emphasize improvements to the pipeline’s maintainability and usability, while enabling richer interaction and input scenarios that better reflect how Greek-language data is accessed and processed in practice. This includes exploring enhancements related to workflow execution, interaction mechanisms, data acquisition paths, and challenges specific to Greek-language and OCR-derived content.

#### Expected Results[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=45) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=45)]

- Improved maintainability of the GlossAPI pipeline codebase
- Targeted improvements addressing real usage issues in dataset ingestion and processing
- Enhanced support for diverse data sources and interaction patterns
- Incremental improvements tailored to the characteristics of Greek-language data
- Documentation and usage notes supporting long-term sustainability and onboarding

#### Duration of the Project[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=46) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=46)]

Large Project - 350 hrs

#### Related Repositories[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=47) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=47)]

[glossAPI](https://github.com/eellak/glossAPI)[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=48) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=48)]

#### Knowledge Prerequisites[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=49) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=49)]

Applicants should have good knowledge of Python, Git/GitHub, experience with data processing pipelines

#### Mentors[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=50) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=50)]

Dimitrios Athanasopoulos, Nikos Tsekos

**GlossAPI: ML-assisted Anonymization Layer and Targeted Pipeline Improvements for Greek Datasets**[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=51) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=51)]

#### Brief Explanation[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=52) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=52)]

This project focuses on extending GlossAPI with a production-ready anonymization layer for Greek text datasets, addressing a critical need for privacy-preserving dataset publication, while also contributing targeted updates to the existing pipeline based on requirements that emerge during its evolution.

The core of the project is the design and implementation of an ML-assisted anonymization module that detects and masks sensitive personal information (such as names, emails, phone numbers, and organizations) in Greek text. Due to the linguistic characteristics of Greek and the presence of OCR noise in many datasets, the anonymization layer will explore and evaluate multiple approaches, including rule-based techniques and ML-based methods such as Named Entity Recognition, potentially using transformer-based or other state-of-the-art models depending on empirical results.

#### Expected Results[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=53) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=53)]

- Integrated anonymization module for Greek text datasets within GlossAPI
- Detection and masking of common personal identifiers (names, emails, phone numbers, organizations)
- Targeted updates to specific parts of the GlossAPI pipeline, limited to what is necessary to support anonymization
- Documentation and usage examples for maintainers and future contributors

#### Duration of the Project[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=54) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=54)]

Large Project - 350 hrs

#### Related Repositories[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=55) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=55)]

[glossAPI](https://github.com/eellak/glossAPI)[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=56) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=56)]

#### Knowledge Prerequisites[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=57) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=57)]

Applicants should have good knowledge of Python, Git/GitHub, Basic NLP/ML concepts, and Regular expressions.

#### Mentors[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=58) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=58)]

Myrsini Ioannou, Nikos Tsekos, Dimitrios Athanasopoulos

** FOSSBot Platform: Simulation Enhancements and AI Integration **[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=59) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=59)]

#### Brief Explanation[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=60) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=60)]

The FOSSBot Platform aims to enhance robotic simulation environments by integrating AI-driven capabilities and improving simulation realism. The project focuses on extending existing open-source robotic simulation tools with advanced features that support experimentation, education, and research in autonomous systems. Emphasis is placed on modularity, extensibility, and reproducibility within open-source ecosystems.

#### Expected Results[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=61) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=61)]

The expected outcomes include enhanced simulation modules, AI-assisted decision-making components, improved documentation, and example use cases. The project will deliver code contributions upstream, along with benchmarks and demonstrations showcasing the improvements in robotic simulation fidelity and usability.

#### Duration of the Project[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=62) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=62)]

Large Project - 350 hrs

#### Related Repositories[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=63) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=63)]

[https://github.com/eellak/fossbot-platform](https://github.com/eellak/fossbot-platform)
[https://github.com/eellak/fossbot](https://github.com/eellak/fossbot)
[https://fossbot.gr](https://fossbot.gr)

#### Knowledge Prerequisites[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=64) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=64)]

Applicants should have good knowledge of JavaScript, Python, robotics simulation environments, and basic AI/ML concepts. Familiarity with open-source workflows and collaborative development is required.

#### Mentors[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=65) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=65)]

Christos Chronis, Eleftheria Papageorgiou, Irida Ntinou

** AI assisted KMC **[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=66) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=66)]

#### Brief Explanation[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=67) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=67)]

This project explores the integration of machine learning techniques into Kinetic Monte Carlo (KMC) simulations. The goal is to accelerate simulations and improve predictive accuracy by leveraging AI models trained on simulation data. The project targets scientific computing and materials science applications.

#### Expected Results[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=68) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=68)]

Deliverables include AI-augmented KMC algorithms, performance evaluations against traditional methods, and a reproducible pipeline for training and inference. Documentation and example experiments will accompany the final implementation.

#### Duration of the Project[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=69) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=69)]

Large Project - 350 hrs

#### Related Repositories[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=70) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=70)]

[https://github.com/nixeimar/Apothesis](https://github.com/nixeimar/Apothesis)

#### Knowledge Prerequisites[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=71) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=71)]

C++, working knowledge of machine learning techniques, numerical methods, and statistical modeling. Prior experience with scientific simulations is a plus.

#### Mentors[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=72) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=72)]

Cheimarios Nikolaos, Vissarion Fysikopoulos



**Unified SBOM Management via RDF Database Abstraction**[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=73) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=73)]

#### Brief Explanation[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=74) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=74)]

Software Bill of Materials (SBOM) documents, specifically in the ISO standard SPDX format, are becoming the cornerstone of software supply chain security. As the volume of SBOM data grows, simple file-based storage is no longer sufficient for complex analysis and cross-referencing. This project aims to develop a suite of tools to ingest, store, and extract SPDX documents using RDF databases (Triplestores). By utilizing the triplestore Python library, these tools will remain database-agnostic, allowing users to seamlessly switch between backends like Apache Jena, AllegroGraph, Blazegraph, GraphDB, and Oxigraph without changing the codebase.

#### Background information[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=75) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=75)]

Triplestores are a type of database specialized in storing triples, a data structure for representing information in a subject-predicate-object format. They are crucial in semantic web technologies, such as RDF, SPARQL, and OWL. However, there are numerous triplestore alternatives available, each with its own strengths and weaknesses. For GSoC 2025, a Python library abstracting some commonly used databases was developed.

SBOM data in SPDX format can be serialized in RDF, and therefore can be stored in such databases.

#### Project Description[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=76) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=76)]

The current SPDX ecosystem relies heavily on flat files (JSON, RDF/XML, or even Tag-Value for SPDXv2). While effective for transport, these files are difficult to query at scale—for example, when looking for a specific vulnerable component across thousands of SBOMs. Since SPDXv3 is natively based on an knowledge graph model, storing it in a RDF Triplestore is the most logical and powerful way to handle this data. However, different RDF databases have varying APIs and connection protocols.

This project will leverage the triplestore library (which provides a high-level Python abstraction) to build tools that:

- *Ingest:* Parse SPDX documents (multi-format support) and map them to the unified RDF store.

- *Extract:* Reconstruct valid SPDX documents from the database based on specific queries (e.g., "Export the SBOM for Project X version 1.2").

- *Manage:* Provide basic management functions like listing stored SBOMs, deleting old versions, and validating data integrity.

#### Expected Outcome[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=77) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=77)]

By the end of the project, we expect to have a number of well-documented tools that can operate on SBOM data. These will allow users to seemlessly move between SPDX documents and RDF databases.

An indicative list of tools and deliverables is:

- *SBOM-to-Store Ingestor:* A CLI tool to upload SPDX documents (v2 and v3) into any supported triplestore.

- *Store-to-SBOM Exporter:* A tool to query the database and output a standard-compliant SPDX file.

- *Database Management Utilities:* Tools for basic CRUD operations on the stored SBOM data.

- *Test Suite:* A comprehensive set of tests to verify the abstraction works.

- *Documentation:* User guide for the CLI tools and developer documentation for the API.

#### Duration of the Project[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=78) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=78)]

Long (350 hours)

#### Related Resources and Repositories[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=79) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=79)]

- [https://github.com/eellak/triplestore](https://github.com/eellak/triplestore)

- [https://github.com/spdx/tools-python](https://github.com/spdx/tools-python)

- [https://github.com/RDFLib/rdflib](https://github.com/RDFLib/rdflib)

- [https://spdx.github.io/spdx-spec](https://spdx.github.io/spdx-spec)

#### Knowledge Areas[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=80) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=80)]

Python3, RDF, SPARQL, SPDX specifications.

*Tip for your application:* Study SPDX v3 (and v2): SPDX is heavily RDF-centric. Demonstrating knowledge of how 3.0 maps to triples will make your proposal stand out.

#### Mentors[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=81) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=81)]

Alexios Zavras, TBD



**Using SWHID to Identify Software Components**[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=82) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=82)]

#### Brief Explanation[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=83) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=83)]

This project addresses a critical gap in software supply chain security and reproducibility: the connection between package-level identifiers (like package-name@version) and content-level identifiers (SWHIDs).

#### Background information[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=84) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=84)]

Software Hash IDentifiers (SWHID) are a standardized way to identify software artifacts, based on content. The definition is officially adopted as ISO/IEC 18670:2025 and is available at [https://swhid.org](https://swhid.org).

However, most developers interact with software through package managers like Cargo (Rust), PyPI (Python), Maven (Java), or APT (Debian/Ubuntu). There is currently a "semantic gap" between the package version (e.g., requests 2.31.0) and its corresponding SWHID, which depends on its contents.

#### Project Description[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=85) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=85)]

The goal of this project is to develop tooling that automatically computes, verifies, and publishes the SWHIDs for components across major package registries. By creating a verifiable mapping between package releases and SWHIDs, we can enable better SBOM integration, improved vulnerability tracking, and long-term reproducibility of the global software supply chain.

This project will involve three main phases:

- *Computation and Archival:* Build a pipeline to fetch packages from registries (like Crates.io, PyPI, Maven Central, etc.) and compute their SWHIDs locally to ensure integrity.

- *Mapping & Verification:* Generate a high-quality dataset that maps registry data (URL and version) to SWHID. This will require handling the specific packaging quirks of each ecosystem.

- *Publication:* Publish these identifiers in a way that makes them useful to the community. This could include: contributing to a public lookup service or API; exporting mappings to SPDX format; or proposing metadata additions to the package registries themselves.

#### Expected Outcome[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=86) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=86)]

- *CLI Tool:* A reusable utility that takes a package name/version and returns a verified SWHID.

- *Public Dataset:* A comprehensive mapping of the most popular packages across ecosystems to their SWHIDs.

- *Documentation:* A guide on how package maintainers can include SWHIDs in their own release workflows.

- *Upstream Contributions:* (Stretch goal) Integration with tools like cargo-swhid or pyproject.toml plugins.

#### Duration of the Project[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=87) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=87)]

Short or Regular or Long, depending on breadth and depth.

#### Related Resources and Repositories[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=88) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=88)]

#### Knowledge Areas[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=89) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=89)]

Python and bash scripting (for the solution), knowledge of other ecosystems (Rust, Java, etc.) is required to understand their packaging.

*Tip for your application:* Study SWHID and the different ecosystems. Demonstrating understanding of ecosystem specific challenges will make your proposal stand out.

#### Mentors[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=90) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=90)]

Alexios Zavras, TBD

**Who is who: Alexandria3k entity disambiguation extentions**[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=91) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=91)]

#### Brief Explanation[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=92) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=92)]

The alexandria3k Python package supplies a command-line tool and an API providing fast and space-efficient relational query access to several large scientific publication open data sets. Data are decompressed on the fly, thus allowing the package's use even on storage-restricted laptops. This project will enhance Alexandria3k by integrating a scalable, high-precision author and affiliation disambiguation pipeline over Crossref metadata that does not rely on ORCID or ROR, using probabilistic clustering optimized for large-scale bibliometrics. We will implement aggressive normalization and blocking to control candidate growth, represent authors as paper-level mentions, and fuse lightweight, interpretable signals—name similarity, affiliation token overlap, co-author graph structure, venue/topic coherence, and temporal constraints—into conservative merge decisions that favor precision over recall. Disambiguation will be incremental and auditable, with stable cluster IDs, merge provenance, confidence scores, and an explicit “unknown” class to avoid over-merging common names. In parallel, we will cluster affiliation strings into canonical organization buckets using country-aware token blocking and city/org matching, enabling robust institution-level analyses even with noisy or missing data. Together, these additions will materially improve the reliability of author- and organization-centric metrics in Alexandria3k while remaining scalable, reproducible, and resilient to incomplete identifiers.

#### Expected Results[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=93) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=93)]

New Alexandria3k actions to dissambiguate authors and organizations by adding corresponding fields in the populated database.

#### Duration of the Project[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=94) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=94)]

Large Project – 350 hrs

#### Related Repositories[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=95) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=95)]

[https://github.com/dspinellis/alexandria3k](https://github.com/dspinellis/alexandria3k)

#### Knowledge Prerequisites[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=96) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=96)]

Python; machine learning; SQL

#### Mentors[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=97) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=97)]

Diomidis Spinellis

**Python bindings for Apothesis**[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=98) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=98)]

#### Brief Explanation[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=99) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=99)]

This project focuses on creating modern Python bindings for Apothesis to seamlessly connect its high-performance C++ core with Python-based AI workflows. While the existing C++ implementation delivers speed and efficiency for large-scale computation, the lack of native Python integration limits accessibility for researchers and machine learning practitioners who primarily work within Python ecosystems such as NumPy, PyTorch, and TensorFlow. The bindings will expose Apothesis’ core functionality through a clean, Pythonic API, preserving performance while ensuring memory safety and ease of installation. By bridging efficient C++ algorithms with Python’s flexibility and extensive AI tooling, this work enables rapid experimentation, smoother integration into machine learning pipelines, and broader adoption within the research community.

#### Expected Results[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=100) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=100)]

The expected results of the project are the delivery of fully functional Python bindings for Apothesis that provide seamless access to its C++ core from Python. The bindings will expose the main computational components through a clean and intuitive API, while preserving the performance and efficiency of the underlying C++ implementation.The project will also include comprehensive documentation, usage examples, and unit tests to ensure reliability, maintainability, and ease of adoption. Overall, the outcome will be a stable, extensible interface that lowers the barrier to entry for researchers and developers, enabling faster experimentation, improved interoperability with machine learning pipelines, and broader community engagement.

#### Duration of the Project[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=101) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=101)]

Large Project – 350 hrs

#### Related Repositories[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=102) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=102)]

[https://github.com/nixeimar/Apothesis](https://github.com/nixeimar/Apothesis)

#### Knowledge Prerequisites[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=103) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=103)]

C++, python

#### Mentors[[επεξεργασία](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&veaction=edit§ion=104) | [επεξεργασία κώδικα](https://ellak.gr/wiki/index.php?title=Google_Summer_of_Code_2026_proposed_ideas&action=edit§ion=104)]

Cheimarios Nikolaos, Vissarion Fysikopoulos
