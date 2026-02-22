# dora-rs — Project Ideas

**Source:** https://github.com/dora-rs/dora/wiki/GSoC_2026
**Scraped:** 2026-02-22T23:28:47.577607

---

Dora is a dataflow-based, low-latency middleware designed to revolutionize the development of robotic applications. In the field of robotics, where efficiency and speed are crucial, Dora stands out by supporting multiple programming languages, including Python, Rust, C, and C++. This multi-language support enables developers from diverse backgrounds to contribute and innovate.

The following is a list of projects suggested for GSoC 2026. These projects aim to further expand Dora's capabilities, enhance its usability, and contribute to the growth of the global robotics community.

# Project #1: Testing & Simulation Infrastructure

# Theme 3: AI Developer Experience & Tooling

**Action:** Provide a rich set of pre-built nodes and tools tailored for AI development.

**Details:** Accelerate the development of AI applications by providing ready-made components and insights.

**Why:** Developers shouldn't have to reinvent the wheel for common AI tasks like inference or data preprocessing.

**What:** A suite of AI-focused tools and nodes.

**How:**

1. **Optimized Inference Nodes:** Create and maintain nodes for popular inference runtimes (e.g., dora-onnx, dora-tensorrt, dora-tflite).

2. **Data-Centric Tooling:** Enhance dora-record and dora-replay to facilitate the creation of high-quality datasets for model training and fine-tuning from real-world robot data.

3. **Performance Tooling:** Enhance dora stats and dora inspect to provide detailed AI-specific metrics, such as inference latency, GPU utilization, and memory usage per node.

**Description**
The lack of a formal testing strategy beyond unit tests is a major gap for a robotics framework. This project aims to provide developers with the visibility, control, and isolation needed to effectively test and debug DORA dataflows. A robust testing infrastructure is essential for building reliable robotic applications.

**Expected Outcomes**
* **Creating `dora-test-utils` library** with mock implementations for DORA APIs (`send`, `receive`, `subscribe`, state management) to enable isolated unit testing with standard frameworks (pytest, cargo test).
* **Implementing scenario-based integration testing** leveraging the `dora-record`/`dora-replay` workflow for regression testing.
* **Developing programmatic control APIs** in Python and Rust SDKs to programmatically load, start, stop, pause, resume dataflows, inject data, observe outputs, and inspect state from test scripts.
* **Creating specialized test harness nodes** including `dora-test-source` (emit test data), `dora-test-sink` (capture output for assertions), and `dora-assertion-node` (in-dataflow assertions).
* **Building debugging probe nodes** including `dora-print-node`, `dora-save-node`, `dora-throttle-node`, and `dora-breakpoint-node` for runtime debugging.
* **Writing comprehensive documentation** with examples demonstrating testing patterns and best practices.

**Resources**. <br>
https://github.com/dora-rs/dora <br>

**Skills required/preferred**. Rust, Python, Testing frameworks, DORA

**Difficulty rating**.   medium

**Expected size:**  350h


# Project #2: Package & Dependency Management

**Description**
The current `node-hub` approach will not scale as a simple folder and leads to dependency conflicts. This project addresses the critical need for robust package and dependency management to foster a thriving, multi-language DORA ecosystem, ensuring reproducibility, discoverability, and security.

**Expected Outcomes**
* **Formalizing DORA Node Package Specification** with a language-agnostic `Dora.toml` or `dora-node.yaml` defining name, version, language, entrypoint, dependencies, capabilities, and checksum or within `Cargo.toml` or `pyproject.toml`.
* **Designing a centralized node registry** with HTTP/HTTPS server storing node metadata and packaged artifacts, authentication for publishing, and search/discovery API.
* **Enhancing `dora build`** to parse dataflows, resolve dependencies (local cache then registry), compile Rust/C/C++ nodes, prepare isolated Python environments, and generate lock files (`dora-lock.yml`).
* **Implementing `dora publish` and `dora install` commands** for publishing and fetching nodes from the registry.
* **Implementing runtime isolation** with dedicated Python `venv` per node and proper RPATH/LD_LIBRARY_PATH handling for compiled nodes.
* **Adding security mechanisms** including cryptographic signatures for packages and vulnerability scanning integration.
* **Writing comprehensive documentation** covering package creation, publishing, and consumption workflows.

