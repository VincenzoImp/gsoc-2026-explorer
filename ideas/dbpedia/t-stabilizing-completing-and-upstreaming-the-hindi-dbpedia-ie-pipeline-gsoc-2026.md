# Stabilizing, Completing, and Upstreaming the Hindi DBpedia IE Pipeline — GSoC 2026 ⚠️ mentors needed

**Parent:** DBpedia — Project Ideas
**Source:** https://forum.dbpedia.org/t/stabilizing-completing-and-upstreaming-the-hindi-dbpedia-ie-pipeline-gsoc-2026-mentors-needed/4776
**Scraped:** 2026-02-22T23:28:47.608343

---

**> Stabilizing, Completing, and Upstreaming the Hindi DBpedia IE Pipeline**


DESCRIPTION

During GSoC 2025, a comprehensive Hindi Information Extraction (IE) pipeline was developed for DBpedia, covering SLM-guided triplet extraction, IndIE enhancement, link prediction, predicate linking to the DBpedia ontology, and SPARQL endpoint deployment. While the core functionality has been implemented and evaluated, several critical components remain unfinished or unmerged, preventing the pipeline from being production-ready and fully integrated into DBpedia’s main infrastructure.

This project focuses on completing, stabilizing, and upstreaming the Hindi IE pipeline developed in GSoC 2025. The work emphasizes finalizing pending technical components (notably type/isA predicate linking, mappings integration, and finetuning), improving robustness and reproducibility, cleaning overlaps across modules, and preparing the existing pull requests and infrastructure for merge into the main DBpedia repositories.

Rather than introducing an entirely new pipeline, the project consolidates and strengthens a substantial existing contribution, ensuring long-term usability, maintainability, and extensibility of Hindi DBpedia.


GOAL

-
Complete pending GSoC 2025 tasks, including:

-
Predicate linking for type (isA / rdf:type) relations, where objects are ontology classes rather than properties

-
Finalizing Hindi mappings via the DBpedia mappings UI

-
Optional finetuning of Gemma-3 using the existing filtered synthetic dataset

-
Improving error handling and logging across stages (IndIE, LLM-IE, predicate linking)

-
Ensuring reproducible runs using clean configuration, caching, and setup instructions

-
Reducing code duplication across IndIE, ReAct, and llm_IE modules

-
Prepare and upstream existing work by:

-
Cleaning and finalizing pending PRs (e.g., neural-extraction-framework#20, extraction-framework#776)

-
Aligning the GSoC25_H fork with DBpedia’s main repository structure

-
Enable production readiness by:

-
Preparing deployment-ready SPARQL setup for a permanent Hindi DBpedia endpoint

-
Documenting deployment, usage, and troubleshooting for maintainers and contributors

-
Lower the entry barrier for new contributors through clear documentation and well-defined extension points.



IMPACT

-
Immediate impact

-
Delivers a stable, merge-ready Hindi IE pipeline for DBpedia

-
Enables consistent extraction, ontology linking, and querying over Hindi Wikipedia

-
Community impact

-
Reduces technical debt accumulated across multiple GSoC cycles

-
Makes Hindi DBpedia easier to maintain and extend by future contributors

-
Sustainability

-
Improves reproducibility and robustness for low-resource language IE pipelines

-
Establishes a cleaner foundation for multilingual expansion beyond Hindi

-
Research & practice

-
Strengthens reproducible evaluation for SLM-based IE and hybrid rule/LLM pipelines

-
Improves ontology alignment for non-English knowledge graphs



WARM-UP TASKS

-
Clone and run the complete Hindi IE pipeline (GSoC25_H) end-to-end

-
Reproduce published results on the Hindi-BenchIE dataset and report deviations

-
Execute predicate linking for both property and type (rdf:type) relations and analyze failure cases

-
Identify and fix at least one concrete issue (bug, logging gap, or documentation flaw)

-
Submit a small but meaningful PR (documentation, error handling, or predicate linking improvement)



PROJECT SIZE

175 hours (Medium)


KEYWORDS

Information Extraction, Knowledge Graphs, Hindi NLP, DBpedia, Predicate Linking,

Ontology Alignment, Low-Resource Languages, Pipeline Stabilization, SPARQL, Reproducibility
