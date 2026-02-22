# DBpedia Hindi Chapter 2026: Fine-Tuning Indic Models for Hindi Relational Triple Extraction + Human-in-the-Loop Feedback — GSoC 2026

**Parent:** DBpedia — Project Ideas
**Source:** https://forum.dbpedia.org/t/dbpedia-hindi-chapter-2026-fine-tuning-indic-models-for-hindi-relational-triple-extraction-human-in-the-loop-feedback-gsoc-2026/4788
**Scraped:** 2026-02-22T23:28:47.607981

---

**Project Title:**

DBpedia Hindi Chapter 2026: Fine-Tuning Indic Models for Hindi Relational Triple Extraction + Human-in-the-Loop Feedback

**Description:**

The DBpedia Hindi Chapter aims to expand the multilingual depth of DBpedia by extracting structured relational triples (subject → predicate → object) from Hindi Wikipedia and integrating them into the DBpedia knowledge graph. While DBpedia’s existing extraction framework provides strong support for infobox-based triples, the extraction of relations from free text using neural and NLP-driven methods—particularly for Hindi—remains underdeveloped. As a result, a large portion of relational knowledge present in Hindi Wikipedia articles is not yet represented in structured form within DBpedia.

Previous efforts have shown clear limitations in current approaches. Triple extraction using LLMs or prompt-only methods often suffers from inconsistency and a lack of robustness across different linguistic contexts, while rule-based extractors such as IndIE alone are insufficient to capture the richness and variability of Hindi language constructions. Furthermore, the absence of an integrated human validation and correction mechanism prevents systematic improvement of training datasets and limits the ability to iteratively refine extraction models, ultimately affecting the quality and reliability of the resulting knowledge graph.

**## Goal**

This project proposes:

-
Fine-tuning a small language model (SLM) for reliable relational triple extraction from Hindi text, improving over current prompt-only and rule-based baselines.

-
Building a lightweight UI for human feedback on extracted triples, enabling iterative dataset improvement (via correction labels, edits) — crucial for error analysis, dataset curation, and future active learning.


This work supports the DBpedia extraction ecosystem and accelerates automated extraction methods for Hindi Wikipedia content, enhancing coverage, quality, and usability of the Hindi DBpedia chapter.

**# Material**

See Warm-up tasks.

Project size

This project is medium-sized (175 hours).

Impact

This project will directly enhance the DBpedia Hindi Chapter by improving the quality and coverage of relational triple extraction from Hindi Wikipedia. By fine-tuning a small language model and incorporating human-in-the-loop validation, it will produce more accurate, trustworthy triples suitable for DBpedia ingestion. The resulting open-source pipeline and feedback dataset will support sustainable growth of [hi.dbpedia.org](http://hi.dbpedia.org) and provide a reusable foundation for extending neural extraction methods to other low-resource languages in DBpedia.

Warm-up Tasks

- Read carefully DBpedia extraction framework, ontology, and existing Hindi DBpedia resources and review past GSoC work related to DBpedia Hindi and Indic information extraction.
- Explore Hindi BenchIE and understand its annotation schema and evaluation protocol and reproduce baseline results using prompt-based extraction and rule-based systems (e.g., IndIE and the GSoC25 pipeline).
- Analyze Hindi Wikipedia text characteristics relevant to relation extraction.
- Set up the training environment (HuggingFace, evaluation scripts, reproducibility configs).
- Run small-scale experiments with candidate SLMs (gemma3) on sample data.
- Sketch the feedback workflow and data schema for triplet validation and build a minimal prototype to display extracted triples and collect annotations.

These warm-up tasks will ensure early alignment with DBpedia goals, reduce onboarding time, and enable faster progress once the coding phase begins.

Mentors

Sanju Tiwari ([@tiwarisanju18](https://forum.dbpedia.org/u/tiwarisanju18)), Aditya Venkatesh, Debarghya Dutta, Ronak Panchal
