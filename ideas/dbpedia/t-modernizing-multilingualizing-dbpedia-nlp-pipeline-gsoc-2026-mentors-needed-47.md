# Modernizing & Multilingualizing DBpedia NLP Pipeline — GSoC 2026 ⚠️ mentors needed

**Parent:** DBpedia — Project Ideas
**Source:** https://forum.dbpedia.org/t/modernizing-multilingualizing-dbpedia-nlp-pipeline-gsoc-2026-mentors-needed/4786
**Scraped:** 2026-02-22T23:28:47.608270

---

I am Charitha, a third-year B.Tech student specializing in AI/ML and a new contributor to DBpedia.

Based on my recent contributions to the fact-extractor repository (multilingual TF-IDF fixes and Python 3 compatibility updates), I would like to propose a potential GSoC 2026 project idea focused on modernizing and multilingualizing DBpedia’s NLP pipeline.

Proposed scope:

Fully remove remaining hard-coded language assumptions in NLP components

Standardize language-aware preprocessing across extraction and ranking stages

Modernize legacy Python 2 style code to Python 3

Improve multilingual tokenization, stopword handling, and evaluation

Add basic automated tests for multilingual NLP components

The goal would be to make DBpedia’s extraction pipeline more robust, maintainable, and ready for multilingual expansion.

I would appreciate feedback on whether this aligns with DBpedia’s GSoC 2026 goals, and which components would be most impactful to focus on.

I have marked this post with ‘mentors needed’. You can still submit a project proposal without supervision, however it is quite rare that it will be accepted. Any mentor who is interested in this project will get in touch with you.

Below is a more concrete and DBpedia-specific reformulation of my project idea.

Description

This project focuses on modernizing and multilingualizing the DBpedia fact-extractor NLP pipeline, with particular emphasis on the text processing and ranking stages (e.g., TF-IDF-based verb and fact ranking).
Currently, parts of the pipeline rely on legacy Python 2 code and language-specific assumptions (such as hard-coded Italian stopwords), which limit extensibility and multilingual scalability.

Goal

Fully migrate the fact-extractor NLP components to Python 3

Remove language-specific hardcoding and make language handling configurable across the pipeline

Improve maintainability and extensibility for adding new languages and NLP components

Material

Existing DBpedia fact-extractor repository

DBpedia StopWords infrastructure

Multilingual Wikipedia dumps for testing

Python NLP tooling already used in DBpedia (regex-based processing, TF-IDF, etc.)

Project size(s)

Medium (175 hours): Python 3 migration + multilingual parameterization of text processing stages

Large (350 hours): Above, plus refactoring and documentation of the NLP pipeline, validation across multiple languages, and benchmarks

Impact

Improves long-term maintainability of DBpedia’s extraction framework

Enables easier onboarding of new languages

Reduces technical debt in a core DBpedia component used downstream by multiple projects

I would be happy to further narrow the scope if there are specific fact-extractor or MARVIN components you recommend focusing on.
