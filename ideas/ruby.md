# Ruby — Project Ideas

**Source:** https://github.com/rubygsoc/rubygsoc/wiki/Ideas-List-(2026)
**Scraped:** 2026-02-22T23:28:47.589616

---

Welcome! This is the central hub for project ideas for the **Ruby Organization** in [Google Summer of Code (GSoC) 2026](https://opensource.googleblog.com/2025/12/shape-future-with-google-summer-of-code.html).

We are looking for mentors and sub-projects from across the Ruby ecosystem (including Rails, Hanami, SciRuby, etc.) to submit project proposals. This year, Google is placing a special emphasis on projects within the **AI, Security, and Machine Learning** domains. We highly encourage ideas that help Ruby stay at the forefront of these fields.

### 📢 Call for Mentors & Projects

If you are a maintainer or a regular contributor to a Ruby-related project, we invite you to add your project ideas below.

**Deadline for Idea Submission:** Please finalize your entries by **February 1, 2026**, to give us time to review before the Organization Application deadline on Feb 3.

### 📝 Submission Guidelines

To ensure our application is successful, every project idea **must** follow the template below. Google requires clear outcomes and defined scopes.

* **No "Bug Trackers":** Do not simply link to a list of issues. Each idea must be a cohesive project.
* **Mentor Commitment:** Every project should ideally have two mentors identified to ensure redundancy.
* **Scope:** Ensure the project size (90, 175, or 350 hours) is realistic for a summer timeframe.

---

### 🛠 How to add your idea

Follow the format layout while [Defining a Project Idea List](https://google.github.io/gsocguides/mentor/defining-a-project-ideas-list) specified in the [Mentor guide](https://google.github.io/gsocguides/mentor/), please provide the following information for each idea:

Please copy the template below, create a new section under the appropriate category (AI/ML, Security, or General Ruby), and fill in the details.

#### [Copy-Paste Template]

```markdown
### [Project Title: e.g., Enhancing Ruby-Tensorflow integration]
* **Description**: A 2-5 sentence summary of the problem and the proposed solution.
* **Expected Outcome**: What will the contributor have accomplished by the end of the program? (e.g., "A new gem for X," "Integration of Y into Z").
* **Skills Required**: List specific skills (e.g., Ruby, C, Linear Algebra, OpenSSL knowledge).
* **Difficulty**: Easy / Medium / Hard
* **Project Size**: Small (90h) / Medium (175h) / Large (350h)
* **Mentors**: [Name/GitHub Handle], [Second Mentor Name/GitHub Handle]
* **Domain**: AI / Security / Machine Learning / Core Ruby

```

---

## 🤖 AI & Machine Learning Ideas

*Focus: Libraries for LLMs, data processing, tensor manipulation, and AI-driven automation.*

## 🛡 Security & Infrastructure Ideas

*Focus: Cryptography, vulnerability scanning, secure Gem management, and Ruby core security improvements.*

## 💎 General Ruby & Ecosystem Ideas

*Focus: Performance improvements, developer tooling, and community-driven features.*

---

## RubyGems.org 

### Event Transparency Logs

* **Description**: RubyGems.org currently lacks transparency into critical package registry events such as gem publications, ownership changes, and deletions, making it difficult to detect supply chain compromises or unauthorized modifications. This project proposes implementing a Merkle tree–based transparency log that records these events in an immutable, append-only structure. The log will provide cryptographically verifiable records that allow maintainers to detect unexpected changes and enable security researchers to audit the Ruby ecosystem.
* **Expected Outcome**: A working proof-of-concept transparency log system integrated into RubyGems.org that captures and cryptographically logs critical registry events, with verification APIs and a basic interface for maintainers to monitor their packages.
* **Skills Required**: Ruby, Ruby on Rails, Cryptography fundamentals
* **Difficulty**: Hard
* **Project Size**: Large (350h)
* **Mentors**: Colby Swandale (@colby-swandale), Jenny Shen (@jenshenny), Josef Šimánek (@simi)
* **Domain**: Security

### Bundle Audit

* **Description**: Ruby developers currently lack official tooling to automatically detect known vulnerabilities in their dependencies, leaving many unaware of security risks. Although the community-maintained bundler-audit tool exists, it requires separate installation and manual execution, resulting in inconsistent adoption. This project aims to integrate ruby-advisory-db directly into Bundler to provide automatic vulnerability scanning as part of the standard workflow.
* **Expected Outcome**: Bundler ships with built-in `bundle audit` functionality that checks dependencies against ruby-advisory-db and optionally warns users during `bundle install` when vulnerable gems are detected.
* **Skills Required**: Ruby, Bundler internals
* **Difficulty**: Medium
* **Project Size**: Medium (175h)
* **Mentors**: Colby Swandale (@colby-swandale), Jenny Shen (@jenshenny), Josef Šimánek (@simi)
* **Domain**: Security

---

## Rage Framework

[Rage Homepage](https://rage-rb.dev) | [Rage GitHub](https://github.com/rage-rb/rage)

### Observability: Metrics & Context Propagation
* **Description**: To run Rage in production at scale, it needs robust observability. This project addresses two critical gaps in running Rage at scale: Context Propagation and Runtime Metrics. This project aims to close these gaps, making Rage fully observable out of the box.
  * **Context Loss:** Many Rage applications use `ActiveSupport::CurrentAttributes` to track global request data (e.g., `Current.user`). However, because Rage's background tasks are executed in separate fibers, this context is lost when execution moves to the background. This project involves introducing Active Support integration to ensure Current attributes automatically travel with a task when it is enqueued.
  * **Missing Metrics:** Users cannot see how hard the engine is working. Critical indicators like "Event Loop Lag" or "Socket Backlog" are currently invisible.
* **Expected Outcome**: An updated `Rage::Telemetry` interface that allows developers to export low-level reactor metrics (loop lag, queue depth) to OpenTelemetry, and a context-propagation patch ensuring `ActiveSupport::CurrentAttributes` persist across background task boundaries.
* **Skills Required**:
  * **Ruby Internals:** Understanding Active Support internals and Fiber storage.
  * **Systems Programming:** Understanding event loops and sockets.
  * **OpenTelemetry:** Understanding tracing and metrics.
* **Difficulty**: Medium
* **Project Size**: Medium (175h)
* **Mentors**: @cuneyter @daz-codes 
* **Domain**: Core Ruby

### HTTP Streaming
* **Description**: Modern applications (like ChatGPT) rely heavily on HTTP Streaming to deliver content incrementally. Rage is built on fibers, making it a perfect candidate for handling long-running requests. Currently, Rage buffers responses, which prevents this behavior. This project aims to unlock real-time capabilities in Rage by implementing support for Chunked Transfer Encoding and, potentially, Server-Sent Events (SSE). Crucially, the API must be designed to be protocol agnostic: while the underlying transport will initially be HTTP/1.1, the interface must be abstract enough to support HTTP/2 streams in the future.
* **Expected Outcome**: Core support for Chunked Transfer Encoding within the Rage engine, and a developer-friendly public API for streaming data (including a helper for Server-Sent Events) that abstracts away the underlying transport protocol.
* **Skills Required**:
  * **Networking:** Understanding HTTP/1.1 and HTTP/2 protocols, buffering, and sockets.
  * **Rack:** Understanding the Rack interface and body proxies.
* **Difficulty**: Hard
* **Project Size**: Medium (175h)
* **Mentors**: @tonekk @rsamoilov
* **Domain**: Core Ruby

### SQL Adapter for Background Tasks
* **Description**: Rage's background system ([Rage::Deferred](https://rage-rb.dev/docs/deferred)) currently relies on a disk-based Write-Ahead Log (WAL) for durability. While it introduces no dependencies and requires no setup, this approach is problematic for modern cloud deployments (like Heroku, K8S, or serverless containers), where disk storage is ephemeral. If a container restarts or is redeployed, the local file is wiped, and pending background tasks are lost. To make Rage cloud-native, we need to allow users to store pending tasks in a database (PostgreSQL/MySQL) instead of a local file.
  * **Important Note:** This project is not about creating a distributed queue like Sidekiq. The execution model of `Rage::Deferred` will remain local (tasks are processed by the same process that enqueued them). The goal of the project is purely data durability in stateless environments.
* **Expected Outcome**: A production-ready database adapter that persists background tasks to a SQL database to ensure durability in containerized environments.
* **Skills Required**:
  * **Software Architecture:** Designing clean interfaces.
  * **Cloud Concepts:** Understanding ephemeral storage vs. persistent storage.
  * **Relational Databases:** Integrating with SQL databases.
* **Difficulty**: Hard
* **Project Size**: Medium (175h)
* **Mentors**: @cuneyter @rsamoilov
* **Domain**: Core Ruby

### Extension System (Railtie Equivalent)
* **Description**: As Rage grows, external libraries need a standard way to hook into the framework's lifecycle. Currently, integrating third-party gems requires manual setup. In Rails, this is solved by "Railties" - a system that allows gems to automatically configure themselves, add initializers, or extend core classes when the application boots. We need a similar extension architecture for Rage. This will allow the Ruby ecosystem to build drop-in integrations for Rage (e.g., `rage-sentry`, `rage-devise`, etc.).
* **Expected Outcome**: A defined `Rage::Extension` (or similar) architecture allowing external gems to hook into the application boot process and configuration, validated by creating a proof-of-concept integration for a standard library (e.g., Sentry or Honeybadger).
* **Skills Required**:
  * **Ruby Metaprogramming:** Understanding how gems are loaded and how to modify classes at runtime.
  * **Framework Architecture:** Understanding boot sequences and dependency injection.
* **Difficulty**: Medium
* **Project Size**: Medium (175h)
* **Mentors**: @daz-codes @cuneyter
* **Domain**: Core Ruby

### Blueprinter Integration for OpenAPI
* **Description**: [Rage::OpenAPI](https://rage-rb.dev/docs/openapi) is a tool that automatically generates OpenAPI documentation by statically analyzing your code. Currently, it supports the `Alba` serializer for defining response structures. [Blueprinter](https://github.com/procore-oss/blueprinter) is another highly popular serializer in the Ruby ecosystem. Because Rage generates docs via static analysis, this project involves parsing Blueprinter classes to extract their schema without loading the entire application environment.
* **Expected Outcome**: A static analysis extension for `Rage::OpenAPI` capable of parsing `Blueprinter` serializer definitions via Prism/AST and converting them into accurate OpenAPI schemas without requiring the application to run.
* **Skills Required**:
  * **Ruby Metaprogramming & Parsing:** Understanding Abstract Syntax Trees (AST) and Static Analysys (`Prism`) .
  * **API Specifications:** Understanding OpenAPI specifications.
* **Difficulty**: Hard
* **Project Size**: Medium (175h)
* **Mentors**: @tonekk @daz-codes
* **Domain**: Core Ruby

---

## LowType

LowType provides optional inline type annotations and type checking in Ruby, all without a build step. Simply include LowType in a class and types are checked per environment, or ignored and just treated as type annotations, depending on user configuration.

[LowType GitHub](https://github.com/low-rb/low_type)

### 1. Support boolean and enum types

* **Description**: LowType supports Ruby's standard types (String, Array, Integer, etc.) as well as "complex types" that are defined by LowType itself (Tuple, Status, Headers) which allow more complex behaviour from a type. For example `Status` type is a subclass of `Integer` and will check that the number provided is a valid HTTP Status Code. Complex types are defined in `lib/types/complex_types.rb` and can be added to using the existing types as a guide.

* **Expected Outcome**:
A boolean type in a method definition will look like:
```ruby
def my_method(my_var: Boolean | false)
```
Where `Boolean` is the type and `false` is the default value if the arg is not supplied.

An enum type in a method defintion will look like:
```ruby
def my_method(my_var: Enum["red", "orange", "yellow"] | "blue")
```
Where `"blue"` is the default value and `"red", "orange", "yellow"` are the allowed values for the enum.

An enum type in a `type()` method will look like:
```ruby
color = type Enum["red", "orange", "yellow"] | arg
```
Where `arg` is the name of the variable representing the value or argument that we are validating and `"red", "orange", "yellow"` are the allowed values for the enum.

* **Skills Required**: Ruby, understanding of [Type Expressions](https://github.com/low-rb/low_type?tab=readme-ov-file#lowtype)
* **Difficulty**: Easy
* **Project Size**: Small (90h)
* **Mentors**: @maedi
* **Domain**: Core Ruby

### 2. Evaluate constants in their original binding

* **Description**: Currently types are evaluated in the binding of LowType, which uses refinements (avoids monkey patching) to implement Array/Hash types with a collection style Array[T]/Hash[T] syntax. We need to evaluate user supplied types like `CustomClass` in the binding of the class from where the type was originally defined. This can be done by getting the constant's full namespace via `FileParser` and evaluating that (`::CustomModule::CustomClass`) or evaluating the type in its original binding/context:

> "Ruby constants can be evaluated in another namespace by utilizing module_eval or const_get on the target module, or by passing a binding to eval. To access TargetModule::CONST from a different scope, use TargetModule.const_get(:CONST) or TargetModule::CONST"

See [Scope](https://github.com/low-rb/low_type?tab=readme-ov-file#scope) and research "ruby refinements" and "ruby execution context" for more information.

* **Expected Outcome**: Use `const_get` and `class_eval` to evaluate user-defined constants in their original binding.
* **Skills Required**: Ruby, Ruby modules/namespaces, Ruby bindings (execution context)
* **Difficulty**: Medium
* **Project Size**: Small (90h)
* **Mentors**: @maedi
* **Domain**: Core Ruby

### 3. Re-evaluate typed arguments without types

* **Description**:  When `config.type_checking` is disabled we currently prepend a "shim" method that ignores validating the types in the user's code. So when calling a previously typed method there is always a guard method to go through. This impacts performance by adding additional method calls in the prepended "shim" method. Instead let's rewrite the method to contain no types at all.

Benefits:
- Improve performance (no "shim" method)
- Simplify debugging (one less step)
- Shorten stack traces (one less line)

* **Expected Outcome**: Rewrite the method's params to be "untyped". We would likely use eval() to do this, which allows us override the method in memory on class load. We can also mirror the line numbers of the original method by suppling them to eval(). Use `low_methods` available on the class to find metadata on the method params and their types, and/or use `FileParser` to access the original method definition as a string and rewrite this string to be without types.

* **Skills Required**: Ruby, Ruby's PRISM, Ruby's eval()
* **Difficulty**: Medium
* **Project Size**: Medium (175h)
* **Mentors**: @maedi
* **Domain**: Core Ruby

### 4. Integrate LowType with RBS

* **Description**: Ruby Signature files are the standard Ruby way to define the types of your class, via a corresponding file that just contains type definitions. These files are traditionally generated manually or inferred via certain tools to varying degrees of accuracy. Exporting LowType's inline type annotations to RBS sig files will allow LowType to be integrated into the core Ruby ecosystem and be integrated with other type checking tools such as Steep.

What makes this project hard is the familiarity needed with RBS, and the skillset needed to generate sig files using PRISM, from the metadata supplied by LowType.

* **Expected Outcome**: A very simple command line tool (CLI) that when called generates the mirrored sig versions of our typed files when run. Ruby Gems provide a way to easily install a CLI command for your gem when the gem is installed. Call this command `lowtype`.
* **Skills Required**: Ruby, RBS, PRISM, CLI
* **Difficulty**: Hard
* **Project Size**: Large (350h)
* **Mentors**: @maedi
* **Domain**: Core Ruby

---

### 💡 Pro-Tip for Mentors:

When drafting your ideas, think about the "First 5 Minutes" for a contributor. Providing a small "warm-up" task or a link to relevant documentation in your description helps attract the best candidates early on!

For any questions, please reach out via our [Discord Channel](https://discord.gg/W2YeZ3sE) or DM [zoras](https://www.linkedin.com/in/zoras/).
