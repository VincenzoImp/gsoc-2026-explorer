# INCF — Project Ideas

**Source:** https://docs.google.com/document/d/1XkelmTUV8zMtg99GsZhbYvPoyUG5uzEIWji7IXj0M4k/edit?tab=t.0
**Scraped:** 2026-03-10T16:58:40.242275

---

GSOC 2026 Ideas list for INCF

1) Brian Simulator - Serialization/deserialization for Brian sim models, results, and input data

2) Brian Simulator - Update Brian documentation infrastructure

3) Brian Simulator - Improved parser for Brian model descriptions

4) Brian Simulator - Complete/finalize code editor support for Brian model equations

5) Brian Simulator - Fix outstanding issues in Brian2CUDA

6) OpenWorm DevoWorm: DevoGraph

7) Open source Community Sustainability Greenfield

8) Open source Community Sustainability LLM

9) Contribute to LORIS

10) Western University - HarmonyHub Music Education Interface (MEI): Mobile App Hardening and Relative Intonation Learning

11) The Virtual Brain : New graphical widget(s) for JupyterLab

12) The Virtual Brain : New components in tvb-ext-xircuits

13) AnalySim : Fixing beta testing and forking

14) AnalySim : Developing user interface design and improve user experience

15) HNN (Human Neocortical Neurosolver) Projects : Refactoring synaptic behavior in HNN-Core

16) HNN (Human Neocortical Neurosolver) Projects : Refactor and expand HNN-Core testing infrastructure

17) Contribute to Experanto

18) SciCommons: Fullstack development and AI features for front-end, back-end and browser extensions

19) ActiveVision: continued development of a data and model portal for the study of goal-directed vision

20) BreathState contribution: a phone-based app for heart-rate variability biofeedback and resonance breathing protocols

21) I-EEG: health application for semi-automated iEEG analysis and viewing in a clinical and research environment

22) OWASP DevSecOps Maturity and controls implementation for the EBRAINS community - a PoC with the MIP platform

23) A Python Command Line Interface (CLI) for the CBRAIN Distributed Computing Platform

24) Improvements to BrainBrowser for neuroimaging visualization

25) ImageJ Active Segmentation platform: Parallel Engine for ASP/IJ

26) ImageJ Active Segmentation platform: UI update for ASP/IJ

27) Integrating personalized hemodynamic response function in The Virtual Brain & EBRAINS

28) Integrating blood arrival time in models of fMRI data in The Virtual Brain in EBRAINS

29) Enhancing simulation-based inference from neuroimaging

30) Large-scale brain models in Probabilistic Programming Languages

31) Accelerating Virtual Brain Inference from Neuroimaging

32) Extending the PCNtoolkit: Charting the rate of change of brain data using velocity models

33) University of Wisconsin-Madison - AStats: an agentic-AI approach to applied statistical practitioner workflows

34) University of Texas at Austin - Improving Statistical Efficiency, Methodological Coverage, and Contributor Onboarding in NiMARE

35) ImageJ Active Segmentation platform: Real-Time Filter Preview

36) Durham university - GestureCap: Creation of mappings to enable music and speech generation, to investigate musical creativity, agency and music-movement-dance interactions

37) ATHENA Research Center / EBRAINS - Automating Performance Verification for the EBRAINS Software Distribution

38) ATHENA Research Center / EBRAINS - Modular Software Environments and Service Integration for the EBRAINS Software Distribution

39) National Brain Research Centre (NBRC) & EBRAINS (NeuroSim) Automating In-Silico Stimulation for Non-Invasive Biomarker Discovery

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-1-brian-simulator-serialization-deserialization-for-brian-sim-models-results-and-input-data-175h-350h/35560](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-1-brian-simulator-serialization-deserialization-for-brian-sim-models-results-and-input-data-175h-350h/35560&sa=D&source=editors&ust=1773159824323571&usg=AOvVaw2I_zN8BUqSCV_Kz9isdZVE)

Brian is a clock-driven spiking neural network simulator that is easy to learn, highly flexible, and simple to extend. Written in Python, it allows users to describe and run arbitrary neural and synaptic models without needing to write code in any other programming language. It is built on a code-generation framework that transforms model descriptions into efficient low-level code.

Currently, the Brian simulator lacks advanced support for complex simulation pipelines that require storing or restoring the state of simulations (e.g., checkpointing) or saving a complete network architecture to a file. Such pipelines are particularly important for studies involving machine learning-like workflows, such as running a network on multiple stimuli for training and testing. In recent years, the Brian simulator has introduced several features to support these approaches, but they come with limitations and do not cover the full range of potential use cases.

The aim of this project is to improve and consolidate the Brian simulator's tools for model and state (de)serialization. Specifically, the goals of this project are to:

- Extend the current store/restore mechanism to work with Brian's C++ standalone mode and Brian2CUDA.
- Refactor the basicexporter from the brian2tools package so that it can be used to serialize a network architecture.
- Create a corresponding basicimporter to reconstruct a network from such a serialization
- For the larger 350h project, additional goals include:

- Implement annotation and metadata for models
- Investigate data formats for neural simulation/recording data (e.g. NWB or NEO) and provide export tools
- Investigate data formats for input data (e.g. AEDAT) and provide import tools
- Identify potential connection points to software from neuromorphic computing/ML and provide tools to facilitate interoperability

Skill level: Intermediate

Required skills: Python, C++

Time commitment: Part-time (175h) or full-time (350h)

Lead mentor: Benjamin Evans (B.D.Evans@sussex.ac.uk)

Project website: [https://github.com/brian-team/brian2tools](https://www.google.com/url?q=https://github.com/brian-team/brian2tools&sa=D&source=editors&ust=1773159824327312&usg=AOvVaw1N_w6N0cKJWH6wZSp2yHHr) and [https://github.com/brian-team/brian2](https://www.google.com/url?q=https://github.com/brian-team/brian2&sa=D&source=editors&ust=1773159824327456&usg=AOvVaw3oNcV6Xec_qdWigqsFe6tS)

Backup mentors: Dan Goodman (d.goodman@imperial.ac.uk; d.goodman on NeuroStars), Marcel Stimberg (marcel.stimberg@sorbonne-universite.fr; mstimberg on NeuroStars)

Tech keywords: Python, C++, serialization, data formats


2) Brian Simulator - Update Brian documentation infrastructure (175h)

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-2-brian-simulator-update-brian-documentation-infrastructure-175h/35561](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-2-brian-simulator-update-brian-documentation-infrastructure-175h/35561&sa=D&source=editors&ust=1773159824328504&usg=AOvVaw2uCRax91Ii7ITebaXL5aXQ)

The Brian 2 simulator provides extensive documentation, examples, and tutorials. Examples and tutorials are provided in different formats: as websites, downloadable files, and jupyter notebooks which can also be executed on the binder infrastructure. Generating these formats is done partly manual, i.e. by running a script on the developer’s local machine, which is inconvenient and error-prone. In addition, the examples and tutorials are not well integrated with the rest of the documentation, which could be improved by replacing some of the Brian-specific scripts by the solutions provided by the Python ecosystem.

This project has the following aims:

- Automatize the generating of example/tutorial content (e.g. by using GitHub Actions)
- Run the examples/tutorials regularly to catch errors and incompatibilities introduced by changes in Brian
- Remove some of the Brian-specific scripts and classes by migrating to established packages such as napoleon or sphinx-gallery
- Improve the presentation of the examples/tutorials and their integration with the rest of the documentation (e.g. with sphinx-gallery).

Skill level: novice

Required skills: Python programming, experience with sphinx and CI infrastructure such as GitHub Actions helpful.

Time commitment: Part-time (175 h)

Lead mentor: Marcel Stimberg (marcel.stimberg@sorbonne-universite.fr; mstimberg on NeuroStars)

Project website: [https://github.com/brian-team/brian2-binder](https://www.google.com/url?q=https://github.com/brian-team/brian-binder&sa=D&source=editors&ust=1773159824332804&usg=AOvVaw26znQKtKNyNvJL8V4wTgOo) and [https://github.com/brian-team/brian2](https://www.google.com/url?q=https://github.com/brian-team/brian2&sa=D&source=editors&ust=1773159824333067&usg=AOvVaw2h2F8o4_CUPAsZTBDMHG-k)

Backup mentors: Dan Goodman (d.goodman@imperial.ac.uk; d.goodman on NeuroStars), Benjamin Evans (B.D.Evans@sussex.ac.uk)

Tech keywords: Python, Sphinx, GitHub Action

3) Brian Simulator - Improved parser for Brian model descriptions (175h)

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-3-brian-simulator-improved-parser-for-brian-model-descriptions-175h/35562](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-3-brian-simulator-improved-parser-for-brian-model-descriptions-175h/35562&sa=D&source=editors&ust=1773159824334826&usg=AOvVaw0w8TnrkigYxwiaBqex5J-2)

Computational research in biology commonly consists of describing a model system and its parameters, simulating the system with specialized software, and then analyzing the results. Model descriptions often make use of a domain-specific language that is parsed and interpreted by the simulation software. Such languages have the advantage that they are more accessible to researchers than code written in a general-purpose programming language; they also make it easier to discuss and share models with other researchers.

Parsing such languages is mostly straightforward with standard techniques, but these techniques regularly have at least two shortcomings:

- For syntactically incorrect descriptions, e.g. a missing parenthesis, error messages are typically not very helpful and of the form “unexpected symbol at position x”, and
- annotations via comments are usually simply ignored, instead of being used to enrich a model description.

Both of these shortcomings are currently present in the Brian simulator, an open-source simulator for biological spiking neural networks written in Python, developed in our research group and used by researchers world-wide. The Brian simulator describes models with a domain-specific language that uses mathematical notation with additional annotations, e.g. to assure the consistency of physical dimensions.

The goal of this internship is to rewrite the Brian simulator’s parsing code to give clear and helpful error messages for incorrect model descriptions, as well as treating comments in the model descriptions as annotations that are stored for future usage.

Skill level: Advanced

Required skills: Python programming, parser/compiler techniques.

Time commitment: Part-time (175 h)

Lead mentor: Dan Goodman (d.goodman@imperial.ac.uk; d.goodman on NeuroStars)

Project website: [https://github.com/brian-team/brian2](https://www.google.com/url?q=https://github.com/brian-team/brian2&sa=D&source=editors&ust=1773159824340020&usg=AOvVaw0GyL__O1bEF309pnqFQo-Y)

Backup mentors: Benjamin Evans (B.D.Evans@sussex.ac.uk), Marcel Stimberg (marcel.stimberg@sorbonne-universite.fr; mstimberg on NeuroStars)

Tech keywords: Python, PyParsing, Parsing, Compiler

4) Brian Simulator - Complete/finalize code editor support for Brian model equations (175h)

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-4-brian-simulator-complete-finalize-code-editor-support-for-brian-model-equations-175h/35563](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-4-brian-simulator-complete-finalize-code-editor-support-for-brian-model-equations-175h/35563&sa=D&source=editors&ust=1773159824342643&usg=AOvVaw08ouQ2s6HbUC2M5zpflLbW)

Differential equations, defined in Python strings, are at the core of Brian’s model descriptions. They use a language familiar to computational neuroscientists, and closely follow the way that languages are described in scientific articles. Defining these equations in strings has the advantage that these descriptions are very concise, and can be read as mathematical equations, and not as programming code. The fact that equations are “just strings” does have disadvantages as well, though: from the point of view of a code editor, they are simply text and do not benefit from helpful features such as syntax highlighting, autocompletion, or syntax checks.

To improve this situation, a former GSoC student implemented g a Brian-specific “Language Server extension” and syntax highlighting rules, that provides these features for Brian equations embedded in a Python script. The Language Server Protocol (LSP) has been created by Microsoft and is used to provide advanced editing features to editors such as Visual Studio Code, but it is now supported by a large number of editors.

The goal of this project is to complete the work on the existing proof-of-concept and make it production-ready. In particular:

- Make the installation progress smooth and integrate with VS Code's existing Python support
- Implement a smart and robust detection of equation strings
- Implement semantic autocompletion
- Implement helpful error displays inside an equation string
- If time permits: add support for automatic formatting of equations

Skill level: intermediate

Required skills: JavaScript/TypeScript, JSON, asynchronous programming, basic knowledge of grammars/regular expressions.

Lead mentor: Benjamin Evans ([B.D.Evans@sussex.ac.uk](mailto:B.D.Evans@sussex.ac.uk))

