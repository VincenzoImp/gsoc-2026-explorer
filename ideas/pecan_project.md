# PEcAn Project — Project Ideas

**Source:** https://pecanproject.github.io/gsoc_ideas
**Scraped:** 2026-02-22T23:28:47.583292

---

# GSoC - PEcAn Project Ideas

PEcAn is an open-source ecosystem modeling framework integrating data, models, and uncertainty quantification. Below is a list of potential ideas where contributors can help improve and expand PEcAn. To get started contributing to PEcAn, check out [this guide](https://github.com/PecanProject/pecan/discussions/3469). Come find us on Slack to discuss. If you have questions or would like to propose your own idea, contact @kooper in or join our ** #gsoc** channel in Slack!

## Project Ideas[](https://pecanproject.github.io#ideas)

Below is a list of project ideas. Feel free to contact the listed mentors on Slack to discuss further or contact @kooper with new ideas and he can help connect you with mentors.

[Refactor and Parallelize Input Processing Pipelines](https://pecanproject.github.io#input)[Benchmarking and Validation Framework](https://pecanproject.github.io#validation)[Increase PEcAn modularity](https://pecanproject.github.io#module)[Standardizing Model Couplers Across Models](https://pecanproject.github.io#couplertools)[LLM-Assisted Extraction of Agronomic Experiments into BETYdb](https://pecanproject.github.io#llm-betydb)

### 1. Refactor and Parallelize Input Processing Pipelines[](https://pecanproject.github.io#input)

Input-processing code in PEcAn (e.g., meteorological preparation) is currently centered around monolithic orchestration functions such as `do.conversions`

and `met.process`

. These functions mix low-level data transformations with sequential control flow, implicit dependencies, and caching behavior, making them difficult to test, debug, scale, or parallelize across sites and ensemble members.

This project will deprecate `do.conversions`

as currently implemented and replace it with input preprocessing workflows that are explicitly structured around data dependencies and are naturally parallelizable across data streams, sites, and ensemble members. The work will refactor or deprecate `met.process`

to remove monolithic orchestration and reduce or eliminate opaque caching, while retaining and strengthening existing low-level transformation functions.

As part of the refactor, orchestration logic should be rebuilt to make inputs, outputs, and dependencies explicit. A workflow tool such as `targets`

may be used to help define and validate the dependency graph and caching behavior, but must not become a required or exclusive execution path for PEcAn.

This refactoring should also reduce or eliminate implicit dependencies on the global settings object (see Project 3), enabling clearer APIs and improved testability.

**Expected outcomes:**

A successful project would complete the following tasks:

-
Deprecation plan for do.conversions, with a replacement that provides a modular suite of preprocessing tools that

- explicitly defines inputs and outputs, and
- supports parallel execution across products, sites, and ensemble members. Key here is a high-level plan for development that will continue beyond what is accomplished this summer.

-
Refactor and/or deprecation plan for met.process that:

- removes monolithic orchestration and hidden control flow,
- reduces or eliminates over-engineered caching,
- retains and documents low-level transformation functions.

-
Demonstration of parallel execution on a multi-site or multi-ensemble example.

-
Basic correctness and performance benchmarks, including unit and integration tests and validation of PEcAn-standard inputs (formats and units).

-
Updated developer documentation covering:

- the new input-processing architecture,
- how to add a new preprocessing step,
- migration guidance from legacy entry points.


**Prerequisites:**

- Required: R (existing workflow and prototype is in R)
- Helpful: familiarity with parallel computing, workflow refactoring

**Contact persons:**

Chris Black (@infotroph), @Henry Priest

**Duration:**

Large (350 hr)

**Difficulty:**

High

### 2. Benchmarking and Validation Framework[](https://pecanproject.github.io#validation)

A key task in any modeling workflow is the validation of model outputs against held out observations. When a validation dataset is used repeatedly and agreed upon by a broad community to have particular value in assessing model performance it often gets elevated to the status of a persistent "benchmark" dataset. In PEcAn, there is a need to replace our earlier benchmarking module, whose design was never fully implemented, with a simpler framework. In designing this framework we'd encourage participants to build upon the existing low-level infrastructure in the existing benchmarking module for model-data alignment tools and comparison metrics like RMSE, MAE, and R2. Work should also build upon and generalize existing examples of "one off" validation scripts (e.g., CARB cropland validations, North American data assimilation validations).

**Expected outcomes:**

A successful project would complete the following tasks:

- A high-level design and plan for development that will continue beyond what is accomplished this summer
- Unit and integration tests
- A generalized example of a validation workflow and/or notebook using California cropland datasets spanning multiple sites and crop types.
- Documentation

**Prerequisites:**

- Required: R (existing workflow and prototype is in R), familiarity with statistical methods for model validation
- Helpful: Familiarity with existing benchmarking workflow systems

**Contact person:**

David LeBauer (@dlebauer), Akash BV (@divine7022)

**Duration:**

Flexible to work as either a Medium (175hr) or Large (350 hr)

**Difficulty:**

Medium

### 3. Increase PEcAn modularity[](https://pecanproject.github.io#module)

Existing PEcAn workflows rely heavily on reading a large `settings`

object and writing .RData files or other opaque artifacts to disk to pass state between steps. This behavior reduces transparency, testability, and user understanding. The high-level goal of this project is to make PEcAn’s core functionality more modular and transparent, so that users can more easily build, maintain, and expand PEcAn workflows.

This project refactors a single, well-defined workflow so that functions return explicit R objects (e.g., data frames or lists) instead of relying on hidden on-disk side effects.

To minimize disruption with existing workflows, the preferred approach would be:

- To begin by documenting existing functionality
- Where needed, write tests for existing functionality
- Document new functionality
- Write tests for new functionality (TDD)
- Refactoring of functions to return objects
- Then refactor downstream functions use those objects
- Only after that’s working, stop writing out the files.
- If time permits, analyze how PEcAn's high-level modules are using the
`settings`

object and, where possible, refactor function inputs to only pass the required subset of variables or variable lists. - Along the way, it would also be beneficial to reassess which functions need to be exported, with the idea that fewer exported functions would make it easier for new users to see what PEcAn’s core modules actually are, and better documenting the core functions and modules we expect users to need to learn/use

**Expected outcomes**:

- Refactored functions that return explicit R objects instead of writing .RData
- Clear definition and doucmentation of object structures passed between steps
- Backward-compatible wrappers where needed to avoid breaking existing workflows
- Unit tests that no longer depend on on-disk state or output_dir
- Documentation describing .RData deprecation, migration guidance, and examples

**Skills Required**:

- Required: R (existing workflow and prototype is in R) and R package development
- Helpful: familiarity with code refactoring

**Contact person:**

Mike @Dietze

**Duration:**

Suitable for a Medium (175hr) or Large (350 hr) project.

**Difficulty:**

Medium

### 4. Standardizing Model Couplers Across Models[](https://pecanproject.github.io#couplertools)

PEcAn models frequently duplicate similar logic for writing configuration files, translating meteorological inputs, and handling model-specific I/O. This copy–paste pattern increases maintenance cost and makes it harder to integrate new models consistently.

This project identifies a small set of shared configuration and I/O patterns and refactors them into documented helper functions with well-defined interfaces. Possible examples include netCDF reading/writing, parsing standardized input files, test fixtures, settings validation, and others. The approach should be demonstrated across a limited number of models coupler packages under active development.

**Expected outcomes:**
A successful project will deliver an inventory of duplicated configuration and I/O patterns along with one or more of the following steps toward deduplication:

- Shared helper functions with explicit inputs, outputs, and unit conventions
- Refactored model code using standardized helpers
- Unit tests ensuring consistent behavior across models
- Updated developer documentation describing standard interfaces and recommended usage

**Prerequisites:**
Required: Proficiency in R
Helpful: experience with unit testing

**Contact person:**
Chris Black, @infotroph

**Duration:**:
Medium (175hr) or Large (350 hr) depending on number of deliverables

**Difficulty:**
Medium

### 5. LLM-Assisted Extraction of Agronomic and Ecological Experiments into Structured Data[](https://pecanproject.github.io#llm-betydb)

Manual extraction of agronomic and ecological experiments from scientific literature into a structured format that can be used to calibrate and validate models is slow, error-prone, and labor-intensive. Researchers must interpret complex experimental designs, reconstruct management timelines, identify treatments and controls, handle factorial structures, and link outcomes with correct covariates and uncertainty estimates. Data are often reported as summary statistics (for example mean and standard error) in text, tables, or figures and require additional context from disturbance or management time series. These tasks require scientific judgment beyond simple text extraction. Current manual workflows can take hours per paper and introduce inconsistencies that compromise downstream data quality and meta-analyses.

This project proposes a human-supervised, LLM-based system to accelerate data extraction while preserving scientific rigor and traceability. It will leverage existing labeled training data (scientific papers with ground‑truth entries), including aligned PDF‑to‑structured‑data records from [BETYdb](https://betydb.org) and [ForC](https://forc-db.github.io/index.html), which represent expert‑curated, production‑quality datasets. Combined, these resources include over 80,000 plant and ecosystem observations from more than 1,000 sources, providing high-quality supervision for extraction from text, tables, and figures. Evaluation should include held-out, out-of-sample papers. The system will ingest PDFs of scientific papers and produce tables compatible with the [spreadsheet used to upload data to BETYdb](https://docs.google.com/spreadsheets/d/e/2PACX-1vSAa7jBHSaas-bH0ARxQjVLKhz3Iq03t97wrxMZrgVVi98L5bYQi5ZUC0b57xIZBlHEkPH9qYf22xQS/pubhtml) (sites, treatments, management time series, traits+yields bulk upload table) with every field labeled as extracted, inferred, or unresolved and linked to provenance evidence in the source document.

The architecture follows a two-layer design: (1) a schema-validated intermediate representation (IR) preserving evidence links, confidence scores, and flagged conflicts, and (2) a materialization layer that enforces semantics, validation rules, and generates upload-ready CSVs or API payloads with full audit trails. Implementation is flexible—ranging from agentic LLM workflows to fine-tuned specialist models to an adaptive hybrid—and should be informed by empirical evaluation during the project.

Implementation is flexible—ranging from agentic LLM workflows to fine‑tuned specialist models to an adaptive hybrid—and should be informed by empirical evaluation during the project.

**Expected outcomes:**

A successful project would complete the following tasks:

- IR schema definition with validation rules and documented field semantics covering sites, treatments, managements, and traits/yields
- Modular extraction pipeline for document parsing, information extraction, and IR generation with clear separation between extraction and validation logic
- Independent validators for BETYdb semantics, unit consistency, temporal logic, and required fields
- BETYdb export module producing upload-ready management CSVs and bulk trait upload formats with full provenance preservation
- Scientist-in-the-loop review interface for approving, correcting, or rejecting extracted entries with inline evidence and confidence scores
- Evaluation harness with automated metrics for extraction accuracy, inference quality, coverage, and time savings relative to manual curation on held‑out test papers
- Documentation covering IR schema specification, developer guidance for adding new extraction components, and user guidance for the review interface

**Prerequisites:**

- Required: Python; familiarity with natural language processing, information extraction, and machine learning
- Helpful: experience with LLM APIs and fine-tuning frameworks, knowledge of BETYdb schema and workflows, familiarity with scientific writing and agronomic or ecological experimental design/analysis

**Contact persons:**

Nihar Sanda (@koolgax99), David LeBauer (@dlebauer)

**Duration:**

Large (350 hr)

**Difficulty:**

High