**Resources**. <br>
https://github.com/dora-rs/dora <br>
https://doc.rust-lang.org/cargo/ <br>

**Skills required/preferred**. Rust, Python, Package management, DORA

**Difficulty rating**.   hard

**Expected size:**  350h


# Project #3: Distributed State Management

**Description**
DORA is primarily stateless, which limits its applicability for many robotics tasks like SLAM that require persistent state. This project implements a distributed state store for the daemon, eliminating it as a single point of failure and enabling more complex robotic applications.

**Expected Outcomes**
* **Integrating a distributed state backend** using either `DataFusion` `openraft` (pure-Rust Raft implementation) with `sled` key-value store.
* **Implementing daemon cluster formation** where multiple `dora-daemon` instances replicate state using Raft consensus.
* **Refactoring daemon to be stateless** by redesigning it to rely entirely on the distributed store for persistent state, watching for desired state changes and reconciling with actual state.
* **Defining and exposing state schema** formalizing the schema for control plane state (dataflow definitions, runtime status, daemon health) with clear APIs.
* **Implementing node-level state APIs** including `node.get_state()` and `node.set_state()` for application-level persistent state.
* **Creating failover tests** demonstrating daemon high availability and state consistency.
* **Writing documentation** covering cluster setup and state management patterns.

**Resources**. <br>
https://github.com/dora-rs/dora <br>
https://github.com/datafuselabs/openraft <br>

**Skills required/preferred**. Rust, Distributed systems, Consensus algorithms, DORA

**Difficulty rating**.   hard

**Expected size:**  350h


# Project #4: dora-studio: GUI for dataflow management

**Description**
To build a truly modern and accessible ecosystem, DORA needs to move beyond a CLI-only interface. This project creates a unified interface that seamlessly integrates a visual dataflow editor with an interactive operations console, providing a single pane of glass for the entire application lifecycle.

**Expected Outcomes**
* **Exposing a public control plane API** by documenting and exposing the coordinator's gRPC services as a stable, versioned API with gRPC-Web proxy for browser access.
* **Developing the "Operate" view** with an interactive console for deploying, monitoring, and controlling running dataflows including live topic inspection, node lifecycle control, and OpenTelemetry trace visualization.
* **Developing the "Design" view** with a drag-and-drop canvas for visually building, configuring, and saving DORA dataflows with node library browser.
* **Implementing real-time updates** using WebSocket or Server-Sent Events for live dataflow status and metrics.
* **Publishing JavaScript/TypeScript SDK** for the control plane API to enable third-party tooling.
* **Creating user documentation** with tutorials for using the web platform.

**Resources**. <br>
https://github.com/dora-rs/dora-studio <br>
https://opentelemetry.io/ <br>

**Skills required/preferred**. rust, DORA

**Difficulty rating**.   hard

**Expected size:**  350h

# Project #4: Refactor Getting Started Documentation

 **Description**
Currently the getting started is demonstrating only a limited amount of the capabilities of dora-rs but it could be great to showcases additional features. 

**Resources**. <br>
https://dora-rs.ai<br>
https://github.com/dora-rs/dora<br>
https://github.com/dora-rs/dora-hub <br>

**Skills required/preferred**. rust, DORA

**Difficulty rating**.   Medium

**Expected size:**  100h


# Project #5: Clean up unused features from dora-rs

**Description**
Currently within dora-rs, we implemented some experimental features that is not used any longer and it could be great if someone could help us refactor dora-rs.

**Skills required/preferred**. rust, DORA

**Difficulty rating**.   Medium

**Expected size:**  100h