Project website: [https://github.com/brian-team/brian2](https://www.google.com/url?q=https://github.com/brian-team/brian2&sa=D&source=editors&ust=1773159824347902&usg=AOvVaw1rhJOUbVIeZncoRgvJbY5Y) and [https://github.com/brian-team/brian-code-editor](https://www.google.com/url?q=https://github.com/brian-team/brian-code-editor&sa=D&source=editors&ust=1773159824348213&usg=AOvVaw1VDGPrBZoDGGY1ltzP3w_k)

Backup mentors: Marcel Stimberg (marcel.stimberg@sorbonne-universite.fr; mstimberg on NeuroStars) , Dan Goodman (d.goodman@imperial.ac.uk; d.goodman on NeuroStars)

Tech keywords: Python, Visual Studio Code, Language Server Protocol

Neurostars Link for idea discussion:[https://neurostars.org/t/gsoc-2026-project-5-brian-simulator-fix-outstanding-issues-in-brian2cuda-175h-350h/35564](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-5-brian-simulator-fix-outstanding-issues-in-brian2cuda-175h-350h/35564&sa=D&source=editors&ust=1773159824350017&usg=AOvVaw3HjN50SPobKkadl6ENoF2Q)

The Brian simulator's "C++ standalone mode" has been extended to support code generation for CUDA via the Brian2CUDA package (Alevi et al. 2022, Frontiers Neuroinformatics). This makes it possible to accelerate simulations by making use of the parallel processing capabilities of NVIDIA GPUs. The package is already widely used, despite the software still being in a "beta" state. The aim of this project is to make the package "production-ready" by tackling various issues from the project's issue tracker. Particular aims include:

- Add Windows support by adapting the makefile and compilation options
- Improve compilation speed
- Update and extend documentation
- Implement support for preference files
- Implement a configurable logging system
- For the bigger project scope, in addition:

- Triage the existing issue reports
- Triage and fix (if necessary/possible) the existing performance issues
- Set up a basic test suite that can be run online on free infrastructure (e.g. Google Collab with GPU support)

Skill level: intermediate

Required skills: C++, CUDA, Python

Lead mentor: Marcel Stimberg (marcel.stimberg@sorbonne-universite.fr; mstimberg on NeuroStars)

Project Website: [https://github.com/brian-team/brian2cuda](https://www.google.com/url?q=https://github.com/brian-team/brian2cuda&sa=D&source=editors&ust=1773159824354199&usg=AOvVaw2yk5PU58Zr65BzgTTe2tVC) and [https://github.com/brian-team/brian2](https://www.google.com/url?q=https://github.com/brian-team/brian2&sa=D&source=editors&ust=1773159824354413&usg=AOvVaw0WTW6G8ZOUUQAFTXtSkXkg)

Backup mentors: Dan Goodman (d.goodman@imperial.ac.uk; d.goodman on NeuroStars), Benjamin Evans ([B.D.Evans@sussex.ac.uk](mailto:B.D.Evans@sussex.ac.uk))

Tech keywords: Python, C++, CUDA, GPU, Makefile

6) OpenWorm DevoWorm: DevoGraph

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-6-openworm-devoworm-devograph/35565](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-6-openworm-devoworm-devograph/35565&sa=D&source=editors&ust=1773159824355602&usg=AOvVaw0F1D0cYcgA6vW2YvI2f_QS)

Mentors: Bradly Alicea <[bradly.alicea@outlook.com](mailto:bradly.alicea@outlook.com)>, Mehul Arora <[22mehularora22@gmail.com](mailto:22mehularora22@gmail.com)>, Jesse Parent <[jesse@jopro.org](mailto:jesse@jopro.org)>

Skill level: Advanced

Required skills: All of our existing models are built for PyTorch, so experience with Python and PyTorch/Tensorflow workflows is preferred. The ability to work with datasets, such as segmenting video and generating graph visualizations is essential. An ability to build web interfaces, UI design, basic knowledge of biology, open-source practices, and applied mathematical tools will also be useful.

Time commitment: Full time (350 hours)


About: The DevoWorm group has developed an open-source Graph neural network (GNN) framework for embryogenetic data called DevoGraph. Developmental GNNs (D-GNNs) allow us to characterize a growing network that undergoes shape transformations along with increases in size. This is ultimately important for understanding formation of the connectome and the origins of embodied behavior.

Aims: For this year’s project, the successful applicant will work on extending our two outcomes from last year:

- The first direction involves working with Neural Developmental Programs to build growing neural networks. This provides a means to model the function of embryogenetic networks, developing connectomes, and other growth processes
- The second direction involves working with hyper graph representations, enabling multiscale modeling from a network perspective.

We aim to tie our D-GNN work into the group’s ongoing theoretical and computational work. As such, this project will require the ability to work with mathematical models and associated algorithms. Knowledge of graph and/or network theory is helpful, but not required.

What can I do before GSoC?

You can ask one of the mentors to direct you to the data source and you can start working on it. Please feel free to join the Openworm Slack or attend our meetings to raise questions/discussions regarding your approach to the problem.

- OpenWorm Foundation:
[https://openworm.org/](https://www.google.com/url?q=https://openworm.org/&sa=D&source=editors&ust=1773159824358910&usg=AOvVaw09NoQoeTDA-bHqhC9dbfRu) - DevoWorm website:
[https://devoworm.weebly.com/](https://www.google.com/url?q=https://devoworm.weebly.com/&sa=D&source=editors&ust=1773159824359161&usg=AOvVaw0F6ekh-ZfcBC-2Hf2YbAWO) - DevoGraph (Github):
[GitHub - DevoLearn/DevoGraph](https://www.google.com/url?q=https://github.com/DevoLearn/DevoGraph&sa=D&source=editors&ust=1773159824359364&usg=AOvVaw26bFGQmgnjFNmt1vGxfWe5) - DevoWorm AI:
[DevoWorm.AI](https://www.google.com/url?q=http://devoworm.ai&sa=D&source=editors&ust=1773159824359543&usg=AOvVaw0dwsayLzfO9XIDnjtmFiK5)

Project website: [https://devoworm.weebly.com](https://www.google.com/url?q=https://devoworm.weebly.com&sa=D&source=editors&ust=1773159824359803&usg=AOvVaw3hYttNqZOj2wQDrODIbQaJ)

Tech keywords: GNNs, Computational Biology, Graph Theory, PyTorch

7) Open source Community Sustainability Greenfield


Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-7-open-source-community-sustainability-greenfield/35566](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-7-open-source-community-sustainability-greenfield/35566&sa=D&source=editors&ust=1773159824360617&usg=AOvVaw3BP45cStEFxN7sIONTJKxd)

Mentors: Bradly Alicea <[bradly.alicea@outlook.com](mailto:bradly.alicea@outlook.com)>, Sarrah Bastawala <[sarrahbastaw@google.com](mailto:sarrahbastaw@google.com)>, Jesse Parent <[jesse@jopro.org](mailto:jesse@jopro.org)>

Skill level: Advanced

Required skills: Expertise or the ability to integrate multiple development environments is an important baseline skill. The ability to extract model representations from complex systems is helpful. Knowledge of open-source development practices and an interest in interdisciplinary research are a must.

Time commitment: Fulltime (350 hours)

About: Open-source communities are only as powerful as their ability to collectively complete tasks and projects. One way to enable the functional capacity of such a community is to model the collective behavioral and cognitive aspects of day-to-day project engagement. Your current involvement will involve the maintenance, development, and further implementation of two models from past years: a Reinforcement Learning model, and a hybrid Agent-based/Large Language Model. The candidate will build an analytical model that incorporates features such as general feedback loops (recurrent relationships) and causal loops (reciprocal causality). This might be in the form of a traditional boxes and arrows (input-output) model, or something more exotic such as Reinforcement Learning.

Aims: In 2024, Github activity was simulated with a CodeSpace Environment. This included generating issues of varying difficulty for both contributor and maintainer agents. Implementing CodeSpace resulted in the following capabilities: different coding ability and experience levels, a discussion space to discuss various approaches for a particular task among agents, an automated pull request lifecycle as well as multiple decision-making algorithms to choose task allocation for contributors and corresponding metrics for its simulation. For 2025, you might help to improve upon the underlying models (https://github.com/OREL-group/GSoC/issues/64) or add a ConversationSpace (https://github.com/OREL-group/GSoC/issues/60) within this framework to simulate a IRC (Internet Relay Chat) / Slack / Discord model, an essential part of many open source communities. Last year’s project utilized RAG (Retrieval Augmented Generation) ([https://github.com/OREL-group/GSoC/issues/62](https://www.google.com/url?q=https://github.com/OREL-group/GSoC/issues/62&sa=D&source=editors&ust=1773159824364460&usg=AOvVaw01c-G4DYx5-7VwrddpUXHL)), but other approaches backed by research are also welcome. Our goal is to develop one or more maintainers of the platform who are also capable of research software engineering ([https://www.hpcwire.com/off-the-wire/ncsa-innovators-bridging-research-and-software-engineering/](https://www.google.com/url?q=https://www.hpcwire.com/off-the-wire/ncsa-innovators-bridging-research-and-software-engineering/&sa=D&source=editors&ust=1773159824365093&usg=AOvVaw1NZbzIVNERh9b-4zEcKl3M)).

What can I do before GSoC?

You can join the Orthogonal Lab Slack and Github, as well as attend our Saturday

Morning NeuroSim meetings. You might also become familiar with the existing codebase:

- LLAMOSC (Agent-based and Large Language Hybrid Model):
[https://github.com/OREL-group/GSoC/tree/main/Open%20Source%20Sustainibility%20using%20LLMs](https://www.google.com/url?q=https://github.com/OREL-group/GSoC/tree/main/Open%2520Source%2520Sustainibility%2520using%2520LLMs&sa=D&source=editors&ust=1773159824365807&usg=AOvVaw1gMZMrgn3VreQWqHQbZeRU) - MARLSOC (Multi-agent Reinforcement Learning):
[https://github.com/OREL-](https://www.google.com/url?q=https://github.com/OREL-&sa=D&source=editors&ust=1773159824366102&usg=AOvVaw2y0p-0lB9NQkHHG2pLkPoJ)

[group/GSoC/tree/main/Open%20Source%20Sustainability%20using%20RL](https://www.google.com/url?q=https://github.com/OREL-&sa=D&source=editors&ust=1773159824366287&usg=AOvVaw384ToY1__b4va0cDdA45Pi)

Project website: [https://orthogonal-research.weebly.com](https://www.google.com/url?q=https://orthogonal-research.weebly.com&sa=D&source=editors&ust=1773159824366523&usg=AOvVaw2qXFXTWuEqgiXZnr9w3h1Y)

Tech keywords: Computational Modeling, Reinforcement Learning, Language Models

8) Open source Community Sustainability LLM

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-8-open-source-community-sustainability-llm/35567](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-8-open-source-community-sustainability-llm/35567&sa=D&source=editors&ust=1773159824367172&usg=AOvVaw2ZDAkb8MZPkyv5D9ZuVtEs)


As demonstrated by many organizations, open-source communities can do great things. But this is only true if the contributor community can maintain public goods such as the software codebase and institutional knowledge over time and despite contributor turnover. Moreover, as the demand for open-source software continues to grow, so do the challenges related to community management, collaboration, and sustainability. During GSoC 2024, one of the approaches to address this was the creation of LLAMOSC (LLM-Powered Agent-Based Model for Open Source Communities), a comprehensive framework designed to simulate and enhance the sustainability of open-source communities using Large Language Models (LLMs)([https://github.com/OREL-group/GSoC/tree/main/Open%20Source%20Sustainibility%20using%20LLMs](https://www.google.com/url?q=https://github.com/OREL-group/GSoC/tree/main/Open%2520Source%2520Sustainibility%2520using%2520LLMs&sa=D&source=editors&ust=1773159824368355&usg=AOvVaw0eWQ1WurQAXbONGRTBshCH)).

In 2024, the main work was done to simulate Github i.e a CodeSpace Environment within this framework, complete with issues of varying difficulty, contributor as well as maintainer agents with different coding ability and experience levels, an discussion space to discuss various approaches for a particular task among agents, an automated pull request lifecycle as well as multiple decision-making algorithms to choose task allocation for contributors and corresponding metrics for its simulation. For this project, the need is to maintain and develop the LLAMOSC framework. Additional features also include to improve upon the underlying models ([https://github.com/OREL-group/GSoC/issues/64](https://www.google.com/url?q=https://github.com/OREL-group/GSoC/issues/64&sa=D&source=editors&ust=1773159824369345&usg=AOvVaw3Sq6PBQw9L2LYm_oU-sMFd)) and add a ConversationSpace ([https://github.com/OREL-group/GSoC/issues/60](https://www.google.com/url?q=https://github.com/OREL-group/GSoC/issues/60&sa=D&source=editors&ust=1773159824369535&usg=AOvVaw2_RatNOI1Ykgrv64aVs86J)) within this framework to simulate a IRC (Internet Relay Chat) / Slack / Discord model, an essential part of many open source communities. A possible approach for this is using RAG (Retrieval Augmented Generation) ([https://github.com/OREL-group/GSoC/issues/62](https://www.google.com/url?q=https://github.com/OREL-group/GSoC/issues/62&sa=D&source=editors&ust=1773159824369940&usg=AOvVaw3tokS1kTEx_szS0IW9XhqN)) but other approaches backed by research are also welcome. Our goal is to develop one or more maintainers of the platform who are also capable of research software engineering ([https://www.hpcwire.com/off-the-wire/ncsa-innovators-bridging-research-and-software-engineering/](https://www.google.com/url?q=https://www.hpcwire.com/off-the-wire/ncsa-innovators-bridging-research-and-software-engineering/&sa=D&source=editors&ust=1773159824370372&usg=AOvVaw1quPs1GhRXR8kG4Z22_1BV)).

What can I do before GSoC? You can join the Orthogonal Lab, as well as attend our Saturday Morning NeuroSim meetings. You will work with our Ethics, Society, and Technology group, and interactions with your colleagues is key. You will also want to become familiar with our various Open Source Sustainibility Models ([https://github.com/OREL-group/GSoC](https://www.google.com/url?q=https://github.com/OREL-group/GSoC&sa=D&source=editors&ust=1773159824370943&usg=AOvVaw2o7rJdehgi9QKwJg0bRaEC)) developed in previous years, as well as go through installation steps ([https://github.com/OREL-group/GSoC/tree/main/Open%20Source%20Sustainibility%20using%20LLMs#installation-instructions](https://www.google.com/url?q=https://github.com/OREL-group/GSoC/tree/main/Open%2520Source%2520Sustainibility%2520using%2520LLMs%23installation-instructions&sa=D&source=editors&ust=1773159824371257&usg=AOvVaw1goNVkhEaALTbCZOlUNXsJ)) and various open issues related to LLAMOSC ([https://github.com/OREL-group/GSoC/issues/created_by/sarrah-basta](https://www.google.com/url?q=https://github.com/OREL-group/GSoC/issues/created_by/sarrah-basta&sa=D&source=editors&ust=1773159824371456&usg=AOvVaw1iqLmVfTuo2pUFTitsPA-o))

Orthogonal Research and Education Lab:[ ](https://www.google.com/url?q=https://orthogonal-research.weebly.com/&sa=D&source=editors&ust=1773159824371663&usg=AOvVaw0Bf4xzEiMIT-JIiThBZhYE)[https://orthogonal-research.weebly.com/](https://www.google.com/url?q=https://orthogonal-research.weebly.com/&sa=D&source=editors&ust=1773159824371761&usg=AOvVaw04s88DtBqtjQm-CeAufBgF)

Skill level: Intermediate

Required skills: The following languages and frameworks will be used extensively throughout the project: Python, PyQT and Ollama. This project will also involve working with Large Language Models, computational and agent-based models, UI design, and open-source community-building, so experience in these areas is helpful but not required. Knowledge of open-source development practices and an interest in interdisciplinary research are a must.

Time commitment: Full-time (350 h)

Lead mentor: Sarrah Bastawala ([sarrahbastaw@gmail.com](mailto:sarrahbastaw@gmail.com))

Project website:[ ](https://www.google.com/url?q=https://orthogonal-research.weebly.com/&sa=D&source=editors&ust=1773159824373353&usg=AOvVaw0M0Iwal8WtuYEt333TgswV)[https://orthogonal-research.weebly.com/](https://www.google.com/url?q=https://orthogonal-research.weebly.com/&sa=D&source=editors&ust=1773159824373481&usg=AOvVaw2FA0t4OEQprlBcmhQqcFSd)

Backup mentors: Bradly Alicea ([bradly.alicea@outlook.com](mailto:bradly.alicea@outlook.com)), Jesse Parent ([jesse@jopro.org](mailto:jesse@jopro.org))

Tech keywords: Open Source Communities, Large Language Models (LLM), Agent-based Models, Python, PyQT, Ollama

9) Contribute to LORIS

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-9-contribute-to-loris/35568](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-9-contribute-to-loris/35568&sa=D&source=editors&ust=1773159824374470&usg=AOvVaw2-pqbXqJMTKvu2yFeRWIjN)


Project Idea: Feature enhancements for LORIS multimodal open neuroscience platform

Mentors: Christine Rogers <Christine.rogers@mcin.ca> and Saagar Arya <[saagar.arya@mcgill.ca](mailto:saagar.arya@mcgill.ca)>

Skill level: Advanced

Required skills: Solid programming background, generally a combination of python or javascript, and unix-based development experience. Some familiarity with psychology/science research, databasing or medical imaging is an asset.

Important: We cannot support Machine Learning project proposals due to ethical constraints on sharing sensitive research data and synthetic generation costs.

Time commitment: Flexible (175/350 hours). 350 hours preferred for long-format project.

About: LORIS is an open-source database for neuroscience research projects and Open Science initiatives. Scientists and doctors worldwide use LORIS' open-stack web platform to collect and curate, analyze and share data - including brain scans, genetic data, psychological tests, wearables, electrophysiology and more. LORIS database instances are utilized by research projects in 22 countries, and open data projects are also accessed by researchers worldwide. Within the LORIS platform, 3D visualization and advanced data tools offer a dynamic workflow environment for complex neuroinformatics research - see [demo.loris.ca](https://www.google.com/url?q=https://demo.loris.ca/&sa=D&source=editors&ust=1773159824377066&usg=AOvVaw0fYoZpQdM_54MwiQ2ZwGM5).

For a few examples, LORIS currently hosts datasets such as the UK Biobank and the BigBrain 3D Atlas ([bigbrain.loris.ca](https://www.google.com/url?q=http://bigbrain.loris.ca/&sa=D&source=editors&ust=1773159824377424&usg=AOvVaw02k2RD1k-58hxn7uVpIWVJ) ) - a high-resolution model of the human brain.

Working with LORIS: LORIS runs on linux, mysql, javascript/React and php, with a RESTful API and NoSQL querying engine. LORIS developers work on this open stack, and we collectively test and review code at [github.com/aces/loris](https://www.google.com/url?q=https://github.com/aces/loris&sa=D&source=editors&ust=1773159824377946&usg=AOvVaw18YkCPW16l4K_9YqRDZPih) . We'd love to have you join our diverse team of 20 developers affiliated with the Montreal Neurological Institute and McGill University in Montreal, Canada – We especially encourage those from underrepresented backgrounds and/or interest in neuroscience, medicine or psychology research, bioinformatics, or image/signal processing to apply.

Aims: Projects can be proposed to align with the applicant's interests, background and strengths, and developed with input from our team. Some examples from past INCF Google Summer of Code projects include: new module development, imaging pipelines, automated testing, API development. Machine Learning project proposals cannot be accepted.

Website: [https://loris.ca/](https://www.google.com/url?q=https://loris.ca/&sa=D&source=editors&ust=1773159824378976&usg=AOvVaw3ge9igFBscJrRnrj2luUXi)

Tech keywords: LORIS, JavaScript, React, REST, NoSQL, databasing, imaging, platform, open science, MRI, EEG

About AI-assisted contributions: Please carefully review our [Contributing.md and AI Policy](https://www.google.com/url?q=https://github.com/aces/Loris/blob/main/CONTRIBUTING.md%23ai-policy&sa=D&source=editors&ust=1773159824379463&usg=AOvVaw0duVbBGprR7kQ9xcGwC1dl).

How to Apply:

To get in touch with us, please be sure to email christine.rogers@mcin.ca your CV (attachment) and GitHub profile link and let us know about any relevant background (e.g. clinical / research / neuroimaging). We will work with as many candidates as we can to give guidance on suitable project proposals for their interests and experience.

10) Western University - Music Education Interface (MEI): Mobile App Hardening and Relative Intonation Learning

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-10-western-university-music-education-interface-mei-mobile-app-hardening-and-relative-intonation-learning/35569](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-10-western-university-music-education-interface-mei-mobile-app-hardening-and-relative-intonation-learning/35569&sa=D&source=editors&ust=1773159824380695&usg=AOvVaw22HQe4X730tOo-nE7f0n7f)

Context: This project continues and expands the Music Education Interface (MEI), an educational web app that supports learners in building core instrumental skills (rhythm, fingering, intonation, articulation, timbre) through dedicated interactive modules. Learn more about the current app here: [https://albertoacquilino.github.io/en/portfolio_music_education_interface.html](https://www.google.com/url?q=https://albertoacquilino.github.io/en/portfolio_music_education_interface.html&sa=D&source=editors&ust=1773159824381216&usg=AOvVaw3J2KGWZUFZsHsLA6-USXFw)

MEI already runs in the browser and is also available as a beta app on iOS and Android. The roadmap highlights mobile-first experiences and new practice components as key next steps.

Project description: The main goal is to make MEI robust, responsive and maintainable across mobile devices, and to ensure reliable store-ready builds for both Apple App Store and Google Play. The contributor is expected to work on mobile release engineering, including managing iOS and Android store builds and submission using existing developer accounts. In the second half of the project, the contributor will implement a new learning module: a Relative Intonation exercise that trains students to play in tune with what they hear, using the app's existing score display, audio generation and tuner components. This component will be developed after the mobile app is stable and successfully published, and will reuse the existing modular architecture of MEI. By the end of GSoC, the project will deliver:

- A mobile-first MEI app that is responsive across screen sizes, stable and easier to maintain.
- A documented, repeatable release workflow for iOS and Android (build, versioning, store submission readiness & bug triage), building on the existing Capacitor setup.
- A new relative intonation exercise module, integrated into the current app using already-existing musical notation, synthesis and tuner features.

Why this project matters: Many music apps help with timing (metronomes) and absolute pitch (tuners), but real ensemble playing requires relative intonation: the ability of staying in tune with another sound (a partner musician, a synthesized sound; at unison or within a chord). Students often look at the tuner instead of learning to listen and adjust. This module trains the ear by letting the learner:

- See a note on a staff (music notation).
- Hear a reference sound in headphones (generated by the app).
- Play while matching the reference by ear, optionally using the tuner as training wheels.

The exercise supports two learning modes:

- Unison matching: the student plays the same note they hear.
- Chord completion: the app plays a chord with one note missing, and the student plays the missing note so the result sounds locked in and stable.

Objectives :-

Part A: Mobile UI/UX + Store Release Hardening (continuative)

- Refactor UI to be fully responsive (mobile-first layouts; small/large phones; tablets) and ensure consistent behavior across iOS, Android, and browser targets.
- Stabilize the mobile app release pipeline:

- Ensure reproducible builds with Ionic + Angular + Capacitor.
- Handle versioning correctly (iOS/Android) and document the process.

- Bug triage and fixes focused on real-device issues (audio I/O, permissions, latency, UI glitches, crashes, edge cases).
- Enable dark mode for the web-app
- Add screen reader support (enhanced accessibility)
- Improve developer documentation so future contributors can publish updates confidently.

Part B: New Module: "Relative Intonation" Exercise

- Design and implement a new exercise that combines existing components:

- Score rendering (display notes to play).
- Audio generation (play reference notes/chords).
- Tuner / pitch detection (optional live feedback).

- Implement the two modes:

- Mode 1: Unison (match pitch with a synthesized reference of the same instrument type).
- Mode 2: Chord completion (play the missing chord tone).

- Provide a simple scoring/feedback loop (e.g., in-tune percentage over time, stability indicator, and optional tuner view toggle).

Technologies and Frameworks

- Ionic + Angular + TypeScript (core stack).
- JavaScript/Web Audio (audio synthesis/playback).
- Capacitor iOS/Android toolchain (store builds and native integration).
- Responsive CSS / UI patterns for multi-screen support.

Suggested timeline (12 weeks)

What can I do before GSoC?

- Familiarize yourself with the existing HarmonyHub codebase, particularly the front-end architecture.
- Explore responsive design principles and best practices for cross-platform development.
- Experiment with Angular and Ionic to understand their capabilities for building modular, reusable components.

Skills Required

- Strong Ionic + Angular + TypeScript/JavaScript skills.
- Proven experience building, releasing, and maintaining mobile apps on iOS and Android, including hands-on familiarity with App Store Connect and Google Play Console workflows.
- Understanding of responsive design and real-device testing.
- Basic comfort with audio concepts (latency, microphone permissions, pitch detection).

Bonus Skills

- Experience developing native mobile apps for iOS and Android.
- Music performance experience.

Skill level: Advanced

Time Commitment: Large (approx. 350 hours)

Lead mentor: Alberto Acquilino ([aacquili@uwo.ca](mailto:aacquili@uwo.ca))

Backup mentors:

- Mirko D’Andrea (
[mirko.dandrea@gmail.com](mailto:mirko.dandrea@gmail.com)) - Komal Bhalotia (
[bhalotiakomal60@gmail.com](mailto:bhalotiakomal60@gmail.com)) - Priyanshu (
[techarena955@gmail.com](mailto:techarena955@gmail.com))

Project affiliation: This project is part of the research initiatives at Western University, aiming to improve music education through digital means.

GitHub repository: [https://github.com/albertoacquilino/music_education_interface](https://www.google.com/url?q=https://github.com/albertoacquilino/music_education_interface&sa=D&source=editors&ust=1773159824391023&usg=AOvVaw0T8HBzfqT-QrHbk0NvCt33)

Project website: [https://albertoacquilino.github.io/en/mei_gsoc_project.html](https://www.google.com/url?q=https://albertoacquilino.github.io/en/mei_gsoc_project.html&sa=D&source=editors&ust=1773159824391316&usg=AOvVaw3sFKzN4h8Rx5ofDC-6Zi53)

GsoC 2025 Final Report: [https://gist.github.com/bhalotia05/0202d8d8cdab05e1b545c969440848bc](https://www.google.com/url?q=https://gist.github.com/bhalotia05/0202d8d8cdab05e1b545c969440848bc&sa=D&source=editors&ust=1773159824391643&usg=AOvVaw1OugHpYHZQIrb9704unjCc)

Tech Keywords: Front-End Development, Mobile App Development, Angular, Ionic, Responsive Design, Web Audio, Accessibility, UI/UX Design, Music Education


11) The Virtual Brain : New graphical widget(s) for JupyterLab

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-11-the-virtual-brain-new-graphical-widget-s-for-jupyterlab/35570](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-11-the-virtual-brain-new-graphical-widget-s-for-jupyterlab/35570&sa=D&source=editors&ust=1773159824392283&usg=AOvVaw0fw84qYC0pRX3P3J5dKy8v)

Description: In the TVB (https://www.thevirtualbrain.org/) ecosystem there is a new code repository called tvb-widgets offering neat UI widgets for Jupyterlab environments. These widgets are compatible with TVB data formats and able to display these data in different forms: 2D, 3D. The purpose of this project is to implement a new set of widgets, which would allow users to work in Jupyter Lab in 3D, with the connectivity matrices (nodes & edges), surfaces (cortical, subcortical, face), sensors and all data involved in a TVB simulation. Necessary features for this widget: select from a drive the list of available datesets, load/unload a dataset, display connectivity matrix, 3D surface, connections, colours, animated timeseries, etc. Of course, these new widgets have to run in a Jupyterlab notebook as well. We have most of these already in the existent widgets, but we are looking into maybe new libraries to use, better performance, better usability - so a renovation of some of the existent features. Finally, it would be great to have all the widgets linked into the tvb-ext-xircuits repository which is a Jupyterlab extension based on React JS. At the moment, only the PhasePlaneWidget is linked there, but the rest could be added in a similar manner.

Examples of TVB data formats can be found on Zenodo. Check out our Jupyter notebooks to play with the widgets we have available so far.

Expected results: A set of classes , with at least one demo Jupyter notebook, and unit tests.

Preferred Tech keywords: Python, IPywidgets, React JS, Jupyterlab, Jupyterlab extensions

Skills level: junior+, mid

Mentors: Lia Domide (lead) <[lia.domide@codemart.ro](mailto:lia.domide@codemart.ro)>, Paula Prodan <[paula.popa@codemart.ro](mailto:paula.popa@codemart.ro)>, Teodora Misan (backup) <[teodora.misan@codemart.ro](mailto:teodora.misan@codemart.ro)>

12) The Virtual Brain : New components in tvb-ext-xircuits

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-12-the-virtual-brain-new-components-in-tvb-ext-xircuits/35571](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-12-the-virtual-brain-new-components-in-tvb-ext-xircuits/35571&sa=D&source=editors&ust=1773159824395882&usg=AOvVaw3VN364emDYLF0e3z2mGJ2n)

Description: In the TVB (https://www.thevirtualbrain.org/) ecosystem there is a code repository called tvb-ext-xircuits offering a graphical way to define, configure and run simulation workflows. The purpose of this project is to implement a new set of xircuits components, in particular for running Parameter Space Explorations (so a range of simulations with little variation in 2-3 parameters).

Expected results: A set of new xircuits components , with at least one demo xircuits file.

Preferred Tech keywords: Python, xircuits, Jupyterlab4, Jupyterlab extensions

Skills level: junior+, mid

Mentors: Lia Domide (lead) <[lia.domide@codemart.ro](mailto:lia.domide@codemart.ro)>, Paula Prodan <[paula.popa@codemart.ro](mailto:paula.popa@codemart.ro)>, Teodora Misan (backup) <[teodora.misan@codemart.ro](mailto:teodora.misan@codemart.ro)>

13) AnalySim : Fixing beta testing and forking

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-13-analysim-fixing-beta-testing-and-forking/35572](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-13-analysim-fixing-beta-testing-and-forking/35572&sa=D&source=editors&ust=1773159824398784&usg=AOvVaw0ZjvWGJRr25EYy7-UJ2iXg)

Mentors: Cengiz Gunay <[cgunay@ggc.edu](mailto:cgunay@ggc.edu)>, Anca Doloc-Mihu, <[adolocm@gmail.com](mailto:adolocm@gmail.com)> (Planned break for both mentors due to CNS meeting: July 5 - July 9 with limited email contact)

Skill level: intermediate/advanced preferable

Required skills: C#, .Net, HTML/CSS/Bootstrap, Angular, TypeScript, PostgreSQL, Docker

Time commitment: Full-time (350 hours)

About: AnalySim is a data sharing and analysis platform that seeks to simplify the visualization of datasets. With Analysim, researchers can collaborate by hosting their data and publishing their analysis notebooks to the world, or browse through multiple user-generated projects. Analysim is currently being hosted on the NSF-funded ACCESS-CI project infrastructure, but it can also be deployed independently via Docker.

AnalySim aims to be a general data sharing and hosting resource for crowdsourced-analysis, but it provides additional support for a specific type of dataset: one where many parameter combinations need to be tested and measurements are recorded for each instance. These datasets are very useful in mathematical modeling of natural phenomena, such as in computational neuroscience. We provide easy sharing, analysis, visualization, and collaboration capabilities on these datasets. In this GSoC iteration, we are improving on features developed in the summer and winter of 2024.

Aims: Helping run the controlled beta testing by fixing issues and adding new features for forking datasets/projects, following/joining projects. Improving usability of CSV data browser, versioning, and querying components.

Website: Project is still in progress and a demo site is available at: https://analysim.tech and a development version is at https://dev.analysim.tech

Source code: [https://github.com/soft-eng-practicum/AnalySim](https://www.google.com/url?q=https://github.com/soft-eng-practicum/AnalySim&sa=D&source=editors&ust=1773159824404031&usg=AOvVaw352S9HfFkpvYPl4gNrOpkW)

Tech Keywords: Angular (Typescript), HTML/CSS/Bootstrap, .Net Core (C#), PostgreSQL, and for analysis notebooks: JavaScript (ObservableHQ, D3.js, Vega, Plotly) and Python (Jupyter)


14) AnalySim : Developing user interface design and improve user experience

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-14-analysim-developing-user-interface-design-and-improve-user-experience/35573](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-14-analysim-developing-user-interface-design-and-improve-user-experience/35573&sa=D&source=editors&ust=1773159824405725&usg=AOvVaw2conIh5eGYtzL0h5oOP7Hn)

Mentors: Anca Doloc-Mihu, <[adolocm@gmail.com](mailto:adolocm@gmail.com)>, Cengiz Gunay <[cgunay@ggc.edu](mailto:cgunay@ggc.edu)>

Skill level: intermediate/advanced preferable

Required skills: HTML/CSS/Bootstrap, Angular, TypeScript

Time commitment: half-time or more (175-350 hours flexible)

About: AnalySim is a data sharing and analysis platform that seeks to simplify the visualization of datasets. With Analysim, researchers can collaborate by hosting their data and publishing their analysis notebooks to the world, or browse through multiple user-generated projects. Analysim is currently being hosted on the NSF-funded ACCESS-CI project infrastructure, but it can also be deployed independently via Docker.

AnalySim aims to be a general data sharing and hosting resource for crowdsourced-analysis, but it provides additional support for a specific type of dataset: one where many parameter combinations need to be tested and measurements are recorded for each instance. These datasets are very useful in mathematical modeling of natural phenomena, such as in computational neuroscience. We provide easy sharing, analysis, visualization, and collaboration capabilities on these datasets. In this GSoC iteration, we are improving on features developed in the summer and winter of 2024.

Aims: Working on a more consistent visual user interface style and improved user experience. Design an optimal dashboard layout along with other necessary pages for project notebooks, publications, and commenting. Design new pages to incorporate al necessary user operations, project operations, and datasets analysis and sharing operation. Improve user experience workflow for common actions, and improve usability of CSV data browser. Adding examples of datasets, notebooks, and projects. Implement and test bootstrap on all pages to make the app available with a consistent clean layout on mobile devices.

Tech Keywords: Angular (Typescript), HTML/CSS/Bootstrap, .Net Core (C#), PostgreSQL, and for analysis notebooks: JavaScript (ObservableHQ, D3.js, Vega, Plotly) and Python (Jupyter)

Website: Project is still in progress and a demo site is available at: https://analysim.tech and a development version is at https://dev.analysim.tech Source code: [https://github.com/soft-eng-practicum/AnalySim](https://www.google.com/url?q=https://github.com/soft-eng-practicum/AnalySim&sa=D&source=editors&ust=1773159824412874&usg=AOvVaw08XNeOlEnoBodKtXsifgh1)

15) HNN (Human Neocortical Neurosolver) Projects : Refactoring synaptic behavior in HNN-Core

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-15-hnn-human-neocortical-neurosolver-projects-refactoring-synaptic-behavior-in-hnn-core/35574](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-15-hnn-human-neocortical-neurosolver-projects-refactoring-synaptic-behavior-in-hnn-core/35574&sa=D&source=editors&ust=1773159824414108&usg=AOvVaw3TeHUoGbXUlxoD3_hh_IKm)

Difficulty: Intermediate - Advanced

Duration: 350 hours (full time)

Skills:

- Experience with Python programming, including Numpy and Scipy

- Experience with Git version control

- Experience with neuroscience and synaptic physiology is optional but advantageous

Mentors:

Nicholas Tolley ([https://github.com/ntolley](https://www.google.com/url?q=https://github.com/ntolley&sa=D&source=editors&ust=1773159824416081&usg=AOvVaw3kCXC56DQQiMQlX7XWawmK)), Katharina Duecker ([https://github.com/katduecker](https://www.google.com/url?q=https://github.com/katduecker&sa=D&source=editors&ust=1773159824416374&usg=AOvVaw1HQxSav-gw8CU4E0PN4wQB)), Dylan Daniels ([https://github.com/dylansdaniels](https://www.google.com/url?q=https://github.com/dylansdaniels&sa=D&source=editors&ust=1773159824416636&usg=AOvVaw34AXpN0enpbXqmhBIKv_7Y)), Anna Cattani ([https://github.com/annacatt](https://www.google.com/url?q=https://github.com/annacatt&sa=D&source=editors&ust=1773159824416864&usg=AOvVaw1olgIztkKPimU79HOXh_Sf))

About HNN-Core: The Human Neocortical Neurosolver (HNN) is a software for interpreting the cell and circuit neural origin of macroscale magneto-/electro-encephalography (MEG/EEG) data using biophysically-detailed microcircuit simulations. HNN-Core is the modern open source interface defining the HNN network model that allows simulations to be run through a user-friendly graphical user interface (GUI) or through a Python API as a library. Official website of HNN software (https://hnn.brown.edu/), HNN Textbook website with tutorials and examples (https://jonescompneurolab.github.io/textbook/content/preface.html), Contributing guide (https://jonescompneurolab.github.io/hnn-core/stable/contributing.html).


Goal: HNN-core is a biophysical modeling framework based on the NEURON simulator (https://nrn.readthedocs.io/en/9.0.1/). The cells in HNN-core consist of one or several sections (in biophysical modeling referred to as “compartments”), that are connected in a way that approximates the morphology of biological neurons. In the current implementation in HNN-core, synapses are placed at fixed locations at the center of each section. While only a subset of these synapses are active connections from thalamic and cortical inputs, the NEURON simulator solves the differential equations for all synapses, including those with inactive connections. The synaptic currents are stored as simulation outputs in an HNN-core network object, again including synapses with zero current flow. The goal of this project is to refactor the placement of synapses to locations at which a neuron receives synaptic inputs. This will improve the computational and memory efficiency of simulations in HNN-core and improve user-friendliness in interpreting simulation outputs. A bonus goal is to introduce biologically realistic variability in the synapse placement for different neurons (time permitting). This includes thalamic inputs and synaptic connections to other cells in the network.

Subgoals:

- Parameterize synapse position within Section, such that synapses are only placed at locations where the cell receives thalamic or cortical input, while maintaining backwards compatibility.

- Refactor code such that synaptic current is only recorded for active synapses.

- Update predefined network models.

- Create comprehensive tests and documentation

- Validate and create visualization tools for synaptic currents

- Bonus: implement position distributions for synapse placement, both for thalamic inputs (drives) and within-network connections

- Bonus: Extend existing drive and connectivity API to support heterogeneous placement

- Bonus: Add cell-level and network-level variability options

- Bonus: Create visualization tools for synapses

Tech keywords: Python, NEURON simulator, Compartmental modeling

16) HNN (Human Neocortical Neurosolver) Projects : Refactor and expand HNN-Core testing infrastructure

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-16-hnn-human-neocortical-neurosolver-projects-refactor-and-expand-hnn-core-testing-infrastructure/35575](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-16-hnn-human-neocortical-neurosolver-projects-refactor-and-expand-hnn-core-testing-infrastructure/35575&sa=D&source=editors&ust=1773159824425566&usg=AOvVaw3eNx593GeFIM41fQ4xGCZ6)

Difficulty: Intermediate

Duration: 350 hours (full time)

Skills:

- Experience with Python programming

- Experience with Git version control

- Experience with software testing, including `pytest` or similar testing frameworks

- Optional: Experience with Github Actions, Continuous Integration, and Continuous Delivery

Mentors:

Austin Soplata ([https://github.com/asoplata](https://www.google.com/url?q=https://github.com/asoplata&sa=D&source=editors&ust=1773159824427699&usg=AOvVaw2tRDHG5bx9d40fn7doQYG7)), Nicholas Tolley ([https://github.com/ntolley](https://www.google.com/url?q=https://github.com/ntolley&sa=D&source=editors&ust=1773159824427967&usg=AOvVaw26fhTwD414YKyUiqu1D73l))

About HNN-Core: The Human Neocortical Neurosolver (HNN) is a software for interpreting the cell and circuit neural origin of macroscale magneto-/electro-encephalography (MEG/EEG) data using biophysically-detailed microcircuit simulations. HNN-Core is the modern open source interface defining the HNN network model that allows simulations to be run through a user-friendly graphical user interface (GUI) or through a Python API as a library. Official website of HNN software (https://hnn.brown.edu/), HNN Textbook website with tutorials and examples (https://jonescompneurolab.github.io/textbook/content/preface.html), Contributing guide (https://jonescompneurolab.github.io/hnn-core/stable/contributing.html).

Goal: The current testing suite in HNN-Core has several areas that could be significantly improved to simplify and generalize how tests work, increase code reliability, and test edge cases more comprehensively. The goal of this project is to refactor the test infrastructure to be more systematic, comprehensive, and maintainable while improving code coverage across the codebase.

Subgoals:

- Main issue summarizing requirements: https://github.com/jonescompneurolab/hnn-core/issues/1118

- Expand the existing `Network` fixture in `conftest.py` to support multiple network configurations including networks with no drives, different sizes, and various drive combinations. Refactor existing tests to use these standardized fixtures consistently, instead of defining their own networks locally.

- Identify and split long, monolithic tests into smaller, independent test functions where possible. For example, refactor `test_add_drives` to test individual drive types and their arguments separately before testing combinations.

- Use Codecov or pytest coverage tools to identify untested code paths and add targeted tests to improve coverage, focusing on edge cases and full argument coverage for functions.

- Add at least one long-duration simulation test using the default model with standard drives to catch timing-related bugs that only appear over extended timeframes.

- Modernize the codebase by, for example, replacing `os.path` usage with `Pathlib` throughout the test suite for improved readability and maintainability.

- Enable tests to run on all installation types (not just editable source) to support a wider range of development workflows and better debugging for users.

- Bonus: Expand our GUI testing framework in particular.

Tech keywords: Python, software testing, pytest, code coverage, continuous integration, computational neuroscience, NEURON simulator

Related issues:

- [https://github.com/jonescompneurolab/hnn-core/issues/1118](https://www.google.com/url?q=https://github.com/jonescompneurolab/hnn-core/issues/1118&sa=D&source=editors&ust=1773159824433935&usg=AOvVaw0p3d65TVltoPYPvKu-HCdq)

- [https://github.com/jonescompneurolab/hnn-core/issues/960](https://www.google.com/url?q=https://github.com/jonescompneurolab/hnn-core/issues/960&sa=D&source=editors&ust=1773159824434332&usg=AOvVaw1ltq3C7SLjUeZXVQoVBQxW)

- [https://github.com/jonescompneurolab/hnn-core/issues/1144](https://www.google.com/url?q=https://github.com/jonescompneurolab/hnn-core/issues/1144&sa=D&source=editors&ust=1773159824434560&usg=AOvVaw36JePnFu-4j3FZCocEZrc4)

17) Contribute to Experanto

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-17-contribute-to-experanto/35576](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-17-contribute-to-experanto/35576&sa=D&source=editors&ust=1773159824435086&usg=AOvVaw0R-6JLLCBYLFBJvn8JYywc)

Understanding the brain requires aligning high-dimensional stimuli with large-scale neuronal recordings. Experanto is a Python framework designed to bridge this gap, providing a unified interface for interpolating and aligning time series (calcium imaging, continuous behavior such as running speed), events (spiking data, action-based behavior), and media (images, video). Optimized for deep learning, Experanto recently powered [OmniMouse](https://www.google.com/url?q=https://openreview.net/forum?id%3DmEw4lhAn0F&sa=D&source=editors&ust=1773159824435962&usg=AOvVaw1l0ef2jSsgffK5yTev4891), a large-scale multimodal neural predictive model.

The core strength of Experanto is its flexibility: it allows users to resample frequencies, filter data by behavioral criteria (e.g., "only when running"), and integrate multiple experiments into a single pipeline.

The goal of this project is to expand Experanto’s functionality, visualization tools, and robustness. Proposed focus areas include:

- Open-Source Data Integration: Currently supporting the
[Allen Brain Calcium Imaging dataset](https://www.google.com/url?q=https://allensdk.readthedocs.io/en/latest/visual_behavior_optical_physiology.html&sa=D&source=editors&ust=1773159824436971&usg=AOvVaw2M9sjhk6Sveu80LuTGrzr0), we aim to expand to the[Brain Wide Map](https://www.google.com/url?q=https://www.nature.com/articles/s41586-025-09235-0&sa=D&source=editors&ust=1773159824437116&usg=AOvVaw3FWAWJwjWKcuZxOm_tlsZ4)and[Allen Neuropixels](https://www.google.com/url?q=https://allensdk.readthedocs.io/en/latest/visual_behavior_neuropixels.html&sa=D&source=editors&ust=1773159824437251&usg=AOvVaw113ycKNJlIr3V6CvqySTLI)datasets. Ideally, this involves creating a "[brainsets-style](https://www.google.com/url?q=https://github.com/neuro-galaxy/brainsets&sa=D&source=editors&ust=1773159824437402&usg=AOvVaw1a1--b-K9qDGolfnvlAXgJ)" library to automatically download and map these datasets to Experanto. - Extend experanto functionality:

- Enhanced Filtering & Parsing: Developing a string-based configuration interface for complex data filtering—for example: (treadmill > 0 and eye is not nan) & screen == video.
- Event-Driven Data Handling: Explicitly adding support for event-based data types to better process free-animal behavior experiments.
- Visualization & Documentation: Building built-in visualization tools and expanding tutorials for data analysis and neural predictive modeling.

Skill level: Beginner/intermediate

Required skills: Strong coding foundation in python, including object oriented programming and writing tests, familiarity with git and git CI/CD. Some knowledge of digital signal processing and interest in neuroscience is preferred.

Time commitment: Flexible (175/350 h, 350 preferred)

Lead mentor: Fabian Sinz

Project website: [https://github.com/sensorium-competition/experanto](https://www.google.com/url?q=https://github.com/sensorium-competition/experanto&sa=D&source=editors&ust=1773159824439655&usg=AOvVaw3qNu0LPNcLFPVRAtjAR9Oz)

Backup mentors: Polina Turishcheva, René Burghardt, Tom Olschewski


Tech keywords: Python, object oriented programming, digital signal processing, open science, timeseries, calcium imaging, electrophysiology, datasets


18) SciCommons: Fullstack development and AI features for front-end, back-end and browser extensions

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-18-scicommons-fullstack-development-and-ai-features-for-front-end-back-end-and-browser-extensions/35577](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-18-scicommons-fullstack-development-and-ai-features-for-front-end-back-end-and-browser-extensions/35577&sa=D&source=editors&ust=1773159824440840&usg=AOvVaw1Xq1MzkBQ7_XjyX6H_Rpjp)

Mentors: Armaan Alam <[armanalam032001@gmail.com](mailto:armanalam032001@gmail.com)>, Mohd Faisal Ansari <[fa058593@gmail.com](mailto:fa058593@gmail.com)>, Suresh Krishna <[suresh.krishna@mcgill.ca](mailto:suresh.krishna@mcgill.ca)>


Skill level: Intermediate – Advanced

Required Skills: If working on the front-end, familiarity with Next.js, React, Server Side Rendering, TanStack Query, and component-based UI systems such as ShadCN/Radix UI is expected. If working on the backend, familiarity with Django and REST APIs is useful. For AI/NLP work, experience with LLMs, NLP pipelines, and open-source models is preferred. Experience with browser extensions or research tools is a plus.

Time commitment: Full time (350 hours)

About: Over the last few GSoC cycles, we have built SciCommons ([https://www.scicommons.org](https://www.google.com/url?q=https://www.scicommons.org&sa=D&source=editors&ust=1773159824443017&usg=AOvVaw1uM6d0M2sBuYA-fMW8NL3L)), a web platform to support open scientific discussion, article reviews, ratings, and community-driven evaluation of research. The core frontend (Next.js) and backend (Django) are now stable and in active development and testing, and the platform is approaching a wider public release. The project is now moving into a phase of expanding features, improving usability, and building tools around the platform.

Aims: This year, we invite GSoC contributors to help extend SciCommons in several directions: improving the front-end experience, building a browser extension to connect SciCommons directly with relevant websites, adding AI-based tools for a range of tasks including literature discovery and summarization, and developing features for community-run journals and editorial workflows. The goal is to make SciCommons not just a place to comment on papers, but a complete environment for discovering, reading, discussing, and organizing scientific knowledge. The work will focus on the following areas:

- Front-end and UX improvements for reading, reviewing, and discussion workflows

- A browser extension to save papers, view discussions, and annotate articles from anywhere on the web

- AI tools for semantic search, recommendations, and paper/discussion summarization using open-source models

- Journal and community management features (editorial flows, moderation, curation, integrations)

Website: [https://alphatest.scicommons.org](https://www.google.com/url?q=https://alphatest.scicommons.org&sa=D&source=editors&ust=1773159824446446&usg=AOvVaw2JuCBz0aZhRECVOd_xs43-)

Tech keywords: Science publishing, social web, science portals, Next.js, Django, browser extensions, natural language processing, large language models, AI-assisted literature discovery.


19) ActiveVision: continued development of a data and model portal for the study of goal-directed vision


Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-19-activevision-continued-development-of-a-data-and-model-portal-for-the-study-of-goal-directed-vision/35578](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-19-activevision-continued-development-of-a-data-and-model-portal-for-the-study-of-goal-directed-vision/35578&sa=D&source=editors&ust=1773159824447479&usg=AOvVaw0ASnHsyyUcnIatpLwgkhM-)

Mentors: Buxin Liao <[buxin.liao@mail.mcgill.ca](mailto:buxin.liao@mail.mcgill.ca)>, Katarzyna Jurewicz <[jurewicz.ka@gmail.com](mailto:jurewicz.ka@gmail.com)>, Suresh Krishna <[suresh.krishna@mcgill.ca](mailto:suresh.krishna@mcgill.ca)>

Skill level: Intermediate – Advanced

Required Skills: Familiarity with open-source vision and multimodal AI models. Fluency in Python and PyTorch. Familiarity with Slurm and working with clusters preferred. Basic web-development skills or interest in learning them will be useful.

Time commitment: Full time (350 hours)

About: Salience map research in computer vision has extensively examined where human observers look in images and videos during free viewing. Despite cognitive psychology recognizing the role of behavioral goals for over 50 years, integrating task dependence into quantitative models and large open datasets is a recent development. This project aims to create an open portal that consolidates existing machine learning/AI models and eye-tracking datasets related to goal-directed vision (e.g., visual search) while providing tools for model testing and validation. A key focus is on multimodal AI, particularly language-vision integration. Additionally, this platform will serve as a prototype for similar data+model initiatives on public hardware platforms.

Aims: In last year's GSoC project ( [https://gist.github.com/lc542/a6d58ded278ab4d13570d5d99e7cb306](https://www.google.com/url?q=https://gist.github.com/lc542/a6d58ded278ab4d13570d5d99e7cb306&sa=D&source=editors&ust=1773159824450341&usg=AOvVaw1ibODKD4iJq3-l16RWNiYi)), we created a library of machine vision models and a toolbox for their application to scanpath datasets. Over the past year, there has been substantial progress in terms of better models and datasets. This year's project aims to bring the library and toolbox up to date, and additionally create a user-facing web portal on Compute Canada that will facilitate submission and evaluation of models on scanpath datasets.

Project website: [https://github.com/m2b3/ActiveVisionPortal](https://www.google.com/url?q=https://github.com/m2b3/ActiveVisionPortal&sa=D&source=editors&ust=1773159824451246&usg=AOvVaw1wdJMZxsRrdbPRgJ5fjdvd) and[https://github.com/m2b3/SciCommons-frontend](https://www.google.com/url?q=https://github.com/m2b3/SciCommons-frontend&sa=D&source=editors&ust=1773159824451426&usg=AOvVaw0C_hgu1Z_I0c1jBdwF2uzn)

Tech keywords: Python, PyTorch, Visual search, Saliency, Science portals, Vision AI, Vision-language models.


20) BreathState contribution: a phone-based app for heart-rate variability biofeedback and resonance breathing protocols

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-20-breathstate-contribution-a-phone-based-app-for-heart-rate-variability-biofeedback-and-resonance-breathing-protocols/35579](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-20-breathstate-contribution-a-phone-based-app-for-heart-rate-variability-biofeedback-and-resonance-breathing-protocols/35579&sa=D&source=editors&ust=1773159824452391&usg=AOvVaw1eLK9cNTk2zx8kfs5wEGTf)

Topic detail: BreathState - front-end and feature development as well as device compatibility extension of a phone-based app for heart-rate variability biofeedback and resonance breathing protocols

Mentors: Alex Zhao <[alex.zhao@mail.mcgill.ca](mailto:alex.zhao@mail.mcgill.ca)>, Ashok Jummigumpula <[ashok.j@manipal.edu](mailto:ashok.j@manipal.edu)>, Sachin Bhat <[sachinbhat88@gmail.com](mailto:sachinbhat88@gmail.com)>, Suresh Krishna <[suresh.krishna@mcgill.ca](mailto:suresh.krishna@mcgill.ca)>

Skill level: Intermediate – Advanced

Required Skills: Fluency with Android/iOS development and Flutter. Basic signal processing familiarity preferred, as well familiarity with at least one of Python/Matlab. Familiarity with a VR framework (e.g. Unity) is a plus.

Time commitment: Full time (350 hours)

About:

In last year's GSoC ([https://gist.github.com/michaelLewis04/126e29b5450704977f8c45c1d443813b](https://www.google.com/url?q=https://gist.github.com/michaelLewis04/126e29b5450704977f8c45c1d443813b&sa=D&source=editors&ust=1773159824454801&usg=AOvVaw0VD3HIoV7YYEV-tDPPHrXB)), we built an open-source app to record heart-rate (via a Bluetooth connection to the Polar H10) and breathing (via the phone microphone) simultaneously and provide a small set of metrics and algorithms operating on the two time-series, along with front-end design to facilitate guided breathing protocols.

Aims: This year's project can have multiple goals. 1. Interface with a breathing sensor to measure respiration in a better fashion (than using the phone's microphone). Include support for visualization of ongoing heart-rate variability through a VR device like Meta Quest 3(S) for increased immersion and biofeedback-guided HRV self-adjustment. 3. Interface with Muse to simultaneously record EEG. 4. Improve the front-end and include additional biometrics as well breathing protocols, in collaboration with the clinician mentors. These will allow the study of autonomic nervous function, and will allow biofeedback protocols for mood and health intervention to be implemented via live tracking of breathing and heart-rate.

Website: [https://github.com/m2b3/BreathState2](https://www.google.com/url?q=https://github.com/m2b3/BreathState2&sa=D&source=editors&ust=1773159824456687&usg=AOvVaw2tRGCchuRbPiuc03X2XL1i)

Tech keywords: App development, biofeedback, mood intervention, health ML/AI, biosignals


21) I-EEG: health application for semi-automated iEEG analysis and viewing in a clinical and research environment

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-21-i-eeg-health-application-for-semi-automated-ieeg-analysis-and-viewing-in-a-clinical-and-research-environment/35598](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-21-i-eeg-health-application-for-semi-automated-ieeg-analysis-and-viewing-in-a-clinical-and-research-environment/35598&sa=D&source=editors&ust=1773159824457922&usg=AOvVaw3LLbEH5RuM5KGxUlIyUKXQ)

Mentors: Maya Aderka <[maya.aderka@mail.mcgill.ca](mailto:maya.aderka@mail.mcgill.ca)>, Suresh Krishna <[suresh.krishna@mcgill.ca](mailto:suresh.krishna@mcgill.ca)>, Elie Bou Assi <[elie.bou.assi.chum@ssss.gouv.qc.ca](mailto:elie.bou.assi.chum@ssss.gouv.qc.ca)>

Skill level: Intermediate – Advanced

Required Skills: Fluency in at least one of Python or Matlab (Python preferred, and ideally with reasonable ability in MATLAB). Experience with (bio)signal processing and with front-end development preferred.

Time commitment: Full time (350 hours)

About: There is an acute need for (open-source) software to handle human intracranial neural recordings, usually from patients who are undergoing diagnostic intracranial EEG (iEEG) recordings for epilepsy treatment. Such software would provide an integrated viewer, implement major existing (semi-)automated algorithms for seizure-onset zone definition, seizure prediction and surgical outcome prognostication. This is a fairly new project, that the GSoC contributor will build on, with help and mentorship from us.

Aims: This year, the project will aim to implement additional key published iEEG algorithms, improve the front-end for visualization, create a pipeline that allows the incorporation of expert human input to fine-tune the automated analyses, and to build a framework for testing/comparison of different algorithms and human-in-the-loop pipelines to each other.

Website: [https://github.com/m2b3/iEEG](https://www.google.com/url?q=https://github.com/m2b3/iEEG&sa=D&source=editors&ust=1773159824461344&usg=AOvVaw2vBvYkNjTwA04z2YPkNN3g)

Tech keywords: Health ML/AI, Epilepsy, Neuroscience, Biosignals, Neuroinformatics


22) Title: OWASP DevSecOps Maturity and controls implementation for the EBRAINS community - a PoC with the MIP platform


Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-22-title-owasp-devsecops-maturity-and-controls-implementation-for-the-ebrains-community-a-poc-with-the-mip-platform/35599](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-22-title-owasp-devsecops-maturity-and-controls-implementation-for-the-ebrains-community-a-poc-with-the-mip-platform/35599&sa=D&source=editors&ust=1773159824462812&usg=AOvVaw03ZR2SF-D6uDUQ5DSvguoM)

Mentors: Julien Dhallenne <[firstname.lastname@chuv.ch](mailto:firstname.lastname@chuv.ch)>, Konstantinos Filippopolitis, Jonathan Haab

Skill level: Intermediate to Advanced (advanced mostly due to tool integration + reducing false positives + documentation quality)

Required skills: Git, CI/CD, basic security mindset, scripting, Docker, Linux, Python

Time commitment: part time or full time (175/350h)

About: Current code, infrastructure and CI/CD security practices vary in EBRAINS and the Neuroinformatics community. In many projects, they are only partially meeting security standards required by the Cyber Resilience Act (CRA) and NIS2. Using the Medical Informatics Platform (MIP) [1] as a PoC for demonstrating feasibility in the wider community, we want use the OWASP DevSecOps Maturity Model (DSOMM) [2], as the baseline to assess our current pipeline maturity, and the OWASP DevSecOps Guideline [3] as the reference for implementation. We have both Kubernetes-related IaC and software stacks that can be worked on. The MIP is a federated platform designed to help clinicians, clinical scientists, and clinical data scientists who want to adopt advanced analytics for clinical research. Users can explore harmonized medical data extracted from pre-processed neuroimaging, neurophysiological and medical records and research cohort datasets without transferring original clinical data.

Aims: This project starts with a DSOMM-based maturity snapshot that we will convert into an actionable implementation plan. We will implement the first controls of a "real" DevSecOps-enabled infrastructure for end-to-end quality and security of software. The outcome will be a working reference pipeline (IaC or application code) that produces security artifacts automatically (ex: scan reports, SBOM, policy results), demonstrating that high quality and secure software production is achievable in our community and reusable across teams. Finally, the contributor will package the results as a reusable "secure pipeline blueprint". We will also plan upstream contributions to OWASP, should there be some discrepancies encountered in the OWASP guides and framework along the way.

Expected outcomes: There will be 3 phases, following the general GSoC calendar.

Phase 1: DSOMM baseline assessment + choose controls to implement (planning). Deliverables: DSOMM assessment report (simple matrix: current state → target maturity → chosen activities)

Phase 2: Implement DSOMM controls in pipelines and generate artifacts (main work). The amount of controls implemented depends on the time commitment.

Deliverables: Reference CI/CD pipeline implementation (GitHub Actions) with secret scanning, SCA+SBOM, IaC misconfiguration scanning or application SAST (depending on chosen focus of applicants) and Pipeline artifacts produced automatically (reports in CI artifacts, SARIF, SBOM files, policy checks, etc...)

Phase 3: Make it reusable, contribute upstream and polish documentation.

Deliverables: Documentation and developer workflow (ie. "how to fix findings, automatically or manually" and "how to adopt in another repo") and finalize upstream contribution PRs (that could have been started during the project)

Website: [https://github.com/Medical-Informatics-Platform/mip-infra](https://www.google.com/url?q=https://github.com/Medical-Informatics-Platform/mip-infra&sa=D&source=editors&ust=1773159824468946&usg=AOvVaw2aPJl5aGEvffO3Az_V5PGn)

Tech keywords: Git, CI/CD, Security, Scripting, Kubernetes, Github workflows, SAST, Kubernetes, DevOps, DevSecOps, SARIF, SBOM, DSOMM


Resources:

[1] Medical Informatics Platform: [https://ebrains.eu/data-tools-services/medical-analytics/medical-informatics-platform](https://www.google.com/url?q=https://ebrains.eu/data-tools-services/medical-analytics/medical-informatics-platform&sa=D&source=editors&ust=1773159824469801&usg=AOvVaw3jvI9ZcNDGaHdjxPZnTexd)

[2] OWASP Devsecops Maturity Model: [https://owasp.org/www-project-devsecops-maturity-model/](https://www.google.com/url?q=https://owasp.org/www-project-devsecops-maturity-model/&sa=D&source=editors&ust=1773159824470060&usg=AOvVaw3KIbk4-KpdCUDbc5uIjejk)

[3] OWASP DevSecOps Guideline: [https://owasp.org/www-project-devsecops-guideline/](https://www.google.com/url?q=https://owasp.org/www-project-devsecops-guideline/&sa=D&source=editors&ust=1773159824470268&usg=AOvVaw0f6UjlYzq9eWMWoHuW6ofk)


23) A Python Command Line Interface (CLI) for the CBRAIN Distributed Computing Platform

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-23-a-python-command-line-interface-cli-for-the-cbrain-distributed-computing-platform/35600](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-23-a-python-command-line-interface-cli-for-the-cbrain-distributed-computing-platform/35600&sa=D&source=editors&ust=1773159824470803&usg=AOvVaw0e3YzA3zwIaFTjQnlV_WoB)


Mentors: Bryan Caron <[bryan.caron@mcgill.ca](mailto:bryan.caron@mcgill.ca)>, Pierre Rioux, Natacha Beck, Serge Boroday, Darcy Quesnel

Skill level: Intermediate - Advanced

Required skills: Python; experience with version control systems (i.e. git) and team-based development methodologies; good understanding of the Linux operating system and development in a Linux environment


Time commitment: part time or full time (350 hours)

About: CBRAIN is a web-enabled distributed computing platform that facilitates collaborative research on large, distributed data by creating an easy-to-use interface for users (or groups of collaborating users) to access high-performance computing (HPC) and Cloud Computing resources. Through a series of web-based services, CBRAIN manages data access, transfer, caching and provenance, as well as data processing and reporting. While predominantly used to support researchers in neuroinformatics, CBRAIN is generic and modular, and can easily be extended with new data models and tools for a broad range of research disciplines. CBRAIN is an open source, flexible Ruby on Rails framework for accessing and processing large amounts of data across a distributed network of High Performance Computing (HPC) and Cloud Computing infrastructures. With over 1800 users from over 35 countries, CBRAIN is a key resource that lowers the technical barriers for scientists to conduct neuroinformatics research. More information about CBRAIN can be found at https://cbrain.ca and https://github.com/aces/cbrain.

Aims: The objective of the project is to create a python-based command line interface (CLI), leveraging the CBRAIN APIs, which will enable more advanced users to perform all the typical operations of CBRAIN for data upload / download, file querying / selection, and processing task creation, execution and monitoring from a CLI that can be run on a remote resource without requiring the user to perform the same actions through the CBRAIN web interface. A CLI approach would provide users the ability to create more complex workflows while still leveraging CBRAIN’s core abilities to manage data movement and large-scale data processing.

Website: [https://cbrain.ca](https://www.google.com/url?q=https://cbrain.ca&sa=D&source=editors&ust=1773159824474645&usg=AOvVaw1vi3CPFvpssnHBiPi9dVpT) and [https://github.com/aces/cbrain](https://www.google.com/url?q=https://github.com/aces/cbrain&sa=D&source=editors&ust=1773159824474817&usg=AOvVaw0F66mAUHKW-o0TMqcrWAn1)

Tech keywords: Keywords: Python, imaging, CBRAIN, distributed computing, cloud computing


24) Improvements to BrainBrowser for neuroimaging visualization


Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-24-improvements-to-brainbrowser-for-neuroimaging-visualization/35601](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-24-improvements-to-brainbrowser-for-neuroimaging-visualization/35601&sa=D&source=editors&ust=1773159824475774&usg=AOvVaw0ojIWoA04k7udzAteNLIkZ)

Mentors: Natacha Beck, Bryan Caron <[bryan.caron@mcgill.ca](mailto:bryan.caron@mcgill.ca)>, Pierre Rioux

Skill level: Intermediate - Advanced

Required skills: Javascript; experience with version control systems (i.e. git) and team-based development methodologies; good understanding of the Linux operating system and development in a Linux environment

Time commitment: Part time or full time (350 hours)

About: BrainBrowser is an open source JavaScript visualization library that allows for real-time manipulation and analysis of 3D imaging data within a web browser. The BrainBrowser library is lightweight and highly performant, built to provide easy-to-use, powerful, on-demand visualization of remote datasets. BrainBrowser leverages modern web technologies such as WebGL, HTML5 and Web Workers, to visualize 3D surface and volumetric neuroimaging data in any modern web browser without requiring any browser plugins. BrainBrowser's integration into the standardized web platform also allows users to consider using 3D data visualization in novel ways, such as for data distribution, data sharing and dynamic online publications. BrainBrowser is already being used in major online platforms including CBRAIN, LORIS and Brainlife, among others. More information about BrainBrowser can be found at https://brainbrowser.cbrain.mcgill.ca and https://github.com/aces/brainbrowser.

Aims: The objective of the project is to update the BrainBrowser visualization library in a number of key areas, increasing performance and providing additional feature richness based upon community requests. The contribution would particularly focus on updating BrainBrowser’s dependencies to include bug fixes, feature and performance updates associated with the three.js library. The project is expected to resolve known transparency issues with the BrainBrowser SurfaceViewer when removing some shapes, and would therefore be a valuable outcome for the neuroscientific research community that rely on BrainBrowser for their visualization needs.

Website: [https://brainbrowser.cbrain.mcgill.ca](https://www.google.com/url?q=https://brainbrowser.cbrain.mcgill.ca&sa=D&source=editors&ust=1773159824478901&usg=AOvVaw3hOqz6qRkr_N6C8sGz4q0C) and [https://github.com/aces/brainbrowser](https://www.google.com/url?q=https://github.com/aces/brainbrowser&sa=D&source=editors&ust=1773159824479036&usg=AOvVaw2_k_IOMErVMTvzOrcJVnnQ)

Tech keywords: Javascript, visualization, imaging, CBRAIN


25) ImageJ Active Segmentation platform: Parallel Engine for ASP/IJ

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-25-imagej-active-segmentation-platform-parallel-engine-for-asp-ij/35602](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-25-imagej-active-segmentation-platform-parallel-engine-for-asp-ij/35602&sa=D&source=editors&ust=1773159824479758&usg=AOvVaw232a6f8-SNW44m8hHF2BWx)


The Active Segmentation platform for ImageJ (ASP/IJ)[2] was developed in the scope of GSOC 2016 - 2025. The plugin provides a general-purpose environment that allows biologists and other domain experts to use transparently state-of-the-art techniques in machine learning to achieve excellent image segmentation and classification. ImageJ [1] is a public-domain Java image processing program extensively used in life and material sciences. Recent years have experienced explosive development in the GPU-accelerated computing. The project will explore the existing parallel filtering framework and extend it towards TornadoVM framework [4]. TornadoVM is an open-source software technology that automatically accelerates Java programs on multi-core CPUs, GPUs, and FPGAs.

The project will explore some of established Java-based GPU computing frameworks [4,5,6,7] and port the convolution engine used by the ASP/IJ to parallel implementation.

The project idea: The project will extend the convolution engine used by the ASP/IJ to the TornadoVM framework.

Tasks

• Fix existing issues and bugs

• GPU computing frameworks evaluation and testing

• Implementation and profiling of selected convolution filters

Minimal set of deliverables

• Requirement specification – Prepared by the candidate after understanding the functionality.

• System Design – Detailed plan for development of the plugin and test cases.

• Implementation and testing – Details of implementation and testing of the platform.


Desired skills: Java, Machine learning

Mentors: Dimiter Prodanov ([dimiterpp@gmail.com](mailto:dimiterpp@gmail.com)) IICT-BAS; Teodor Minev IICT -BAS ([teodorminev98@gmail.com](mailto:teodorminev98@gmail.com)); Rikas Ilamdeen ([rikasilamdeen@gmail.com](mailto:rikasilamdeen@gmail.com))

References

1. ImageJ: [https://imagej.nih.gov/](https://www.google.com/url?q=https://imagej.nih.gov/&sa=D&source=editors&ust=1773159824483147&usg=AOvVaw0CA2tP5CK8tfCX4BGgHY94)

2. Active Segmentation: [https://github.com/sumit3203/ACTIVESEGMENTATION](https://www.google.com/url?q=https://github.com/sumit3203/ACTIVESEGMENTATION&sa=D&source=editors&ust=1773159824483434&usg=AOvVaw335NAfxjFBvUY-j7umPPNG)

3. Eclipse IDE [https://www.eclipse.org/](https://www.google.com/url?q=https://www.eclipse.org/&sa=D&source=editors&ust=1773159824483677&usg=AOvVaw3qkg6pESW1Zwxo49du4Rgj)

4. TornadoVM [https://www.tornadovm.org/](https://www.google.com/url?q=https://www.tornadovm.org/&sa=D&source=editors&ust=1773159824483861&usg=AOvVaw080RToOaT6LnlSWGzb7Ur0)

26) ImageJ Active Segmentation platform: UI update for ASP/IJ

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-26-imagej-active-segmentation-platform-ui-update-for-asp-ij/35603](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-26-imagej-active-segmentation-platform-ui-update-for-asp-ij/35603&sa=D&source=editors&ust=1773159824484353&usg=AOvVaw3eTlZBLWBbXH1s6oTWDSML)


The Active Segmentation platform for ImageJ (ASP/IJ) [2] was developed in the scope of GSOC 2016 – 2024. The plugin provides a general-purpose environment that allows biologists and other domain experts to use transparently state-of-the-art techniques in machine learning to achieve excellent image segmentation and classification. ImageJ [1] is a public-domain Java image processing program extensively used in life and material sciences. The program was designed with an open architecture and is extensible via plugins.


The project idea: The project will streamline and simplify the existing UI implementation using WindowBuilder for Eclipse [3].

Tasks

• Fix existing issues and bugs

• UI implementation and testing


Minimal set of deliverables

• Requirement specification - Prepared by the candidate after understanding the functionality.

• System Design - Detailed plan for development of the plugin and test cases.

• Implementation and testing - Details of implementation and testing of the platform.


Desired skills: Java

Mentors: Dimiter Prodanov ([dimiterpp@gmail.com](mailto:dimiterpp@gmail.com)) IICT-BAS; Teodor Minev IICT -BAS ([teodorminev98@gmail.com](mailto:teodorminev98@gmail.com))

References

1. ImageJ: [https://imagej.nih.gov/](https://www.google.com/url?q=https://imagej.nih.gov/&sa=D&source=editors&ust=1773159824487270&usg=AOvVaw3Kwj0SR7sKChcDrU0tLMsH)

2. Active Segmentation: [https://github.com/sumit3203/ACTIVESEGMENTATION](https://www.google.com/url?q=https://github.com/sumit3203/ACTIVESEGMENTATION&sa=D&source=editors&ust=1773159824487489&usg=AOvVaw1UuzNv31NUvT9sCgmxCeG4)

3. Eclipse IDE [https://www.eclipse.org/](https://www.google.com/url?q=https://www.eclipse.org/&sa=D&source=editors&ust=1773159824487668&usg=AOvVaw12ujUiz3BHGw3WxcMJBnyI)

27) Integrating personalized hemodynamic response function in The Virtual Brain & EBRAINS


Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-27-integrating-personalized-hemodynamic-response-function-in-the-virtual-brain-ebrains/35604](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-27-integrating-personalized-hemodynamic-response-function-in-the-virtual-brain-ebrains/35604&sa=D&source=editors&ust=1773159824488272&usg=AOvVaw32g5PbOcLPNV-wu1ueofOK)

Mentor: Daniele Marinazzo <[daniele.marinazzo@gmail.com](mailto:daniele.marinazzo@gmail.com)>

Skill level: Intermediate to Advanced

Required skills: Python, Docker; familiarity with neuroimaging tools (AFNI, FSL, FreeSurfer) would be beneficial

Time commitment: Full time (350 hours)

About: The hemodynamic response function (HRF) is a crucial mapping between neural activity and the recorded BOLD signal in fMRI experiments. Accounting for differences in the HRF shape is crucial when making inference on neural activity. The same should apply to computational models of large scale brain activity when the target is the BOLD signal or properties derived from it such as the Functional Connectivity. On the other hand models so far use a standard shape for the HRF. In resting state fMRI there is no explicit onset of neural activation, making it challenging to estimate the HRF using a linear model. A toolbox by our group proposes a point process model to estimate the HRF from resting state BOLD signals.

Aims: This project will have the aim to derive the empirical HRF for each brain region and each subject from BOLD recordings, and then to use this HRF in a computational model of brain activity (The Virtual Brain, implemented in EBRAINS). The legacy approach will be compared with the proposed one.

Website: [https://ebrains.eu/data-tools-services/tools/rshrf](https://www.google.com/url?q=https://ebrains.eu/data-tools-services/tools/rshrf&sa=D&source=editors&ust=1773159824490708&usg=AOvVaw1XndhYEZRjY-1uJM_B1jNV)

Tech keywords: Python, Docker, The Virtual Brain, rsHRF


28) Title: Integrating blood arrival time in models of fMRI data in The Virtual Brain in EBRAINS


Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-28-title-integrating-blood-arrival-time-in-models-of-fmri-data-in-the-virtual-brain-in-ebrains/35605](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-28-title-integrating-blood-arrival-time-in-models-of-fmri-data-in-the-virtual-brain-in-ebrains/35605&sa=D&source=editors&ust=1773159824491560&usg=AOvVaw10h6kCzaIpmxZXnmB4qSkN)

Mentor: Daniele Marinazzo <[daniele.marinazzo@gmail.com](mailto:daniele.marinazzo@gmail.com)>

Skill level: Intermediate to Advanced

Required skills: Python, Docker; familiarity with neuroimaging tools (AFNI, FSL, FreeSurfer) would be beneficial

Time commitment: Full time (350 hours)

About: Statistical dependencies (Functional Connectivity, FC) between BOLD time series from different brain regions in fMRI experiments are modulated by the relative delays in blood arrival time in these regions. This crucial aspect has been mostly overlooked in empirical studies, and completely overlooked in computational models of large scale BOLD activity, where (neuronal transmission) delays play a crucial role, such as The Virtual Brain. Delays in blood arrival time can be estimated using a tool called Rapidtide, which allows also to estimate and regress systemic low frequency oscillations (sLFOs).

Aims: This project will have the aim to include blood arrival time delays in computational models of brain activity with TVB in EBRAINS, and to compare the results with those obtained with the legacy approach with no blood arrival time delays.

Websites: [https://rapidtide.readthedocs.io/en/latest/](https://www.google.com/url?q=https://rapidtide.readthedocs.io/en/latest/&sa=D&source=editors&ust=1773159824493789&usg=AOvVaw0ASmOSL78UGqxL9mvN9XMo), [https://ebrains.eu/data-tools-services/tools/the-virtual-brain](https://www.google.com/url?q=https://ebrains.eu/data-tools-services/tools/the-virtual-brain&sa=D&source=editors&ust=1773159824493964&usg=AOvVaw0m82sf5HbPpTaGk-gJQt12)

Tech keywords: Python, Docker, The Virtual Brain, rapidtide, sLFOs


29) Enhancing simulation-based inference from neuroimaging


Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-29-enhancing-simulation-based-inference-from-neuroimaging/35606](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-29-enhancing-simulation-based-inference-from-neuroimaging/35606&sa=D&source=editors&ust=1773159824494637&usg=AOvVaw2OvHffvNcszN0hqMM9HmD7)

Mentor/s: Meysam HASHEMI <[meysam.hashemi@gmail.com](mailto:meysam.hashemi@gmail.com)/ [meysam.hashemi@univ-amu.fr](mailto:meysam.hashemi@univ-amu.fr)>

Skill level: Intermediate to Advanced

Required skills: Signal analysis, simulations of differential equations, Python and Git; familiarity with neural mass models, JAX, and techniques such as deep neural density estimators would be beneficial.

Time commitment: Full time (350 hours)

About: Virtual Brain Inference (VBI) is a flexible and integrative toolkit for efficient probabilistic inference on virtual brain models. It provides fast simulations of whole-brain models and deep neural density estimators in Python. Extending the scalable implementation to JAX and adding automatic feature extraction will facilitate the use cases.

Aims:

Reproduction of existing use cases,

Changing model parameters and testing,

Integrating new tools to existing workflows,

Use cases in form of notebooks.

The final output will be a lightweight demonstrator with clear documentation, enabling users to quickly run a standardized example. Website: [https://github.com/ins-amu/vbi](https://www.google.com/url?q=https://github.com/ins-amu/vbi&sa=D&source=editors&ust=1773159824497480&usg=AOvVaw3ijEv8mKyTFdc4he_MYJ9g)

30) Large-scale brain models in Probabilistic Programming Languages


Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-30-large-scale-brain-models-in-probabilistic-programming-languages/35607](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-30-large-scale-brain-models-in-probabilistic-programming-languages/35607&sa=D&source=editors&ust=1773159824498109&usg=AOvVaw34xkA34ym2D43hzsL1wDc6)


Mentor/s: Meysam HASHEMI <[meysam.hashemi@gmail.com](mailto:meysam.hashemi@gmail.com)/ [meysam.hashemi@univ-amu.fr](mailto:meysam.hashemi@univ-amu.fr)>

Skill level: Intermediate to Advanced

Required skills: Simulations of differential equations, Python and Git; familiarity with neural mass models, and Bayesian inference in tools such as Numpyro/PyMC would be beneficial.

Time commitment: Full time (350 hours)

About: Bayesian inference on brain models translates into probabilistic estimation of latent and observed states within systems driven by network input and stimuli, modeled by high-dimensional nonlinear differential equations, with potentially correlated parameters. To address these challenges, advanced inference algorithms embedded in Probabilistic Programming Languages (PPLs) have shown remarkable results. In particular, No-U-Turn Sampler, and alternatives such as automatic variational and Laplace approximation in Numpyro and PyMC have demonstrated effectiveness in achieving reliable Bayesian inference even in the presence of multimodal parameter distributions.

Aims:

* Implementation of dynamical brain models using JAX-based frameworks, such as NumPyro/PyMC, and in-silico validation.

* Benchmark existing algorithms within to systematically identify their strengths and weaknesses in handling high-dimensional settings.

* Monitor algorithm convergence for ensuring reliable inference in the presence of multimodal parameter distributions.

Final output will be a lightweight demonstrator with clear documentation, enabling users to quickly run a standardized example. Website: [https://github.com/ins-amu/DCM_PPLs](https://www.google.com/url?q=https://github.com/ins-amu/DCM_PPLs&sa=D&source=editors&ust=1773159824501395&usg=AOvVaw1Wu4jdC37b_52uMjjJs1dq)

31) Accelerating Virtual Brain Inference from Neuroimaging

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-31-accelerating-virtual-brain-inference-from-neuroimaging/35608](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-31-accelerating-virtual-brain-inference-from-neuroimaging/35608&sa=D&source=editors&ust=1773159824501881&usg=AOvVaw31JqBQ2TzO9_jhsUQ1LaHd)

Skill level: Intermediate to Advanced

Required skills: Data analysis, Simulations of differential equations, Python and Git; familiarity with JAX, whole-brain models, and simulation-based inference would be beneficial.

Time commitment: Full time (350 hours)

About: Virtual Brain Inference (VBI) provides fast simulations, taxonomy of feature extraction, efficient data storage and loading, and probabilistic machine learning algorithms, enabling biophysically interpretable inference from non-invasive and invasive recordings. Scalable JAX simulations and automatic feature extraction will support the use cases.

Aims:

* Reproduction of existing use cases in JAX

* Incorporating scalable JAX-based simulations

* Automatic feature extraction in the use cases

* Tuning and testing model parameters and in silico-validation

Final output will be a lightweight demonstrator with clear documentation, enabling users to quickly run a standardized example. Website: [https://github.com/ins-amu/vbi](https://www.google.com/url?q=https://github.com/ins-amu/vbi&sa=D&source=editors&ust=1773159824503970&usg=AOvVaw3VtrXpOCuHeKV3F2WKKMU2)


32) Extending the PCNtoolkit: Charting the rate of change of brain data using velocity models

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-32-extending-the-pcntoolkit-charting-the-rate-of-change-of-brain-data-using-velocity-models/35610](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-32-extending-the-pcntoolkit-charting-the-rate-of-change-of-brain-data-using-velocity-models/35610&sa=D&source=editors&ust=1773159824504711&usg=AOvVaw0KOnas-4pdB8PE16yzTJxA)


Mentors: Johanna Bayer <[johanna.bayer@radboudumc.nl](mailto:johanna.bayer@radboudumc.nl)>, Konstantinos Tsilimparis <[konstantinos.tsilimparis@radboudumc.nl](mailto:konstantinos.tsilimparis@radboudumc.nl)>, Augustijn de Boer <[augustijndeboer@gmail.com](mailto:augustijndeboer@gmail.com)>, Andre Marquand <[Andre.Marquand@radboudumc.nl](mailto:Andre.Marquand@radboudumc.nl)>

Skill level: Intermediate

Required skills: The applicant combines expertise in neuroscience with software engineering skills, including machine learning, Python and object-oriented programming.

Bonus skills: Statistics/Bayesian modelling, longitudinal modelling, scientific software practices (testing/CI/documentation), high-performance computing (HPC), experience with brain data (especially MRI)

Time commitment: 350h (full-time or part-time)

About: The Predictive Clinical Neuroscience toolkit (PCNtoolkit) is an open-source Python toolbox for normative modelling in neuroimaging and other clinical data. Normative modelling enables predictions at the subject level, which is particularly valuable for clinical applications and precision medicine. More specifically, normative models estimate a reference distribution of variation (for example on covariates such as age/sex/site) and allow the computation of subject-level deviation scores (e.g., z-scores) relative to that reference cohort (Marquand et al. 2016, 2019). The focus of the PCNtookit lies in the implementation of new models for normative modelling, such as implementing non-Gaussian and heteroscedastic noise models (de Boer et al., 2025) that can more accurately fit neuroimaging data and derivatives.

Aims: The aim for this project is the implementation of longitudinal (velocity) normative models. Hence, whereas standard normative modelling asks the question: “Where does an individual lie within the normative distribution given their age and other covariates?”, velocity modelling supports questions like: “Is this person changing faster/slower than expected given their age and other covariate, taking into account their past history?” The theoretical foundations of velocity normative modelling have already been described (Bayer et al., 2026), and an initial implementation is available in PCNtoolkit. This project will focus on validating, extending, and hardening this functionality into a robust, well-documented, and well-tested component of the toolbox.

Tasks:

- Validate and extend the existing velocity normative modelling architecture in the PCNtookit
- Extend the architecture to make predictions based on a past trajectory (multiple time points) instead of just based on one time point. This will include translating existing code that already exists outside the toolbox, into the toolbox
- Develop tutorials and documentation for velocity and longitudinal normative modelling workflows.
- Extend unit and integration test coverage to ensure reliability and maintainability.

Website: https://pcntoolkit.readthedocs.io/en/latest/

What can I do before GSoC to familiarize myself with the project?

1) Familiarize yourself with the existing PCNtoolkit codebase and its modular (class-based) architecture: [https://github.com/amarquand/PCNtoolkit](https://www.google.com/url?q=https://github.com/amarquand/PCNtoolkit&sa=D&source=editors&ust=1773159824514216&usg=AOvVaw3qlfyyMCt99ORyKzQEItYo)

2) Explore the PCNtoolkit documentation: [https://pcntoolkit.readthedocs.io/en/latest/](https://www.google.com/url?q=https://pcntoolkit.readthedocs.io/en/latest/&sa=D&source=editors&ust=1773159824514687&usg=AOvVaw0A-j1nK7Ai-ExtQi9y4HHs)

3) Work through the PCNtoolkit demo tutorials:

[https://github.com/predictive-clinical-neuroscience/PCNtoolkit-demo](https://www.google.com/url?q=https://github.com/predictive-clinical-neuroscience/PCNtoolkit-demo&sa=D&source=editors&ust=1773159824515023&usg=AOvVaw19_jdV3GaWaZ8LkYyGf_zc)

Helpful literature:

- Introduction to velocity normative modelling paper (Bayer et al., 2026,
[https://arxiv.org/abs/2601.07591](https://www.google.com/url?q=https://arxiv.org/abs/2601.07591&sa=D&source=editors&ust=1773159824515550&usg=AOvVaw0VNOJdtQ6N7g5Ojg_VMg16)) - Overview paper about normative modelling (Rutherford et al. 2022
[https://www.nature.com/articles/s41596-022-00696-5](https://www.google.com/url?q=https://www.nature.com/articles/s41596-022-00696-5&sa=D&source=editors&ust=1773159824515911&usg=AOvVaw1swA4sx6YccS2EO5hdyBzI)) - A recent review paper on normative modelling:
[https://www.sciencedirect.com/science/article/pii/S0149763425002854](https://www.google.com/url?q=https://www.sciencedirect.com/science/article/pii/S0149763425002854&sa=D&source=editors&ust=1773159824516440&usg=AOvVaw1K_iyAMc5jPpeYkFLmu3O9) - Non-Gaussian normative modelling with hierarchical Bayesian regression:

(de Boer et al., 2025, [https://direct.mit.edu/imag/article/doi/10.1162/imag_a_00132/120371/Non-Gaussian-normative-modelling-with-hierarchical](https://www.google.com/url?q=https://direct.mit.edu/imag/article/doi/10.1162/imag_a_00132/120371/Non-Gaussian-normative-modelling-with-hierarchical&sa=D&source=editors&ust=1773159824517261&usg=AOvVaw1T2mnuRyKJCSL4jK42M_J7))

Tech keywords: Machine learning, normative modelling, computational modelling, longitudinal modelling, Bayesian modelling, Python, object oriented programming


33) University of Wisconsin-Madison - AStats: an agentic-AI approach to applied statistical practitioner workflows

Neurostars Link for idea discussion:

Mentors: Jonathan Morris <[jmorris28@wisc.edu](mailto:jmorris28@wisc.edu)>, Yohai-Eliel Berreby <[yohai-eliel.berreby@mail.mcgill.ca](mailto:yohai-eliel.berreby@mail.mcgill.ca)>, Suresh Krishna <[suresh.krishna@mcgill.ca](mailto:suresh.krishna@mcgill.ca)>

Skill level: Intermediate – Advanced

Required Skills: Familiarity with the use of agentic AI workflows and the use of LLMs. Familiarity with statistical practice at a moderately advanced level is a plus. Familiarity with setting up and using open-weight LLMs and with fine-tuning LLMs is a plus. Familiarity with Slurm and working with clusters preferred.

Time commitment: Full time (350 hours)

About: Informal use and much anecdotal evidence suggests that the most recent LLMs, accessed via agentic AI coding systems, have reached a stage where they are very capable of exploring large datasets under supervision and with human guidance. Both exploratory and confirmatory analysis appears to be possible with results presented for verification by the practitioner. The A in AStats could stand for autonomous, augmented, automatic, applied, etc.

Aims: This is a new project, that this GSoC contributor will start from scratch, with help and mentorship from us. We have had good success in the past with such an approach, with successful projects going on to second and third years for additional development, and contributors from one year joining in as mentors for the following year. The project will explore and define good practices for robust workflows that incorporate agentic AI into statical exploration and practice. Practitioners already often use recipe-driven methods (e.g. JASP, Jamovi) to guide their use of statistical tools in familiar contexts. A major focus will be on the automatic exploration of large datasets, as well as the possibility of fine-tuning workflows or even models and using open-weight models to reduce cost and customize usage and make workflows more predictable.

Project website: [https://github.com/m2b3/AStats](https://www.google.com/url?q=https://github.com/m2b3/AStats&sa=D&source=editors&ust=1773159824522476&usg=AOvVaw0t4oRVHPZ898bCbxCCrtDD)

Tech keywords: Agentic AI, Statistics, Data science,

Python, PyTorch, Visual search, Saliency, Science portals, Vision AI, Vision-language models.


34) University of Texas at Austin - Improving Statistical Efficiency, Methodological Coverage, and Contributor Onboarding in NiMARE

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-34-university-of-texas-at-austin-improving-statistical-efficiency-methodological-coverage-and-contributor-onboarding-in-nimare/35611](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-34-university-of-texas-at-austin-improving-statistical-efficiency-methodological-coverage-and-contributor-onboarding-in-nimare/35611&sa=D&source=editors&ust=1773159824523556&usg=AOvVaw1VaxkU9lksfc8cxqLHfuZ7)


Project Summary: NiMARE is a Python library for coordinate- and image-based neuroimaging meta-analysis. It provides rigorously tested implementations of widely used methods such as ALE and MKDA, enabling reproducible synthesis of large neuroimaging literatures. NiMARE also serves as a long-term maintenance layer for research methods that are often released as one-off academic code, ensuring sustainability, documentation, and integration into a unified statistical framework.

This project has two complementary objectives:

- Improve contributor onboarding and development documentation, reducing friction for new developers.
- Enhance NiMARE’s statistical capabilities by implementing adaptive early stopping for permutation-based inference (mandatory), and, time permitting, adding Signed Difference Mapping (SDM) and publication bias diagnostics as stretch goals.
- These improvements will directly benefit both NiMARE users and downstream platforms such as Neurosynth Compose (2,700+ registered users), which relies on NiMARE for backend statistical computation.

Project Scope (175 Hours)

Weeks 1–2: Contributor onboarding improvements

Weeks 3–8: Algorithm development

Mandatory: Adaptive early stopping for permutation-based inference

Stretch goals: SDM implementation and publication bias diagnostics


Phase 1: Contributor Onboarding Improvements (Weeks 1–2)

Motivation

While NiMARE has an existing contributor guide, elements of the development environment setup and git workflow documentation are outdated. Although there are no known critical bottlenecks, ensuring that documentation reflects current practices reduces barriers for new contributors and minimizes avoidable friction.

Deliverables

Updated contributor guide covering:

Environment setup (Python versioning, dependency management, testing)

CI expectations

Code style and linting requirements

Clear documentation of recommended git workflow for PR submission.

Review and cleanup of outdated sections.

Verification that documentation reflects current repository structure and tooling.

Success Criteria

Documentation validated through a clean setup from scratch.

Clear, reproducible development environment instructions.

No outdated workflow steps.

All changes merged and published in documentation site.


Phase 2: Algorithm Development (Weeks 3–8)

1. Adaptive Early Stopping for Permutation-Based Inference (Mandatory)

Motivation

Permutation-based Monte Carlo inference is central to ALE and MKDA workflows but can be computationally expensive. Currently, users often rely on fixed iteration counts (e.g., 10,000 permutations), which may be either insufficient or excessive.

This project will implement a fixed-width confidence interval stopping rule for permutation testing in both ALE and MKDA workflows. The objective is to:

Maintain strict type I error control.

Reduce unnecessary computational cost.

Dynamically determine when sufficient precision has been achieved.

Technical Plan

Implement fixed-width confidence interval stopping based on variance stabilization of p-value estimates.

Evaluate whether 10,000 iterations are sufficient or unnecessarily conservative.

Integrate stopping logic into permutation pipelines for ALE and MKDA.

Preserve statistical validity and type I error guarantees.

Validation

Benchmark against fixed 10,000-permutation runs.

Compare convergence behavior.

Confirm preservation of nominal type I error bounds using simulation.

Deliverables

Integrated early stopping implementation for ALE and MKDA.

Unit tests covering convergence logic.

≥85% test coverage maintained.

Benchmarking results documented.

2. Signed Difference Mapping (SDM) (Stretch Goal)

Motivation

Signed Difference Mapping allows integration of coordinate- and image-based meta-analytic data within a unified framework. Implementing one SDM algorithm would broaden NiMARE’s methodological coverage and support mixed-modality analyses.

Technical Considerations

Requires extension of NiMARE’s Estimator base class.

API changes may be necessary to support SDM-specific data structures.

Must preserve backward compatibility where possible.

Validation

Compare output against existing SDM implementations using available validation datasets.

Confirm statistical consistency with reference results.

Deliverables

One SDM estimator implemented.

Necessary base class modifications.

Comprehensive unit tests.

Documentation describing usage and assumptions.

Risk Mitigation

Any API changes will be versioned carefully.

Backward compatibility impacts will be explicitly documented.

Core NiMARE workflows will be regression tested.


3. Publication Bias Diagnostic (Stretch Goal)

- Motivation- Neuroimaging meta-analyses may be susceptible to publication bias. A common diagnostic approach is estimating how many null studies would need to be added to render results non-significant (fail-safe N–style methods).

- This project will implement a standalone diagnostic module to estimate how many null studies would be required to overturn significance.

- Technical Challenges

Computational scaling if large numbers of simulated null studies are required.

Efficient simulation strategies may be necessary.

Deliverables

Standalone diagnostic module.

Simulation-based validation.

Unit tests with ≥85% coverage.

Documentation describing assumptions and limitations.

Validation & Testing Standards

- All new code must meet NiMARE’s testing standards (≥85% coverage).

- Existing workflows must pass regression tests.

- Simulation-based validation datasets are available.

- Continuous integration checks must pass for all PRs.

Risks and Mitigation

Risk

Mitigation Strategy

API instability due to SDM integration

Careful extension of Estimator base class; preserve backward compatibility where possible

Computational scaling for fail-safe diagnostic

Implement optimized simulation strategies; cap simulation growth

Statistical correctness of early stopping

Simulation studies to verify type I error control

The mandatory early stopping implementation is feasible within the timeline. Stretch goals will be pursued sequentially based on progress.

Impact: This project will:

- Improve computational efficiency in permutation-based inference.

- Expand NiMARE’s methodological coverage.

- Strengthen reproducibility and sustainability of neuroimaging meta-analysis.

- Improve developer onboarding, lowering contribution barriers.

- Because NiMARE serves as the statistical backend for Neurosynth Compose (2,700+ registered users), improvements will directly affect real-world meta-analytic workflows.


35) ImageJ Active Segmentation platform: Real-Time Filter Preview

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-35-imagej-active-segmentation-platform-real-time-filter-preview/35613](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-35-imagej-active-segmentation-platform-real-time-filter-preview/35613&sa=D&source=editors&ust=1773159824540530&usg=AOvVaw2cYSoKN-Jz6k7rlSei5WvD)


The Active Segmentation platform for ImageJ (ASP/IJ) [2] was developed in the scope of GSOC 2016 – 2025. The plugin provides a general-purpose environment that allows biologists and other domain experts to transparently use state-of-the-art techniques in machine learning to achieve excellent image segmentation and classification. ImageJ [1] is a public-domain Java image processing program extensively used in life and material sciences. The program was designed with an open architecture and is extensible via plugins.

The project idea: Users can tweak filter parameters via sliders/spinners and immediately see the effect on the image.

Tasks

• Fix existing issues and bugs

• UI implementation and testing

Minimal set of deliverables

• Requirement specification - Prepared by the candidate after understanding the functionality.

• System Design - Detailed plan for development of the plugin and test cases.

• Implementation and testing - Details of implementation and testing of the platform.


Desired skills: Java

Mentors: Dimiter Prodanov ([dimiterpp@gmail.com](mailto:dimiterpp@gmail.com)) IICT-BAS; Rikas Ilamdeen ([rikasilamdeen@gmail.com](mailto:rikasilamdeen@gmail.com))


36) Durham university - GestureCap: Creation of mappings to enable music and speech generation, to investigate musical creativity, agency and music-movement-dance interactions

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-36-durham-university-gesturecap-creation-of-mappings-to-enable-music-and-speech-generation-to-investigate-musical-creativity-agency-and-music-movement-dance-interactions/35614](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-36-durham-university-gesturecap-creation-of-mappings-to-enable-music-and-speech-generation-to-investigate-musical-creativity-agency-and-music-movement-dance-interactions/35614&sa=D&source=editors&ust=1773159824544578&usg=AOvVaw0sxic5dC4j13b0ZIKo2ivG)

Mentors: Alison Wang <[jiaxi.wang@durham.ac.uk](mailto:jiaxi.wang@durham.ac.uk)>, Deepansh Goel <[deepansh.04614815623@cseaiml.mait.ac.in](mailto:deepansh.04614815623@cseaiml.mait.ac.in)>, Suresh Krishna <[suresh.krishna@mcgill.ca](mailto:suresh.krishna@mcgill.ca)>

Skill level: Intermediate – Advanced

Required skills: If interested in music generation, experience/familiarity with a framework like Max/CSound/PureData/SuperCollider required and some experience with Python preferred. If interested in speech generation, fluency in Python required and experience with sign-language transcription / speech generation libraries preferred.

Time commitment: Full time (350 hours)

About: Over the last two years, we have developed GestureCap (GSoC 2024 report · GitH), a tool that uses markerless gesture-recognition and motion-capture (using Google’s MediaPipe) to create a working framework whereby movements can be translated into sound with short-latency, allowing for example, gesture-driven new musical instruments. We have created a pipeline whereby we can get down to 12 ms gesture to sound latency, thus increasing the range of possibilities for markerless gesture-driven musical expression. We have also created elementary mappings to go from gesture to sound.

Aims: This year, we aim to build on this initial proof-of-concept to create a usable tool that enables gesture-responsive music and speech generation. Of particular interest is the creationo of a workflow/framework that enables the creation of new mappings from detected gestures to sound. The development of GestureCap will facilitate both artistic creation, as well as scientific exploration of multiple areas, including for example - how people engage interactively with vision, sound, and movement and combine their respective latent creative spaces. Such a tool will also have therapeutic/rehabilitative applications in populations of people with limited ability to generate music and in whom agency and creativity in producing music have been shown to produce beneficial effects.

Project website: [https://github.com/m2b3/gesturecap2025](https://www.google.com/url?q=https://github.com/m2b3/gesturecap2025&sa=D&source=editors&ust=1773159824549777&usg=AOvVaw1WEzS16mxh92UGAo0obBf3)

Tech keywords: Sound/music generation, Image processing, Python, MediaPipe, Wekinator, AI, Deep-learning


37) ATHENA Research Center / EBRAINS - Automating Performance Verification for the EBRAINS Software Distribution

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-37-athena-research-center-ebrains-automating-performance-verification-for-the-ebrains-software-distribution/35615](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-37-athena-research-center-ebrains-automating-performance-verification-for-the-ebrains-software-distribution/35615&sa=D&source=editors&ust=1773159824551125&usg=AOvVaw0lxM9-xdCGMatHASUH_aGp)

The EBRAINS Software Distribution (ESD) is a curated collection of tools for computational neuroscience, supporting education, research, and simulation across heterogeneous hardware — including HPC, GPUs, and neuromorphic computing systems. Many ESD tools are developed by the research community and leverage diverse hardware architectures for performance and scalability.

This project aims to integrate, parameterize, and automate a comprehensive benchmarking suite for key neural simulators within ESD. The focus will be on established benchmarks for widely used simulators like Arbor, NEURON, and NEST, creating a unified framework for performance validation, regression testing, and hardware profiling across EBRAINS cloud and HPC environments.

Key Objectives:


1) Integrate and Unify Simulator Benchmarks

2) Develop a framework to incorporate existing benchmark suites into spack package descriptions for:

- Arbor: HPC-focused simulator benchmark suite

- NEURON: Widely-used classic simulator performance tests

- NEST: Large-scale network simulation benchmarks

3) Parameterize Benchmark Configurations

4) Design a flexible configuration leveraging the related ESD spack package descriptions system allowing users and CI systems to easily adjust:

- Model size and complexity

- Hardware targets (CPU core counts, GPU usage, MPI configuration)

- Output granularity (performance summaries, detailed profiling)

5) Embed Micro-Benchmarks for System Profiling and Performance Verification

6) Integrate low-level performance tests into the ESD to complement simulator benchmarks:

- OSU Micro-Benchmarks — Network and MPI performance

- nccl-test — Multi-GPU communication scaling

Technology Stack & Required Skills:

- Primary (Must Have): Python and Shell Scripting (Bash)

- Secondary (Good to Have): SLURM, Spack Package Manager, System Benchmarking


38) ATHENA Research Center / EBRAINS - Modular Software Environments and Service Integration for the EBRAINS Software Distribution


Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-38-athena-research-center-ebrains-modular-software-environments-and-service-integration-for-the-ebrains-software-distribution/35617](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-38-athena-research-center-ebrains-modular-software-environments-and-service-integration-for-the-ebrains-software-distribution/35617&sa=D&source=editors&ust=1773159824557202&usg=AOvVaw29ZA-3wVmPj5w9xXcptov2)

The EBRAINS Software Distribution (ESD) is a curated collection of tools for computational neuroscience, supporting education, research, and simulation across heterogeneous hardware — including HPC, GPUs, and neuromorphic computing systems. Many ESD tools are developed by the research community and leverage diverse hardware architectures for performance and scalability. Currently, the ESD covers ~70 top-level scientific tools and 800+ dependencies, and it is deployed as a “monolith”. This creates two major challenges:

Flexibility: Researchers might want to combine the ESD with other, possibly experimental, tools that are not yet in the official release. Conversely, smaller minimum-size software ecosystems can be beneficial for other applications, such as for GDPR-sensitive environments.

Service compatibility: The ESD contains “client” software that interacts with EBRAINS “web” services. The service-side environment must be strictly compatible with the client-side version, which can’t be guaranteed unless services are also part of the ESD.

This project focuses on adding modularity to the ESD’s spack buildtool-based build and deployment functionality to support more flexible, on-demand environments. You will develop spack-based tooling to generate custom environments, both subsets and supersets, that maintain consistency and alignment with the official ESD releases.

Another part of this project involves extending the ESD to support “services”. While most of the ESD comprises end-user tools, services often depend on a smaller or different set of dependencies. By leveraging the spack package manager used by the ESD, we can explicitly track distinct service-side dependencies and define compatibility constraints between client and server versions, influencing both the ESD client-side and the service-side build configurations.

Key Objectives:

1) Add support for creating ESD-derived software ecosystems:

2) Develop tools to extract partially overlapping subsets of the ESD while ensuring the “concretized” dependency tree remains compatible with the full official deployment.

3) Develop and integrate a format for ESD service packages based on the spack package format; i.e. recipes for backend services that define strict compatibility constraints with their client-side counterparts in the ESD.

4) Showcase a service build (e.g., for a Knowledge Graph or Neuromorphic access service) that adheres to specific client-server version range constraints and can be deployed as a lightweight, ESD-aligned container.

Technology Stack & Required Skills:

1) Primary (Must Have): Python

2) Secondary (Good to Have): Spack Package Manager, Shell Scripting, Build tools


39) National Brain Research Centre (NBRC) & EBRAINS (NeuroSim) Automating In-Silico Stimulation for Non-Invasive Biomarker Discovery

Neurostars Link for idea discussion: [https://neurostars.org/t/gsoc-2026-project-39-national-brain-research-centre-nbrc-ebrains-neurosim-automating-in-silico-stimulation-for-non-invasive-biomarker-discovery/35619](https://www.google.com/url?q=https://neurostars.org/t/gsoc-2026-project-39-national-brain-research-centre-nbrc-ebrains-neurosim-automating-in-silico-stimulation-for-non-invasive-biomarker-discovery/35619&sa=D&source=editors&ust=1773159824565023&usg=AOvVaw2BP55nxtRRXOchaiwCRZSC)


Mentor/s: Dr Khusbu Agarwal <[khusbu.agarwal@nbrc.ac.in](mailto:khusbu.agarwal@nbrc.ac.in)>

Project Synopsis: This project aims to build NeuroSim, an open-source "In-Silico Stimulation" engine. Unlike standard tools that simply analyze static functional connectivity, NeuroSim integrates Network Control Theory (NCT) with Effective Connectivity modeling to quantify the energy dynamics of brain state transitions. The pipeline will be validated by identifying "Stuck States" (Attractor Basins) in Alcohol Use Disorder (AUD), Alzheimer’s Disease and Epilepsy, effectively creating a mimic framework for virtual therapeutic stress-testing.


The Problem: Current neuroinformatics workflows largely focus on static functional connectivity (correlations). However, understanding complex pathologies—from neurodegeneration to addiction—requires quantifying the dynamic cost of brain state transitions. While wet lab approaches like intracranial stimulation (TMS/DBS) can probe these dynamics, they are invasive and limited to pre-surgical patients. There is a critical unmet need for a pre-emptive computational framework that can simulate these dynamics non-invasively to identify biomarkers before physical intervention is attempted.


The Objectives: The aim is to build a robust, modular Python pipeline to provide an effective solution to the problem, utilizing Network Control Theory and Manifold Learning. The project has three specific technical goals:

1. Automate In-Silico Stimulation: Develop a workflow to calculate "Control Energy" landscapes. This allows researchers to simulate how hard it is for a brain to switch between cognitive states.

2. Ensure Physical Validity: Implement Effective Connectivity estimation. This allows Network Control Theory to be validly applied to functional (fMRI) data, therefore bridging the gap between structural and functional analysis.

3. Validate via Case Studies: Demonstrate the tool’s utility by isolating dynamical biomarkers in three distinct regimes with the first one as control. They are: the healthy baseline (HCP), the entropic collapse of neurodegeneration (ADNI), the rigid attractor states of addiction (AUD) and the facilitator nodes that drive seizure propagation in Epilepsy (OpenNeuro).


Methodology & Implementation Plan: The pipeline will be developed as a Python library, consisting of three core modules:

a) Collection, Cleaning & Harmonization: Standardization of BIDS-formatted data from different sources (HCP, ADNI, OpenNeuro). To account for multi-site scanner effects, this module will incorporate neuroCombat. This guarantees that true biological variance, not site noise and artifacts, which is reflected in downstream physical modeling.

b) Network Control Theory: This module constitutes the computational engine. It will first estimate Effective Connectivity (e.g., via spectral inversion or regression methods). This will construct directed adjacency matrices. It will then compute key control metrics:

• Average Controllability: To Quantify the brain's general capacity to navigate state space.

• Modal Controllability: To identify nodes that drive difficult state transitions (potential "Facilitator Nodes" in epilepsy or addiction).

c) Trajectory Inference & Visualization A visualization engine using Manifold Learning (UMAP) and Pseudo-Time Inference. This will project high-dimensional control energy profiles onto a low-dimensional manifold, allowing clinicians to visualize a patient's position on a disease trajectory.


Expected Outcomes:

1. A fully documented NeuroSim Python library.

2. Jupyter Notebook Tutorials hosted on GitHub, that demonstrate how to run an "In-Silico Stimulation" on patient data.

3. Validation Report: A benchmark comparison of Control Energy biomarkers vs. standard Static Connectivity in distinguishing AUD patients from healthy controls.

Skills Required: Python (Advanced), Neuroimaging (Nilearn, Nibabel), Linear Algebra (SciPy), Graph Theory, Basic Machine Learning (Scikit-learn, UMAP).
