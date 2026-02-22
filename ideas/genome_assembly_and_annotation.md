# Genome Assembly and Annotation — Project Ideas

**Source:** https://www.ebi.ac.uk/about/events/events/public-event/2025/2026-google-summer-of-code/
**Scraped:** 2026-02-22T23:28:47.629579

---

Public event/Ext Seminar event | Other

EMBL-EBI is a global leader in biological data. We develop and maintain open data resources and open-source software that support life science research worldwide. Our teams work at the intersection of biology, data science, and software engineering, building tools used daily by researchers across academia, healthcare, and industry.

Through Google Summer of Code (GSoC), EMBL-EBI mentors contributors to work on real-world open-source projects, helping them develop technical skills, domain knowledge, and experience contributing to widely used scientific software. The project ideas listed below reflect the breadth of work across EMBL-EBI and are designed to support contributors at different experience levels.

How to apply

Google Summer of Code contributors apply directly through the GSoC platform, but we strongly encourage you to engage with EMBL-EBI **before** submitting your application.

**Step 1: Explore the project ideas**Review the project ideas listed below and identify one (or more) that match your interests and skills. Each project includes information about expected outcomes, required skills, and difficulty level.

**Step 2: Do some background reading** You are not expected to be an expert in the domain, but spending some time familiarising yourself with the relevant technologies, data resources, or scientific context will help you prepare a stronger application.

