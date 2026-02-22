# Fortran-lang — Project Ideas

**Source:** https://github.com/fortran-lang/webpage/wiki/GSoC-2026-Project-ideas
**Scraped:** 2026-02-22T23:28:47.580071

---

<!-- This comment is not visible to the final document.

NOTE: Please update the Project Index if a project is added, removed or renamed.

-->

Welcome to the Fortran-Lang ideas page for contributors applying for Google Summer of Code (GSoC).
If you are interested in applying for GSoC, see the
[Contributor Instructions](/ideas/fortran-lang/gsoc-2026-contributor-instructions)
for more information on how to apply.

The list here is based on priorities identified by Fortran-Lang contributors and should inform you
about the state and direction of each project. If you are interested in an idea on this page, please
contact us on our [Discourse](https://fortran-lang.discourse.group/t/google-summer-of-code-2026/10674/2)
to ask any questions and get the latest information about the project idea.
Please read the existing discussion(s) in any linked issues.

The project ideas on this page are grouped by the repository.
Please familiarize yourself with each repository before exploring the ideas here.

We are not limited to the project ideas listed on this page.
If you have your own project idea that is not listed here, let us know.

Contacts for prospective mentors: [Mentors list](/ideas/fortran-lang/gsoc-2026-mentors)

## Project Index

- fpm - Fortran Package Manager
  - [Version Constraint Resolution](#version-constraint-resolution-fpm)
  - [Build Process Enhancements](#build-process-enhancements-fpm)
  - [Extended Testing Support](#extended-testing-support-fpm)
  - [Export build order and `compile_commands.json`](#export-build-order-and-compile_commandsjson-fpm)
  - [Support of external third-party preprocessors](#support-of-external-third-party-preprocessors)
- stdlib - Fortran Standard Library
  - [File system library](#file-system-library-stdlib)
  - [Library to work with OS processes](#library-to-work-with-os-processes-stdlib)
  - [Linear algebra and sparse matrices](#linear-algebra-and-sparse-matrices-stdlib)
  - [String to number conversion](#string-to-number-conversion-stdlib)
- LFortran
  - [Compile any Fortran code](#compile-any-fortran-code-LFortran)
  - [Compile neural-fortran using LFortran](#compile-neural-fortran-using-LFortran)
  - [Compile benchmarking code written in Fortran with LFortran and improving LFortran's performance on these benchmarks](#compile-benchmarking-code-written-in-fortran-with-lfortran-and-improving-lfortrans-performance-on-these-benchmarks-lfortran)
  - [Allow running Fortran in the browser](#allow-running-fortran-in-the-browser-lfortran)
  - [Implementation of features on the ASR and LLVM level](#Implementation-of-features-on-the-ASR-and-LLVM-level-lfortran)
  - [Other LFortran ideas](#other-lfortran-ideas-lfortran)
- fortls - Fortran Language Server
  - [MPI support](#mpi-support-fortls)
  - [Semantic highlighting and collapsable scopes](#semantic-highlighting-and-collapsable-scopes-fortls)
  - [Replace explicit LSP interface with pygls](#replace-explicit-lsp-interface-with-pygls-fortls)
- vscode-fortran-support - Modern Fortran for VS Code
  - [Python environment manager](#python-environment-manager-vscode-fortran-support)
  - [vscode integration with fpm](#vscode-integration-with-fpm-vscode-fortran-support)
- Other
  - [Standard Conformance Suite](#standard-conformance-suite)
  - [Coarray Fortran Framework of Efficient Interfaces to Network Environments (Caffeine)](#coarray-fortran-framework-of-efficient-interfaces-to-network-environments-caffeine)
  - [Get fortran-lang/minpack to be used in SciPy](#get-fortran-langminpack-to-be-used-in-scipy)
  - [Improving fastGPT: Making it Faster, Easier to Use, and More General](#improving-fastgpt-making-it-faster-easier-to-use-and-more-general)
  - [Fortran Graphics Library](#fortran-graphics-library)
  - [Improved generation of Fortran interfaces for PETSc](#improved-generation-of-fortran-interfaces-for-petsc)

-----

## Version Constraint Resolution (fpm)

The current decentralized package system in fpm allows dependencies to be fetched via a git repository URL. As part of this, a git tag or commit can be given to require a specific version of a dependency. There is however no way of specifying version compatibility requirements (_e.g._ `>= 1.0.0, <2.0.0`) and no way to resolve such requirements across a dependency tree.

This project will involve:

- Defining a manifest syntax for version compatibility matching
- Implementing support in fpm for solving a set of version compatibility constraints

A possible approach would be to interface with an existing satisfiability solver such as:

- [libsolv](https://github.com/openSUSE/libsolv):
  interface via `iso_c_binding` as a separate fpm package

__See also:__ existing options for version matching syntax:

- [conda](https://docs.conda.io/projects/conda-build/en/latest/resources/package-spec.html#package-match-specifications)
- [npm](https://docs.npmjs.com/about-semantic-versioning/)
- [cargo](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html)

__Expected outcomes:__ Implemented a working version constraint mechanism in fpm

__Skills preferred:__ Fortran programming, experience with one or more build systems

__Difficulty:__ Intermediate, 350 hours

__Mentors:__
Brad Richardson ([@everythingfunctional](https://github.com/everythingfunctional)),
Sebastian Ehlert ([@awvwgk](https://github.com/awvwgk)), Umashankar Sivakumar ([@usivakum](https://github.com/usivakum))


## Build Process Enhancements (fpm)

Fortran Package Manager (fpm) is pivotal for long-term Fortran success. This GSoC project aims to improve fpm’s build process by improving dependency detection, optimizing linking, implementing shared libraries, ensuring safe concurrent builds, and introducing external Makefile generation.

The project will address the following tasks:
1. **Custom flags and configurations**
     - Implement custom and compiler-dependent flags, and configurations 
2. **External build system Generation:**
     - Enable generation of external Makefiles akin to `cmake -G` for advanced project configuration.
3. **Linking Optimization:**
     - Replace one-liner linking with static libraries to prevent line buffer overflow in Windows builds.
4. **Shared Library Implementation:**
     - Introduce support for shared library targets for project flexibility.
5. **Dependency Detection**:
     - Enhance fpm’s dependency detection to minimize rebuilds by parsing or hashing module/submodule files or parsing procedure interfaces in module files. fpm should not rebuild dependencies to a module whose public interface has not changed.

__Expected Outcomes__:
* Enhanced dependency tracking and reduced rebuild times.
* Improved reliability in linking, particularly in Windows.
* Increased project versatility with shared library support.
* Safer concurrent builds through file locking.
* Greater project configuration flexibility with external Makefile generation.

**Difficulty:** Intermediate, 175 hours.

**Skills preferred:** Fortran programming, experience with one or more build systems

**Mentors:**
Federico Perini ([@perazz](https://github.com/perazz)), José Alves ([@jalvesz](https://github.com/jalvesz)), Henil Panchal ([@henilp105](https://github.com/henilp105))

## Extended Testing Support (fpm)

The aim of this project is to create a manifest specification to provide defaults to executable targets in fpm projects.
Information can be passed as environment variables, command-line arguments or as a runner.
Desired features include:

- Programs should have a way to find resources of which the relative position within the project source directory is known.
- The current binary directory to access other targets within a project.
- Default runners like `mpirun`/`cafrun` or scripts from test frameworks should be usable to launch programs.
- A general syntax to define environment variables and command-line arguments should be defined.

Some features should be implemented directly in fpm, while more elaborated functionality could be implemented in a separate fpm package as an official Fortran-lang fpm package.

__Related issues:__
- [fpm#179](https://github.com/fortran-lang/fpm/issues/179): Testing with fpm test

__Related discussions:__
- [fpm#328](https://github.com/fortran-lang/fpm/discussions/328): Example which requires external data

__Expected outcomes:__ fpm has broader and deeper testing functionality

__Skills preferred:__ Fortran programming and writing unit tests

__Difficulty:__ Easy, 175 hours

__Mentors:__
Sebastian Ehlert ([@awvwgk](https://github.com/awvwgk)),
Brad Richardson ([@everythingfunctional](https://github.com/everythingfunctional))

## Export build order and `compile_commands.json` (fpm)

`fpm` has the ability to automatically determine the build order of a project's
source files. This information is valuable to third party tools such as
language servers and code analysis tools. The goal of this project is to
export the build order of a project's source files in the `compile_commands.json`.

The second leg of this project is to implement the full syntax of
`compile_commands.json` as described in the [Clang documentation](https://clang.llvm.org/docs/JSONCompilationDatabase.html). This would bring `fpm` a step closer
to being compatible with other build tools.

**Expected outcomes:** `fpm` will export a complete `compile_commands.json` file.

**Skills preferred:** Fortran programming, experience with one or more build systems

**Difficulty:** Hard, 350 hours

**Mentors**:
Giannis Nikiteas ([@gnikit](https://github.com/gnikit))

## Support of external third-party preprocessors

Adding support for external third-party preprocessors is important for fpm due to the additional flexibility they provide when building complex packages.
In particular, the Fortran-lang [stdlib](https://github.com/fortran-lang/stdlib) project exploits the powerful [fypp](https://github.com/aradi/fypp) preprocessor for code generation and the support of fypp by fpm is required for stdlib to eventually be compatible as an fpm package.

This project will require to:

- Modify fpm to optionally invoke a third-party preprocessor before compiling sources;
- Extend the current manifest syntax of fpm for defining preprocessor variables in a preprocessor-independent manner, if necessary;
- Extend the current manifest syntax of fpm for specifying a third-party preprocessor and the corresponding file suffixes, if necessary;
- Passe defined preprocessor variables to built-in preprocessors if necessary;

Third-party preprocessors should be specified on a per-project basis, _i.e._ multiple preprocessors might be required, and fpm should be able to report useful errors for missing third-party preprocessors.

__Related issues:__
- [fpm#78](https://github.com/fortran-lang/fpm/issues/78): support for third-party preprocessors (_e.g._ fypp)
- [fpm#308](https://github.com/fortran-lang/fpm/issues/308): Fortran-based smart code generation in fpm
- [fpm#469](https://github.com/fortran-lang/fpm/issues/469): Source pre-processing prior to determining dependencies

__Expected outcomes:__ fpm has a working preprocessing capability

__Skills preferred:__ Fortran, C, or Python programming, experience using one or more preprocessors

__Difficulty:__ easy, 175 hours

__Mentors:__ 
Laurence Kedward ([@lkedward](https://github.com/lkedward)),
Milan Curcic ([@milancurcic](https://github.com/milancurcic)),
Federico Perini ([@perazz](https://github.com/perazz)),
Jeremie Vandenplas ([@jvdp1](https://github.com/jvdp1))


## File system library (stdlib)

Currently, file system operations such as listing contents of directories, traversing directories, and similar,
are restricted to 3rd party libraries and compiler extensions that are platform-specific and not portable.
This project will entail designing and implementing a cross-platform solution for file system operations.

__Related issues:__
- [stdlib#201](https://github.com/fortran-lang/stdlib/issues/201): File system operations
- [stdlib#220](https://github.com/fortran-lang/stdlib/issues/220): API for file system operations, directory manipulation

__WIP implementation:__
- [stdlib_os](https://github.com/MarDiehl/stdlib_os)

__Expected outcomes:__ Implemented an stdlib module that provides cross-platform file-system utilities

__Skills preferred:__ Fortran and C programming, experience using Linux, macOS, and Windows

__Difficulty:__ Intermediate, 350 hours

__Mentors__:
Arjen Markus ([@arjenmarkus](https://github.com/arjenmarkus)),
Milan Curcic ([@milancurcic](https://github.com/milancurcic))

## Library to work with OS processes (stdlib)

Cross-platform solution to abstract POSIX and Windows API for creating subprocesses.

__Related issues:__
- [stdlib#22](https://github.com/fortran-lang/stdlib/issues/22): Interface to POSIX I/O API
- [stdlib#308](https://github.com/fortran-lang/stdlib/issues/308): Subprocesses and Multiprocessing

__Discourse thread:__
- [Ideas for command module](https://fortran-lang.discourse.group/t/ideas-for-command-module/439)

__Skills preferred:__ Fortran and C programming, experience using Linux, macOS, and Windows

__Difficulty:__ Intermediate, 350 hours

__Mentors:__ Sebastian Ehlert ([@awvwgk](https://github.com/awvwgk))

## Linear algebra and sparse matrices (stdlib)

Improve dense and sparse linear algebra APIs in the Fortran Standard Library. 

The API development should closely follow the developements on dense [linear algebra](https://stdlib.fortran-lang.org/page/specs/stdlib_linalg.html) in order to keep a coherent interface for sparse and dense matrices.

__Related issue__: [#931](https://github.com/fortran-lang/stdlib/issues/931) [#930](https://github.com/fortran-lang/stdlib/issues/930) [#910](https://github.com/fortran-lang/stdlib/issues/910) [#898](https://github.com/fortran-lang/stdlib/issues/898) [#891](https://github.com/fortran-lang/stdlib/issues/891) [#763](https://github.com/fortran-lang/stdlib/issues/763) [#934](https://github.com/fortran-lang/stdlib/issues/934)

__WIP implementations__: [#915](https://github.com/fortran-lang/stdlib/pull/915) [#844](https://github.com/fortran-lang/stdlib/pull/844) [FSPARSE](https://github.com/jalvesz/FSPARSE)

__Expected outcomes:__ Improved linear algebra and sparse matrix functionality in the `stdlib_linalg` module

__Skills preferred:__ Fortran programming, understanding of linear algebra

__Difficulty:__ Hard, 350 hours

__Mentors:__
Ondřej Čertík ([@certik](https://github.com/certik)),
Ivan Pribec ([@ivan-pi](https://github.com/ivan-pi/)),
Jeremie Vandenplas ([@jvdp1](https://github.com/jvdp1)),
Jose Alves ([@jalvesz](https://github.com/jalvesz)),
Federico Perini ([@perazz](https://github.com/perazz))

## String to number conversion (stdlib)

This project will enhance stdlib's string handling capabilities for fast number parsing in Fortran.

Recently, a new module was added to stdlib called [`stdlib_str2num`](https://github.com/fortran-lang/stdlib/blob/master/src/stdlib_str2num.fypp) which implements fast routines for converting strings to numerical types. The participant would get familiar with these implementations and subsequently:

* Create a full benchmark suite for the string to number conversion, across compiler vendors, operating systems, and CPU architectures.
* Explore ways to improve robustness and efficiency, e.g. error handling.
* Propose a shallow interface for the [string_type](https://github.com/fortran-lang/stdlib/blob/master/src/stdlib_string_type.fypp) facility in stdlib.
* Propose an enhancement to the [loadtxt](https://github.com/fortran-lang/stdlib/blob/master/src/stdlib_io.fypp) facility function to speed-up file reading.
* Depending on the advancement, the participant is also encouraged to include a roadmap for inclusion of the inverse conversion by following the intitiative in this thread [ryu-based to_string function](https://github.com/fortran-lang/stdlib/issues/627)

__Relevant thread on Fortran Discrouse__: [Faster string to double](https://fortran-lang.discourse.group/t/faster-string-to-double/2208)

__Expected outcomes:__ Enhancement of stdlib fast string to number conversion

__Skills preferred:__ Fortran and C programming, understanding of floating-point arithmetic

__Difficulty:__ Hard, 350 hours

__Mentors:__
Jose Alves ([@jalvesz](https://github.com/jalvesz)),
Carl Burkert ([@carltoffel](https://github.com/carltoffel))
Brad Richardson ([@everythingfunctional](https://github.com/everythingfunctional)),
Ivan Pribec ([@ivan-pi](https://github.com/ivan-pi/))

## Compile benchmarking code written in Fortran with LFortran and improving LFortran's performance on these benchmarks (LFortran)

https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/fortran.html contains all the benchmark codes written for various problems such as `n-body`, `sepctral norm`, `mandelbrot`. The workflow would involve first doing bug fixes to compile the code (modifying the input code would be okay) with LFortran and producing correct outputs. Then, improving LFortran to perform better or equivalent to other Fortran compilers such as GFortran.

`n-body` already compiles with workarounds with LFortran main. See, https://github.com/lfortran/lfortran/pull/1213. More work needs to be done for other benchmark codes. 


__Expected outcomes:__ LFortran can compile as many benchmark codes as possible. Performing better than other compilers would be an additional plus.

__Skills preferred:__ Fortran and C++ programming

__Difficulty:__ intermediate/hard, 350 hours

**Mentors** - Ondřej Čertík


## Compile any Fortran code (LFortran)

The primary goal is to compile as many codes as possible. We have identified and listed those at [label:code-to-be-compiled](https://github.com/lfortran/lfortran/labels/Code%20to%20be%20Compiled). 

This project aims to pick up a code and get it compiled to ASR, then to LLVM, binary and assure that values align with GFortran (or other Fortran compilers). We can have several of these projects at the same time.

__Expected outcomes:__ LFortran can compile chosen code.

__Skills preferred:__ Fortran and C++ programming

__Difficulty:__ intermediate/hard, 350 hours

**Mentors** - Pranav Goswami

## Compile `neural-fortran` using LFortran

Currently LFortran compiles 14% of `neural-fortran`. It is a parallel framework for deep learning. 

__Expected outcomes:__ LFortran can compile `neural-fortran` code.

__Skills preferred:__ Fortran and C++ programming

__Difficulty:__ intermediate/hard, 350 hours

**Mentors** - Pranav Goswami


## Allow running Fortran in the browser (LFortran)

We have LFortran running in the browser using WASM here: https://dev.lfortran.org/, the goal of this project would be to improve the user interface. Here is a list of issues that the project can work on fixing: https://github.com/lfortran/lcompilers_frontend/issues

This project would entail working with LFortran, LLVM, Emscripten,
and Webassembly to allow running Fortran in the browser.

__Skills preferred:__ Fortran and C++ programming

__Difficulty:__ intermediate, 350 hours

**Mentors** - Ondřej Čertík


## Implementation of features on the ASR and LLVM level (LFortran)

The roadmap https://gitlab.com/lfortran/lfortran/-/issues/272 issue contains a list of Fortran features that we want implemented. Each feature should be implemented at the ASR level and in the LLVM backend to be complete. If AST is missing for a given feature, then it has to be implemented also.

Here you can pick a feature or a set of features from the list and propose it as a GSoC project. In other words, this project idea can accommodate multiple student projects.

List of resources for more information and background:

* [ASR.asdl](https://gitlab.com/lfortran/lfortran/-/blob/0391231553932e7df230c7c88bc05528d5348f85/grammar/ASR.asdl), the comment at the top explains the design motivation
* [asr_to_llvm.cpp](https://gitlab.com/lfortran/lfortran/-/blob/0391231553932e7df230c7c88bc05528d5348f85/src/lfortran/codegen/asr_to_llvm.cpp) is the LLVM backend
* [ast_to_asr.cpp](https://gitlab.com/lfortran/lfortran/-/blob/0391231553932e7df230c7c88bc05528d5348f85/src/lfortran/semantics/ast_to_asr.cpp) is the AST -> ASR conversion where all semantics checks are being done and compiler errors reported to the user
* [Developer Tutorial](https://docs.lfortran.org/developer_tutorial)

If you have any questions, please do not hesitate to ask, we can discuss or provide more details.

__Mentors:__
Ondrej Certik ([@certik](https://github.com/certik))

## Other LFortran ideas (LFortran)

More LFortran project ideas for GSoC can be found at: <https://github.com/lfortran/lfortran/wiki/GSoC-2026-Ideas>

## MPI support (fortls)

`fortls` has support for Fortran intrinsics, Standard modules and OpenMP.
It does not however support MPI. The goal of this project is to add full support
for completions, hover and signature help for MPI variables, subroutines and functions.

Due to the size of the MPI standard, the process of extracting the necessary
information from the standard such as names, interfaces and documentation will
be automated. The student will be responsible for creating a scraper/parser
to fetch the necessary information from the MPI standard and then create the
serialised data (JSON) to be used by `fortls`.

**Discourse thread:** [MPI documentation and interfaces](https://fortran-lang.discourse.group/t/mpi-documentation-and-interfaces/7252)

**Expected outcomes:** `fortls` will have completion and hover support for MPI.

**Skills preferred:** Python programming and understanding of Fortran

**Difficulty:** Intermediate, 175 hours

**Mentors**:
Giannis Nikiteas ([@gnikit](https://github.com/gnikit))

## Semantic highlighting and collapsable scopes (fortls)

As part of this project the student will add support to `fortls` for the
Semantics Tokens request, which is used to provide improved syntax highlighting
and the Folding Range request, which is used to provide collapsable scopes.

**Related Issues:**

- [fortls#56](https://github.com/fortran-lang/fortls/issues/56)

**Expected outcomes:** `fortls` will serve for semantic highlighting and collapsable scopes requests.

**Skills preferred:** Python programming and understanding of Fortran

**Difficulty:** Intermediate, 175 hours

**Mentors**:
Giannis Nikiteas ([@gnikit](https://github.com/gnikit))

## Replace explicit LSP interface with pygls (fortls)

`fortls` uses explicit interfaces to the Language Server Protocol (LSP).
To decrease code duplication and increase maintainability, the work of
maintaining the explicit interfaces should be replaced with the use of
`pygls`' module.

**Related Issues:**

- [fortls#96](https://github.com/fortran-lang/fortls/issues/96)

**Expected outcomes:** `fortls` uses `pygls`' to define LSP interfaces, types and requests.

**Skills preferred:** Python programming and understanding of the Language Server Protocol

**Difficulty:** Hard, 350 hours

**Mentors**:
Giannis Nikiteas ([@gnikit](https://github.com/gnikit))

## Python environment manager (vscode-fortran-support)

In the Modern Fortran for VS Code extension, the use of Python as a means to
install third party tools is essential. The goal of this project is to
create a robust Python environment manager for installing and running third
party tools such as `fortls`, `fpm`, `findent`, etc., taking into account
the user's setup (venv, conda, system Python, etc.).

**Expected outcomes:** Modern Fortran for VS Code will have a robust Python environment manager for installing and running third party tools.

**Skills preferred:** Typescript, Python programming

**Difficulty:** Hard, 175 hours

**Mentors**:
Giannis Nikiteas ([@gnikit](https://github.com/gnikit))

## vscode integration with fpm (vscode-fortran-support)

The goal of this project is to allow `fpm` integration with the Modern Fortran
extension for Visual Studio Code, similar to how CMake and Meson are integrated
in VS Code.

Using an Activity bar icon, the user will be able to build and run projects,
tests and examples. The student will be responsible for creating the GUI
integration and the necessary backend to communicate with `fpm`.

**Expected outcomes:** Modern Fortran for VS Code will have a GUI integration
with `fpm` to build and run projects, tests and examples.

**Skills preferred:** Typescript, Fortran programming

**Difficulty:** Hard, 350 hours

**Mentors**:
Giannis Nikiteas ([@gnikit](https://github.com/gnikit))

## Standard Conformance Suite

Fortran compilers' support for ISO Fortran standards generally lag the publication of the standard by
several years or longer.  Fortran consultants Ian Chivers and Jane Sleightholme periodically publish
a [paper](https://dl.acm.org/doi/10.1145/3432987.3432991) containing a table detailing the standard
features supported by 10 compilers.  Gathering the tabulated data requires a considerable amount of
effort on the part of the authors and the compiler developers.  The chosen venue for publishing the 
table also puts it behind a paywall: access requires a subscription to ACM SIGPLAN Fortran Forum.
The project will automate the generation of the table, make it more detailed and empower the community to contribute to
by submitting small tests to an open-source conformance test suite.

__Prior work:__
- [fortran-compiler-tests](https://github.com/nncarlson/fortran-compiler-tests)
- [flibs chkfeatures](https://sourceforge.net/p/flibs/svncode/HEAD/tree/trunk/chkfeatures/)
- [Defunct](https://github.com/sourceryinstitute/Defunct)
- [Fortran Testsuite Proposal](https://github.com/j3-fortran/fortran_proposals/issues/57)

__Expected outcomes:__ A comprehensive test suite that generates a report of standard conformance for any Fortran compiler.
The suite is not expected to be 100% complete by the end of the project, but should be significant in terms of standard coverage.

__Skills preferred:__ Fortran programming, experience reading and interpreting the Fortran Standard, and writing tests

__Difficulty:__ Hard, 350 hours

__Mentors:__
Damian Rouson ([@rouson](https://github.com/rouson)),
Arjen Markus ([@arjenmarkus](https://github.com/arjenmarkus)),
Ondřej Čertík ([@certik](https://github.com/certik))

## Coarray Fortran Framework of Efficient Interfaces to Network Environments ([Caffeine](https://github.com/berkeleylab/caffeine))

This project would add support for grouping images (parallel processes) into teams that allow submodes to execute independently.
Caffeine 0.1.0 uses the [GASNet-EX](https://go.lbl.gov/gasnet) networking middleware software as a back end for supporting most of the non-coarray parallel features of Fortran 2018 except for the intrinsic derived `team_type` and related features.
Work is underway to support the coarray features that most applications will need for expressing custom parallel algorithms.
The teams feature set is the one significant non-coarray parallel group of features not yet implemented in Caffeine.

__Expected outcomes:__ Caffeine can be used to create images groups in execution parallel programs

__Skills preferred:__ Fortran and C programming

__Difficulty:__ Intermediate, 175 hours

__Mentors:__ Damian Rouson ([@rouson](https://github.com/rouson))

## Get fortran-lang/minpack to be used in SciPy

[fortran-lang/minpack #14](https://github.com/fortran-lang/minpack/issues/14)

The participant would work with Fortran-lang and SciPy teams toward implementing
fortran-lang/minpack in SciPy.

__Expected outcomes:__ fortran-lang/minpack is incorporated into SciPy.

__Skills preferred:__ Fortran-C interop, Python programming

__Difficulty:__ Easy, 175 hours

__Mentors:__ Sebastian Ehlert ([@awvwgk](https://github.com/awvwgk))

## Improving fastGPT: Making it Faster, Easier to Use, and More General

The [fastGPT](https://github.com/certik/fastGPT) project is a Fortran implementation of GPT-2 that is comparable in speed to PyTorch. Although it is already very fast on CPUs, there is still room for improvement in terms of usability and performance on CPU and other architectures, such as GPUs.

This project aims to explore various aspects of fastGPT to improve its usability and performance. Some potential areas of exploration include:

*   *Parallelism*: Investigate the use of parallelism in fastGPT, including MPI and coarrays, to potentially make it even faster. Given that GPT inference is dominated by large matrix-matrix multiplications over a few layers, we will carefully investigate which parallel approach is the best (whether MPI, coarrays, OpenMP or just parallel BLAS that we already have).

*   *Reduced precision models*: Experiment with using reduced precision models (e.g., 16-bit or 8-bit floats) instead of the default 32-bit to potentially speed up inference.

*   *GPU acceleration*: Explore how to optimize fastGPT for GPU architectures to potentially make it even faster.

*   *UI improvements*: Add a chat mode (similar to chatGPT). Explore how to make it easier to use as a grammar checker, or creating summaries, or other areas where GPT-2 is strong. Make it a nice Fortran library, installable using fpm, usable in other projects. Investigate how to use it with the `neural-fortran` project.

__Expected outcomes:__ Create an improved fastGPT implementation that is faster, easier to use, and more general.

__Skills preferred:__ Fortran, linear algebra

__Difficulty:__ Intermediate, 175 hours

__Mentors:__
Ondřej Čertík ([@certik](https://github.com/certik)),
Milan Curcic ([@milancurcic](https://github.com/milancurcic))

## Fortran Graphics Library 

Fortran does not have native graphics handling capabilities. While several bindings interfacing Fortran to graphics and plotting libraries are available (e.g., [f03gl](https://www-stone.ch.cam.ac.uk/pub/f03gl/index.xhtml), [sdl](https://github.com/interkosmos/fortran-sdl2), [pyplot](https://github.com/jacobwilliams/pyplot-fortran), [dislin](https://www.dislin.de/exa_f90.html#section_12d), [plplot](https://plplot.sourceforge.net) ), no up-to-date open-source graphics package with a pure, modern Fortran API is available. 

The aim of this project is to lay out the basics of an object-oriented "canvas" representation in object-oriented Fortran. The contributor would implement, document, and test basic graphics classes (2d points, lines, brushes, etc.), an abstract graphics canvas API with backends to both file and graphics devices (i.e., bitmap, PNG, OpenGL, SVG, etc.) The outcome of this project would be a contribution to the development of a platform-agnostic graphics library for Fortran.  

__Expected outcomes:__ Design and implement classes for 2d graphics primitives, a unified graphics canvas API, and several backend implementations.

__Skills preferred:__ Fortran, C, 2D graphics basics 

__Difficulty:__ Intermediate, 350 hours

__Mentors:__
Federico Perini ([@perazz](https://github.com/perazz))*

## Improved generation of Fortran interfaces for PETSc

[PETSc](https://petsc.org), the Portable, Extensible Toolkit for Scientific Computation, pronounced PET-see, is for the scalable (parallel) solution of scientific applications modeled by partial differential equations (PDEs).
It has bindings for C, Fortran, and Python (via petsc4py). PETSc also contains TAO, the Toolkit for Advanced Optimization, software library. It supports MPI, and GPUs through CUDA, HIP, Kokkos, or OpenCL, as well as hybrid MPI-GPU parallelism; it also supports the NEC-SX Tsubasa Vector Engine.

Currently, only a part of the Fortran interfaces can be generated automatically using [bfort](http://wgropp.cs.illinois.edu/projects/software/sowing/bfort/bfort.htm).
Since the manual generation of the remaining interfaces is tedious and error prone, this project is about an improved generation of Fortran interfaces from PETSc's C code.

The main tasks of this project are

 * Definition of a robust and future-proof structure for the Fortran interfaces
 * Selection and/or development of a tool that creates the interfaces automatically


More specifically, the first task is about finding a suitable structure of the C-to-Fortran interface that reduces the need of 'stubs' on the C and Fortran side making use of modern Fortran features where appropriate.
This task will involve evaluating different approaches found in other projects taking into account the object-oriented approach of PETSc.
Prototypes will be implemented manually and evaluated with the help of the PETSc community.
The second task is then the automated generation of the Fortran interfaces using the approach selected in the first task.
To this end, it will be evaluated whether an extension of bfort, the use of another existing tool, or the development of a completely new tool (probably in Python) is the most suitable approach.

**Links**:

 * [PETSc](https://petsc.org)
 * [bfort](http://wgropp.cs.illinois.edu/projects/software/sowing/bfort/bfort.htm)
 * [Fortran Wiki: Generating C Interfaces](https://fortranwiki.org/fortran/show/Generating+C+Interfaces)
 * [Fortran Discourse: ISO_C_binding](https://fortran-lang.discourse.group/t/iso-c-binding-looking-for-practical-example-of-how-it-helps-with-mangling/3393)

**Expected outcomes**: Stable and robust autogeneration of Fortran interfaces for PETSc that works for almost all routines

**Skills preferred**: Programming experience in multiple languages, ideally C and/or Fortran

**Difficulty**: Intermediate, 350 hours

**Mentors**: Martin Diehl ([@MarDiehl](https://github.com/MarDiehl)), Ivan Pribec ([@ivan-pi](https://github.com/ivan-pi))
