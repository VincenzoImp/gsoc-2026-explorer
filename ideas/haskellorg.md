# Haskell.org — Project Ideas

**Source:** https://summer.haskell.org/ideas.html
**Scraped:** 2026-02-22T23:28:47.603569

---

# GSoC 2026 Ideas

This is a list of ideas for contributors who are considering to apply to
Google Summer of Code 2026 for *Haskell.org*

## For project maintainers

Are you working on a Haskell project and you could use the help of a
contributor during the summer? Consider adding it as an idea here!
You can contribute ideas by sending a pull request to our
[github
repository](https://github.com/haskell-org/summer-of-haskell)
([example from 2024](https://github.com/haskell-org/summer-of-haskell/commit/63f360ed17cb1a1c1aeee9a14804b337e5169d14)).
If you just want to discuss a possible idea,
[please contact us](/ideas/haskellorg/contact).

What is a good idea? **Anything that improves the Haskell ecosystem is
valid**. The GSoC rules state that it must involve writing code
primarily (as opposed to docs).

Projects should be **concrete and small enough in scope** such
that they can be finished by the contributor. Past experience has
shown that keeping projects âsmallâ is almost always a good idea.

**Important changes since 2021/2022**:
In the past, GSoC projects were expected to take up the equivalent of full
time employment for a student. In 2021, this was reduced to
half time positions: students were expected to work around 175 hours in a 10
week period. Since 2022, contributors now have the choice between a larger
(around 350 hours) or a smaller project. Ideas should indicate in which
category they fall.

Projects should benefit as many people as possible â e.g. an improvement to GHC will benefit more people than an update to a specific library or tool, but both are acceptable. New libraries and applications written in Haskell, rather than improvements to existing ones, are also welcome.

## For students/contributors

[We have added some tips on writing a proposal here](/ideas/haskellorg/tips).
Please be aware that:

- This is not an all-inclusive list, so you can apply for projects not in this list and we will try our best to match you with a mentor.
- You can apply for up to two ideas (but only one can be accepted).

# Table of Contents

[Case split plugin](https://summer.haskell.org#casesplit)[Dynamic LSP capabilities](https://summer.haskell.org#dynamic-lsp-capabilities)[Goto dependency definition](https://summer.haskell.org#goto-third-party-deps)[Parquet for Haskell - A production-grade Apache Parquet reader/writer.](https://summer.haskell.org#parquet-support-for-dataframe)[Revive the support for type-class elaboration in Liquid Haskell](https://summer.haskell.org#revive-type-class-elaboration-in-lh)[UI Layout Library for Haskell - Declarative and dynamic layouts for 2D graphic frameworks](https://summer.haskell.org#ui-layout-library-for-haskell)[xeus-haskell - GHC/Wasm Backend Integration Prototype](https://summer.haskell.org#xeus-haskell-ghc-wasm)[xeus-haskell - Library Expansion and Packaging for MicroHs](https://summer.haskell.org#xeus-haskell-libraries)[xeus-haskell - Precompilation and Caching for Instant Startup](https://summer.haskell.org#xeus-haskell-performance)[xeus-haskell - Interactive Widgets for Haskell Notebooks](https://summer.haskell.org#xeus-haskell-widgets)

## Case split plugin[ð](https://summer.haskell.org#casesplit)

This project will extend the Haskell Ide, HLS, by introducing a new plugin, the case split plugin.

When writing some snippet of code on variables that can be one of a finite number of types, for example since it is an enum or algebraic datatype, we sometimes want to do different things, depending on the constructor of the variable.

See the simple code example below:

Here the programmer would like a completion option which inserts all the possible types of foo instead of having to type them out themselves. The case split plugin will then offer to complete the above code snippet as shown below:

This plugin should work on enums as well as algebraic data types and also work on incomplete `case`

expressions, i.e.Â in the above example if there was already an implementation for the case of type `A`

but the other possible types of foo would still need to be handled.
Unfortunately, implementing this functionality is complex, as it requires parsing existing code using exact printing.
The current idea is to use the [exact printing library](https://github.com/alanz/ghc-exactprint).

This project requires strong Haskell skills as the participant needs to gain a deep understanding of the above library, the GHC AST and the HLS codebase. Therefore they should have a good understanding of type level programming concepts such as type families. Ideally, the participant should already have experience with the GHC AST, otherwise this project will be very difficult to achieve within the timeframe.

Issue: https://github.com/haskell/haskell-language-server/issues/3525

Context:

- https://github.com/haskell/haskell-language-server/issues/2437
- https://github.com/haskell/haskell-language-server/pull/3338
- https://github.com/alanz/ghc-exactprint/pull/116

**Goals**

- New plugin
`hls-case-split-plugin`

- Support GHC 9.14.1
- Can casesplit on enum types
- Can casesplit on arbitrary algebraic datatypes

This project will only accept participants with prior contributions to HLS or GHC.

Mentors: TBD

Project size: 350hrs

Difficulty: Hard

## Dynamic LSP capabilities[ð](https://summer.haskell.org#dynamic-lsp-capabilities)

A [capability in LSP](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#capabilities), the Language Server Protocol describes the kind of features a Language Server offers to the client (e.g., VSCode). These capabilities are statically declared in HLS, i.e., on startup, we infer the language serverâs capabilities, based on the plugin handlers.
However, HLS is highly configurable!
It should be possible to enable or disable features at run-time, but since HLS can only declare capabilities on startup, the editor can request features even though they are disabled in HLS!

For example, [semantic tokens](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_semanticTokens) is one of HLSâ experimental features which is disabled by default.
The client will still request semantic tokens for documents, as HLS has previously advertised the feature, leading to error messages polluting the logs and confusing the user.
Similarly, the `hls-cabal-plugin`

implements a language server for `.cabal`

files within HLS, but the plugin supports noticably different features for `.cabal`

files than for `haskell`

files.
The result is that many LSP requests are rejected by HLS, confusing users.

This can be solved by introducing [dynamic capabilities](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#client_registerCapability), capabilities that can be registered and also de-registered by HLS at runtime if a feature is disabled.
Rather than sending all capabilities on startup, HLS can check its enabled plugins, and register a capability for individual HLS features on demand.

This project will improve the support for dynamic capabilities in [ lsp](https://github.com/haskell/lsp/), and then port HLS to use dynamic capabilities where available.
In

`lsp`

, there should be the possibility to automatically infer the dynamic capabilities, similarly to how we infer the [static capabilities on startup](https://github.com/haskell/lsp/blob/master/lsp/src/Language/LSP/Server/Processing.hs#L217). Ideally, dynamic capability registration remains opaque to HLS plugins and is entirely handled by the internal mechanisms of

[.](https://github.com/haskell/haskell-language-server/tree/master/ghcide)

`ghcide`

This project requires strong Haskell skills, especially with type level programming concepts such as type families. As the implementation will touch many places within HLS, prior knowledge of HLS, its rule system and plugin system is highly recommended.

Issue: https://github.com/haskell/haskell-language-server/issues/4084

**Goals**

`lsp`

can send and process dynamic registration of capabilities.`lsp`

can infer and send dynamic capability registration based on handlers`staticHandlers`

vs`dynamicHandlers`


`lsp-test`

can handle dynamic capability registrations.- HLS can register dynamic capabilities manually
- HLS can infer dynamic capabilities

This project will only accept participants with prior contributions to HLS or `lsp`

.

Mentors: fendor, TBD

Project size: 175hrs, the scope could be expanded to 350hrs

Difficulty: Medium

## Goto dependency definition[ð](https://summer.haskell.org#goto-third-party-deps)

Haskell-Language-Server (HLS) supports goto definition for locally implemented functions.
But, Haskellers often also want to know the implementation of functions when using a library from an external dependency.
This project will implement `goto dependency definition`

, allowing programmers to inspect the implementation of dependencies from the comfort of their Ide, without having to google them or find them on hackage.

GHC versions can produce [ .hie files](https://gitlab.haskell.org/ghc/ghc-wiki-mirror/-/blob/master/hie-files.md) at compilation time,
which contain detailed information, as well as the sources.
These files can be indexed, for example by

[, to provide source locations for third-party libraries, which can then be used by HLS for the âGoto Definitionâ feature.](https://github.com/wz1000/HieDb/)

`hiedb`

This project will require participants to work with the notoriously difficult GHC API in HLS.

This project already has a prototype implementation in [PR #3749](https://github.com/haskell/haskell-language-server/pull/3749).
However, before the PR can be finished, HLS needs to be taught to ignore files from dependencies, i.e., must not try to type check them, but rather only serve LSP requests from hiedb. The PRs [#4406](https://github.com/haskell/haskell-language-server/pull/4406) and [#4449](https://github.com/haskell/haskell-language-server/pull/4449) implement new rule types that shall ensure HLS never accidentally tries to load modules from dependencies.

Issue: https://github.com/haskell/haskell-language-server/issues/708

This project requires strong Haskell skills, especially with type level programming concepts such as type families. As the implementation will touch many places within HLS, prior knowledge of HLS, its rule system and plugin system is highly recommended.

This project will only accept participants with prior contributions to HLS.

Mentors: fendor, wz1000

Project size: 350hrs, 175hrs if experienced

Difficulty: Hard

## Parquet for Haskell - A production-grade Apache Parquet reader/writer.[ð](https://summer.haskell.org#parquet-support-for-dataframe)

Apache Parquet is the âinterchange formatâ for analytics in the modern data stack, so having a production-grade Parquet implementation in Haskell is what turns Haskell data tooling from a silo into something that plugs into how data is actually stored and moved in industry. Having a strong Parquet implementation benefits Haskell beyond âdata science librariesâ because it gives any Haskell project a modern, efficient, interoperable storage format for tabular and semi-structured data: fast column scans, good compression/encodings, and a widely-supported on-disk standard that other tools can immediately consume. In practice, this means Haskell apps can persist intermediate results, caches, feature stores, logs/telemetry aggregates in a format that scales and can be queried/validated with existing industry tools, instead of inventing bespoke binary formats or round-tripping through another language.

[ dataframe](https://github.com/mchav/dataframe) already ships a working Parquet reader and includes a growing Parquet implementation. This project makes Parquet a

**first-class, production-ready I/O format inside**, by:

`dataframe`

- hardening and extending the existing reader to handle more real-world files safely,
- implementing a streaming Parquet writer
- writing round trip tests for Parquet files
- documenting a clear support matrix and performance expectations (which will eventually be added to the
[Parquet implementation status page](https://parquet.apache.org/docs/file-format/implementationstatus/))

The work is spec-driven (Parquet file format + metadata + encodings) but deliberately scoped to ship high-quality improvements within the GSoC timeline.

The project is at least medium difficulty (~175 hours). Hardening the reader and shipping a writer with plain encoding is a moderately difficult task. It can be extended to a ~350 hour project if we extend the scope to supporting run length encoding and a streaming writer/reader.

**Mentorship**

- Michael Chavinda (mchav)
- Adithya Obilisetty (adithyaov)

## Revive the support for type-class elaboration in Liquid Haskell[ð](https://summer.haskell.org#revive-type-class-elaboration-in-lh)

#### Goals

Update the implementation of [Liquid Haskell](https://ucsd-progsys.github.io/liquidhaskell/) to reenable support for [type-class elaboration][].

#### Background

Liquid Haskell is a verification tool for Haskell programs. The programmer writes specifications for these programs, and Liquid Haskell checks if the programs actually meet the specifications.

Liquid Haskell analyzes the Core language of the GHC compiler, which allows it to work with many syntactic features of Haskell that are eliminated during desugaring. One exception to this is type classes, which require Liquid Haskell to associate type class and instance definitions with dictionaries as they materialize in Core.

There are tests in the testsuite which rehearse type-class support, but
some of them [have been disabled](https://github.com/ucsd-progsys/liquidhaskell/blob/92c0a7eeb93045ace8a83df311c51287dee056fc/tests/tests.cabal#L2601-L2608) after upgrades to GHC introduced
incompatibilities with the Liquid Haskell implementation. Specifically, the
tests in question are related to type-class elaboration.

This project is about surveying the support of Liquid Haskell for reasoning
with type classes, updating the implementation to make it work with the latest
GHC version, improving the documentation, and grooming the testsuite to
reenable and complete the failing tests. This is the [corresponding issue](https://github.com/ucsd-progsys/liquidhaskell/issues/2450)
in the Liquid Haskell repository.

#### Outcomes

The main outcomes are a pull request with the implementation, tests, documentation, and the reports on the insights discovered during the project in the corresponding issue of the repository.

A secondary outcome is a blogpost describing the experience and the results of the project.

#### Size & Difficulty

Project size should be near 175 hours. The project will require a fair amount of reading of existing Haskell code, and the GHC interfaces it uses. Familiarity with the verification mechanisms is not necessary a priori, though some user-level understanding of Liquid Haskell is going to be needed to write tests.

Difficulty: intermediate

#### Required Skills

- Read and write technical English
- Haskell programming basics

#### Project Mentor

- Facundo DomÃnguez (facundo.dominguez at tweag.io) comaintainer of Liquid Haskell

## UI Layout Library for Haskell - Declarative and dynamic layouts for 2D graphic frameworks[ð](https://summer.haskell.org#ui-layout-library-for-haskell)

Haskell has several low-level libraries/bindings for 2D graphics like
[sdl3-hs](https://projects.kylelukaszek.com/sdl3-hs/) and
[GLFW-b](https://hackage.haskell.org/package/GLFW-b).
Furthermore, there are interactive application frameworks
like [Gloss](https://github.com/benl23x5/gloss),
[Brillo](https://github.com/ad-si/Brillo),
[Diagrams](https://diagrams.github.io), and others.

However, they all share a common limitation: Developers must manually calculate positions and sizes for every UI element. This becomes tedious and error-prone as interfaces grow in complexity.

This project aims to create a **declarative layout library** for Haskell
that can be used with any 2D rendering backend.
The goal is to let developers describe *what* they want
(a row of buttons, a centered panel, a sidebar next to content)
rather than *where* each pixel goes,
transforming Haskellâs graphics libraries into viable foundations
for building real applications with proper user interfaces.

The implementation can take one of several approaches:

**Extend an existing Haskell layout library**[FULE](https://github.com/pschnapp/FULE)(Functional UI Layout Engine), an experimental library for positioning UI elements that already provides container types, centering, and a monadic API[gloss-relative](https://hackage.haskell.org/package/gloss-relative), which provides relative sizing and automatic resizing for Gloss.

This would involve hardening the library, adding missing layout primitives, and creating integrations and examples for popular rendering backends.

**Wrap an existing C layout engine**[Clay](https://github.com/nicbarker/clay), a high-performance library that provides flexbox-style layouts with microsecond performance.

This would involve creating Haskell FFI bindings and adapters for Haskell rendering libraries.

**Implement a new pure Haskell layout engine**inspired by flexbox/CSS layout algorithms. This provides the tightest integration with Haskell idioms and avoids FFI complexity, though it requires more implementation work.

Any approach should deliver:

- A declarative API for building layouts (rows, columns, padding, alignment, spacing)
- Support for common layout patterns (flexbox-style grow/shrink, fixed vs.Â flexible sizing)
- Integration with popular Haskell 2D graphics libraries
- Simple text measurement and wrapping support
- Documentation and examples demonstrating typical UI patterns

The project can be scoped as a small project (~175 hours) covering a minimal layout system with rows, columns, interactions (click, hover, etc.), and basic sizing.

It could also be extended to a ~350 hour project by adding floating/overlay elements, scroll containers, responsive layouts, advanced text layouts, etc.

**Mentorship**

- Adrian Sieber (ad-si)

## xeus-haskell - GHC/Wasm Backend Integration Prototype[ð](https://summer.haskell.org#xeus-haskell-ghc-wasm)

#### Project Context

As part of the **jupyter-xeus** organization,
[ xeus-haskell](https://github.com/jupyter-xeus/xeus-haskell) aims to provide a
ârun anywhereâ Haskell environment. While the current MicroHs backend is
optimized for size and speed in the browser, a GHC/Wasm-backed execution mode
would unlock the full power of the Haskell ecosystem (Hackage). This
research-intensive engineering project focuses on bridging the

`xeus`

C++
framework with the emerging GHC WebAssembly backend to support more complex
production workflows in the browser.#### Goals

**Proof of Concept:**Extend the C++ bridge (`mhs_repl.cpp`

) to route execution requests to a GHC/Wasm-compiled runtime.**Runtime Optimization:**Document and mitigate browser-specific constraints, such as bundle size, startup latency, and filesystem access.**Backend Interoperability:**Define a clean architecture to allow users to switch between the lightweight MicroHs and the full-featured GHC/Wasm backends.

#### Prerequisites

**Language:**Advanced Haskell (GHC extensions, FFI, and compiler internals).**Systems:**Proficiency in C++ (standard 14 or higher) for kernel-level integration.**WebAssembly:**Familiarity with Wasm runtimes, Emscripten, or the WASI standard.**Bonus:**Experience with GHCâs Javascript/Wasm backends or`xeus`

core development.

**Mentors:** [Masaya Taniguchi](https://github.com/tani)

**Project Size:** 350h (Large)

**Difficulty:** Hard

## xeus-haskell - Library Expansion and Packaging for MicroHs[ð](https://summer.haskell.org#xeus-haskell-libraries)

#### Project Context

[ xeus-haskell](https://github.com/jupyter-xeus/xeus-haskell) is an official
Jupyter kernel for Haskell, maintained under the

**jupyter-xeus**organization. It is based on

**xeus**, the native C++ implementation of the Jupyter protocol. By leveraging the MicroHs compiler,

`xeus-haskell`

provides a unique experience
that runs both natively (Linux, macOS, Windows) and directly in the browser via
WebAssembly (JupyterLite). This project aims to transition the kernel from a
proof-of-concept to a robust tool for data science and education by expanding
its library ecosystem.#### Goals

**Feasibility Study:**Identify high-impact libraries (Haskell 2010 subset) that can be realistically compiled under MicroHs.**Library Expansion:**Port and validate a priority set of libraries (e.g.,`containers`

,`mtl`

,`bytestring`

,`aeson`

) for the MicroHs backend.**Automated Packaging:**Integrate with`pixi`

,`conda-forge`

, and`emscripten-forge`

to automate CI/CD pipelines for both native and Wasm targets.**Educational Content:**Develop âGetting Startedâ notebooks that demonstrate these libraries in a zero-install JupyterLite environment.

#### Prerequisites

**Language:**Strong proficiency in Haskell (especially Haskell 2010 standards).**Tooling:**Familiarity with modern package management (Conda / Pixi).**Systems:**Basic understanding of CI/CD workflows (GitHub Actions).**Bonus:**Previous experience with the MicroHs compiler or contributing to`conda-forge`

.

**Mentors:** [Masaya Taniguchi](https://github.com/tani)

**Project Size:** 175h (Medium) / 350h (Large)

**Difficulty:** Medium

## xeus-haskell - Precompilation and Caching for Instant Startup[ð](https://summer.haskell.org#xeus-haskell-performance)

#### Project Context

A key value proposition of the **jupyter-xeus** project
[ xeus-haskell](https://github.com/jupyter-xeus/xeus-haskell) is its
zero-install accessibility via JupyterLite. However, loading libraries in a web
environment can introduce latency. This project focuses on developer ergonomics
and performance by implementing a precompilation and caching strategy. The goal
is to ensure that when a student or researcher opens a Haskell notebook, the
environment is ready for execution instantly.

#### Goals

**Artifact Caching:**Develop a mechanism to precompile MicroHs core modules and third-party libraries into portable, cacheable artifacts.**Pipeline Integration:**Automate cache generation within the`emscripten-forge`

and`conda-forge`

packaging workflows.**Performance Benchmarking:**Establish quantitative metrics to measure cold-start vs.Â warm-start latency and ensure a smooth user experience.

#### Prerequisites

**Language:**Comfortable reading Haskell and C++ code.**Tooling:**Experience with build systems (Make, CMake) and shell scripting.**DevOps:**Familiarity with GitHub Actions or other automation platforms.**Bonus:**Knowledge of compiler optimization techniques or file system caching strategies.

**Mentors:** [Masaya Taniguchi](https://github.com/tani)

**Project Size:** 175h (Medium)

**Difficulty:** Medium

## xeus-haskell - Interactive Widgets for Haskell Notebooks[ð](https://summer.haskell.org#xeus-haskell-widgets)

#### Project Context

Developed under the **jupyter-xeus** umbrella,
[ xeus-haskell](https://github.com/jupyter-xeus/xeus-haskell) already supports
rich display outputs (HTML, LaTeX, Markdown). This project will implement

**ipywidgets**compatibility, enabling truly interactive notebooks. By adding support for the Jupyter âcommâ protocol, you will allow users to create Haskell-driven GUI elementsâsuch as sliders, buttons, and dropdownsâthat can manipulate data visualizations in real-time.

#### Goals

**Protocol Implementation:**Implement Jupyter âcommâ messages for state synchronization between the Haskell kernel and the browser frontend.**Widget Library:**Build a developer-friendly Haskell DSL/library to instantiate and control standard widgets (Slider, Button, Text).**Interactive Demos:**Create curated notebooks demonstrating the power of interactive widgets combined with the`Display`

typeclass for teaching and data exploration.

#### Prerequisites

**Language:**Solid Haskell skills, specifically in state management and handling side effects.**Protocol:**Understanding of JSON-based network protocols or the Jupyter messaging spec.**Frontend:**Basic knowledge of HTML/CSS for widget rendering and styling.**Bonus:**Experience using`ipywidgets`

in Python or a similar interactive system in another language.

**Mentors:** [Masaya Taniguchi](https://github.com/tani)

**Project Size:** 175h (Medium) / 350h (Large)

**Difficulty:** Medium