**Step 3: Get in touch with us early** Once you have a project in mind, contact our GSoC helpdesk (

- a short CV or link to relevant experience (e.g. GitHub, portfolio)
- the project you are interested in
- a brief explanation of why you are interested
- any specific questions you may have

If you are interested in proposing your own project idea, include a short description and the technologies you expect to use so we can assess mentor availability.

**Step 4: Draft your application** Prepare your application well ahead of the deadline. A strong proposal clearly explains:

- what you plan to build
- how you will approach the work
- a realistic timeline with milestones
- what you hope to learn during the project

Mentors can provide guidance and feedback, but they will not write the application for you.

**Step 5: Incorporate feedback and submit** Use any feedback provided to refine your proposal, then submit your final application via the official GSoC website before the deadline.

For more detailed advice, please see our [Contributor Guide](https://www.ebi.ac.uk#contributor-guide), which outlines what we look for in successful applications and how contributors engage with EMBL-EBI teams during the programme.

[Expose a subset of ENA REST Services as MCP](https://www.ebi.ac.uk#project-1)[Creating a knowledge graph from a subset of ENA and BioSamples data](https://www.ebi.ac.uk#project-2)[Annotation metrics reporting & analysis modules for the Ensembl Assembly/Annotation tracking app](https://www.ebi.ac.uk#project-3)[Development of a refinement tool to identify selenoproteins in Ensembl genesets](https://www.ebi.ac.uk#project-4)[Expanding a pipeline for small non-coding RNA (sncRNA) identification in Ensembl Genomes](https://www.ebi.ac.uk#project-5)[Expand genome metadata in Ensembl with AI tools](https://www.ebi.ac.uk#project-6)[BUSCO-Missing Investigator (BMI): a reproducible pipeline to explain “missing/fragmented BUSCOs”](https://www.ebi.ac.uk#project-7)[Ask VEPai. Trained chatbot interface for Ensembl VEP web.](https://www.ebi.ac.uk#project-8)[nf-core/vep: Extending and standardising Ensembl VEP workflow for nf-core](https://www.ebi.ac.uk#project-9)[Building a perturbation-aware LLM for multimodal](https://www.ebi.ac.uk#project-10)*in-silico*perturbation modelling[Designing an open access Ensembl GraphQL Workshop](https://www.ebi.ac.uk#project-11)[Standardised evaluation for microbiome dataset classifiers](https://www.ebi.ac.uk#project-12)[Sequence similarity networks for the visualisation and exploration of MGnify Proteins](https://www.ebi.ac.uk#project-13)[A genomic feature database in the browser](https://www.ebi.ac.uk#project-14)[Design and API-aware UI generation using MCP servers and Figma APIs](https://www.ebi.ac.uk#project-15)[Expose BioSamples Submission and Search Capabilities as MCP Tools for AI-Assisted Metadata Interaction](https://www.ebi.ac.uk#project-16)

**Brief Explanation**

The European Nucleotide Archive (ENA) provides a rich set of REST APIs that allow users to query genomic metadata, sequence records, and submission information. While these APIs are powerful, they are not directly accessible to modern AI agents or LLM-based tools that rely on standardized interaction protocols.

This project aims to expose a carefully selected subset of ENA REST services through the **Model Context Protocol (MCP)**, enabling AI agents to interact with ENA programmatically in a safe, structured, and reproducible way. MCP acts as a bridge between large language models and external tools by defining explicit schemas, inputs, and outputs, preventing hallucinations and ensuring reliable access to authoritative data sources.

The student will design and implement an MCP server that wraps ENA REST endpoints (e.g. study metadata lookup, run/sample queries, accession search) and exposes them as well-defined MCP tools. The project focuses on correctness, usability, and extensibility rather than deep bioinformatics analysis.

This project is intentionally scoped to be beginner-friendly, with limited bioinformatics background required, and emphasizes software engineering, API design, and AI-tool integration.

**Expected results**

- A production-ready MCP server exposing a broad subset of ENA REST APIs
- Demonstrations of:
- LLM or agent-based querying of ENA via MCP
- Deterministic, traceable responses backed by ENA data
- A scalable foundation that can be extended to other EMBL-EBI data resources

- Comprehensive documentation, including:
- Architecture and design decisions
- MCP tool specifications, Examples of AI agent workflows using ENA MCP tools

- Support for advanced capabilities such as:
- Composing multiple ENA queries into a single logical operation
- Normalizing heterogeneous ENA responses into consistent formats
- Caching and rate-limit-aware request handling

- Well-designed MCP tool schemas with:
- Strong input validation, explicit output contracts, clear error semantics


Required knowledge

- Strong Python programming skills
- REST APIs, HTTP, and JSON
- Software architecture and modular design
- Schema definition and validation

Desirable knowledge

- Familiarity with MCP or LLM tool/function calling
- API performance optimization and caching strategies
- Experience with containerization (Docker) or CI/CD pipelines

Difficulty

Medium

Length

Medium – 175h

Mentors

**Brief explanation**

European Nucleotide Archive (ENA), one of the three major nucleotide databases in the world, is hosting over 70 PB of genomics data. LLMs are well-developed to parse unstructured data but less so with the structured data.

This project is to create a prototype of a knowledge graph (KG) to make the database directly accessible to AI tools. A graph engine will be integrated with the existing structured data store to avoid duplicating data into a graph database. An AI-friendly Graph Query Language (GQL) will be used to interact with the KG backed by the relational data model via the graph engine dynamically. High profile LLM models are to be evaluated to generate GQL statements. The final output will be one or more AI agents to support Graph RAG to interact with a subset of the structured genomics data in ENA with the following characteristics:

- A working prototype capable of querying a small subset of ENA data (e.g. pathogen, AMR or data deposition analytics).
- A clear path to scale up the prototype to expand to all structured data in ENA.
- AI agent(s) with absolutely no hallucination.

**Expected results**

- Students would learn how AI components are used to construct agent workflows.
- Students would gain firsthand experience how to create working prototypes beyond “hello-world” toys.
- Students would be able to create standalone AI agents capable of interacting with ENA data but with minimum dependency.
- Students would be able to apply the knowledge learned in the summer school to create Graph RAGs on any structured data.

**Required knowledge**

- AI-friendly GQL (e.g. Gremlin)
- Graph engine (e.g. PuppyGraph)
- Python and libraries for AI-agent construction (e.g. LangChain)
- Methodology for benchmarking Graph RAG and GQL

**Desirable knowledge**

- ENA schema and tagging mechanism
- Kubernetes and its scaling
- Scalable local deployment of LLM models (e.g. Ollama)

**Difficulty**: High

**Length**: 350h

**Mentors**: [David Yuan](mailto: davidyuan@ebi.ac.uk)

**Brief explanation**

Ensembl maintains an internal web application to track genome assembly status (e.g. candidates for annotation), Ensembl annotation status, and associated quality/completeness metrics. While the app stores important annotation completeness scores and other quantitative measures, it currently lacks richer reporting and comparative views that help users quickly interpret genome annotation quality across many species.

This project focuses on designing and implementing Python-based analysis modules for genome annotation metrics and comparative analysis, with a strong emphasis on clean workflows, test coverage, and maintainability. These modules will generate per-genome reports and perform comparative analyses across taxonomic groupings, enabling annotators and production teams to identify unusual annotations, trends, and priorities in a reproducible and testable way.

There is an opportunity to integrate the resulting modules into the existing tracking web application, but web/UI integration is not essential to the core project. The primary goal is to produce robust, well-tested backend analysis components that can later be surfaced via the app or reused in other contexts (e.g. batch reporting, pipelines).

**Expected results**

Deliverable 1: Per-genome annotation metrics report module

- Develop a Python module that generates a structured metrics report for a single genome, based on the existing data model.
- The report should include (as available in the stored data model), for example:
- annotation completeness scores (and/or component sub-scores)
- number of protein-coding genes/transcripts
- exon counts and distribution summaries (e.g. exons per transcript)
- gene/transcript length distributions or summary stats
- any other tracked QC/production metrics already stored

- Include clear tables and a small set of “at-a-glance” visuals (e.g. sparklines, histograms, boxplots, score badges).
- Unit tests for individual metric calculations
- Integration tests for full per-genome report generation
- Clear separation between data access, computation, and presentation layers

Deliverable 2: Taxonomy grouping + comparative analysis module

- Add functionality to group genomes by taxonomic classification at multiple ranks (e.g. species/genus/family/order/class/phylum).
- Provide controls to select:
- taxonomic rank
- comparison set (e.g., “all annotated in Ensembl release X”)
- metrics to include in analysis

- Implement multivariate analysis (MVA) to identify trends and outliers within each group, e.g.:
- PCA (or similar dimensionality reduction)
- clustering (optional, depending on scope and usefulness)
- outlier detection heuristics (distance-based, robust z-scores, etc.)

- Produce “nice visuals” suitable for production/QC workflows, such as:
- PCA scatter with interactive point details (genome name, key metrics)
- heatmaps/correlation views
- rank-based comparison plots (e.g. boxplots per clade)
- outlier summary list linking back to the genome report page


**Final project output**

- A set of well-documented, reusable Python modules for:
- per-genome annotation metric reporting
- taxonomy-based comparative analysis

- Comprehensive test suite covering core logic and analysis workflows
- Clear documentation describing:
- module data flow
- how metrics are computed
- how to extend the system with new metrics or analyses

- Optional (stretch goal): example integration points or lightweight endpoints demonstrating how the modules could be plugged into the existing tracking web application

**Required knowledge**

- Python for data handling and statistical analysis.
- Basic understanding of genome annotations and common metrics (genes/transcripts/exons, completeness/QC measures).

**Desirable knowledge**

- Experience with multivariate analysis (PCA, clustering) and practical outlier detection.
- Familiarity with taxonomy sources/identifiers and rank-based grouping (NCBI taxonomy, etc.).
- Experience producing clear scientific dashboards/visualisations.
- Experience working with existing codebases and adding features in a maintainable way (tests, docs, code style).
- Experience designing clean APIs and modular analysis code
- Experience working in existing codebases with an emphasis on testing, documentation, and code quality
- Familiarity with web application backends or data visualisation, for optional integration work (FastAPI)
- Familiarity with web application frontends for optional integration work (React/
[Node.js](http://node.js)) - Interest in product design and design tools (ex. Figma)

**Difficulty**: Beginner

**Length**: 175h

**Mentors**: [Anna Lazar](mailto:lazar@ebi.ac.uk), [Simarpreet Kaur Bhurji](mailto:sbhurji@ebi.ac.uk), [Leanne Haggerty](mailto:leanne@ebi.ac.uk)

**Brief explanation**

Selenocysteine-containing proteins (selenoproteins) play crucial biological roles, but their annotation remains challenging due to the unique incorporation of selenocysteine (Sec, U) at UGA codons. Currently, Ensembl uses Exonerate to align known selenoproteins to genomes and manually verifies models based on sequence identity and coverage. However, the existing approach is inefficient and outdated, requiring a more scalable and automated solution.

This project will develop a Nextflow pipeline to efficiently annotate selenoproteins that can be applied to Ensembl gene sets by:

- Optimising the search for selenoprotein homologs
- Aligning known selenoproteins against the genome using more efficient tools like MMseqs2, DIAMOND, or TBLASTN.
- Filtering candidate regions based on sequence similarity, focusing on high-identity and high-coverage matches.

- Improving selenocysteine validation
- Detecting UGA codons in aligned models and verifying the presence of SECIS elements (selenocysteine insertion sequences) in downstream regions.
- Ensuring selenocysteine positions match the reference protein sequences.

- Automated filtering and quality control
- Retaining only models with expected coverage and sequence identity to known selenoproteins.
- Benchmarking against accurate but computationally intensive dedicated selenoprotein annotation tools
- Benchmarking against accurate but computationally intensive dedicated selenoprotein annotation tools
- Removing false positives by integrating BUSCO-like completeness scoring with clade specific selenoprotein sets.
- Generating quality assessment reports.

- Deployability and scalability
- Implementing the pipeline in Nextflow to improve reproducibility and scalability across multiple genomes.
- Providing Docker/Singularity containers for easy deployment in HPC and cloud environments.


The final pipeline will be integrated within Ensembl’s genome annotation pipeline to be integrated within Ensembl’s genome annotation pipeline to streamline selenoprotein identificationidentification, thus thus improving accuracy, efficiency, and automation.

**Expected results**

- A Nextflow-based selenoprotein annotation pipeline that aligns known selenoproteins and predicts valid selenocysteine-containing models.
- Automated verification of UGA codons and SECIS elements.
- Integration-ready outputs for Ensembl gene sets.
- Containerised workflow for deployment on multiple computing environments.

**Required knowledge**

- Nextflow or similar workflow automation tools.
- Sequence alignment tools (DIAMOND, MMseqs2, TBLASTN, Exonerate).
- Genome annotation formats (FASTA, GFF3).
- Basic knowledge of selenoprotein biology and SECIS elements.

**Desirable knowledge**

- Experience with gene annotation pipelines (e.g., AUGUSTUS, BRAKER, HELIXER, HELIXER).
- RNA structure analysis tools for SECIS detection (e.g., SECISearch, Infernal).
- BUSCO or other completeness assessment tools.
- Containerisation technologies (Docker, Singularity).

**Difficulty**: Medium

**Length**: 175h

**Mentors**: [Jack Tierney](mailto:jackt@ebi.ac.uk)

**Brief explanation**

This project aims to enhance an existing pipeline for identifying small non-coding RNAs (sncRNAs) in Ensembl genomes. Building on the current MirMachine modules, the pipeline will be expanded to incorporate additional analyses using RFAM and miRBase databases.

Further improvements will include running sequence similarity searches with NCBI-BLAST and generating structural models using the Infernal software suite. The final pipeline will be optimised for flexibility, supporting various input sources, and containerised using Docker/Singularity to ensure reproducibility and shareability.

**Expected results**

- Integration of RFAM and miRBase data for improved sncRNA annotation.
- Incorporation of NCBI-BLAST for sequence similarity searches.
- Implementation of Infernal for RNA structural model generation.
- Optimisation of pipeline scalability and flexibility for different input sources.
- Containerisation of the pipeline using Docker/Singularity for easy deployment.
- Documentation and testing to ensure usability and reproducibility.

**Required knowledge**

- NextFlow or other workflow management tools.
- Python and/or Bash for pipeline scripting.
- Basic RNA bioinformatics (FASTA, GFF3 formats, RNA databases).

**Desirable knowledge**

- Experience with RFAM, miRBase, and NCBI-BLAST.
- Familiarity with Infernal for RNA secondary structure modeling.
- Knowledge of Docker/Singularity for workflow containerisation.
- Experience in workflow optimisation for large-scale genomic data.

**Difficulty**: Medium

**Length**: 175h

**Mentors**: [Jose Perez-Silva](mailto:ereboperezsilva@ebi.ac.uk), [Vianey Paola Barrera Enriquez](mailto:vianey@ebi.ac.uk)

**Brief explanation**

Ensembl Plants and Ensembl Metazoa import publicly available genome assemblies and their annotations from community contributors. Whilst assemblies are submitted to INSDC sequence archives, it is often the case that these submissions are missing some key information that can usually be found in the paper publication corresponding to that assembly (most frequently due to those metadata fields being not available in the submission process). This metadata is not useful useful for our users, but Ensembl can benefit from it, e.g. polyploid genomes require different processing parameters/tools than diploid genomes when it comes to comparative genomics. Current AI tools are making fetching such metadata from research papers much easier, so we would like to build a standalone module that performs such task with the ultimate goal to incorporate it into our genome loading pipeline.

**Expected results**

- A standalone module (preferrably written in Python, but any current bioinformatics programming language would be acceptable) that can fetch the required genome metadata from current (publicly available) literature
- The code will include documentation as well as type hints (if the selected programming language allows it) and unit testing
- Capacity to retrain/expand as new research papers are published

**Required knowledge**

- AI tools for fetching/querying a database of research papers
- Build of a module to be later included as part of a production pipeline written in Nextflow

**Desirable knowledge**

- Familiarity with the metadata associated with invertebrate and/or plant assemblies

**Difficulty**: Medium

**Length**: 175h

**Mentors**: [Jorge Alvarez](mailto:jalvarez@ebi.ac.uk), [Disha Lodha](mailto:dishalodha@ebi.ac.uk)

**Brief description**

BUSCO is widely used to measure assembly completeness, but after seeing “Missing” (and often “Fragmented”) BUSCOs, users still need to answer: why are these genes missing and what should I do next?

This project proposes a reproducible, best-practice pipeline/tool that takes BUSCO outputs (and optionally assemblies/annotations/reads) and automatically gathers evidence to generate interpretable, ranked explanations per BUSCO along with a clean, actionable report.

**Expected results**

- Summary table: BUSCO ID → status, top reason code(s), confidence scores
- Report (HTML/Markdown): overview plots + top actionable recommendations (e.g., “try a closer lineage dataset”, “investigate contig ends”, “annotation rerun suggested”, “coverage drop suggests gap”)

**Required skills**

- Command line + Linux basics
- Python (or similar) for parsing, feature extraction, and reporting
- Genomics basics (assemblies, gene models, alignments)
- Reproducibility practices

**Desirable skills**

- Familiarity with alignment outputs and scoring
- Workflow engineering (Nextflow)
- Experience packaging bioinformatics tools and writing robust docs/tests

**Difficulty**: Medium

**Length**: 175 hours

**Mentors**: [Swati Sinha](mailto:swati@ebi.ac.uk), [Jitender Jit Singh Cheema](mailto:jitender@ebi.ac.uk)

**Brief explanation**

Ensembl VEP is a widely used tool (10+ million dockerhub pulls alone) enabling the annotation and prioritisation of genetic variants and is used extensively in academic research and clinical assessments.

This project would be to prototype an AI chatbot configuration interface for the version of Ensembl VEP run from the new Ensembl website. The current selection of options for running the web version of Ensembl VEP is extensive, and requires users to be experienced or willing to read lots of tooltips and help documentation. A better option would be if they were able to describe their data and what they’re trying to achieve then receive a set of suggested options, with justifications. They could then click to apply these to the configuration before Ensembl runs.

Each Ensembl VEP option would be assessed and labelled and weighted appropriately. We would then identify an appropriate base chat-bot model and assemble a corpus of training data, from a mixture of our responses to users and specific constructed examples. These would be divided into training and test sets for first training the model and then assessing responses.

If this is completed, an optional extension of the project would be to produce a simple API wrapper for IO.

**Expected results**

- Assemble and label training data
- Train a prototype model
- (Optional) API wrapper

**Required knowledge**

- Python (and ML libraries)
- Data annotation
- Desirable knowledge
- HPC interaction
- Model training experience
- Prompt engineering
- Understanding / interest in genetic variant annotation

**Learning outcomes**

Gain experience with data annotation and agent model training and testing, supporting a globally utilised genetic variant annotation tool.

**Difficulty**: Medium

**Length**: 175 hours

**Mentors**: [Likhitha Surapaneni](mailto:likhithas@ebi.ac.uk)

**Brief explanation**

The goal of this project is to design, develop, and document an nf-core pipeline for the Ensembl Variant Effect Predictor (VEP) that follows nf-core best practices, fully modularizes the existing Nextflow VEP workflow from the Ensembl repository, providing required testing and continuous integration. This project will bring the Nextflow VEP workflow inline with [nf-core standards](https://nf-co.re/docs/guidelines/pipelines/overview), providing greater usability for the community.

The [Ensembl VEP](https://github.com/Ensembl/ensembl-vep) is a widely used variant annotation tool capable of producing rich functional annotations for genomic variants. It has been part of different bioinformatics workflows. A Nextflow workflow already exists that leverages nextflow parallel processing capabilities (e.g., splitting VCFs, parallelizing chromosome analysis, and merging results), but it is not packaged as an nf-core pipeline with the community standards around modularity, container support, automated testing, documentation, and configuration profiles.

**Expected results**

- A repository containing the workflow following nf-core guidelines which needs to include –
- Required modules and workflows
- Nextflow configurations profile for different executor environments
- Easy-to-follow and standard documentation

- Publishing the workflow in nf-core

**Required knowledge**

- Strong Python programming skills
- Nextflow core concepts

**Desirable knowledge**

- Basic understanding of HPC environments
- Experience working with Ensembl VEP
- Familiarity with unit testing and CI/CD
- Familiarity with Groovy and scripting languages such as bash

**Learning outcomes**

Enhanced understanding of the structure and workflows required for production pipelines. Appreciation of community standards implementation and the generation of reliable, repeatable and reusable workflows.

**Difficulty**: Medium

**Length**: 175 hours

**Mentors**: [Syed Hossain](mailto:snhossain@ebi.ac.uk)

**Brief explanation**

Recent advances in single-cell foundation models and perturbation-driven datasets are bringing the concept of a “virtual cell” closer to reality. However, most current models remain siloed by modality (CRISPR screens, MAVE, scPerturb-seq) and lack a unifying layer that can integrate causal perturbation knowledge across data types.

In this project, the student will build a prototype perturbation-aware large language model (LLM) by fine-tuning an existing open-source model on curated perturbation datasets from the Perturbation Catalogue. The goal is not to train a foundation model from scratch, but to explore how LLMs can act as a knowledge-integration layer that connects genetic perturbations, variants, and single-cell responses.

The project directly supports the emerging “lab-in-the-loop” and scPerturb-seq Atlas concepts, where models guide experimental design and hypothesis generation by predicting cellular responses to unseen perturbations. The student will prototype workflows for:

- Encoding perturbation experiments into LLM-friendly representations
- Integrating multiple modalities (CRISPR screens, MAVE, scPerturb-seq)
- Evaluating how well an LLM can support reasoning over causal perturbation data

This will position the Perturbation Catalogue as a core resource for next-generation in silico perturbation modelling and virtual cell development.

**Expected results**

By the end of the project, the student will deliver:

- A curated multimodal training corpus derived from the Perturbation Catalogue, including:
- CRISPR screen summaries
- MAVE variant–effect annotations
- scPerturb-seq perturbation–response profiles

- A fine-tuned perturbation-aware LLM prototype capable of:
- Answering structured questions about perturbation effects
- Reasoning across modalities (e.g. linking variant effects to transcriptional responses)
- Supporting simple in silico perturbation queries (e.g. “What happens if gene X is knocked out in cell type Y?”)

- Benchmarking and evaluation framework, comparing:
- LLM-based reasoning vs simple baselines
- Performance across perturbation regimes (seen vs unseen genes, cell types, variants)

- A reproducible open-source pipeline, including:
- Data preprocessing scripts
- Fine-tuning notebooks/workflows
- Documentation for future contributors

- A short technical report and blog post describing how LLMs can support the “virtual cell” and lab-in-the-loop paradigms in perturbation biology.

**Required knowledge**

- Strong Python programming skills
- Basic machine-learning concepts (training, validation, overfitting)
- Familiarity with deep-learning frameworks (PyTorch preferred)
- Experience working with structured biological data (e.g. CSV/TSV, JSON, HDF5)
- Background in computational biology or bioinformatics
- Familiarity with single-cell data (scRNA-seq, perturb-seq concepts)
- Experience with large language models and fine-tuning (e.g. HuggingFace ecosystem)

**Desirable knowledge**

- Knowledge of causal inference or perturbation biology
- Basic understanding of cloud or HPC environments

**Difficulty**: High

**Length**: 350h

**Mentors**: [Alexey Sokolov](mailto:alexey@ebi.ac.uk), [Kirill Tsukanov](mailto:ktsukanov@ebi.ac.uk), [Aleksandr Zakirov](mailto:zakirov@ebi.ac.uk)

**Brief explanation**

The Ensembl GraphQL service can be used to access information about genes, transcripts, assemblies and associated metadata held by Ensembl.This project will be conducted in collaboration with the Ensembl Outreach and Platform team to develop a freely available hands‑on, workshop teaching participants how to query Ensembl data using GraphQL. The workshop will include modules covering an introduction to GraphQL, schema exploration, query building, and techniques for error handling and debugging. As part of the project, the participant will create documentation with example prompts that can be used with AI assistants (e.g. Gemini) to help generate valid GraphQL queries or assist in debugging scripts. The workshop will be designed to be reproducible and easily extendable, enabling integration of future Ensembl GraphQL resources.

This experience will provide a mentored learning pathway focusing on practical software and data science skills, preparing the contributor for future open-source work.

**Learning objectives**

- Understand the structure and functionality of Ensembl core GraphQL API, including its schema and queries.
- Workshop design and educational resource development.
- Gain foundational understanding of key Ensembl data entities such as genes, transcripts, assemblies and species.

**Aims**

- Develop a teaching kit, including presentation slides, Jupyter notebooks with real world examples of exporting genomic data via Ensembl GraphQL.
- Document all components comprehensively so that another trainer can run the workshop with minimal setup or additional development.
- Design structured AI prompts that help participants use an AI assistant to construct accurate and efficient GraphQL queries.

**Expected results**

- A robust and interactive Ensembl GraphQL training resource featuring example code, helper functions, and debugging documentation.
- A transferable design adaptable to other Ensembl GraphQL resources in the future.

**Required knowledge**

- Intermediate programming skills (preferably in Python), including HTTP requests, JSON handling, and basic packaging or testing workflows.
- Experience in interacting with AI models (e.g. Gemini) including prompt design.

**Desirable skills**

- Core genomics knowledge, such as genes, transcripts, variants, and species identifiers, sufficient to interpret Ensembl data.
- Basic understanding of GraphQL, including schemas, queries, arguments, nesting, and executing GraphQL endpoints with POST requests

**Difficulty**: Medium

**Length**: 175 hours

**Mentors**: [Aleena Mushtaq](mailto:amushtaq@ebi.ac.uk), [Bilal El Houdaigui](mailto:bilal@ebi.ac.uk)

**Brief explanation**

Accurate metadata is essential for interpreting and comparing microbiome datasets. Despite its importance, it often remains incomplete or inconsistent in life-science public repositories. [Trapiche](https://github.com/Finn-Lab/trapiche) is a metadata classification tool for microbiome datasets that combines microbial composition (taxonomic) profiles with free text from project and sample descriptions. The base models can be repurposed for other classification tasks, but users currently lack a simple, standardised way to evaluate model quality and interpret results.

This project will develop an evaluation and reporting toolkit for Trapiche that automatically produces standardised metrics and human-readable reports. A key focus will be to monitor and compare the contribution of both input components: the taxonomic profiles and the text features. This will allow users to understand not only how well models perform, but also how each input type influences the predictions.

The resulting module will shorten development cycles for new microbiome classification tasks and support more reliable, comparable, and reusable life-science datasets.

**Expected results**

- A Python evaluation module that computes standard classification metrics (accuracy, precision, recall, F1-score, confusion matrix).
- Support for component-aware evaluation, reporting performance for text-only, taxonomy-only, and combined inputs.
- An automated report generator producing HTML or PDF summaries with metrics and plots.
- Documentation covering installation, usage, and interpretation of results.
- A walk-through Jupyter notebook demonstrating the use of the module.

**Required knowledge**

- Proficiency in Bash and Python.
- Experience with data processing using Pandas and NumPy.
- Familiarity with machine learning evaluation concepts and Scikit-learn metrics.
- Experience with data visualisation tools such as Matplotlib or similar.

**Desirable knowledge**

- Familiarity with version control (Git) and collaborative coding workflows
- Fundamentals of metagenomics and its applications
- Experience with natural language processing (NLP) methods

**Difficulty**: Medium

**Length**: 175 hours

**Mentors**: [Santiago Fragoso](mailto:fragoso@ebi.ac.uk), [Mahfouz Shehu](mailto:mahfouz@ebi.ac.uk)

**Brief explanation**

In this project, we aim to develop a prototype method for the generation of [sequence similarity networks](https://pubs.acs.org/doi/full/10.1021/acs.biochem.8b00473) (SSNs) for the MGnify Proteins database to help enable graph-based analyses of its sequence space. Using tools like [MMseqs2](https://github.com/soedinglab/MMseqs2) to compute pairwise sequence similarities, and Python graph libraries like NetworkX, a collection of representative SSNs will be generated for a small subset of the database of ~10 million proteins. The nodes of these networks will then be annotated with relevant MGnify metadata, starting with biome of origin. Finally, we will generate visualisations of these annotated SSNs to be displayed on the MGnify Proteins website using modern graph rendering tools like [Cytoscape](https://cytoscape.org/) and [Cosmograph](https://cosmograph.app/).

The latest release of the[ MGnify Proteins Database](/ideas/genome-assembly-and-annotation/metagenomics-proteins) contains over 2.4 billion non-redundant protein records including relevant metagenomics metadata. The visualisation of sets of protein sequences using SSNs is a common approach for extracting novel insights about protein-protein relationships, including functional, structural, and evolutionary hypotheses. Facilitating the generation of SSNs for the MGnify Proteins database would therefore be a significant contribution to open metagenomics science.

**Expected results**

- Develop a prototype workflow for generating SSNs for a given set of protein sequences using MMSeqs2
- Apply the latter workflow to a workable subset of the MGnify Proteins representative clusters to generate SSN representations
- Annotate generated SSNs with biome of origin
- Generate visualisations for all biome-annotated SSNs

**Required knowledge**

- Proficiency in Bash and Python
- Comfortable with using a Unix shell
- Basic git skills for version-control of work

**Desirable knowledge**

- Familiar with graph theory and network analysis concepts
- Experience with Python graph libraries like NetworkX
- Experience with workflow design and implementation

**Difficulty**: Beginner

**Length**: 350 hours

**Mentors**: [Christian Atallah](mailto:chrisata@ebi.ac.uk)

**Brief explanation**

Interactive data science web applications often need to support efficient search over large structured datasets, while keeping latency low and avoiding heavy server-side infrastructure. At large scale, this can be done in several ways, for example: 1) precompute an index file to accompany the dataset; 2) load records into a server-side indexed database behind a REST API; or 3) index and query data in the browser (e.g. using IndexedDB).

In bioinformatics, annotating (meta)genomes involves tagging regions of genomic sequences with feature details (like the location of a gene and its function). Computational pipelines produce these annotations and output standardised formats like GFF (General Feature Format) – effectively a TSV file for genomics. There are various ways to interrogate and visualise these annotations, including genome browsers like [JBrowse](https://jbrowse.org/jb2/). A frequent use case is to search the annotations by a query such as a function category label, and then browse to the matching locations in the sequences. Like any database, this becomes challenging for large datasets – in particular the metagenomes we analyse in [MGnify](https://www.ebi.ac.uk/metagenomics) become very large.

The objective of this project is to try a mixed approach: convert GFF (and other) files into a SQLite database using [gffutils](https://daler.github.io/gffutils/database-import.html), creating extra database indexes at the same time. We would like to distribute this feature SQLite to the browser, and query it using the [sqlite3 WASM](https://sqlite.org/wasm/doc/trunk/index.md) in-browser capabilities to both display a feature search interface and pass data to JBrowse (perhaps via a new [plugin](https://github.com/GMOD/jbrowse-plugin-template)).

**Expected results**

- A python script that uses gffutils to produce a suitably indexed SQLite database from a large metagenome GFF genomic feature file.
- Unit tests for the script.
- A react javascript component that queries the SQLite file client-side, using sqlite3 WASM’s javascript API
- Ideally: the ability to partially read the SQLite file from a remote server, using HTTP Range requests
- Demonstrated integration with the JBrowse viewer, e.g. via a plugin

**Required knowledge**

- Python
- Python testing frameworks e.g. pytest
- Javascript:
[React.js](http://react.js) - Relational database concepts (e.g. SQL)
- Version control

**Desirable knowledge**

- Use of WASM (Web Assembly)
- Database indexing
- Bioinformatics file formats

**Difficulty**: Medium

**Length**: 175 hours

**Mentor**: [Vikas Gupta](mailto:vikasg@ebi.ac.uk)

**Brief explanation**

MGnify’s web interfaces are built on a large and evolving API surface, with complex data relationships and established frontend patterns. Translating Figma designs into production-ready UI code currently requires significant manual effort, particularly when wiring components to backend endpoints and maintaining consistency across the application.

MGnify already has a prototype **(Model Context Protocol) server** that exposes tools backed by existing API endpoints. However, coverage is currently partial and focused on selected workflows.

This project proposes **extending and integrating an existing MCP server prototype** with the **Figma API**, enabling a design- and API-aware pipeline that assists developers in generating frontend components that are:

- Grounded in authoritative Figma design artifacts (Visual Framework Assets)
- Aware of MGnify’s API surface and response schemas
- Aligned with existing frontend conventions, dependencies, and coding patterns

The system will act as **developer-assist infrastructure**, reducing repetitive boilerplate work and accelerating the design-to-implementation cycle while preserving full human control.

**Expected results**

By the end of the project, the student will deliver:

End-to-end proof of concept

- Demonstrate generating a new or updated MGnify UI page (e.g. a detail or results page) from:
- A Figma design
- MCP-exposed API context

- An integrated MCP server using a Client Side LLM Chat interface e.g Claude Desktop

**Learning outcomes**

Through this project, the student will gain experience in designing and implementing production-grade developer tooling that integrates design systems, APIs, and modern web frameworks. Specifically, the student will learn to:

- Work with large, real-world APIs
- Understand and extend an existing MCP server exposing a complex, evolving API surface
- Reason about API schemas, relationships, pagination, and error handling
- Design abstractions that remain stable as backend APIs evolve
- Learn to integrate with external APIs
- Responsibly build AI assisted developer tools

**Required knowledge**

- JavaScript/TypeScript, Python
- Experience with modern frontend frameworks (React preferred)
- REST APIs and JSON schema interpretation
- Git and collaborative software development workflows

**Desirable knowledge**

- Familiarity with design systems and component libraries
- Experience with Figma or design-to-code tooling
- Backend development experience (Node.js or Python)
- Interest in developer tooling and automation
- Exposure to scientific or data-heavy web platforms

**Difficulty**: Medium

The project involves real-world system integration and design decisions, but is well-scoped and suitable for a student with solid web development fundamentals.

**Length**: 175 Hours

**Mentors**: [Mahfouz Shehu](mailto:mahfouz@ebi.ac.uk)

**Brief explanation**

The BioSamples database at EMBL-EBI provides a central repository for the storage, validation, and retrieval of biological sample metadata across a wide range of life science domains. BioSamples plays a critical role in ensuring that sample descriptions are structured, standards-compliant, and reusable across downstream archives such as ENA, ArrayExpress, and others.

Despite the availability of REST APIs for sample submission, validation, and search, these interfaces are not directly accessible to modern AI agents or large language model (LLM)–based systems, which require explicit schemas, deterministic interactions, and well-defined tool boundaries. As a result, the use of AI for assisting users in preparing high-quality BioSamples submissions or performing structured sample discovery remains limited.

This project aims to design and implement a **BioSamples MCP server** that exposes a carefully selected subset of BioSamples submission and search functionality through the **Model Context Protocol (MCP)**. The system will enable AI agents to interact with BioSamples in a safe, structured, and reproducible manner, reducing metadata errors while improving usability for submitters and data consumers.

The project focuses on two complementary capabilities:

**AI-assisted sample submission**from plain-text descriptions, with interactive clarification and validation against BioSamples checklists.**Natural-language-driven sample search**, converting free-text queries into structured BioSamples search requests.

By leveraging MCP’s explicit tool schemas, input/output contracts, and error semantics, the project prevents hallucinations, enforces metadata correctness, and ensures that all responses are traceable to authoritative BioSamples data sources.

The project is intentionally scoped to be beginner-friendly, requiring limited domain-specific bioinformatics knowledge, and emphasizes software engineering, API design, schema validation, and AI-tool integration rather than biological interpretation.

**Project objectives**

The primary objectives of the project are to:

- Expose BioSamples submission and search functionality as MCP-compatible tools
- Enable AI agents to assist users in creating valid, checklist-compliant BioSamples metadata
- Provide deterministic, explainable responses grounded in BioSamples APIs
- Demonstrate interactive clarification workflows for incomplete or invalid metadata
- Establish a reusable MCP-based foundation that can be extended to other EMBL-EBI data resources

**Scope and functionality**

1. AI-Assisted BioSamples Submission

The system will allow users to describe a biological sample using **plain natural language**, for example:

“Human liver biopsy collected in London in 2023 from a patient with cirrhosis.”

The MCP server, in combination with an LLM-based agent, will:

- Extract candidate metadata fields from the text
- Map extracted information to BioSamples attributes
- Validate the resulting sample against a selected BioSamples checklist
- Detect missing mandatory attributes (e.g. organism, material, collection date)
- Detect missing or incomplete spatiotemporal metadata
- Prompt the user with explicit clarification questions when required information is missing
- Produce a fully structured BioSamples sample representation once all requirements are satisfied

The final output will be a validated, submission-ready BioSamples sample object, with all validation decisions and user interactions explicitly traceable.

2. Natural-Language BioSamples Search

The project will also support **plain-text search queries**, such as:

“Human blood samples collected in Europe after 2020 related to diabetes.”

The system will:

- Parse the free-text query into structured search criteria
- Translate these criteria into BioSamples-compatible search filters
- Execute the search via BioSamples APIs
- Normalize and summarize the returned results into a consistent, human-readable format
- Return accession identifiers and key metadata fields for downstream exploration

This enables AI agents to act as structured discovery interfaces while preserving the determinism and correctness of the underlying BioSamples queries.

**Expected results**

By the end of the project, the following deliverables are expected:

- A near production-ready MCP server exposing a subset of BioSamples submission and search APIs
- Demonstrations of:
- AI-assisted, checklist-aware BioSamples submissions
- Interactive clarification workflows for incomplete metadata
- Natural-language-driven BioSamples search via MCP

- Deterministic, auditable responses fully backed by BioSamples APIs
- A scalable MCP-based architecture that can be extended to additional checklists or EMBL-EBI resources

**Advanced capabilities (optional / stretch goals)**

Depending on time and interest, the project may additionally explore:

- Composing multiple BioSamples operations into a single logical workflow (e.g. validate → clarify → submit)
- Normalizing heterogeneous BioSamples responses into a unified internal representation
- Rate-limit-aware request handling and response caching
- Clear error categorization (validation errors vs. system errors vs. user input issues)
- Multi-turn conversational state management for submissions spanning multiple interactions

**Documentation requirements**

The project will include comprehensive documentation covering:

- System architecture and design decisions
- MCP tool definitions and schemas
- Validation and clarification workflows
- Example AI agent interactions for submission and search
- Limitations, assumptions, and potential extensions

**Required knowledge**

- Strong Java or Python programming skills
- REST APIs, HTTP, and JSON
- Software architecture and modular design
- Schema definition and validation
- Basic understanding of metadata modeling

**Desirable knowledge**

- Familiarity with BioSamples or similar metadata repositories
- Experience with MCP or LLM tool/function calling
- API performance optimization and caching strategies
- Experience with containerization (Docker) or CI/CD pipelines

**Difficulty**: Medium

**Length**: 175 hours

**Mentor**: [Dipayan Gupta](mailto:dgupta@ebi.ac.uk)

To be successful with your application, it is important to demonstrate the following:

**1. An understanding of the major aims of the project**

We do not expect contributors to have expert domain knowledge at the outset. However, some light background reading on the proposed technologies and underlying science will help you better understand the project context and goals.

**2. An ability to build on the project idea**

We provide a set of project ideas as starting points. Strong applications go beyond simply restating the description and instead bring new ideas, questions, or alternative approaches that build on the initial outline.

**3. Clear and appropriate communication with mentors**

Engaging with potential mentors ahead of submitting an application is key to success. Mentors are available to answer questions and provide guidance, but they will not write your application for you.

If you need clarification or additional background, communicate this clearly and in good time. Be concise and specific in your questions. Last-minute requests for substantial feedback are generally a sign of poor planning.

**4. A realistic and well-structured timeline**

Although GSoC timelines are flexible and can sometimes be extended, the programme is still relatively short. A good application includes:

- clearly defined milestones
- deliverables aligned with GSoC evaluation periods
- a workload that is realistic given your other commitments

We value sustainable working practices and do not expect contributors to work excessive hours. Availability and constraints should be clearly stated and discussed with mentors.

**5. Genuine enthusiasm and engagement**

Demonstrated interest in the project, the technologies involved, and working with EMBL-EBI teams goes a long way. Enthusiastic and engaged contributors tend to have more productive mentor relationships and more successful projects.

The steps below provide a general guide to submitting a strong application. While we publish a list of suggested projects, contributor-proposed ideas are also welcome.

**Review the project ideas**Review our GSoC project ideas page to explore available projects and their associated technologies.**Select a project of interest**Read the description carefully and do some light background research if needed.**Get in touch with us**Contact our GSoC helpdesk ([helpdesk@ensembl.org](mailto:helpdesk@ensembl.org)) with the subject line**“GSoC”**. Please include:- a short CV or link to relevant experience
- a brief explanation of your interest in the project
- any specific questions you may have

- If you are proposing your own project idea, include a short description and the technologies you expect to use so we can assess mentor availability.
**Draft your application early**Prepare a first draft well ahead of the deadline and share it with your mentor(s) or via the helpdesk for feedback.**Incorporate feedback and finalise**Use the feedback provided to refine your proposal, then submit the final version once it has been reviewed.

GSoC contributors at EMBL-EBI are treated as members of their project teams. Contributors typically engage through:

- Slack and mailing lists
- GitHub issues and pull requests
- regular meetings with mentors

Where time zones permit, contributors may also attend team or section-wide meetings and may be invited to present their work during the programme.

Good luck with your application. GSoC has consistently been a rewarding experience for both contributors and mentors at EMBL-EBI, and we look forward to supporting contributors in developing skills, gaining domain knowledge, and contributing to open scientific software.

**GSoC Resources**

**EMBL-EBI resources and services**We develop and maintain a wide range of open biological data resources, including:

[Ensembl](https://www.ensembl.org)and the[beta Ensembl website](https://beta.ensembl.org)[European Nucleotide Archive (ENA)](/ideas/genome-assembly-and-annotation/ena)[BioStudies](/ideas/genome-assembly-and-annotation/biostudies)[MGnify (Metagenomics)](https://www.ebi.ac.uk/metagenomics)

**Code repositories**

- Ensembl:
[https://github.com/Ensembl](https://github.com/Ensembl) - ENA:
[https://github.com/enasequence](https://github.com/enasequence) - BioStudies:
[https://github.com/EBIBioStudies](https://github.com/EBIBioStudies) - MGnify:
[https://github.com/EBI-Metagenomics](https://github.com/EBI-Metagenomics)

Date: 16 - 31 Mar 2026

Location: Virtual

Venue: Online
