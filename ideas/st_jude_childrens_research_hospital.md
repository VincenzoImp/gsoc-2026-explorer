# St. Jude Children's Research Hospital — Project Ideas

**Source:** https://gist.github.com/claymcleod/ee8e62831a4975cba2032d888bb52080
**Scraped:** 2026-02-22T23:28:47.625502

---

# St. Jude Children's Research Hospital - Google Summer of Code 2026

Welcome to St. Jude's Google Summer of Code 2026 homepage! With any questions, feel free to reach out to us via email at clay.mcleod@stjude.org and stephanie.sandor@stjude.org. Please include `[GSoC]` in the subject line.

If you do apply, please be sure to use our [Application template](#application-template)!

## Table of Contents

- [Background](#background)
- [Projects](#projects)
  - [Python bindings for Sprocket's WDL tooling](#python-bindings-for-sprockets-wdl-tooling)
  - [Plugin system for custom execution backends in Sprocket](#plugin-system-for-custom-execution-backends-in-sprocket)
  - [Type-safe genomic interval library for `omics`](#type-safe-genomic-interval-library-for-omics)
  - [SIMD-accelerated sequence alignment for `omics`](#simd-accelerated-sequence-alignment-for-omics)
- [We're open to other, relevant ideas](#were-open-to-other-relevant-ideas)
- [Application template](#application-template)

## Background

Our projects are centered around changing how genomics analysis is done at scale. In an effort to advance cures for pediatric catastrophic diseases as quickly as possible, St. Jude has been sharing critical research data with the biomedical community for about 8 years now (see the [St. Jude Cloud paper](https://pubmed.ncbi.nlm.nih.gov/33408242/) for more details). This endeavor has led to a great deal of experience in understanding the challenges of sharing this data with the broader academic community. To address those issues, we recently started our own workflow execution engine written in Rust called **Sprocket** aimed at enabling genomic analyses at petabyte-scale. Though we're focused on genomics, we think that Sprocket can be used for nearly all scientific domains.

Sprocket is built on top of the open Workflow Description Language ([github.com/openwdl](https://github.com/openwdl)), of which we have multiple people on the governance committee, and alongside the execution engine we're building, there are also many language design problems we're tackling such as building our own lexer, parser, abstract syntax tree, concrete syntax tree, linter, validation tools, language server protocol, VSCode plugin, formatter, and documentation generator. We're also building foundational Rust libraries for genomics through our [`omics`](https://github.com/stjude-rust-labs/omics) project, which provides primitives for coordinates, molecules, and variations.

Last year, our GSoC contributor [Vaibhav Raj](https://github.com/dead8309) made substantial contributions to the Sprocket ecosystem, including 60+ commits implementing the core LSP features (auto-completions, semantic highlighting, go-to-definition, find-references, hover, and rename support), new linting rules, and critical bug fixes.

You can find out more by navigating to the links below:

- **https://github.com/stjude-rust-labs/sprocket**. The user-facing command line tool that brings all of the functionality together. Check out [sprocket.bio](https://sprocket.bio) for documentation.
- **https://github.com/stjude-rust-labs/sprocket/tree/main/crates**. The core `wdl-*` crates for the project, located in the Sprocket repository. These crates contain functionality covering the lexing, parsing, abstract syntax tree, concrete syntax tree, linting, validation, language server protocol, formatting, and documentation generation.
- **https://github.com/stjude-rust-labs/crankshaft**. A headless workflow execution engine. The `crankshaft` crate(s) contain the language-agnostic plumbing code for submitting jobs to backend execution platforms (local, Docker, Cloud, HPC, etc).
- **https://github.com/stjude-rust-labs/omics**. Foundational Rust libraries for genomics, including primitives for coordinates, molecules, and variations.
- **https://github.com/openwdl/wdl**. Some projects may require interacting with or making suggestions to the Workflow Description Language. The linked repository here includes the entire specification that you can browse to get a sense of how it works.
- **https://github.com/stjude-rust-labs**. The organization as a whole. We encourage you to check out the other projects we're working on here—particularly as it relates to other projects you might want to propose.

## Projects

### Python bindings for Sprocket's WDL tooling

**Length:** 175 hours | **Difficulty:** Medium

#### Description

Python is the dominant language in bioinformatics, yet Sprocket's powerful WDL tooling (lexer, parser, linter, validator) is only accessible from Rust. This project creates Python bindings using PyO3 (or comparable), enabling Python developers to programmatically parse, lint, and validate WDL documents. This opens the door to a vibrant ecosystem of Python-based WDL tooling—IDE plugins, CI integrations, and analysis scripts—without reimplementing the core logic we've built up in Sprocket.

#### Outcomes

- A `sprocket-py` package exposing lexing, parsing, and linting APIs *(Project, Python developers)*
- Published to PyPI for easy installation *(Project, end users)*
- *(Stretch Goal)* Workflow execution APIs exposed to Python *(Project, stretch goal)*
- Experience with Rust FFI, PyO3 (or similar), and cross-language API design *(Contributor)*

#### Relevant Skills

Fluency in both Rust and Python. Experience with PyO3 or similar FFI tooling preferred but not required.

#### Potential Mentors

[Ari Frantz](https://github.com/a-frantz) w/ support from [Clay McLeod](https://github.com/claymcleod).

#### Proposal Advice

First, explore PyO3's (or similar) documentation and build a minimal Rust-to-Python binding. Then examine the `wdl` crate structure to understand which types would be most valuable to expose. Consider: What would a Python user expect from `import sprocket`? Include your findings in your application. Justify why you chose your approach to this problem. What other ancillary deliverables will be needed for community adoption?

---

### Plugin system for custom execution backends in Sprocket

**Length:** 350 hours | **Difficulty:** Hard

#### Description

Sprocket currently supports several execution backends (Docker, TES, LSF+Apptainer, Slurm+Apptainer), but organizations often have unique infrastructure requirements—currently unsupported HPC schedulers, cloud platforms, or specialized compute environments. This project researches and implements a plugin architecture that allows users to develop their own execution backends without modifying Sprocket's core. The contributor will study existing solutions (including Nextflow's plugin system), evaluate approaches for plugins in a compiled Rust world (WASM, dynamic libraries, RPC), and design an extensible backend interface.

#### Outcomes

- A plugin interface for execution backends with clear documentation *(Project, plugin authors)*
- At least one example plugin demonstrating the architecture *(Project, reference implementation)*
- Plugin loading and configuration mechanism integrated into Sprocket *(Project, end users)*
- Deep understanding of systems programming, plugin architectures, and Rust *(Contributor)*

#### Relevant Skills

Strong Rust skills required. Experience with systems programming, dynamic loading, or plugin architectures preferred. Willingness to conduct substantial research and propose novel solutions is essential.

#### Potential Mentors

[Clay McLeod](https://github.com/claymcleod)

#### Proposal Advice

Start by examining how Nextflow handles plugins ([Nextflow Plugins documentation](https://www.nextflow.io/docs/latest/plugins/plugins.html)) and what extension points it offers. Then review Crankshaft's existing backend implementations to understand the current architecture. We've been considering several approaches: WebAssembly modules, subprocess-based plugins with JSON-RPC or similar transport, and dynamic shared libraries. Each has distinct tradeoffs around performance, portability, sandboxing, and language flexibility. **Your application should include a clear recommendation for which approach you believe is best and why**. We want to see your reasoning process and technical judgment, not just a summary of options.

---

### Type-safe genomic interval library for `omics`

**Length:** 350 hours | **Difficulty:** Hard

#### Description

Genomic interval operations are fundamental to bioinformatics pipelines, yet a persistent source of bugs is coordinate system mismatches—mixing interbase intervals (BED) with in-base intervals (VCF, GFF). This project builds a genomic interval library within the `omics` ecosystem that makes these bugs structurally impossible by leveraging Rust's type system. Intervals are parameterized by coordinate system at compile time, ensuring operations between incompatible systems won't compile. The library will support core overlap queries, full set algebra (union, intersection, difference, complement, merge), and streaming/iterator-based processing for large datasets.

#### Outcomes

- Type-safe interval types integrated with `omics::coordinate` *(Project, bioinformatics developers)*
- Efficient overlap queries using proven algorithms ([implicit interval trees](https://pubmed.ncbi.nlm.nih.gov/32966548/), [augmented interval lists](https://pubmed.ncbi.nlm.nih.gov/31150060/)) *(Project, pipeline authors)*
- Complete set algebra operations matching bedtools functionality *(Project, end users)*
- Streaming/lazy operations for memory-efficient processing of large datasets *(Project, large-scale analysis)*
- Deep understanding of genomic data structures and Rust type system *(Contributor)*

#### Relevant Skills

Strong Rust skills required. Familiarity with genomic coordinate systems and interval data structures preferred. Interest in leveraging type systems for correctness.

#### Potential Mentors

[Clay McLeod](https://github.com/claymcleod)

#### Proposal Advice

Start by reading the [omics-coordinate documentation](https://docs.rs/omics-coordinate) to understand the distinction between *interbase* (pointing to spaces between nucleotides) and *in-base* (pointing directly to nucleotides) coordinate systems—and why mixing them causes bugs. Review existing libraries like [rust-lapper](https://github.com/sstadick/rust-lapper), [coitrees](https://github.com/dcjones/coitrees), and [bedrs](https://lib.rs/crates/bedrs) to understand current approaches. Your proposal should explain how you'd leverage Rust's type system to prevent coordinate system mismatches at compile time.

---

### SIMD-accelerated sequence alignment for `omics`

**Length:** 350 hours | **Difficulty:** Hard

#### Description

Sequence alignment is fundamental to bioinformatics—comparing DNA, RNA, or protein sequences to find similarities, identify mutations, or infer evolutionary relationships. Modern CPUs offer SIMD (Single Instruction Multiple Data) instructions that can dramatically accelerate the dynamic programming algorithms at the heart of alignment. This project builds a SIMD-accelerated alignment module for the `omics` ecosystem, including developing foundational primitives (protein sequence types, amino acid representations), alignment infrastructure (scoring matrices, gap penalty models, CIGAR result types), and high-performance implementations of global and local alignments.

#### Outcomes

- Protein sequence primitives: amino acid types, protein polymers extending `omics::molecule` *(Project, library foundation)*
- Alignment infrastructure: scoring matrices, gap penalties, result types *(Project, core types)*
- SIMD-accelerated Smith-Waterman (local) and Needleman-Wunsch (global) implementations *(Project, core algorithms)*
- Integration with existing `omics::molecule` DNA/RNA types *(Project, ecosystem cohesion)*
- Benchmarks demonstrating performance against existing tools *(Project, community)*

#### Relevant Skills

Strong Rust skills required. Familiarity with SIMD intrinsics (AVX2, NEON) or willingness to learn. Understanding of dynamic programming and sequence alignment algorithms preferred.

#### Potential Mentors

[Clay McLeod](https://github.com/claymcleod)

#### Proposal Advice

Start by understanding Smith-Waterman and Needleman-Wunsch algorithms, then explore how SIMD parallelism accelerates them. Review [Block Aligner](https://github.com/Daniel-Liu-c0deb0t/block-aligner) ([paper](https://pubmed.ncbi.nlm.nih.gov/37535681/)) as a reference for SIMD techniques. Examine `omics::molecule` to understand the current sequence representations—note that protein types, scoring infrastructure, and alignment result types will need to be built as part of this project. Your proposal should outline the primitives you'd create, your approach to SIMD acceleration, and how the API would feel to end users.

---

## We're open to other, relevant ideas

We're also open to other ideas! Feel free to check out the [St. Jude Rust Labs organization](https://github.com/stjude-rust-labs) to see what we're working on. In particular, ideas using the [`omics`](https://github.com/stjude-rust-labs/omics) library and the [`chainfile`](https://github.com/stjude-rust-labs/chainfile) library would be really cool to see. Last, if you do plan to submit your own idea, please discuss them with us briefly during the discussion period before submitting an application—we don't want you to do a lot of work for an idea that's unlikely to be selected!

## Application template

Please use this application template when submitting your proposal.

**Note:** We do **not** require prior contributions to Sprocket or any St. Jude Rust Labs repository before applying.

1. **Project Title.** Give a single sentence title to your project. You can use the existing project titles above or tweak them based on your own interests/ideas.

2. **Abstract (~4-6 sentences).** Describe the big picture of what you plan to accomplish during this project. You can feel free to reuse ideas or language that we used above—just make sure you give a sense of what you want to accomplish underneath those broad headings.

3. **Project Description.** An unbounded project description. Feel free to talk through the details of how you prepared for submitting this application (did you follow any of our advice for each idea? How did that shape the way you think about the idea, etc) and any more detailed plans for how you plan to go about the project.

4. **Major Contributions.** A list of goals that you hope to accomplish by the end of the program. Use a bulleted list here, and be sure to include both (a) what the outcome is going to be and (b) the target audience of that outcome.

5. **Timeline.** Break down the work to achieve these major contributions into a timeboxed plan as it aligns to the GSoC timeline. We've provided a template here to get started.

| Period | GSoC Phase | What I'll aim to accomplish |
|--------|------------|----------------------------|
| May 1 - May 24 | Community Bonding Period | GSoC contributors get to know mentors, read documentation, get up to speed to begin working on their projects |
| May 25 - May 31 | Coding (Week 1) | |
| June 1 - June 7 | Coding (Week 2) | |
| June 8 - June 14 | Coding (Week 3) | |
| June 15 - June 21 | Coding (Week 4) | |
| June 22 - June 28 | Coding (Week 5) | |
| June 29 - July 5 | Coding (Week 6) | |
| July 6 - July 12 | Coding (Week 7) | *Midterm evaluation is July 6-10* |
| July 13 - July 19 | Coding (Week 8) | |
| July 20 - July 26 | Coding (Week 9) | |
| July 27 - August 2 | Coding (Week 10) | *Your plan should start to include thinking about documenting the final product around this point.* |
| August 3 - August 9 | Coding (Week 11) | |
| August 10 - August 16 | Coding (Week 12) | |
| August 17 - August 24 | Coding (Final week) | *Final submissions due August 17-24* |

6. **Time Period/Working Hours.** Let us know how much time you plan to spend on the project. Be sure to indicate both (a) how many hours you think the project will take (we're not looking for a complicated hourly breakdown—just if it's 175 hours or 350 hours as defined by the GSoC guidelines) and (b) roughly how many hours per week you plan to spend on the project.

7. **Name and GitHub Username.** Please share with us your name and the GitHub username with which you are going to do the work.

8. **Resume.** Please include a recent copy of a resume/CV.

9. **Code Review.** Please provide us with a link to a code sample that you feel particularly proud of and that demonstrates your abilities. This can be a PR that you made to an existing codebase or a brand new project that you created and worked on. The key is that we want the code to be completely yours (or, at least, it needs to be clear which parts you specifically did, like in the case of a PR you created).
