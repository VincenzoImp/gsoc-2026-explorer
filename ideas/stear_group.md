# Ste||ar group — Project Ideas

**Source:** https://github.com/STEllAR-GROUP/hpx/wiki/Google-Summer-of-Code-(GSoC)-2026#2026-hpx-project-ideas
**Scraped:** 2026-02-22T23:28:47.613994

---

## Introduction
Welcome to the Google Summer of Code (GSoC) page for the HPX project. Here you can find information about student projects, proposal submission templates, advice on writing good proposals, and links to information on getting started with HPX. [The STE||AR Group](http://stellar-group.org "The STE||AR Group: Systems Technology, Emergent Parallelism, and Algorithm Research") will apply as an organization and our goal is to have at least five funded students working on HPX related projects.

## Requirements

Students must submit a proposal. A template for the proposal is available [[here|GSoC Submission Template]]. Find hints for writing a good proposal [[here|Hints for Successful Proposals]].

We strongly suggest that students interested in developing a proposal for HPX discuss their ideas on the [Discord](https://discord.gg/eh4HTXVuWg) channel or the mailing list to help refine the requirements and goals. Students who actively plan and discuss projects with developers are generally ranked before those that do not.

We have intentionally left the descriptions of these projects vague and open to interpretation because we expect students to develop their proposals' requirements by doing initial background research on the topic and interacting with the community. **In addition, it is important to note that the suggested projects on this page are not binding** -- if you have an interest in parallel task-based programming and have an idea for a project that would either improve HPX or demonstrate how well it applies to your problem, then feel free to suggest your idea as a project and write a proposal for it. We will be glad to help you with project goals to improve your proposal if you have ideas, so do not leave them until the last minute.

We will expect students to demonstrate that they have the required level of C++ and CMake knowledge by showing us some of their previous work (e.g., a GitHub repository), or preferably, by them making a small demonstration program using HPX that shows a simple example of something they have created themselves.

## Potential Additional Funding

For students who perform at or above expectations on both GSoC evaluations, the Center of Computation and Technology (CCT) at Louisiana State University (LSU) may fund up to an additional four weeks' work on the project for no more than the GSoC rate of pay. This funding is not guaranteed and is independent of the GSoC program. Students accepted for additional funding will be paid through LSU for the additional weeks and affiliated with LSU during that time. Additional paperwork through LSU will be required.

## Tips for Prospective Students

Some of our former GSoC students that still contribute to our projects have put together the following list. All of them had to go through the same learning experience. Prospective students most probably face this challenge now, so the list provides pointwise help to get into HPX smoothly.

 1. The first thing we suggest is to build HPX from the source using the CMake build system. An example guide to build HPX is [here](https://hpx-docs.stellar-group.org/latest/html/manual/building_hpx.html). Various ways of building HPX (e.g., memory allocators, OTF2 traces, CUDA support) will enable you to understand the capabilities of HPX as a runtime.
 2. Once you're acquainted with the build system, we suggest you read our [docs/wiki](https://hpx-docs.stellar-group.org/latest/html/index.html) and try to familiarize yourself with the basic terminology (e.g., _locality_, _LCO_, _futurization_, etc.).
 3. Next, we suggest you watch talks on [HPX](https://www.youtube.com/results?search_query=HPX+cpp) on YouTube. Doing so should give you a brief overview of the motivations and implementation design of the components within HPX.
 4. At this point, try building and playing with the [examples](https://github.com/STEllAR-GROUP/hpx/tree/master/examples) in HPX. Furthermore, we have a [basic tutorial](https://hpx-docs.stellar-group.org/latest/html/examples.html) that takes you through the features and their usage with code examples.
 5. Going through the examples may be an overwhelming experience, so we suggest you become familiar with our way of writing code through our [summer lecture series](https://www.diehlpk.de/blog/cpp-lectures/). (Hint: Pay attention to *Lecture #4*)
 6. The C++ style used in HPX might not seem intuitive at first, but [this guide](https://wenke-d.github.io/CPP-for-HPX/) will help you build an intuition for why it is used.
 7. When you're familiar with basic usage, we suggest you try writing demo HPX programs (e.g., matrix-matrix multiplication). Go through our [Issue tracker](/ideas/stear-group/stellar-group-hpx-issues) and see if you can find an issue you would like to investigate. Working on bugs is the easiest way to dive into the code base and contribute to HPX.
 8. Dig into our currently active [GSoC issues](/ideas/stear-group/stellar-group-hpx-issues-2) and Pull Requests relevant to them. Furthermore, leave comments and discuss with the corresponding authors.
 9. We **highly recommend** joining our channel, on [Discord](https://discord.gg/eh4HTXVuWg), where you can ask questions, discuss issues, pull requests, and your potential GSoC project. Remember, questions are the key to start contributing!

## Usage of AI tooling
The goal of GSoC is to learn and grow through engagement with mentors and the broader community. AI tools can be helpful for brainstorming, providing suggestions, and assisting in learning new concepts. That said, we expect contributors to use AI tools responsibly. Raw AI output that you cannot understand and explain will not be accepted.

## 2026 HPX Project Ideas 
There are new projects this year, and also ones revamped from previous years (legacy) that are still of interest. These projects have mentors ready and waiting to help students.

## Core HPX Projects
These are projects that involve making changes/improvements/extensions to the core HPX library.
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Potential Additional Funding](#potential-additional-funding)
- [Tips for Prospective Students](#tips-for-prospective-students)
- [Usage of AI tooling](#usage-of-ai-tooling)
- [2026 HPX Project Ideas](#2026-hpx-project-ideas)
- [Core HPX Projects](#core-hpx-projects)
  - [Annotate HPX with Contracts](#annotate-hpx-with-contracts)
  - [Expose HPX using C++ Modules](#expose-hpx-using-c-modules)
  - [Implement the `make_receiver_for` optimization for HPX Senders](#implement-the-make_receiver_for-optimization-for-hpx-senders)
  - [Implement `hpx::system_scheduler` as described in P2079 (System Execution Context)](#implement-hpxsystem_scheduler-as-described-in-p2079-system-execution-context)
  - [Integrate HPX with the Tracy profiler](#integrate-hpx-with-the-tracy-profiler)
  - [Use C++26 reflection for HPX remote operation](#use-c26-reflection-for-hpx-remote-operation)
  - [Hierarchical Collectives for HPX](#hierarchical-collectives-for-hpx)
  - [Implement parallel `hpx::uninitialized_relocate_*` algorithms for overlapping ranges](#implement-parallel-hpxuninitialized_relocate_-algorithms-for-overlapping-ranges)
  - [Add HPX to Compiler Explorer (godbolt.org)](#add-hpx-to-compiler-explorer-godboltorg)
  - [Improve ChplX - Source to Source Transformer for chapel to C++ using HPX](#improve-chplx---source-to-source-transformer-for-chapel-to-c-using-hpx)
  - ["Green out" our Continuous Integration tests](#green-out-our-continuous-integration-tests)
  - [Port HPX to iOS and Mac (M1 architecture)](#port-hpx-to-ios-and-mac-m1-architecture)
  - [Study the performance of Halide applications running on HPX threads.](#study-the-performance-of-halide-applications-running-on-hpx-threads)
  - [HPX distributed algorithms](#hpx-distributed-algorithms)
  - [(Re-)Implement executor API on top of sender/receiver infrastructure](#re-implement-executor-api-on-top-of-senderreceiver-infrastructure)
  - [Explicit Visualization of Accelerators for HPX Trace Visualization](#explicit-visualization-of-accelerators-for-hpx-trace-visualization)
  - [Improved Scalability for HPX OTF2 Trace Visualization](#improved-scalability-for-hpx-otf2-trace-visualization)
  - [Multiple File Load in HPX Trace Visualization](#multiple-file-load-in-hpx-trace-visualization)
- [AI Project Ideas](#ai-project-ideas)
  - [Spatio-Temporal Extrapolation with Generative AI: Advancing Storm Surge Forecast Accuracy through Bias Correction in Unmonitored Areas](#spatio-temporal-extrapolation-with-generative-ai-advancing-storm-surge-forecast-accuracy-through-bias-correction-in-unmonitored-areas)
  - [Spatio-Temporal Extrapolation with GNN: Advancing Storm Surge Forecast Accuracy through Bias Correction in Unmonitored Areas](#spatio-temporal-extrapolation-with-gnn-advancing-storm-surge-forecast-accuracy-through-bias-correction-in-unmonitored-areas)
  - [Transformer-based Image-to-Graph Conversion](#transformer-based-image-to-graph-conversion)
- [Past Year Projects](#past-year-projects)
  - [Coroutine-like Interface](#coroutine-like-interface)
  - [Async I/O using Coroutines and S/R](#async-io-using-coroutines-and-sr)
  - [Add Vectorization to `par_unseq` Implementations of Parallel Algorithms](#add-vectorization-to-par_unseq-implementations-of-parallel-algorithms)
  - [Conflict (Range-Based) Locks](#conflict-range-based-locks)
  - [Standardize and Visualize HPX Benchmarks](#standardize-and-visualize-hpx-benchmarks)
  - [Rustize HPX!](#rustize-hpx)
  - [Pythonize HPX!](#pythonize-hpx)
  - [Create Generic Histogram Performance Counter](#create-generic-histogram-performance-counter)
  - [Fix libCDS broken dependency](#fix-libcds-broken-dependency)
- [HPX User Projects](#hpx-user-projects)
  - [Implement your favorite Computational Algorithm in HPX](#implement-your-favorite-computational-algorithm-in-hpx)
  - [Conduct a thorough Performance Analysis on HPX Parallel Algorithms (and optimize)](#conduct-a-thorough-performance-analysis-on-hpx-parallel-algorithms-and-optimize)
- [Legacy Project Ideas](#legacy-project-ideas)
  - [Implement Your Favorite Parcelport Backend](#implement-your-favorite-parcelport-backend)
  - [Implement a Faster Associative Container for GIDs](#implement-a-faster-associative-container-for-gids)
  - [Create A Parcelport Based on WebSockets](#create-a-parcelport-based-on-websockets)
  - [All to All Communications](#all-to-all-communications)
  - [Distributed Component Placement](#distributed-component-placement)
  - [Port Graph500 to HPX](#port-graph500-to-hpx)
  - [Port Mantevo MiniApps to HPX](#port-mantevo-miniapps-to-hpx)
  - [Distributed solver and load balancing for Peridynamics using asynchronous parallelism](#distributed-solver-and-load-balancing-for-peridynamics-using-asynchronous-parallelism)
  - [Port the GAP Benchmark Suite to HPX](#port-the-gap-benchmark-suite-to-hpx)
  - [HPX backend for OpenMPI](#hpx-backend-for-openmpi)
  - [Bug Hunter](#bug-hunter)
  - [Project: Template](#project-template)

### Annotate HPX with Contracts
- **Abstract:** Recent standardization developments indicate that C++26 will introduce contracts [P2900](https://wg21.link/p2900). Their primary use is to increase language safety by providing developers with ergonomic tools to handle false assertions. They can be used to give defined behavior to pre-condition and post-condition violations of functions. The companion proposal to contracts: [P3471](https://wg21.link/p3471) introduces the notion of a hardened STL, which implements the expected conditions to standard library functions (e.g. vector.front() has a precondition that vector.empty() is false). HPX provides multiple debugging mechanisms, and a rich test suite. Annotating the HPX library functions would further safety and debugging ability.
* **Additional References:** 
	- [Proposal P2900 (Contracts)](https://wg21.link/p2900)
	- [Proposal P3471 (Hardened STL)](https://wg21.link/p3471)
* **Difficulty:** Medium/Advanced
* **Expected result:** Annotate a significant portion of HPX's public facing API with contracts.
* **Knowledge Prerequisite:** C++, Git
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png)), Isidoros Tsaousis-Seiras (tsa.isidoros [at]  gmail.com)
* **Project Size:** 350 hour (large project)


### Expose HPX using C++ Modules
* **Abstract:** [Modules](https://en.cppreference.com/w/cpp/language/modules) were introduced in C++20 as an alternative to header files for sharing declarations and definitions across translation units. C++ Modules can improve compilation times and code isolation. There are several differences when using C++ Modules, mainly they cannot export macros, and declarations have to be explicitly exported using the `export` keyword. We are interested in exposing HPX using C++ Modules (in addition to header files). A lot of work has already been done for this, howver there is quite a bit of work left to expose all of HPX in a convenient way through the C++20 module system.
* **Additional References:** 
Rubén Pérez on bringing C++ Modules to the Boost library: [Part 1](https://anarthal.github.io/cppblog/modules), [Part 2](https://anarthal.github.io/cppblog/modules2), [Part 3](https://anarthal.github.io/cppblog/modules3)
* **Difficulty:** Medium/Advanced
* **Expected result:** Make all of HPX available to users through C++ Modules
* **Knowledge Prerequisite:** C++, Git
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png)), Panagiotis Syskakis (pansysk75 [at] gmail.com)
* **Project Size:** 350 hour (large project)


### Implement the `make_receiver_for` optimization for HPX Senders
* **Abstract:** The Senders/Receivers ([P2300](https://wg21.link/P2300)) framework is constantly evolving to become more optimized and user-friendly. One of the papers accelerating this evolution is [P3425](https://wg21.link/p3425) It proposes that since chained operations have a known byte-size and are stacked contiguously in memory, we can avoid holding pointers to each of them, and we can calculate their addresses on the fly based on the offsets. This presents a massive object size reduction and also aids the compiler in optimizing the code. HPX's senders would greatly benefit from implementing the proposed interface to support this feature.

* **Additional References:** 
	- [Proposal P2300](https://wg21.link/p2300)
	- [Proposal P3425](https://wg21.link/p3425)
* **Difficulty:** Medium/Advanced
* **Expected result:** Implement the `make_receiver_for` interface for `hpx::bulk` as described in [P3425](https://wg21.link/p3425).
* **Knowledge Prerequisite:** C++, Git, Concurrency
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png)), Isidoros Tsaousis-Seiras (tsa.isidoros [at]  gmail.com)
* **Project Size:** 175 hour (medium project)


### Implement `hpx::system_scheduler` as described in P2079 (System Execution Context)
* **Abstract:** C++26 Has evolved to include a modern API for parallelism and task scheduling ([P2300](https://wg21.link/p2300)). HPX implements the proposed interface, as well as multiple schedulers. Proposal ([P2079](https://wg21.link/p2079)) proposes a generic scheduler to OS-provided threads. `hpx::system_scheduler` is the HPX analogue that maps to `hpx::threads` instead, and an excellent way to expose an HPX scheduler with a Sender/Receiver interface.

* **Additional References:** 
	- [Proposal P2300](https://wg21.link/p2300)
	- [Proposal P2079](https://wg21.link/p2079)
* **Difficulty:** Medium/Advanced
* **Expected result:** Implement `system_scheduler` as described in [P2079](https://wg21.link/p2079).
* **Knowledge Prerequisite:** C++, Git, Concurrency
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png)), Isidoros Tsaousis-Seiras (tsa.isidoros [at]  gmail.com)
* **Project Size:** 350 hour (large project)


### Integrate HPX with the Tracy profiler
* **Abstract:** HPX is already integrated with the [Intel VTune](https://www.intel.com/content/www/us/en/developer/tools/oneapi/vtune-profiler-download.html) and [APEX](https://uo-oaciss.github.io/apex/) profilers. HPX has also partial support for integrating with Tracy. Extending and improving support for binding Tracy to HPX will extend the capabilities of introspective and embedded profiling tools for HPX applications. The integration would include annotating key functions, mutexes, thread scheduling, distributed operation, etc. The work would also require extending the CMake based build system integration simplifying using Tracy with HPX and its applications. Part of the project could also be setting up a web-serivice that can be used to visualize collected Tracy data.
* **Additional References:** 
    * [Tracy](https://github.com/wolfpld/tracy)
* **Difficulty:** Medium/Advanced
* **Expected result:** Integrate the Tracy profiler with HPX.
* **Knowledge Prerequisite:** C++, Git, CMake
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png), Panagiotis Syskakis (pansysk75 [at] gmail.com))
* **Project Size:** 350 hour (large project)


### Use C++26 reflection for HPX remote operation
* **Abstract:** HPX has already a remote function invocation (RPC) framework that allows to invoke C++ functions on a different locality. The current implementation of the  RPC mechanisms in the general case relies on the user providing explicit macros that expand to the necessary code blocks that enable the remote invocation of an function. With C++26 reflection becoming available, we should add support for automatically generating this code that relies on using these new language facilities.
* **Additional References:** 
    * [C++ 26 Reflecton](http://wg21.link/P2996)
* **Difficulty:** Medium/Advanced
* **Expected result:** Arbitrary C++ functions can be invoked remotely.
* **Knowledge Prerequisite:** C++, Git, CMake
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png))
* **Project Size:** 350 hour (large project)


### Hierarchical Collectives for HPX
* **Abstract:** The standard collective operations in HPX follow a rather naive approach based on point-to-point communication with one host locality. Recently, hierarchical collectives using tree-based communication patterns were developed for the basic one-to-one and one-to-all collective operations. On large scale, these collective show significant performance improvements compared to their naive counterpart. The goal of this project is to add the remaining all-to-all-based collective operations to HPX using a similar tree-based approach.
* **Difficulty:** Medium
* **Expected result:** Complementing the hierachcial collectives in HPX with all-to-all, all-reduce, all-gather.  
* **Knowledge Prerequisite:** C++, Git
* **Mentor:** Alexander Strack (alexander.strack *[at]* ipvs.uni-stuttgart.com)
* **Project Size:** 350hour (large project)


### Implement parallel `hpx::uninitialized_relocate_*` algorithms for overlapping ranges
* **Abstract:** HPX [implements](https://github.com/STEllAR-GROUP/hpx/tree/master/libs/core/algorithms/include/hpx/parallel/algorithms) the full set of the [C++ standard algorithms](https://en.cppreference.com/w/cpp/algorithm). This includes algorithms that copy data (e.g. `hpx::copy` copies the elements from a source range to a destination range). Recent proposals (see additional references below) suggest the addition of a new type trait (`std::is_trivially_relocatable`) that defines a new group of types that can benefit from **trivial relocation**. When relocating an object, the **relocation** algorithms will determine if it is valid to reduce the *move-constructor* and *destructor* call to a single `memcpy()`. In that way, relocation improves performance and increases safety. The relocation algorithms are: A) `relocate`, `relocate_at`, to operate on single objects and B) `uninitialized_relocate`, `uninitialized_relocate_backward` to operate on ranges of elements. These were added to HPX in a GSoC 2023 Contribution. However, the parallel versions of `hpx::uninitialized_relocate` and `hpx::uninitialized_relocate_backward` cannot handle overlapping ranges properly, as the forward and backward order of the algorithms is not preserved when running in parallel. The contributor is expected to correct the parallelization of these algorithms for overlapping ranges, as well as benchmark, write tests, and evaluate their solution.
* **Additional References:** 
    * [P1144 Object relocation in terms of move plus destroy](http://wg21.link/p1144)
    * [C++Now 2019: "Trivially Relocatable"](https://www.youtube.com/watch?v=SGdfPextuAU)
    * [GSoC 2023: Relocation Semantics in HPX](https://isidorostsa.github.io/gsoc2023/)
    * [Possible choice for a parallelization method](https://github.com/STEllAR-GROUP/hpx/pull/6364#discussion_r1414485678)
* **Difficulty:** Medium/Advanced
* **Expected result:** Parallel implementations of `uninitialized_relocate` and `uninitialized_relocate_backward` that work on overlapping ranges, as well as written tests and benchmarks.
* **Knowledge Prerequisite:** C++, Git, parallel algorithms
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png)) and Isidoros Tsaousis-Seiras (tsa.isidoros *[at]* gmail.com)
* **Project Size:** 175 hour (Medium/Advanced project)


### Add HPX to Compiler Explorer (godbolt.org)
* **Abstract:** Compiler Explorer https://godbolt.org/ is a widely popular web based application which provides easy access to multiple C++ compilers and environments allowing their users to write, test and share anything from small C++ scripts to large CMake-based projects quickly. Given its versatility we thought that it would be a convenient for HPX to have an integration with Compiler Explorer in some way. A preliminary idea is that we will maintain our own fork of Compiler Explorer (which is open source) and experiment with the HPX integration locally before making the integration public through a Pull Request to Compiler Explorer. The result could even be constrained to an environment somewhat similar to Compiler Explorer just for HPX where prospective users would experiment with quick HPX scripts before downloading, building and running the whole library.
* **Difficulty:** Medium/Hard
* **Expected result:** Develop a fork of Compiler Explorer (or application with similar basis) where HPX is integrated and available for quick testing and scripting.
* **Knowledge Prerequisite:** C++, CMake, Compilers, Node.js
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png)) and Giannis Gonidelis (gonidelis [at] hotmail.com)
* **Project Size:** 175 (Medium project)


### Improve ChplX - Source to Source Transformer for chapel to C++ using HPX
* **Abstract:** HPX is an excellent runtime system for doing task-based parallelism. Chapel is one of the most easy to use languages for HPC which are readily scalable. [ChplX](https://github.com/ct-clmsn/chplx) is an attempt to make things interoperable. Chapel gets access to existing C++ tooling in HPX and other toolchain integrations that supports C++. We also have traveler visualization and APEX performance counters which are helpful to determine several statistics. This project has a huge interest from Chapel and other communities. 
* **Difficulty:** Medium
* **Expected result:** 
Propose one of the following or it's sub idea to improve chplx's individual components:
    1. Library - 
        - Add constructs from Chapel language which are not added yet.
        - Suggest improvements to the existing constructs which are incorrect or miss important semantics.
        - Add distributed support. Currently we do not support multiple localities. GPU is not expected for now.
    2. Compiler - 
        - Fix compiler code generation for certain cases when it might fail (this is vague and needs a lot of work to delve into and figure out wrongs and correct those, totally non-trivial - HARD/LARGE project)
        - Add more constructs for the compiler end which already exist in the library.
    3. General Tooling - 
        - Currently there's inconsistency between compilation flags and we need a single command solution i.e. it can build everywhere. Some efforts are on the way https://github.com/SAtacker/chplx/tree/make_integrated_build.
        - Add benchmark measurements tooling. It needs to compile the chapel code using chapel and c++ compilers and give out various statistics available (peak memory usage, timing characteristics, possibly- cache utilization, etc.). We also need non-trivial benchmarks apart from the few we already have.                               
* **Knowledge Prerequisite:** C++, Review [codebase1](https://github.com/ct-clmsn/chplx) [codebase2](https://github.com/SAtacker/chplx/tree/make_integrated_build) so you know what's going on. Codebase1 refers to the basic idea, codebase2 has some efforts to make things bit more integrable rather than having to do it the hard way.
* **Related Talks:** https://youtu.be/JwpQVBcNB7E?si=luZyDNcbD11lVehr https://www.youtube.com/watch?v=aOKqyt00xd8&t=36s
* **Mentor:** Hartmut Kaiser and Shreyas Atre (@SAtacker) and Chris Taylor (please ping us on STEllAR Group's Discord)
* **Project Size:** 350 hour (large project)

### "Green out" our Continuous Integration tests
* **Abstract:** There are tests in our Continuous Integration (CI) that are currently failing. These are mainly under our tests.regressions, tests.segmented_algorithms targets, performance tests and certain new compilers tests (clang-13/14, gcc-12). One can see all the tests that are failing if they randomly select an open PR and scroll down to check the list items indicated with a red 'X'. Fixing those tests would include a wide range of bug hunting tasks and creativity from the student side in order to reproduce them locally until they figure out and fix the errors. 
* **Difficulty:** Easy/Medium
* **Expected result:** All tests in our CI pass (are green).
* **Knowledge Prerequisite:** C++, CMake, slurm
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png)) and Giannis Gonidelis (gonidelis *[at]* hotmail.com)
* **Project Size:** 175 hour (Easy/Medium project)

### Port HPX to iOS and Mac (M1 architecture)
* **Abstract:** HPX has already proven to run efficiently on ARM-based systems. This has been demonstrated with an [application written for Android tablet devices](https://www.youtube.com/watch?v=IwCJpzMi1jc "VanDouken Demo: Using Supercomputer Tech to Animate Paintings"). A port to handheld devices running with iOS would be the next logical step! On top of that since the new Apple M1 ARM-based processors have proven to be very efficient the student should consider providing an HPX version for this architecture as well. To run HPX efficiently on there, we need to adapt our build system to be able to cross-compile for iOS and Mac and add a code to interface with the iOS GUI and other system services. A preexisting Mac support infrastructure exists but the student will need to adapt and update it to current releases.
* **Difficulty:** Easy/Medium
* **Expected result:** Provide a prototype HPX application running on an iPhone or iPad.
* **Knowledge Prerequisite:** C++, Objective-C, iOS
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png)) and Thomas Heller (![thomas%20heller](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/thomas%20heller.png))
* **Project Size:** 350 hour (large project)


### Study the performance of Halide applications running on HPX threads. 
* **Abstract:** [Halide](https://halide-lang.org/) is a programming language designed to facilitate developing high-performance array-based code with regular access to memory on a wide range of modern architectures. Halide also makes it possible to use custom runtimes, such as HPX, in situ of the native runtime. A preliminary [work](https://github.com/STEllAR-GROUP/phylanx_halide/) has shown promising results for the HPX runtime in code generated by Halide. The goal of this project is to investigate the effectiveness of code generated by Halide in libraries that use HPX as a backend. We are notably interested in improving the performance of level 2, and 3 BLAS operations in the [Blaze](https://bitbucket.org/blaze-lib/blaze/src/master/) math library.
* **Difficulty:** Medium
* **Expected result:** Comprehensive performance analysis of Halide code in Blaze and other stencil-like applications.
* **Knowledge Prerequisite:** C++ 
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png)) and Rod Tohid (rtohid [at] cct.lsu.edu)
* **Project Size:** 175 hour (medium project)

### HPX distributed algorithms 
* **Abstract:** Along with the [standard parallel algorithms](https://en.cppreference.com/w/cpp/algorithm) provided by the C++ standard, HPX extends its infrastructure by providing (some of) the corresponding distributed versions of those algorithms that run on multiple nodes and on top of that they take care of communication. We currently miss distributed versions of some of the algorithms, notably distributed sorting should be implemented. This project is about working on implementing one or more of the missing algorithms.
The set of the implemented algorithms can be found [here](https://github.com/STEllAR-GROUP/hpx/tree/master/libs/full/segmented_algorithms/include/hpx/parallel/segmented_algorithms). [Here](/ideas/stear-group/stellar-group-hpx-issues-1338) you can find the corresponding ticket.
* **Difficulty:** Medium/hard
* **Expected result:** Implement segmented (distributed) sorting and/or additional algorithms.
* **Knowledge Prerequisite:** C++, CMake
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png)) and Giannis Gonidelis (gonidelis *[at]* hotmail.com)
* **Project Size:** 350 hour (large project)


### (Re-)Implement executor API on top of sender/receiver infrastructure
* **Abstract:** [P2300](https://wg21.link/p2300) will most likely be accepted for C++26. Our executor API (customization points) currently dispatch to an executor interface defined by wg21.link/p0443R3. All HPX facilities related to scheduling tasks (algorithms, future, dataflow, async, etc.) rely on the executor customization points to perform their operations. Although [major steps](https://github.com/STEllAR-GROUP/hpx/pull/5758) have been taken for the integration of the executors proposal to HPX there is still many facilities that need to be implemented. The project can be correlated with the [Coroutine-like interface project](#coroutine-like-interface) project and the P2300 proposed [awaitables](https://wg21.link/p2300).
* **Difficulty:** Medium
* **Expected result:** The result should be functioning executor customization points built upon senders/receivers.
* **Knowledge Prerequisite:** Parallel algorithms.
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png)) and Giannis Gonidelis (gonidelis *[at]* hotmail.com)
* See [issue #5219 on HPX bug tracker](/ideas/stear-group/stellar-group-hpx-issues-5219) and the corresponding [Pull Request](https://github.com/STEllAR-GROUP/hpx/pull/5758) that's on the works already.
* **Project Size:** 350 hour (large project)


### Explicit Visualization of Accelerators for HPX Trace Visualization
* **Abstract:** HPX traces are collected with APEX and written in as OTF2 files with extensions. These trace files are typically visualized using a Gantt chart or collection of timelines. Presently, there is no differentiation between tasks executed on an accelerator versus other hardware. This project requires (1) investigation regarding what data can be collected about accelerators through HPX and APEX, and (2) design and implementation of how accelerator data is implemented in [Traveler](https://github.com/hdc-arizona/traveler-integrated). Collection will require C++, while the Traveler alterations will also require Python (backend) and Javascript (frontend).  
* **Difficulty:** Medium-Hard
* **Expected result:** Traveler trace visualization includes query support and visual indicators of data regarding accelerators.
* **Knowledge Prerequisite:** C++, Python, Javascript.
* **Mentor:** Kate Isaacs (![kate%20isaacs](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/kate%20isaacs.png)) 
* **Project Size:** Could be 175 hour (medium sized) or 350 hour (large sized) depending on proposal


### Improved Scalability for HPX OTF2 Trace Visualization
* **Abstract:** HPX traces are collected with APEX and written in as OTF2 files with extensions. These trace files are typically visualized using a Gantt chart or collection of timelines in [Traveler](https://github.com/hdc-arizona/traveler-integrated). The present implementation reads the entirety of the trace file before generating the visualization using one of the older APIs to do so. However, the OTF2 interface has support for partial reading of the file and a parallel backend. This project would modify the Gantt chart backend (C++/Python) to utilize these features, thus supporting larger files. The project could also modify the front end to use WebGL (Javascript) when the number of data items is large.
* **Difficulty:** Medium-Hard
* **Expected result:** Files that require more memory than on a single machine can be run from that machine. The time from program-start to visualization is decreased due to the use of large file features.
* **Knowledge Prerequisite:** C++, Python, Javascript.
* **Mentor:** Kate Isaacs (![kate%20isaacs](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/kate%20isaacs.png)) 
* **Project Size:** 175 hour (medium sized)


### Multiple File Load in HPX Trace Visualization
* **Abstract:** HPX traces are collected with APEX and written in as OTF2 files with extensions. These trace files are typically visualized using a Gantt chart or collection of timelines. We want to load multiple of these files at the same time and align the views between the like-charts for comparison in [Traveler](https://github.com/hdc-arizona/traveler-integrated). Traveler alterations will also require Python (backend) and Javascript (frontend).  
* **Difficulty:** Medium-Hard
* **Expected result:** Traveler trace visualization can open multiple files and arranges views so performance can be compared across files.
* **Knowledge Prerequisite:** Python, Javascript.
* **Mentor:** Kate Isaacs (![kate%20isaacs](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/kate%20isaacs.png)) 
* **Project Size:** Could be 175 hour (medium sized)

## AI Project Ideas 
These are project ideas that involve AI methodologies in different applications.
 * [Spatio-Temporal Extrapolation with Generative AI: Advancing Storm Surge Forecast Accuracy through Bias Correction in Unmonitored Areas](#spatio-temporal-extrapolation-with-generative-aI-advancing-storm-surge-forecast-accuracy-through-bias-correction-in-unmonitored-areas)
 * [Spatio-Temporal Extrapolation with GNN: Advancing Storm Surge Forecast Accuracy through Bias Correction in Unmonitored Areas
](#spatio-temporal-extrapolation-with-GNN-advancing-storm-surge-forecast-accuracy-through-bias-correction-in-unmonitored-areas)
 * [Transformer-based Image-to-Graph Conversion](#Transformer-based-Image-to-Graph-Conversion)

### Spatio-Temporal Extrapolation with Generative AI: Advancing Storm Surge Forecast Accuracy through Bias Correction in Unmonitored Areas
* **Abstract:** In 2022, severe storms and tropical cyclones represented 14 out of the 18 documented weather and/or climate related disasters reported in the U.S., leading to a dreadful cost in human lives, but also to an overall financial cost exceeding 135 billion dollars [1]. The pronounced frequency and severity of such events demonstrates the critical importance of improving storm surge forecast tools in terms of both accuracy and efficiency. In this context, recent work aims to predict the systemic error between physics-based storm surge forecast model and observed water level data were obtained from gauge stations and use it to correct the simulation results on gauge stations. However, ensuring the accuracy of water level simulations across extensive and unevenly monitored locations remains a critical challenge. Given the limitations of traditional interpolation methods and the sparse distribution of gauge stations, we propose the innovative use of Generative Artificial Intelligence (AI) to address the challenge of extrapolating bias correction values to unmonitored areas. Generative AI, through its capacity to learn and mimic the distribution of complex datasets, offers a groundbreaking approach to understanding and predicting environmental variables across spatial and temporal scales. By training on available data from gauge stations, Generative AI models can generate accurate bias correction predictions for regions beyond the gauge stations. The proposed methodology leverages the latest advancements in Generative AI, including techniques like Generative Adversarial Networks (GANs) and Variational Autoencoders (VAEs), to model the complex interdependencies within the offsets data. By incorporating spatial correlations and environmental covariates, the Generative AI framework aims to produce spatially coherent and temporally consistent bias corrections across the simulation area. A case study implementing this Generative AI approach will be conducted to validate its effectiveness in enhancing model accuracy.

* **Difficulty:** Medium-Hard
* **Expected result:** Implementation of generative AI AI model for Spatio-Temporal Extrapolation of offsets. 
* **Knowledge Prerequisite:** Python, Machine learning basics  
* **Mentor:** Noujoud Nader (noujoude.nader *[at]* gmail.com) and Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png))
* **Project Size:** 350 hour (large project)


### Spatio-Temporal Extrapolation with GNN: Advancing Storm Surge Forecast Accuracy through Bias Correction in Unmonitored Areas
* **Abstract:** In 2022, severe storms and tropical cyclones represented 14 out of the 18 documented weather and/or climate related disasters reported in the U.S., leading to a dreadful cost in human lives, but also to an overall financial cost exceeding 135 billion dollars [1]. The pronounced frequency and severity of such events demonstrates the critical importance of improving storm surge forecast tools in terms of both accuracy and efficiency. In this context, recent work aims to predict the systemic error between physics-based storm surge forecast model and observed water level data were obtained from gauge stations and use it to correct the simulation results on gauge stations. However, ensuring the accuracy of water level simulations across extensive and unevenly monitored locations remains a critical challenge. Given the limitations of traditional interpolation methods and the sparse distribution of gauge stations, we propose the innovative use of Graph Neural Network (GNN) to address the challenge of extrapolating bias correction values to unmonitored areas. GNNs are inherently good at capturing spatial relationships and dependencies between nodes in a graph. This can be particularly useful for modeling the influence of nearby gauge stations on unmonitored areas. In addition, GNNs can integrate various types of information, including physical properties and geographical context, which can be critical for accurate extrapolation in environmental sciences. They can easily integrate heterogeneous data, making them suitable for our complex environmental systems where offset data is affected by the presence of natural barriers and geographical features, like a lake between two gauge stations.

* **Difficulty:** Medium-Hard
* **Expected result:** Implementation of GNN AI model for Spatio-Temporal Extrapolation of offsets. 
* **Knowledge Prerequisite:** Python, Machine learning basics  
* **Mentor:** Noujoud Nader (noujoude.nader *[at]* gmail.com) and Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png))
* **Project Size:** 350 hour (large project)


### Transformer-based Image-to-Graph Conversion
* **Abstract:** The process of reconstructing graph representations from medical images, known as Image-to-Graph conversion, is a common task, particularly evident in biomedical imaging for extracting vessel graphs. Here, we propose a novel Machine Learning (ML)-based Image-to-Graph pipeline that emphasizes edge features, which are critical for applications such as blood flow simulation. This pipeline incorporates advanced ML algorithms, including the use of the **Transformer** model, to serve dual purposes: firstly, to objectively extract vascular features from medical images without relying on subjective judgment or requiring extensive user skill; and secondly, to facilitate rigorous model validation. For our model training and validation, we will utilize 3D image datasets of healthy and diseased subjects, including those of the brain and lungs.

* **Difficulty:** Medium-Hard
* **Expected result:** Implementation of transformer model for image to graph conversion. 
* **Knowledge Prerequisite:** Python, Machine learning basics, tranformers  
* **Mentor:** Noujoud Nader (noujoude.nader *[at]* gmail.com) and Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png))
* **Project Size:** 350 hour (large project)

## Past Year Projects
These are projects that were worked on in previous years of Google Summer of Code, but still have not been fully resolved. Others in this list might have been partially implemented. If you are interested in any of the following project ideas, please reach out to learn more.
* [Coroutine-like Interface](#coroutine-like-interface)
* [Async I/O using Coroutines and S/R](#async-io-using-coroutines-and-sr) 
* [Add Vectorization to the `par_unseq` Implementations of the Parallel Algorithms](#add-vectorization-to-par_unseq-implementations-of-parallel-algorithms)
 * [Conflict (range-based) Locks](#conflict-range-based-locks)
 * [Standardize and Visualize HPX Benchmarks](#standardize-and-visualize-hpx-benchmarks)
 * [Rustize HPX!](#rustize-hpx)
 * [Pythonize HPX!](#pythonize-hpx)
 * [Create Generic Histogram Performance Counter](#create-generic-histogram-performance-counter)
 * [Fix libCDS broken dependency](#fix-libcds-broken-dependency)

### Coroutine-like Interface
* **Abstract:** HPX is an excellent runtime system for doing task-based parallelism. In its current form, however, the results of tasks can only be expressed in terms of returning from a function. However, there are scenarios where this is not sufficient. One example would be lazy ranges of integers (for example, Fibonacci, 0 to n, etc.). For those, a generator/yield construct would be perfect (more on [coroutines](https://en.cppreference.com/w/cpp/language/coroutines))! Additionally, an option would be to rely on top of the <b>senders/receivers</b> [proposed](http://wg21.link/p2300) facilities, a completely new interface for execution in standard C++ that may (or not) revolutionize the way we implement concurrency.
* **Difficulty:** Medium
* **Expected result:** Implement yield and demonstrate on at least one example
* **Knowledge Prerequisite:** C++
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png)) and Thomas Heller (![thomas%20heller](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/thomas%20heller.png))
* **Project Size:** 350 hour (large project)

### Async I/O using Coroutines and S/R
* **Abstract:** Coroutines along with S/R make a really good use case for async I/O [Ref 1](https://db.in.tum.de/~fent/papers/coroutines.pdf?lang=en). Using the recently added HPX S/R facilities to develop an interface for a relatively faster I/O example would be the goal of this project. Additionally for Linux based platforms with [`io_uring`](https://unixism.net/loti/what_is_io_uring.html) support can have even more performance benefits.
* **Additional References:** 
    * https://github.com/L-v-M/async 
    * https://pabloariasal.github.io/2022/11/12/couring-1/
* **Difficulty:** Easy/Medium
* **Expected result:** Develop a non-trivial use case using the above described tools and HPX.
* **Knowledge Prerequisite:** C++, CMake
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png)) and Giannis Gonidelis (gonidelis *[at]* hotmail.com) and [Shreyas Atre](https://github.com/SAtacker) (Discord: Shreyas)
* **Project Size:** 175 hour (Easy/Medium project)

### Add Vectorization to `par_unseq` Implementations of Parallel Algorithms
* **Abstract:** Our parallel algorithms currently don't support the [`par_unseq` execution policy](http://stellar-group.github.io/hpx/docs/html/hpx.html#hpx.parallel.execution.par_unseq).
  This project is centered around the idea to implement this execution policy for at least some of the existing algorithms (such as `for_each` and similar).
* **Difficulty:** Medium/Hard
* **Expected result:** The result should be functioning parallel algorithms when used with the
  `par_unseq` execution policy. The loop body should end up being vectorized.
* **Knowledge Prerequisite:** Vectorization, parallel algorithms.
* **Mentor:**  Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png)), Srinivas Yadav (vasu.srinivasvasu.14 *[at]* gmail.com), Nikunj Gupta (nikunj *[at]* illinois.edu), Giannis Gonidelis (gonidelis *[at]* hotmail.com)
* See [issue #2271 on HPX bug tracker](/ideas/stear-group/stellar-group-hpx-issues-2271)
* **Project Size:** 350 hour (large project)

### Conflict (Range-Based) Locks
* **Abstract:** Some multi-threaded algorithms may require resources that must be held using a lock, but the locking mechanism may be range-based rather than absolute. Consider a large array of `N` items where a task requires some small subset of the items to be locked while a second task requires a second range. If these tasks are placed into a DAG so that `task2` can only run once `task1` has been completed, it will be inefficient when the range of items used by task2 does not overlap the range from `task1`. When many tasks operate on the range, with randomly overlapping or non-overlapping regions, DAG-based task scheduling leads to a highly inefficient strategy. We need a range based lock that can be templated over `<items>`, and that can then be locked/unlocked on ranges (of those items) and interact with our `future<>` based scheduling so that items will become _ready_ when the range they need has no locks outstanding, and so that when a task releases a lock, any other tasks that overlap the range are in turn signaled as possibly ready. (For an example of how this is used in conventional HPC programming, look up Byte Range locks in MPI for Parallel IO to a single file). A successful implementation can be extended to multi-dimensional locking *2D/3D etc., ideally templated over dimensions and types).
* **Difficulty:** Medium/Hard
* **Expected result:** A test application that creates arrays of items and randomly assigns tasks to operate on regions of those items with locking and schedules the tasks to operate in a non-conflicting way.
* **Knowledge Prerequisite:** Thread-safe programming. Futures.
* **Mentor:** John Biddiscombe (![john%20biddiscombe](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/john%20biddiscombe.png))
* **Project Size:** 350 hour (large project)

### Standardize and Visualize HPX Benchmarks
* **Abstract:** HPX, as a high-performance computing framework, includes various benchmarks to measure the performance of its algorithms and runtime system. However, these benchmarks lack a standardized format and a comprehensive visualization tool that can help in analyzing performance trends over time and across different computing environments. This project aims to standardize the benchmark formats within HPX using third party benchmarking tools (recommendations below) and develop a visualization tool that can display benchmark results in an intuitive manner. The tool will used in conjunction with CI/CD to track and display performance regressions or improvements, and provide insights into the scalability and efficiency of new components.
* **Additional References:** 
    * Recommended Benchmarking Frameworks: [Google Benchmark](https://github.com/google/benchmark), [Nanobench](https://nanobench.ankerl.com/)
    * [Nanobench in HPX](https://github.com/STEllAR-GROUP/hpx/pull/6357)
    * [Google Benchmark in HPX](https://github.com/SAtacker/hpx-template)
* **Difficulty:** Medium/Advanced
* **Expected result:** 1) A unified format for HPX benchmarking using chosen benchmarking framework. 2) Automating the installation of the chosen benchmarking framework in the HPX build system. 3) A visualization tool (suggestion: a python script) to display the results.
* **Knowledge Prerequisite:** C++, Git, Python or plotting framework of your choice
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png)) and Isidoros Tsaousis-Seiras (tsa.isidoros *[at]* gmail.com).
* **Project Size:** 350 hour (Advanced project)

### Rustize HPX!
* **Abstract:** Rust is an increasingly widely adopted language used because of it's performance and apparent safety. Providing performant HPX functionality written in C++ with Rust APIs would facilitate both safety and ease of learning HPX. The student shall design and implement Rust bindings for HPX, exposing all or parts of the HPX functionality with a Rust API. 
* **Difficulty:** Medium
* **Expected result:** Demonstrate functioning bindings by implementing small example scripts for different simple use cases
* **Knowledge Prerequisite:** C++, Rust
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png))
* **Project Size:** 350 hour (large project)

### Pythonize HPX!
* **Abstract:** Python is a widely adopted language due to its simplicity. Providing performant HPX functionality written in C++ with Pythonic APIs would facilitate both usage and ease of learning HPX. The student shall design and implement Python bindings for HPX, exposing all or parts of the HPX functionality with a 'Pythonic' API. This should be possible as Python has a much more dynamic type system than C++. Using [Boost.Python](http://www.boost.org/doc/libs/1_55_0/libs/python/doc/) and/or [Pybind11](https://pybind11.readthedocs.io/en/stable/) seem to be good choices for this.
* **Difficulty:** Medium
* **Expected result:** Demonstrate functioning bindings by implementing small example scripts for different simple use cases
* **Knowledge Prerequisite:** C++, Python
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png))
* **Project Size:** 350 hour (large project)

### Create Generic Histogram Performance Counter
* **Abstract:** HPX supports [performance counters](http://stellar-group.github.io/hpx/docs/html/hpx.html#hpx.manual.performance_counters) that return a set of values for each invocation.
  We have used this to implement performance counters collecting histograms for various characteristics related to parcel coalescing (such as the histogram of the time intervals between parcels). The idea of
  this project is to create a general-purpose performance counter which collects the value of any
  other given performance at given time intervals and calculates a histogram for those values.
  This project could be combined with [Add more arithmetic performance counters](#add-more-arithmetic-performance-counters).
* **Difficulty:** Medium
* **Expected result:** Implement a functioning performance counter which returns the histogram for any
  other given performance counter as collected at given time intervals.
* **Knowledge Prerequisite:** Minimal knowledge of statistical analysis is required.
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png)) and Mikael Simberg (![mikael%20simberg](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/mikael%20simberg.png))
* See [issue #2237 on HPX bug tracker](/ideas/stear-group/stellar-group-hpx-issues-2327)
* **Project Size:** 350 hour (large project)

### Fix libCDS broken dependency
* **Abstract:** [libCDS](https://github.com/khizmax/libcds) is a Concurrent Data Structures library which provides containers that alleviate the user from taking care of synchronization. HPX provides an [integration](https://github.com/STEllAR-GROUP/hpx/blob/99a4b007f49b60809203cac9555a960cde440ef8/CMakeLists.txt#L940-L964) with libCDS which is currently broken. We are looking for a prospective developer that will bring that libCDS up to date with the current version of HPX and provide testing and benchmarking with the contemporary results.
* **Difficulty:** Easy
* **Expected result:** libCDS current version full integration with the latest HPX.
* **Knowledge Prerequisite:** CMake, Data Parallelism, C++.
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png)) and Giannis Gonidelis (gonidelis *[at]* hotmail.com)
* **Project Size:** 350 hour (large project)


## HPX User Projects
These are projects that improve code that uses HPX. In general, the primary goal with these projects is to improve user uptake of HPX by demonstrating its use in other projects, and only minor fixes/changes/extensions should be necessary for the main HPX library itself.

### Implement your favorite Computational Algorithm in HPX 
* **Abstract:** This is an open project for prospective students who don't want to get their hands dirty into core HPX development. The student shall utilize HPX to implement a short independent project that will utilize HPX for performance boost. The program can implement any given problem that requires heavy computational effort from the literature. [Efficient matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm#Parallel_and_distributed_algorithms), sorting, [stencil variations](https://en.wikipedia.org/wiki/Stencil_(numerical_analysis)#See_also) or any AI, Physics related problem would be a good candidate.
An extensive [list of use-case examples](https://github.com/STEllAR-GROUP/hpx/tree/master/examples) is already available in our source code. The goal of this project is for the student to get acquainted with HPX development and contribute to our vast range of applications.
* **Difficulty:** Easy
* **Expected result:** Implement a standalone program that utilizes HPX for performance. 
* **Knowledge Prerequisite:** C++ 
* **Mentor:**  Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png))
 and Giannis Gonidelis (gonidelis *[at]* hotmail.com)
* **Project Size:** 175 hour (medium sized)

### Conduct a thorough Performance Analysis on HPX Parallel Algorithms (and optimize)
* **Abstract:** HPX [implements](https://github.com/STEllAR-GROUP/hpx/tree/master/libs/core/algorithms/include/hpx/parallel/algorithms) all the C++ standard [algorithms](https://en.cppreference.com/w/cpp/algorithm) along with their [ranges](https://en.cppreference.com/w/cpp/ranges) counterparts. Conducting extensive performance analysis on the existing implementations and coming up with possible optimizations would improve the efficiency of our parallel algorithms and boost HPX performance in general. The student shall expect to work both on top of HPX by writing custom benchmarks for [weak and strong scaling](https://en.wikipedia.org/wiki/Scalability#Weak_versus_strong_scaling), evaluate the results and perform source optimizations under the hood (core development).
* **Difficulty:** Medium
* **Expected result:** Boost the performance of at least one C++ standard algorithm in HPX. 
* **Knowledge Prerequisite:** C++
* **Mentor:** Giannis Gonidelis (gonidelis *[at]* hotmail.com) and Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png))
* **Project Size:** 350 hour (large project)
 
## Legacy Project Ideas 
These are project ideas from previous Summer of Code years that we are still interested in working on, but it might be harder to find a mentor willing to supervise a student. Therefore, we would expect only very self-motivated and capable students to select a project from the legacy category. We cannot guarantee that we will select a project from this list unless we are quite satisfied that the student can complete the work.
 * [Implement Your Favorite Parcelport Backend](#implement-your-favorite-parcelport-backend)
 * [Implement A Faster Associative Container for GIDs](#implement-a-faster-associative-container-for-gids)
 * [Create A Parcelport Based on WebSockets](#create-a-parcelport-based-on-websockets)
 * [All to All Communications](#all-to-all-communications)
 * [Distributed Component Placement](#distributed-component-placement)
 * [Port Graph500 to HPX](#port-graph500-to-hpx)
 * [Port Mantevo MiniApps to HPX](#port-mantevo-miniapps-to-hpx)
 * [Distributed solver and load balancing for Peridynamics using asynchronous parallelism](#distributed-solver-and-load-balancing-for-peridynamics-using-asynchronous-parallelism)
 * [Bug Hunter](#bug-hunter)
 * [Project Template](#project-template)

We are looking to fund work on a number of different kinds of proposals (for more details about concrete project ideas, see below):
* Extensions to existing library features,
* New distributed data structures and algorithms
* Multiple competing proposals for the same project

### Implement Your Favorite Parcelport Backend
* **Abstract:** The HPX runtime system uses a module called Parcelport to deliver packages over the network. An efficient implementation of this layer is indispensable and we are searching for new backend implementations based on [CCI](https://github.com/CCI/cci), [ucx](https://github.com/openucx/ucx "Unified Communication X"), [libfabric](https://github.com/ofiwg/libfabric "Open Fabric Interfaces"), or [GASNet](https://gasnet.lbl.gov). These mentioned abstractions over various network transport layers offer the ability to do fast, one-sided RDMA transfers. The purpose of
this project is to explore one of these and implement a parcelport using it.
* **Difficulty:** Medium-Hard
* **Expected result:** A proof of concept for a chosen backend implementation with performance results
* **Knowledge Prerequisite:** C++, Basic understanding of Network transports
* **Mentor:** Thomas Heller (![thomas%20heller](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/thomas%20heller.png))
* **Project Size:** 350 hour (large project)

### Implement a Faster Associative Container for GIDs
* **Abstract:** The HPX runtime system uses Active Global Address Space (AGAS) to address global objects. Objects in HPX are identified by a 128-bit unique global identifier, abbreviated as a GID. The performance of HPX relies on fast lookups of GIDs in associative containers. We have experimented with binary search trees (`std::map`) and hash maps (`std::unordered_map`). However, we believe that we can implement a search data structure based on n-ary trees, tries, or radix trees that exploit the structure of GIDs such that it allows us to have faster lookup and insertion.
* **Difficulty:** Medium-Hard
* **Expected result:** Various container approaches to choose from together with realistic benchmarks to show the performance properties
* **Knowledge Prerequisite:** C++, Algorithms
* **Mentor:** Thomas Heller (![thomas%20heller](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/thomas%20heller.png))
* **Project Size:** 350 hour (large project)

### Create A Parcelport Based on WebSockets
* **Abstract:** Create a new parcelport that is based on WebSockets. The [WebSockets++](http://www.zaphoyd.com/websocketpp "C++ WebSocket Client/Server Library") library seems to be a perfect starting point to avoid having to dig into the WebSocket protocol too deeply.
* **Difficulty:** Medium-Hard
* **Expected result:** A proof of concept parcelport based on WebSockets with benchmark results
* **Knowledge Prerequisite:** C++, knowing WebSockets is a plus
* **Mentor:** Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png)) and Thomas Heller (![thomas%20heller](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/thomas%20heller.png))
* **Project Size:** 350 hour (large project)

### All to All Communications
* **Abstract:** Design and implement efficient all-to-all communication LCOs. While MPI provides mechanisms for [broadcasting](https://www.open-mpi.org/doc/v1.8/man3/MPI_Bcast.3.php), [scattering](http://www.open-mpi.org/doc/v1.5/man3/MPI_Scatter.3.php) and [gathering](https://www.open-mpi.org/doc/v1.8/man3/MPI_Gather.3.php) with all MPI processes inside a communicator, HPX currently misses this feature. It should be possible to exploit the Active Global Address Space to mimic global all-to-all communications without actually communicating with every participating locality. Different strategies should be implemented and tested. A first and very basic [implementation of broadcast](https://github.com/STEllAR-GROUP/hpx/blob/master/hpx/lcos/broadcast.hpp) already exists which tries to tackle the above-described problem. However, more strategies for granularity control and locality exploitation need to be investigated and implemented. We also have the first version of a [gather utility](https://github.com/STEllAR-GROUP/hpx/blob/master/hpx/lcos/gather.hpp) implemented.
* **Difficulty:** Medium-Hard
* **Expected result:** Implement benchmarks and provide performance results for the implemented algorithms
* **Knowledge Prerequisite:** C++
* **Mentor:** Thomas Heller (![thomas%20heller](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/thomas%20heller.png)) and Andreas Schaefer (![andreas%20schaefer](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/andreas%20schaefer.png))
* **Project Size:** 175 hour (medium sized)

### Distributed Component Placement
* **Abstract:** Implement an EDSL to specify the placement policies for components. This could be done similar to [Chapels Domain Maps] (http://chapel.cray.com/tutorials/SC12/SC12-6-DomainMaps.pdf). In Addition, allocators can be built on top of those domain maps to use with C++ standard library containers. This is one of the key features to allow users to efficiently write parallel algorithms without having them worried too much about the initial placement of their distributed objects in the Global Address space
* **Difficulty:** Medium-Hard
* **Expected result:** Provide at least one policy that automatically creates components in the global address space
* **Knowledge Prerequisite:** C++
* **Mentor:** Thomas Heller (![thomas%20heller](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/thomas%20heller.png)) and Hartmut Kaiser (![hartmut%20kaiser](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/hartmut%20kaiser.png))
* **Project Size:** 350 hour (large project)

### Port Graph500 to HPX
* **Abstract:** Implement Graph500 using the HPX Runtime System. Graph500 is the benchmark used by the HPC industry to model important factors of many modern parallel analytical workloads. The Graph500 list is a performance list of systems using the benchmark and was designed to augment the Top 500 list. The current Graph500 benchmarks are implemented using OpenMP and MPI. HPX is well suited for the fine-grain and irregular workloads of graph applications. Porting Graph500 to HPX would require replacing the inherent barrier synchronization with asynchronous communications of HPX, producing a new benchmark for the HPC community as well as an addition to the HPX benchmark suite. See http://www.graph500.org/ for information on the present Graph500 implementations.
* **Difficulty:** Medium
* **Expected result:** New implementation of the Graph500 benchmark.
* **Knowledge Prerequisite:** C++
* **Mentor:** Patricia Grubel (![patricia%20grubel](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/patricia%20grubel.png)), and Thomas Heller (![thomas%20heller](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/thomas%20heller.png))
* **Project Size:** 350 hour (large project)

### Port Mantevo MiniApps to HPX
* **Abstract:** Implement a version of one or more mini-apps from the Mantevo project (http://mantevo.org/ "Mantevo Project Home Page") using HPX Runtime System. We are interested in mini-applications ported to HPX that have irregular workloads. Some of these are under development, and we will have access to them in addition to those listed on the site. On the site, MiniFE and phdMESH would be good addition to include in HPX benchmark suites. Porting the mini-apps would require porting the apps from C to C++ and replacing the inherent barrier synchronization with HPX's asynchronous communication. This project would be a great addition to the HPX benchmark suite and the HPC community.
* **Difficulty:** Medium
* **Expected result:** New implementation of a Mantevo mini-app or apps.
* **Knowledge Prerequisite:** C, C++
* **Mentor:** Patricia Grubel (![patricia%20grubel](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/patricia%20grubel.png)) and Thomas Heller (![thomas%20heller](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/thomas%20heller.png))
* **Project Size:** 175 hour (medium sized)

### Distributed solver and load balancing for Peridynamics using asynchronous parallelism
* **Abstract:**
Peridynamics is a reformulation of classical continuum mechanics (e.g., linear elastodynamics). The internal force at any point in the solid results from the interaction of that point with neighboring points within some distance ϵ. Typically, ϵ is much larger than the mesh size. As a result, the computation is more intensive and introduces more substantial data dependencies when partitioning the domain for parallel implementation. This project aims to develop and implement a distributed solver for Peridynamics in an existing codebase [1]. This project will benefit from the last year's GSoC student's effort on a similar goal but for a simplified nonlocal model [2]. In [2], several challenges associated with the parallelization of nonlocal models are highlighted, and algorithms are developed to address the challenges. In this project, we will apply techniques in [2] to the Peridynamics problem; first, we will implement the distributed solver; second, we will optimize the code so that compute node does the information exchange and calculation on the free degree of freedoms (DoFs) simultaneously to minimize the wait time. Finally, if possible, we will add the load balancing algorithm [2]. Here for the given compute node, free DoFs are those DoFs that do not depend on the data owned by other compute nodes. After GSoC, we intend to write a workshop paper based on this project's efforts and possibly present it at a computer science conference.
* **Difficulty:** Medium-Hard
* **Expected result:** Extend the existing shared memory code to a distributd code
* **Knowledge Prerequisite:** C++
* **Mentor:** Patrick Diehl (![patrick%20diehl](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/patrick%20diehl.png)) and Prashant K. Jha (![prashantk%jha](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/Prashant.png))
* **Project Size:** 350 hour (large project)

[1] [https://github.com/nonlocalmodels/NLMech](https://github.com/nonlocalmodels/NLMech)

[2] [https://arxiv.org/abs/2102.03819](https://arxiv.org/abs/2102.03819)

### Port the GAP Benchmark Suite to HPX

* **Abstract:**

GAP [1] provides a benchmark suite for the following graph algorithms:

* **Breadth-First Search (BFS)** - direction optimizing
* **Single-Source Shortest Paths (SSSP)** - delta stepping
* **PageRank (PR)** - iterative method in pull direction, Gauss-Seidel & Jacobi
* **Connected Components (CC)** - Afforest & Shiloach-Vishkin
* **Betweenness Centrality (BC)** - Brandes
* **Triangle Counting (TC)** - order invariant with possible degree relabelling

This project requires modifying the existing benchmark suite to use HPX's data parallelism and asynchrony capabilities. This project serves as a stepping stone to a distributed implementation. After GSoC, we intend to write a workshop paper based on this project's efforts and possibly present it at a computer science conference.

* **Difficulty:** Easy-Medium
* **Expected result:** Provide an HPX implementation of the existing shared memory code
* **Knowledge Prerequisite:** C++
* **Mentor:** Chris Taylor

[1] [http://gap.cs.berkeley.edu/benchmark.html](http://gap.cs.berkeley.edu/benchmark.html)

[2] [https://github.com/sbeamer/gapbs](https://github.com/sbeamer/gapbs)

### HPX backend for OpenMPI

* **Abstract:**

This project requires modifying the existing OpenMPI implementation to include HPX support. This project will improve distributed HPX application performance. After GSoC, we intend to write a workshop paper based on this project's efforts and possibly present it at a computer science conference.

* **Difficulty:** Medium
* **Expected result:** HPX integration with OpenMPI
* **Knowledge Prerequisite:** C/C++
* **Mentor:** Chris Taylor

### Bug Hunter
* **Abstract:** In addition to our extensive ideas list, several active tickets are listed in our [issue tracker](/ideas/stear-group/stellar-group-hpx-issues) which are worth tackling as a separate project. Feel free to talk to us if you find something interesting. A prospective student should pick at least one ticket with medium to hard difficulty and discuss how to resolve it.
* **Difficulty:** Medium-Hard
* **Expected result:** The selected issues need to be fixed
* **Knowledge Prerequisite:** C++
* **Mentor:** Thomas Heller (![thomas%20heller](https://raw.githubusercontent.com/wiki/STEllAR-GROUP/hpx/pics/thomas%20heller.png))
* **Project Size:** 175 hour (medium sized)

* * *

### Project: Template
* **Abstract:**
* **Difficulty:**
* **Expected result:**
* **Knowledge Prerequisite:** 
* **Mentor:**
