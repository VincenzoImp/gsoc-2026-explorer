# MetaCall — Project Ideas

**Source:** https://github.com/metacall/gsoc-2026
**Scraped:** 2026-02-22T23:28:47.583731

---

List of project ideas for contributors applying to the Google Summer of Code program in 2026 (GSoC 2026).

Please always refer to the [official timeline](https://developers.google.com/open-source/gsoc/timeline).

First of all, and if you have not done that yet, read [the contributor guide](https://google.github.io/gsocguides/student/) which will allow you to understand all this process and how the program works overall. Refer to its left side menu to quick access sections that may interest you the most, although we recommend you to read everything.

This is a required step unless you have dived in into the existing codebase and understood everything perfectly (very hard) and the idea you prefer is on the list below.

If your idea is not listed, please discuss it with the mentors in the available [contact channels](https://github.com/metacall/gsoc-2026?tab=readme-ov-file#find-us). We're always open to new ideas and won't hesitate on choosing them if you demonstrate to be a good candidate!

- You're committing to a project and we may ask you to publicly publish your weekly progress on it.
- We will repeatedly ask you to give feedback on our mentorship and management.
- You wholeheartedly agree with the
[code of conduct](https://github.com/metacall/core/blob/develop/.github/CODE_OF_CONDUCT.md). - You must tell us if there's any proposed idea that you don't think would fit the timeline or could be boring (yes, we're asking for feedback).

We recommend you to follow [Google's guide to Writing a Proposal](https://google.github.io/gsocguides/student/writing-a-proposal) as we won't be too harsh on the format and we won't provide any template. But hey, we're giving you a starting point!

You can send the proposal link to any readable format you wish: Google Docs, plain text, in markdown... and preferably hosted online, accessible with a common browser without downloading anything.

We **highly recommend you to ask for a review** anytime to the community or mentor candidates before the contributor application deadline. It's much easier if you get feedback early than to wait for the last moment.

In order to fit properly our organization standards of how to use AI, [you can check here our policy](/ideas/metacall/blob-main-ai-usage-policy).

You can also propose your own.

**Skills**: C/C++, Programming Language Parsers

**Expected size of the project**: Medium (175 hours)

**Difficulty rating**: Medium

**Description**:

MetaCall Core right now implements support for multiple languages and it provides runtime instrospection by multiple methodologies. This allows to have information for executing the calls in a type safe manner when possible, or list the functions, classes or objects that are loaded into it. This minimal information is only usable for the runtime normally. There is cases like Intellisense or Function Mesh projects, we need to provide a standard tool for generating ASTs from multi-language projects. In this project we will be using a tool like [Tree Sitter](https://tree-sitter.github.io/tree-sitter/) for generating an AST with all the dependency tree between multiple languages. This will be crucial for representing mixed programming language projects in an unified way, so this can be later on consumed by our Visual Studio Code plugin for having Intellisense or by the Function Mesh for breaking down a project in other subparts and distributing the workload.

**Expected outcomes**:

- Cross-platform tool and library written in C/C++ that can be used as a CLI or from a simple C API that can be embeeded into other projects for parsing programming languages supported by MetaCall Core.
- It should be able to list all the functions and classes exported by any language.
- It should be able to create a dependency tree of a multi-language project.

**Possible mentors**: Thomas Rory Gummerson, Vicente Eduardo Ferrer Garcia, Fernando Vaño Garcia, Gil Arasa Verge.

**Resources**:

- Tree Sitter Documentation:
[https://tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/) - Tree Sitter C API:
[https://github.com/tree-sitter/tree-sitter/blob/master/lib/include/tree_sitter/api.h](https://github.com/tree-sitter/tree-sitter/blob/master/lib/include/tree_sitter/api.h) - Tree Sitter Tutorial:
[https://dev.to/shrsv/making-sense-of-tree-sitters-c-api-2318](https://dev.to/shrsv/making-sense-of-tree-sitters-c-api-2318)

**Skills**: C/C++, Distributed Systems, Networking, Compiler Design

**Expected size of the project**: Large (350 hours)

**Difficulty rating**: High

**Description**:

This project focuses on converting monolithic applications into scalable microservices by making each function or module a separate service. By utilizing a Remote Procedure Call (RPC) loader, the goal is to enable functions to communicate across multiple servers, yet appear as local calls to developers. Inspired by Erlang’s distributed computing model, the system would create a seamless environment where developers can build applications that scale effortlessly, without worrying about the complexities of distributed systems. The core challenge is to develop a compiler or runtime system capable of identifying and switching between servers dynamically based on function calls, ensuring minimal overhead for the developer while maximizing system performance and scalability.

**Expected outcomes**:

- A functional distributed mesh system that abstracts communication complexities for developers.
- A compiler or runtime capable of identifying function placement on servers dynamically.
- A scalable system that can be easily integrated into existing monolithic codebases.
- Comprehensive documentation and a guide for integrating existing applications into the mesh architecture.

**Possible mentors**: Thomas Rory Gummerson, Vicente Eduardo Ferrer Garcia, Fernando Vaño Garcia, Gil Arasa Verge, Jose Antonio Dominguez.

**Resources**:

- MetaCall Express FaaS RPC Example:
[https://github.com/metacall/express-faas-rpc-example](https://github.com/metacall/express-faas-rpc-example) - MetaCall Protocol:
[https://github.com/metacall/protocol](https://github.com/metacall/protocol) - MetaCall RPC Loader:
[https://github.com/metacall/core/tree/develop/source/loaders/rpc_loader](https://github.com/metacall/core/tree/develop/source/loaders/rpc_loader)

**Skills**: C/C++, Debugging, Tooling, CI/CD, Low-level Instrumentation

**Expected size of the project**: Small (90 hours)

**Difficulty rating**: High

**Description**:

This project aims to significantly improve code coverage reporting and memory tracking reliability across platforms. The current memory tracking mechanism is very basic and cannot detect leaks in detail, making debugging difficult and reducing developer productivity. Additionally, several tests fail on specific architectures such as ARM64 and PPC64, often without meaningful error messages, and these failures are hard to reproduce locally since they only appear in CI virtualized environments.

The project will explore extending support of existing tools such as Valgrind and AddressSanitizer (ASan) to improve memory leak detection, diagnostics, and reporting. In parallel, it will investigate and implement a custom lightweight instrumentation layer tailored to the project’s runtime, allowing fine-grained tracking of allocations, deallocations, and execution paths without destabilizing the application. A strong focus will be placed on observability, improving logs, traces, and error reporting in CI environments to make elusive bugs easier to detect and reproduce.

**Expected outcomes**:

- Improved memory tracking system that reports leaks without crashing the application.
- Better integration and evaluation of Valgrind and ASan for automated testing and diagnostics.
- A custom code instrumentation mechanism for memory usage and code coverage tracking.
- Enhanced observability in CI pipelines, especially for ARM64 and PPC64 architectures.
- Clear, actionable error messages and documentation for debugging hard-to-reproduce issues.

**Possible mentors**: Thomas Rory Gummerson, Vicente Eduardo Ferrer Garcia, Fernando Vaño Garcia, Gil Arasa Verge, Mostafa Wael Kamal.

**Resources**:

- Sanitizer Setup:
[https://github.com/metacall/core/blob/a370a7f0fb7b1d70dec04d48d3e713e8fc3f1058/cmake/CompileOptions.cmake#L112](https://github.com/metacall/core/blob/a370a7f0fb7b1d70dec04d48d3e713e8fc3f1058/cmake/CompileOptions.cmake#L112) - Valgrind Setup:
[https://github.com/metacall/core/blob/a370a7f0fb7b1d70dec04d48d3e713e8fc3f1058/source/tests/CMakeLists.txt#L55](https://github.com/metacall/core/blob/a370a7f0fb7b1d70dec04d48d3e713e8fc3f1058/source/tests/CMakeLists.txt#L55) - Memory Tracker:
[https://github.com/metacall/core/blob/a370a7f0fb7b1d70dec04d48d3e713e8fc3f1058/source/reflect/include/reflect/reflect_memory_tracker.h](https://github.com/metacall/core/blob/a370a7f0fb7b1d70dec04d48d3e713e8fc3f1058/source/reflect/include/reflect/reflect_memory_tracker.h)

**Skills**: TypeScript, Testing, CI/CD

**Expected size of the project**: Small (90 hours)

**Difficulty rating**: Medium

**Description**:

This project focuses on completing and stabilizing the existing MetaCall Deploy and MetaCall FaaS (Function as a Service) infrastructure. Unlike previous years where MetaCall FaaS required a full reimplementation, the core functionality is now largely in place, and the remaining work consists of resolving pending issues, completing unimplemented features, and finalizing the developer workflow.

MetaCall FaaS enables developers to locally test cloud functions in an environment that closely mimics the production MetaCall FaaS platform. This is a critical component of the MetaCall ecosystem, as it allows developers to validate distributed polyglot applications before deployment. At the moment, the project has partial test coverage (9 tests passing, 6 pending), and several issues remain open that block a fully usable release.

The project will involve fixing failing and pending tests, polishing the TypeScript implementation, and improving the integration between MetaCall Deploy, MetaCall FaaS, and the MetaCall CLI. While the project is closely related to DevOps, it also requires hands-on work in the TypeScript codebase and coordination with MetaCall Protocol to ensure code reuse and consistency.

**Expected outcomes**:

- Completion of pending features in MetaCall Deploy and MetaCall FaaS.
- All tests passing, with improved test coverage and stability.
- A reliable local FaaS environment for testing MetaCall projects.
- Improved integration with MetaCall CLI for a smoother developer workflow.
- Updated documentation describing usage, limitations, and deployment flow.

**Possible mentors**: Thomas Rory Gummerson, Jose Antonio Dominguez, Alexandre Gimenez Fernandez, Param Siddharth, Raj Aryan.

**Resources**:

- MetaCall FaaS (TypeScript):
[https://github.com/metacall/faas](https://github.com/metacall/faas) - MetaCall Deploy:
[https://github.com/metacall/deploy](https://github.com/metacall/deploy) - MetaCall FaaS Dashboard:
[https://dashboard.metacall.io](https://dashboard.metacall.io) - MetaCall Protocol:
[https://github.com/metacall/protocol](https://github.com/metacall/protocol) - Video - Deploying Functions into MetaCall FaaS:
[https://www.youtube.com/watch?v=2RAqTmQAWEc](https://www.youtube.com/watch?v=2RAqTmQAWEc)

**Skills**: Rust, TypeScript, React, Server-Side Rendering, CI/CD

**Expected size of the project**: Large (350 hours)

**Difficulty rating**: Medium

**Description**:

This project focuses on enhancing the MetaCall SSR (Server-Side Rendering) server, which allows high-performance React rendering on the backend across multiple programming languages. While the project has proven its potential in performance benchmarks, it currently faces a number of challenges, including failing tests and stability issues in development mode.

The goal is to stabilize the existing implementation, resolve bugs, and improve the overall developer experience. Key objectives include fixing the failing tests, addressing issues specific to development mode (such as hot reloading, error handling, and debugging), and making MetaSSR fully functional for building and deploying websites in a production environment.

The project will involve deep work in both Rust and TypeScript to ensure seamless integration between the languages. Additionally, it will improve the error reporting, enhance the testing framework, and streamline CI/CD workflows to ensure reliability and scalability for the MetaCall SSR server.

**Expected outcomes**:

- A stable and fully functional MetaCall SSR server with a reliable development mode.
- Fixed failing tests and improved test coverage.
- Improved error handling and debugging experience.
- Seamless integration of React on the backend with minimal friction in deployment.
- Enhanced CI/CD pipelines for automated testing and deployment.

**Possible mentors**: Thomas Rory Gummerson, Vicente Eduardo Ferrer Garcia, Gil Arasa Verge, Mostafa Wael Kamal, Alexandre Gimenez Fernandez, Param Siddharth, Jose Antonio Dominguez, Raj Aryan.

**Resources**:

- MetaSSR Repository:
[https://github.com/metacall/metassr](https://github.com/metacall/metassr) - Previous work:
[https://github.com/metacall/gsoc-2023?tab=readme-ov-file#rust-actix--typescript-react-server-side-rendering-tsx-framework](https://github.com/metacall/gsoc-2023?tab=readme-ov-file#rust-actix--typescript-react-server-side-rendering-tsx-framework)

**Skills**: Rust

**Expected size of the project**: Medium (175 hours)

**Difficulty rating**: Hard

**Description**:

Few years ago [Rust Loader was implemented](https://github.com/metacall/gsoc-2022?tab=readme-ov-file#rust-loader-support) but the code has became outdated due to nature of Rust Compiler unstable API / ABI. This year the code was cleaned, all dependencies were deleted and it was able to compile and run again inside the CI but the version of the compiler supported is still very old (nightly-2021-12-04). The idea of this project is to update to the latest version and add more tests and examples with tutorials. It will be also interesting to find a portable version, or at least to prevent depending on unstable Rust Compiler API (although I am not sure this is possible). Showing examples of mixing Rust and C++ would or script languages using Rust directly without need of using macros in the original Rust code would be also interesting, also [updating existing examples](https://github.com/metacall/python-rust-melody-example). Adding support for more types will be also interesting.

**Expected outcomes**: Implement a fully functional version of the Rust Loader with the latest compiler API. Extend the functionalities that are not implemented and provide more tests and examples with some tutorials about how to use it. Update existing tutorials using Rust Loader.

**Possible mentors**: Vicente Eduardo Ferrer Garcia, Fernando Vaño Garcia, Gil Arasa Verge, Thomas Rory Gummerson.

**Resources**:

- MetaCall Rust Loader Code:
[https://github.com/metacall/core/tree/a370a7f0fb7b1d70dec04d48d3e713e8fc3f1058/source/loaders/rs_loader](https://github.com/metacall/core/tree/a370a7f0fb7b1d70dec04d48d3e713e8fc3f1058/source/loaders/rs_loader) - Previous Work:
[metacall/core#443](https://github.com/metacall/core/issues/443)

**Skills**: GitHub Actions, C/C++, CMake Build System, Homebrew, Guix, Windows Package Managers

**Expected size of the project**: Medium (175 hours)

**Difficulty rating**: Medium

**Description**:

MetaCall Core has support for C by using `libffi`

, `libclang`

and `tcc`

. This is widely tested in Linux on the `metacall/core`

CI but lacks the implementation for MacOs and Windows. The objective of this project is to provide testing support in the Core for [Windows](https://github.com/metacall/core/pull/458) and [MacOs](https://github.com/metacall/core/pull/445) platforms, and once this is done we should implement this in the Distributables repositories. For this requirement, we will need to implement it in Guix (Linux), Homebrew (MacOs) and manually installing with Batch (Windows). It is not easy because the task requires knowledge of CMake build system and knowledge about different architectures. It willl be difficult but the final result of this is that we will be to bootstrap metacall itself with this. All the platforms will contain metacall.h and the metacall library and we can generate the API of metacall itself for multiples languages by using the C Loader. The explanation of this idea itself can be difficult because we are assuming some previous basic knowledge on MetaCall Core, but if you are intereseted you can ask in our chat groups for further explanation.

**Expected outcomes**: MacOs and Windows C Loader support in the Core and the distribution of the C Loader for Windows, MacOs and Linux. We should able to run things like: `metacall test.c`

, once this is implemented.

**Possible mentors**: Vicente Eduardo Ferrer Garcia, Fernando Vaño Garcia, Gil Arasa Verge, Param Siddharth, Mostafa Wael Kamal, Raj Aryan.

**Resources**:

- Previous Work:
[metacall/core#458](https://github.com/metacall/core/pull/458)&[metacall/core#445](https://github.com/metacall/core/pull/445) - Known Issues:
[metacall/core#442](https://github.com/metacall/core/issues/442) - Guix
`libclang`

:[https://git.savannah.gnu.org/cgit/guix.git/tree/gnu/packages/llvm.scm#n2160](https://git.savannah.gnu.org/cgit/guix.git/tree/gnu/packages/llvm.scm#n2160) - Guix
`tcc`

:[https://packages.guix.gnu.org/packages/tcc/](https://packages.guix.gnu.org/packages/tcc/) - Guix
`libffi`

:[https://packages.guix.gnu.org/packages/libffi](https://packages.guix.gnu.org/packages/libffi)

**Skills**: Artificial Intelligence, Model Context Protocol, Serverless Architectures, API Design, JSON, Context Management, Cloud Platforms, Python or TypeScript

**Expected size of the project**: Medium (175 hours)

**Difficulty rating**: Medium

**Description**:

This project aims to integrate the Model Context Protocol (MCP) into MetaCall’s Deploy and FaaS modules, enabling context-aware serverless function deployments. MCP facilitates sharing context between models, which is essential for AI/ML-driven workflows where models maintain or adapt their state across invocations. The integration will focus on storing and propagating context data across functions, allowing seamless state transfer in multi-runtime serverless environments.

The outcome will include a fully functional API for managing and sharing model context, along with middleware to handle context serialization and propagation in cloud-native environments. This functionality will be published as a reusable component, enabling other MetaCall users to deploy context-aware functions.

**Expected outcomes**:

- Implement a minimal project that can be used for Claude or similar LLMs from Visual Studio Code or Antigravity that allows to deploy functions, list the existing ones, or run them locally in multiple languages.
- Documentation and integration for the project in order to make it ready to use for other developers.
- Testing for verifying that the tooling works and it's future proof.

**Possible mentors**: Jose Antonio Dominguez, Alexandre Gimenez Fernandez, Param Siddharth, Mostafa Wael Kamal, Raj Aryan.

**Resources**:

- Model Context Protocol Documentation:
[https://modelcontextprotocol.io/docs/getting-started/intro](https://modelcontextprotocol.io/docs/getting-started/intro) - Model Context Protocol SDK:
[https://modelcontextprotocol.io/docs/sdk](https://modelcontextprotocol.io/docs/sdk) - MetaCall Deploy:
[https://github.com/metacall/deploy](https://github.com/metacall/deploy) - MetaCall FaaS:
[https://github.com/metacall/faas](https://github.com/metacall/faas) - MetaCall Dashboard:
[https://metacall.io/dashboard](https://metacall.io/dashboard) - Video - Deploying Functions into MetaCall FaaS:
[https://www.youtube.com/watch?v=2RAqTmQAWEc](https://www.youtube.com/watch?v=2RAqTmQAWEc)

**Skills**: Cross-platform Development, C/C++, Build Systems, Shell Scripting (Bash), PowerShell, CI/CD, Toolchains

**Expected size of the project**: Medium (175 hours)

**Difficulty rating**: Medium

**Description**:

This project aims to significantly expand MetaCall’s platform and architecture support beyond its current scope. At present, MetaCall supports Linux across multiple architectures (amd64 variants, 386, arm, arm64, riscv64), Windows using the MSVC toolchain, and macOS on both Intel and Apple Silicon. While this already covers many use cases, there is strong interest in supporting additional platforms and environments to improve adoption and portability.

The main goal of this project is to add first-class support for new targets such as Windows via MinGW and Cygwin, as well as additional operating systems like Android and FreeBSD. This involves adapting the build and environment setup logic to correctly detect, configure, and compile MetaCall on these platforms.

A key constraint of the project is that all platform logic must be implemented inside the portable environment setup scripts ([./tools/metacall-environment.sh](https://github.com/metacall/core/blob/565bcbfd785442c2155a89661de0b2b0d125fdf3/tools/metacall-environment.sh) and [./tools/metacall-environment.ps1](https://github.com/metacall/core/blob/565bcbfd785442c2155a89661de0b2b0d125fdf3/tools/metacall-environment.ps1). This ensures that platform support is not tightly coupled to GitHub Actions or any specific CI provider, and that developers can reproduce builds locally with the same tooling used in CI.

In parallel, the project will design and add CI pipelines to automatically build and test MetaCall on all supported platforms and architectures. This will help catch platform-specific regressions early and improve overall reliability.

**Expected outcomes**:

- Support for additional Windows environments, including MinGW and Cygwin.
- Initial support for new platforms such as Android and FreeBSD.
- Refactored and extended metacall-environment scripts to handle platform detection and setup in a portable way.
- CI pipelines covering all supported platforms and architectures.
- Documentation describing platform requirements, limitations, and setup instructions.

**Possible mentors**: Vicente Eduardo Ferrer Garcia, Fernando Vaño Garcia, Gil Arasa Verge, Thomas Rory Gummerson.

**Resources**:

- MetaCall Environment Scripts:
- MetaCall Core Repository:
[https://github.com/metacall/core](https://github.com/metacall/core) - Cross-compilation and Toolchain Documentation (GCC, Clang, MinGW, Android NDK)

**Skills**: Zig, Systems Programming, C

**Expected size of the project**: Small (90 hours)

**Difficulty rating**: Medium

**Description**:

The goal of this project is to create a new Port for MetaCall in Zig, allowing Zig programs to call and integrate other languages like JavaScript, Python, Ruby, and more. This project will require designing and implementing the Zig port from scratch, leveraging Zig's unique features such as comptime to simplify and improve the API's ergonomics for end users. This project will need to implement all supported types of MetaCall, also async APIs and different loading methodologies. Key aspects to be addressed:

- Language Interoperability: Develop the necessary bindings and functionality to enable Zig to call functions from other supported MetaCall languages.
- API Design: Use comptime to build a concise, ergonomic, and type-safe API that makes it easy for developers to integrate MetaCall into their Zig projects.
- Build System: Ensure the port supports using an already installed version of MetaCall without requiring a full recompilation.
- Testing and Documentation: Include extensive tests, documentation, and usage examples.
- Memory Safety: Pay special attention to avoiding memory leaks and ensuring safe integration with Zig's memory model.

Additionally, the project should produce a basic tutorial or article showcasing the Zig port, providing examples of how it can be used to create polyglot applications.

**Expected outcomes**:

- A fully functional Zig port for MetaCall that supports calling multiple languages.
- Comprehensive documentation, tests, and usage examples.
- A tutorial or article demonstrating how developers can use the Zig port to build polyglot applications.

**Possible mentors**: Thomas Rory Gummerson, Vicente Eduardo Ferrer Garcia, Fernando Vaño Garcia, Gil Arasa Verge.

**Resources**:

- Prior Work:
[https://github.com/metacall/core/tree/5b592ac0e9a8e498e3e706623d0a788276f566e0/source/ports/zig_port](https://github.com/metacall/core/tree/5b592ac0e9a8e498e3e706623d0a788276f566e0/source/ports/zig_port) - MetaCall Core:
[https://github.com/metacall/core](https://github.com/metacall/core) - Zig Documentation:
[https://ziglang.org/documentation/master/](https://ziglang.org/documentation/master/)

The three chats are bridged by Matrix (messages sent from one, on the main room/channel, can be seen from all).
