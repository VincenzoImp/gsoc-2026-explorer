# Boa — Project Ideas

**Source:** https://boajs.dev/roadmap
**Scraped:** 2026-02-22T23:28:47.577015

---

# Roadmap 2026

## Garbage Collector Redesign and Integration[](https://boajs.dev#garbage-collector-redesign-and-integration)

- Difficulty: Hard
- Duration: 350 hours
- Required Skills: Rust, memory management, data structures
- Preferred Skills: Garbage collection algorithms, language runtimes

### Description[](https://boajs.dev#description)

Boa currently uses a prototype garbage collector, with experimental work happening in the separate [Oscars repository](https://github.com/boa-dev/oscars). While functional, the GC architecture needs significant redesign to better support performance, maintainability, and future language features.

This project focuses on evaluating, refining, and integrating a production-ready garbage collector into Boa.

### Expected Outcomes[](https://boajs.dev#expected-outcomes)

- Analyze the current GC design and limitations
- Improve or redesign the GC architecture (e.g. tracing strategy, allocation model, rooting)
- Integrate the improved GC into Boa’s runtime
- Add stress tests and benchmarks for GC behavior
- Produce documentation explaining the design and trade-offs

### Possible Extensions[](https://boajs.dev#possible-extensions)

- Incremental or generational GC strategies
- GC-aware optimizations in the VM
- Tooling to visualize heap and GC activity

### Project Discussion:[](https://boajs.dev#project-discussion)

[Matrix Boa/GC](https://matrix.to/#/!ESLxDMqdSvKbprdiyg:matrix.org?via=matrix.org&via=rrogal.ski&via=t2bot.io)
[Matrix Boa/General](https://matrix.to/#/!ZBLAwGpYvzsLqZAZZg:matrix.org?via=matrix.org&via=t2bot.io&via=mozilla.org)

## Public API Audit and 1.0 Stabilization[](https://boajs.dev#public-api-audit-and-10-stabilization)

- Difficulty: Medium
- Duration: 175–200 hours
- Required Skills: Rust, API design
- Preferred Skills: SemVer, library maintenance, documentation

### Description[](https://boajs.dev#description-1)

Boa is approaching its 1.0 release. A key requirement for this milestone is ensuring that our public APIs are well-defined, intentional, and stable, as breaking changes become significantly more costly after 1.0. This project focuses on auditing Boa’s public API surface, identifying areas that may cause long-term maintenance or compatibility issues, and helping prepare the engine for a stable 1.0 release.

### Expected Outcomes[](https://boajs.dev#expected-outcomes-1)

- Identify and document all public-facing APIs (types, traits, functions, feature flags)
- Review APIs for stability, consistency, and long-term viability
- Propose improvements or refactors to reduce future breaking changes
- Help resolve or unblock remaining items needed for the 1.0 milestone
- Improve documentation around public APIs and versioning guarantees

### Possible Extensions[](https://boajs.dev#possible-extensions-1)

- Introduce tooling or CI checks to detect accidental public API changes
- Improve feature gating or visibility (pub vs pub(crate)) across the codebase
- Assist in defining Boa’s post-1.0 stability and deprecation policy

## JavaScript Engine Performance Improvements[](https://boajs.dev#javascript-engine-performance-improvements)

- Difficulty: Medium–Hard
- Duration: 175–350 hours
- Required Skills: Rust, profiling, algorithms
- Preferred Skills: Compiler or VM internals, benchmarking

## Open Issue:[](https://boajs.dev#open-issue)

[https://github.com/boa-dev/boa/issues/4524](https://github.com/boa-dev/boa/issues/4524)

### Description[](https://boajs.dev#description-2)

Performance is a core goal of Boa. While already competitive in many areas, there are clear opportunities to improve execution speed, memory usage, and startup time.

This project focuses on identifying performance bottlenecks and implementing targeted optimizations across the VM, bytecode execution, and runtime systems.

### Expected Outcomes[](https://boajs.dev#expected-outcomes-2)

- Much improved results on boajs.dev/benchmarks
- Identify high-impact performance bottlenecks
- Implement measurable optimizations (e.g. faster bytecode dispatch, improved data structures)
- Add or improve benchmarks to prevent regressions
- Document performance changes and results

### Possible Extensions[](https://boajs.dev#possible-extensions-2)

- Reduced allocation pressure and memory churn
- Improve documentation and tooling for profiling and benchmarking

### Project Discussion[](https://boajs.dev#project-discussion-1)

## ECMAScript Conformance and Spec Compliance[](https://boajs.dev#ecmascript-conformance-and-spec-compliance)

- Difficulty: Medium
- Duration: 175 hours
- Required Skills: Rust, reading specifications
- Preferred Skills: JavaScript engine internals

### Description[](https://boajs.dev#description-3)

Boa already performs well on ECMAScript conformance tests, but maintaining and improving compliance is an ongoing effort as the specification evolves.

This project focuses on closing remaining gaps, improving correctness in edge cases, and strengthening test coverage.

### Expected Outcomes[](https://boajs.dev#expected-outcomes-3)

- Identify areas where Boa diverges from the ECMAScript specification
- Implement missing or partially compliant features
- Improve or expand test coverage
- Reduce known test failures and inconsistencies
- Document tricky or non-obvious spec decisions

### Possible Extensions[](https://boajs.dev#possible-extensions-3)

- Focus on a specific ECMAScript feature set (e.g. async, modules, Intl groundwork)
- Improve error reporting and diagnostics for spec failures

## Developer Tooling and Engine Observability[](https://boajs.dev#developer-tooling-and-engine-observability)

- Difficulty: Medium
- Duration: 175 hours
- Required Skills: Rust, tooling, debugging
- Preferred Skills: Runtime diagnostics, profiling tools

### Description[](https://boajs.dev#description-4)

As Boa grows, better tooling is needed to understand and debug engine behavior. This project focuses on improving observability for developers working on the engine.

### Expected Outcomes[](https://boajs.dev#expected-outcomes-4)

- Improve logging and diagnostics in the VM and runtime
- Add optional tracing or debug modes
- Improve internal metrics (allocation counts, GC timing, bytecode execution stats)
- Document tooling for contributors and users

### Possible Extensions[](https://boajs.dev#possible-extensions-4)

- Debug-friendly execution modes
- Performance and memory visualization tooling
- Integration with existing Rust profiling tools
