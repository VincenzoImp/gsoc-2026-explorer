# Apache Software Foundation — Project Ideas

**Source:** https://s.apache.org/gsoc2026ideas
**Scraped:** 2026-02-22T23:28:47.597654

---

DUE TO SPAM, SIGN-UP IS DISABLED. Goto [Selfserve wiki signup](https://selfserve.apache.org/confluence-account.html) and request an account.

This page is auto-generated! Please do NOT edit it, all changes will be lost on next update

Contents

# APISIX

[JSON Schema to Form UI for APISIX Dashboard](https://issues.apache.org/jira/browse/APISIX-39)

APISIX plugins ship JSON Schema definitions for their configuration. If APISIX Dashboard can render plugin configuration forms directly from JSON Schema, developer experience improves significantly and reduces manual UI maintenance.

Goals (Deliverables)

Must-have:

- A reusable SchemaForm (or equivalent) that renders basic types: string/number/integer/boolean/object/array.
- enum support (Select/Radio etc), defaults, required fields, basic constraints (min/max, pattern, etc) where feasible.
- Support at least the key complex patterns used by APISIX plugin schemas:
- oneOf (select one option and render corresponding fields)
- dependencies / conditional fields
- (Stretch) anyOf if present in target schemas

- Validation pipeline: validate form values against schema (AJV) and show errors in UI consistently.
- Documentation + developer guide: how to add/extend schema-to-widget mapping.
- Tests (unit + minimal integration) to prevent regressions for schema parsing and conditional rendering.

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Yuan Bao*, mail: baoyuan (at) apache.org

*Project Devs*, mail: dev (at) apisix.apache.org

# Apache AsterixDB

[NL2SQL++ assistant ](https://issues.apache.org/jira/browse/ASTERIXDB-3696)

This project aims to develop a modular, extensible NL2SQL component for AsterixDB that translates natural language prompts into executable SQL++ queries. The system will leverage recent advances in Large Language Models (LLMs) to enable users to express complex analytical questions without writing formal queries. It will follow best practices by exposing an OpenAPI-based interface that connects to external LLMs through frameworks such as LangChain4j while remaining model-agnostic. The component will also support locally-hosted LLMs to reduce operating costs and maintain privacy.

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Suryaa Charan*, mail: suryaacharan (at) apache.org

*Project Devs*, mail:

[LLM Agent Protocols/Memory](https://issues.apache.org/jira/browse/ASTERIXDB-3695)

This feature adds agent compatibility to AsterixDB by implementing standard agent protocols and agentic memory capabilities. It involves implementing two emerging standards: the Model Context Protocol (MCP) for tool exposure and structured capability discovery, and the Agent-to-Agent (A2A) protocol for multi-agent coordination. MCP will allow AsterixDB to describe its capabilities, datasets, functions, and safe operations to AI agents. The project also utilizes AsterixDB to provide persistent agentic memory that tracks an agent's query sessions, enabling agents to recall and build on previous interactions.

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Suryaa Charan*, mail: suryaacharan (at) apache.org

*Project Devs*, mail:

[Backup/restore utility for AsterixDB](https://issues.apache.org/jira/browse/ASTERIXDB-3697)

In order to backup and restore a database, one common pattern is to use a tool that takes the current state of the database and generates a set of DDL statements which, when executed, will create the existing state of the database. Currently this is not possible in AsterixDB for DDL statements- you would have to remember which ones you issued to create Types, Datasets, and so on. Therefore having a tool that can take the current state of the Metadata dataverse and craft a set of DDL statements that would create that state, and then for each dataset dump its contents into an INSERT statement, would be a great addition.

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Ian Maxon*, mail: imaxon (at) apache.org

*Project Devs*, mail:

[In-browser packaging of AsterixDB](https://issues.apache.org/jira/browse/ASTERIXDB-3698)

AsterixDB since its inception has always been a distributed system. This has historically led to some friction for new users who simply want to try out the system to get a sense of the language and features. It simply isn't necessary for them to deploy the system as it would be for handling large amounts of data, however the deployment and packaging has to assume someone wants to do this. Therefore it has always been a balance between configurability and simplicity.

With the advancement of WASM and Javascript in general, there now exist versions of other databases, which were previously only run locally, which are adapted and targeted to a WASM or JS environment. This lets the user simply open a browser and get a fully-functioning instance of a real database like they would if it was installed locally or on a server somewhere. Given that AsterixDB is written purely in Java, it should in principle be possible to run AsterixDB on a JVM which can target WASM as an architecture, with WASI or some other platform. Having something similar for AsterixDB would be an amazing tool to help further the adoption of AsterixDB, and SQL++ in general.

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Ian Maxon*, mail: imaxon (at) apache.org

*Project Devs*, mail:

[Dynamic Memory Management ](https://issues.apache.org/jira/browse/ASTERIXDB-3703)

AsterixDB currently uses a static approach for memory allocation in memory-intensive operators, where each operator is assigned a fixed memory budget, either user-provided or derived from defaults. Static budgeting can lead to several issues. Long-running queries may hold large memory allocations for extended periods, reducing concurrency and blocking other queries. In addition, memory estimation errors can result in over-allocation that wastes resources or under-allocation that causes spills and performance degradation.

This project will make key memory-intensive operators dynamically adaptive to memory reallocation requests from a resource broker. The broker will adjust operator memory budgets at runtime based on system conditions and workload objectives, such as improving fairness across concurrent queries, increasing overall throughput, and maintaining predictable performance under contention. The expected outcome is a coordinated memory management loop where operators expose safe resizing hooks and the broker uses feedback signals to rebalance memory across running queries.

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Shiva Jahangiri*, mail: shivajah (at) apache.org

*Project Devs*, mail:

[Top K Nearest Queries Support ](https://issues.apache.org/jira/browse/ASTERIXDB-3699)

AsterixDB currently lacks native support for Top-K-Nearest queries, which return the K tuples whose attribute values are closest to a given reference value or point. Examples include: the five employees whose salaries are closest to the CEO's salary or the five buildings closest to the White House. This project involves designing and implementing efficient Top-K-Nearest query processing within AsterixDB's execution engine (Hyracks), including optimizer support to avoid full scans and to leverage existing indexes where possible. The implementation should integrate cleanly with SQL++.

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Suryaa Charan*, mail: suryaacharan (at) apache.org

*Project Devs*, mail:

# Apache Fineract

[Loan Origination POC](https://issues.apache.org/jira/browse/FINERACT-2442)

**Note: GSOC applicants - this is a "draft concept". Do not work on your proposal until we kick off the process at Fineract for evaluating. We may significantly edit this concept or create new ones to replace it.**

**No one should work on this specific ticket unless assigned - the GSOC candidate we choose will be assigned this ticket.**

**For more information, you should be reviewing emails on this subject and following the Wiki pages.** [https://lists.apache.org/list.html?dev@fineract.apache.org](https://lists.apache.org/list.html?dev@fineract.apache.org)[https://cwiki.apache.org/confluence/display/FINERACT/GSOC+Program+at+Fineract](https://cwiki.apache.org/confluence/display/FINERACT/GSOC+Program+at+Fineract)

**LOAN ORIGINATION CONTEXT**

Fineract has some loan origination functionality but it is not robust enough for many operations. Several vendors, working with Fineract have created new Loan Origination plug ins.

There is also a major enhancement underway that would build out a full Loan Origination flow by supporting the backend needs of data storage for such LOS. See ticket [https://issues.apache.org/jira/browse/FINERACT-2418](https://issues.apache.org/jira/browse/FINERACT-2418) .

The GSOC student would be expected to propose something as a POC (proof of concept) that would either - use the developed Fienract backend solution, or build a new component outside of Fineract to create the flows that would demonstrate the LOS functionality.

That is, this is a moving target, and we would need different proposals from prospective candidates to explore the area of Loan Origination. This may require expertise in risk assessment, loan origination models and business acumen. There will not be much more explanation that this available. The student would be expected to be a self starter.

The mentor for this would need to be an expert at risk modeling, understand Loan Origination, and support a conceptual basis that may involve some things internal to Fineract and some processing elements outside of Fineract. Please comment below if you are an existing Fineract contributor with this expertise.

To try to illustrate: one possible GSOC Proposal archtype we could accept would be a survey of Loan Origination Models, their strengths and weaknesses and to identify commonalities for the community to focus on. This would thus be a Requirements exercise and may help identify future roadmap concepts. In this case, the code to be developed may just expose a few APIs into different screen flows. Thus, perhaps FIGMA flows (or similar) connecting to a set of APIs on the backend.

If those new LOS APIs are existing in June 2026 (ticket 2418 resolved), then those APIs are to be used. if they are NOT there in Fineract, then the student would be requested to create a fork and to implement the POC outside of the main Dev branch.

I welcome additions to this write up. [jdailey](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=jdailey)

**Difficulty:**Minor

**Project size:**~350 hour (large)

**Potential mentors:**

*James Dailey*, mail: jdailey (at) apache.org

*Project Devs*, mail: dev (at) fineract.apache.org

[Front end application MVP (POC)](https://issues.apache.org/jira/browse/FINERACT-2440)

**Note: GSOC applicants - this is a "draft concept". Do not work on your proposal until we kick off the process at Fineract for evaluating. We may significantly edit this concept or create new ones to replace it.**

**No one should work on this specific ticket unless assigned - the GSOC candidate we choose will be assigned this ticket.**

**For more information, you should be reviewing emails on this subject and following the Wiki pages.** [https://lists.apache.org/list.html?dev@fineract.apache.org](https://lists.apache.org/list.html?dev@fineract.apache.org)[https://cwiki.apache.org/confluence/display/FINERACT/GSOC+Program+at+Fineract](https://cwiki.apache.org/confluence/display/FINERACT/GSOC+Program+at+Fineract)

**Build a simple self-service front end that talks to the Self-Service API**

We need a new, user-friendly front end app that connects to our Backend for Front end (**Self-Service API component)** This will be the “customer portal” experience where users can log in, see their accounts, and check recent activity. It should be straightforward, easy to use, and a good reference example for others to build on.

Functionality needed would include:

- Login
- Check balances
- Transfer between accounts owned by the same customer.
- Submit application for a new loan

Testing end to end required.

Solid UI design

Modern app framework

Documentation

**Difficulty:**Minor

**Project size:**~350 hour (large)

**Potential mentors:**

*James Dailey*, mail: jdailey (at) apache.org

*Project Devs*, mail: dev (at) fineract.apache.org

[Create a new backend for front end component POC](https://issues.apache.org/jira/browse/FINERACT-2439)

**Note: GSOC applicants - this is a "draft concept". Do not work on your proposal until we kick off the process at Fineract for evaluating. We may significantly edit this concept or create new ones to replace it.**

**No one should work on this specific ticket unless assigned - the GSOC candidate we choose will be assigned this ticket.**

**For more information, you should be reviewing emails on this subject and following the Wiki pages.** [https://lists.apache.org/list.html?dev@fineract.apache.org](https://lists.apache.org/list.html?dev@fineract.apache.org)[https://cwiki.apache.org/confluence/display/FINERACT/GSOC+Program+at+Fineract](https://cwiki.apache.org/confluence/display/FINERACT/GSOC+Program+at+Fineract)

**Build a Self-Service API Component that Connects to Apache Fineract**

When the project removed self-service APIs in 2025, it did so understanding that we would need an outside component to make that connection as part of an overall solution.

This project is to create - as a Proof of Concept (POC) - a new dedicated Self-Service API component or service that integration with Fineract backend. It will need to expose APIs to consumer facing applications for typical activities like viewing account balances, transaction initiation, loan application, etc.

The idea is for GSOC candidates to propose a design and build the POC.

Minimal criteria include testing, authentication methodology, documentation.

Not included in this GSOC would be the end consumer APP, although that may be undertaken by another project and coordination would be needed.

**Difficulty:**Minor

**Project size:**~350 hour (large)

**Potential mentors:**

*James Dailey*, mail: jdailey (at) apache.org

*Project Devs*, mail: dev (at) fineract.apache.org

[BI connector and demonstration](https://issues.apache.org/jira/browse/FINERACT-2441)

**Note: GSOC applicants - this is a "draft concept". Do not work on your proposal until we kick off the process at Fineract for evaluating. We may significantly edit this concept or create new ones to replace it.**

**No one should work on this specific ticket unless assigned - the GSOC candidate we choose will be assigned this ticket.**

**For more information, you should be reviewing emails on this subject and following the Wiki pages.** [https://lists.apache.org/list.html?dev@fineract.apache.org](https://lists.apache.org/list.html?dev@fineract.apache.org)[https://cwiki.apache.org/confluence/display/FINERACT/GSOC+Program+at+Fineract](https://cwiki.apache.org/confluence/display/FINERACT/GSOC+Program+at+Fineract)

The idea is to create a connector and a demonstration of analytics that would consume and organize data from Fineract.

For example, create a way to pull data out of Fineract and make it easy to use in common analytics such as Power BI or Tableau or, better yet, an open source variant. The data should probably go to a Data Warehouse.

Start by proposing and exploring different options and write up the pros and cons.

Create a demonstration project that takes into account security, levels of access, and security of PII data if it exists.

**Difficulty:**Minor

**Project size:**~350 hour (large)

**Potential mentors:**

*James Dailey*, mail: jdailey (at) apache.org

*Project Devs*, mail: dev (at) fineract.apache.org

[fineract-client-feign usage for integration tests](https://issues.apache.org/jira/browse/FINERACT-2454)

**Note: GSOC applicants - this is a "draft concept". Do not work on your proposal until we kick off the process at Fineract for evaluating. We may significantly edit this concept or create new ones to replace it.**

**No one should work on this specific ticket unless assigned - the GSOC candidate we choose will be assigned this ticket.**

**For more information, you should be reviewing emails on this subject and following the Wiki pages.** [https://lists.apache.org/list.html?dev@fineract.apache.org](https://lists.apache.org/list.html?dev@fineract.apache.org)[https://cwiki.apache.org/confluence/display/FINERACT/GSOC+Program+at+Fineract](https://cwiki.apache.org/confluence/display/FINERACT/GSOC+Program+at+Fineract)

"Moving away from RestAssured (low-level) API calls in integration tests and rather use fineract-client-feign would be a great improvement"

**Summary (with some assist from chatgpt for clarity)**

Apache Fineract has a large set of REST APIs and many integration tests currently call those APIs using **RestAssured**(low-level HTTP requests). This ticket is to help modernize the tests by switching them to use **fineract-client-feign**, which is Fineract’s higher-level API client.

#### Goal

Create a simple migration approach and then migrate a small set of integration tests from RestAssured to fineract-client-feign.

#### Why we’re doing this

- Makes tests easier to read and maintain (less raw HTTP code).

- Encourages consistent API usage across tests.

- Reduces duplicated request-building logic (headers, base URLs, auth, etc.).

## Scope of Work

### 1) Create a short migration plan

Write a short note (in the Jira ticket comments or a small doc) that answers:

- Where are the current RestAssured-based integration tests located?

- What’s the recommended pattern for using fineract-client-feign in tests?

- What should be migrated first (start small)?

### 2) Pick a small “starter set” of tests

Identify **2–5 integration tests** that:

- Are simple (e.g., create/read/update a resource)

- Don’t involve complicated multi-step workflows

- Run reliably in CI

### 3) Implement the migration for the starter set

For each selected test:

- Replace RestAssured calls with fineract-client-feign client calls

- Keep the same assertions (same expected behavior)

- Ensure the tests still pass locally and in CI

### 4) Document the new pattern

Add a short README note or comments in the test code showing:

- How to initialize/configure the Feign client for tests

- How auth/session is handled

- A small “before vs after” explanation (1 paragraph is enough)

## Acceptance Criteria

- A brief migration plan is written and linked in the ticket.

- At least
**2 integration tests**have been converted to use fineract-client-feign.

- All tests pass (locally and/or in CI).

- A short note exists explaining how to write future integration tests using fineract-client-feign.

## Notes / Hints for a beginner

- Start by converting just one very small test to learn the pattern.

- Keep changes small and easy to review (one test per commit is ideal).

- If something is unclear (e.g., how auth is set up), add a comment in the ticket describing what you found.

## Out of Scope (for this ticket)

- Migrating
*all*integration tests across the repo

- Refactoring production API code

- Changing API behavior—this is only a test client swap

**Difficulty:**Minor

**Project size:**~350 hour (large)

**Potential mentors:**

*James Dailey*, mail: jdailey (at) apache.org

*Project Devs*, mail: dev (at) fineract.apache.org

[[GSoC 2026] [POC] Standardize and Harden Transaction Idempotency for Savings and Loans](https://issues.apache.org/jira/browse/FINERACT-2485)

**Goal:** Standardize idempotency enforcement to prevent replay attacks in core financial modules. **Implementation Strategy (Addressing James Dailey's feedback):**

**Opt-In Architecture:**New logic will be behind a Global Configuration flag. Default remains legacy behavior to ensure 100% backward compatibility.

**Phased Approach:**Audit existing m_portfolio_command_source usage and bridge gaps in the Savings module first.

**Testing:**Implementation of integration tests simulating network failures/retries.

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*saifulhuq*, mail: saifulhuq (at) apache.org

*Project Devs*, mail: dev (at) fineract.apache.org

[[Testing] Add unit tests for ApiParameterHelper in fineract-core](https://issues.apache.org/jira/browse/FINERACT-2494)

There is currently no unit test coverage for the ApiParameterHelper utility class. I have implemented a new test suite using JUnit 5 to cover core methods like extractFieldsForResponseIfProvided.

Verification: Successfully ran locally with 1/1 tests passed (100% success rate)


**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Ambika*, mail: ambikasony (at) apache.org

*Project Devs*, mail: dev (at) fineract.apache.org

[New command processing infrastructure](https://issues.apache.org/jira/browse/FINERACT-2169)

## Background and Motivation

Fineract accumulated some technical debt over the years. One area that is implicated is type-safety of internal and external facing APIs, the most prominent of which is Fineract's REST API. In general the package layout of the project reflects a more or less classic layered architecture (REST API, data transfer/value objects, business logic services, storage/repositories). The project predates some of the more modern frameworks and best practices that are available today and on occasions the data structures that are exchanged offer some challenges (e.g. generic types). Fineract's code base reflects that, especially where JSON de-/serialization is involved. Nowadays, this task would be simply delegated to the Jackson framework, but when Fineract (Mifos) started the decision was made to use Google's GSON library and create handcrafted helper classes to deal with JSON parsing. While this provided a lot of flexibility this approach had some downsides:

- the lowest common denominator is the string type (aka JSON blob); this is where we lose the type information
- the strings are transformed into JSONObjects; a little bit better than raw strings, but barely more than a hash map
- a ton of "magic" strings are needed to get/set values
- this approach makes refactoring unnecessarily more difficult
- to be able to serve an OpenAPI descriptor (as JSON and YAML) we had to re-introduce the type information at the REST API level with dummy classes that contain only the specified attributes; those classes are only used with the Swagger annotations and no were else
- some developers skipped the layered architecture and found it too tedious to maintain DTOs and JSON helper classes, and as a result just passed JSONObjects right to the business logic layer
- now the business logic is unnecessarily aware of how Fineract communicates to the outside world and makes replacing/enhancing the communication protocol (e.g. with GRPC) pretty much impossible

The list doesn't end here, but in the end things boil down to two main points:

- poor developer experience: boilerplate code and missing type safety cost more time
- bugs: the more code the more likely errors get introduced, especially when type safety is missing and we have to rely on runtime errors (vs. compile time).

There has been already some preparatory work done concerning type safety, but until now we avoided dealing with the real source of this issue. Fineract's architectures devises read from write requests ("CQRS", [https://martinfowler.com/bliki/CQRS.html](https://martinfowler.com/bliki/CQRS.html)) for improved scalability.

The read requests are not that problematic, but all write requests pass through a component/service that is called "SynchronousCommandProcessingService. As the name suggests the execution of business logic is synchronous (mostly) due to this part of the architecture. This is not necessarily a problem (not immediately at least), but it's nevertheless a central bottleneck in the system. Even more important: this service is responsible to route incoming commands to their respective handler classes which in turn execute functions on one or more business logic services. The payload of these commands are obviously not always the same... which is the main reason why we decided to use the lowest common denominator to be able to handle these various types and rendered all payloads as strings. This compromise bubbles now up in the REST API and the business logic layers (and actually everything in between).

Over the years we've also added additional features (e.g. idempotency guarantees for incoming write requests) that make it now very hard to reason about the execution flow. Testing the performance impact of such additions to the critical execution path even can't be properly measured. Note: the current implementation of idempotency relies on database lookups (quite often, for each incoming request) and none of those queries are cached. If we wanted to store already processed requests (IDs) in a faster system (let's Redis) then this can't be done without major refactoring.

In conclusion, if we really want to fix those issues that are not only cosmetic and affect the performance and the developer experience equally then we urgently need to fix the way how we process write requests aka commands.

## Target Personas

- developers
- integrators
- end users
- BaaS

## Goals

- new command processing will run independently next to the legacy mechanics
- self contained
- fully tested
- ensure that the REST API is 100% backward compatible
- try to contain the migration and make it as easy as possible for the community to integrate those changes
- introduce types where needed and migrate the (old) JAX-RS REST resource classes to Spring Web MVC (better performance and better testability)
- introduce DTOs if not already available and make sure if they exist that they are not outdated
- assemble one DTO as command payload from all incoming REST API parameters (headers, query/path paramters, request bodies)
- annotate attributes in the DTOs with Jakarta Validation annotations to enforce constraints on their values
- wired REST API to the new command processing, one service at a time/pull request
- take a non-critical service (like document management) and migrate it to the new command processing mechanics from top (REST API) to bottom (business logic service)
- refactor command handlers to new internal API
- make sure that the business service logic classes/functions take only one DTO request input parameter (aka don't let a function have 12 input parameters of type string...)
- when all integration tests run successfully then remove all legacy boilerplate code that is not used anymore
- make an ordered list of modules/features (easiest, lowest hanging fruit first)
- maintain at least the same performance as the current implementation
- optional: improve performance if it can be done in a reasonable time frame
- optional: improve resilience if it can be done in a reasonable time frame

## Non-Goals

- current command processing will stay untouched, will run independently of new infrastructure
- don't try cleaning up the storage layer; that's a separate effort for later (type safe queries, query peformance, clean entity classes)
- maker-checker is tightly coupled in the current command processing implementation upstream; this is a separate concern for a separate proposal (domains: security, workflow)
- doesn't need to be optimized for speed immediately
- no changes in the integration tests

## Proposed API Changes

### Command Wrapper

Class contains some generic attributes like:

- username
- tenant ID
- timestamp

The actual payload (aka command input parameters) are defined as a generic parameter "payload". It is expected that the modules implement classes that introduce the payload types and inherit from the abstract command class.

### Command Processing Service

Three performance levels are configurable via application.properties

- synchronously (required): this is pretty much as we do right now (use virtual threads optionally)
- asynchronously (optional): with executor service and completable futures (use virtual threads optionally)
- non-blocking (optional): high performance LMAX Disruptor non-blocking implementation

These different performance level implementations need to be absolute drop-in replacements (for each other). It is expected that more performant implementations need more testing due to increased complexity and possible unforeseen side effects (thread local variables, transactions). In case any problems show up we can always roll back to the required default implementation (synchronous).

NOTE: we should consider providing a command processing implementation based on Apache Camel once this concept is approved and we migrated already a couple of services. They are specialized for exactly this kind of use cases and have more dedicated people working on it's implementation. Could give more flexibility without us needing to maintain code.

### Middlewares

TBD

### Command Handlers

TBD

### References to users (aka AppUser)

Keep things lightweight and only reference users by their user names.f

## Risks

TBD

- feature creep

## ETA

A first prototype of the a new command processing component is ready for evaluation. There is also an initial smoke test (JMH) available.

You can try it out with the following instructions (it's still in a private repository, but will be published soon as an official PR):

git clone git@github.com:vidakovic/fineract.git

cd fineract

git checkout feature/[FINERACT-2169](https://issues.apache.org/jira/browse/FINERACT-2169)

./gradlew :fineract-command:build

./gradlew :fineract-command:jmh

## Diagrams

TBD

## Related Jira Tickets

**Difficulty:**Critical

**Project size:**~350 hour (large)

**Potential mentors:**

*Aleksandar Vidakovic*, mail: aleks (at) apache.org

*Project Devs*, mail: dev (at) fineract.apache.org

# Apache NuttX

[Add support to ESP Hosted on NuttX](https://issues.apache.org/jira/browse/NUTTX-25)

ESP Hosted is a firmware that allows ESP32xx modules shared WiFi and BLE with the host OS, like Linux, RTOS or even some baremetal MCU.

Add ESP Hosted support on NuttX will allow any platform supported by NuttX to WiFi and/or BLE from ESP32xx modules.

More info: [https://github.com/espressif/esp-hosted](https://github.com/espressif/esp-hosted)

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Alan Carvalho de Assis*, mail: acassis (at) apache.org

*Project Devs*, mail: dev (at) nuttx.apache.org

[Dropbear port (or other SSH Server/Client) to NuttX](https://issues.apache.org/jira/browse/NUTTX-21)

NuttX doesn't have a SSH Client/Server support yet.

Supporting a SSH server will open doors to let NuttX boards in the fields to be access remotely for maintenance

Adding support to SSH client will let low cost boards powered by NuttX and LVGL to become a remote console control for more advanced Linux server.

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Alan Carvalho de Assis*, mail: acassis (at) apache.org

*Project Devs*, mail: dev (at) nuttx.apache.org

[Create a NuttX Distribution with Dynamic Binary (ELF) Loading](https://issues.apache.org/jira/browse/NUTTX-20)

NuttX is very Unix/Linux-like RTOS for microcontrollers and it supports dynamic loading of binaries and libraries. It makes perfect sense to have the possibilities to create a NuttX Distros similar to what exists for Linux.

In fact there is already a proposal here: [https://github.com/apache/nuttx/issues/17351](https://github.com/apache/nuttx/issues/17351)

Goals:

1) Test ELF Loading in the current NuttX mainline

2) Create an application that will be downloaded and updated the existing version on the board

3) Add Library support on NuttX/NuttX-Apps (use Android Makefile Library building as reference)


**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Alan Carvalho de Assis*, mail: acassis (at) apache.org

*Project Devs*, mail: dev (at) nuttx.apache.org

[Micro-ROS integration on NuttX](https://issues.apache.org/jira/browse/NUTTX-14)

Micro-ROS ([https://micro.ros.org)](https://micro.ros.org)/) is a ROS2 support to Microcontrollers. Initially the project was developed over NuttX by Bosch and other EU organizations. Later on they added support to FreeRTOS and Zephyr. After that NuttX support started ageing and we didn't get anyone working to fix it (with few exceptions like Roberto Bucher work to test it with pysimCoder).

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Alan Carvalho de Assis*, mail: acassis (at) apache.org

*Project Devs*, mail: dev (at) nuttx.apache.org

[Add X11 graphic support on NuttX using NanoX](https://issues.apache.org/jira/browse/NUTTX-16)

NanoX/Microwindows is a small graphic library what allow Unix/Linux X11 application to run on embedded systems that cannot support X-Server because it is too big. Add it to NuttX will allow many applications to be ported to NuttX. More importantly: it will allow FLTK 1.3 run on NuttX and that could big Dillo web browser.

**Difficulty:**Major

**Project size:**~175 hour (medium)

**Potential mentors:**

*Alan Carvalho de Assis*, mail: acassis (at) apache.org

*Project Devs*, mail: dev (at) nuttx.apache.org

[Wireguard port to NuttX](https://issues.apache.org/jira/browse/NUTTX-22)

Wireguard is a light VPN solution for Linux and microcontrollers.

Porting wireguard for NuttX will allow remote and secure access to NuttX devices.

Projects to be used as reference:

**Difficulty:**Major

**Project size:**~175 hour (medium)

**Potential mentors:**

*Alan Carvalho de Assis*, mail: acassis (at) apache.org

*Project Devs*, mail: dev (at) nuttx.apache.org

[TinyGL support on NuttX](https://issues.apache.org/jira/browse/NUTTX-15)

TinyGL is a small 3D graphical library created by Fabrice Bellard (same creator of QEMU) designed for embedded system. Currently NuttX RTOS doesn´t have a 3D library and this could enable people to add more 3D programs on NuttX.

**Difficulty:**Major

**Project size:**~175 hour (medium)

**Potential mentors:**

*Alan Carvalho de Assis*, mail: acassis (at) apache.org

*Project Devs*, mail: dev (at) nuttx.apache.org

[Add multi-user support for NuttX](https://issues.apache.org/jira/browse/NUTTX-8)

Currently NuttX only support a single user. Also there is no file mode and file owner support.

In fact file mode is already defined in some places in the fs/ but it is not used.

This feature will make NuttX even yet more Unix/Linux-like.

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Alan Carvalho de Assis*, mail: acassis (at) apache.org

*Project Devs*, mail: dev (at) nuttx.apache.org

[NXBoot algorithm extension for two partitions](https://issues.apache.org/jira/browse/NUTTX-23)

Currently NuttX bootloader NXBoot requires three partitions to function properly. This is a trade of between better update speed and higher external memory capacity requirements.

The algorithm isn't suited for devices with small or even none external memory. A different algorithm that uses just two partitions (primary which runs the image) and update (where the update is uploaded) could be used for devices that use only internal memory. It would result in slower update process, but save memory space.

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Michal Lenc*, mail: michallenc (at) apache.org

*Project Devs*, mail: dev (at) nuttx.apache.org

[Analog (ADC/DAC) interfaces unification and better API](https://issues.apache.org/jira/browse/NUTTX-24)

The issue was discussed and is tracked in a GitHub issue [https://github.com/apache/nuttx/issues/16916](https://github.com/apache/nuttx/issues/16916)

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Michal Lenc*, mail: michallenc (at) apache.org

*Project Devs*, mail: dev (at) nuttx.apache.org

# Apache Wayang

[Make Wayang more datalake-friendly](https://issues.apache.org/jira/browse/WAYANG-54)

**Background**

Apache Wayang is a cross-platform data processing framework that allows users to execute analytics pipelines across multiple heterogeneous execution engines such as Apache Spark, Apache Flink, and relational database systems. Wayang’s optimizer automatically selects where to execute a pipeline and enables hybrid pipelines where part of it can be executed in one platform and part of it in another.

Wayang’s architecture is built around a pluggable backend model. Each execution engine is integrated via a dedicated backend implementation that translates Wayang’s logical operators into engine-specific physical operators.

Current execution engines (platforms) that Wayang supports include: JDBC-based databases, Spark, Flink, Tensorflow, Giraph.

**Project Goal**

Design and implement one or more **new execution engine backends** to enable Apache Wayang to work in data lake environments.

Potential target engines include (depending on feasibility and community discussion):

- Apache Datafusion

- Trino / Presto

- Dremio
- BigQuery

The project includes:

- Implementing the backend abstraction layer,

- Mapping Wayang logical operators to the new engine’s execution model,

- Integrating cost estimation for the optimizer.

**Difficulty:** Medium**Project size:** Depends on the number of platforms. It can be 175 (medium) or ~350 hours (large)**Potential mentors:**

- Zoi Kaoudi — zkaoudi (at) apache.org

- Juri Petersen — juri (at) apache.org
- Community — dev (at) wayang.apache.org

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Zoi Kaoudi*, mail: zkaoudi (at) apache.org

*Project Devs*, mail: dev (at) wayang.apache.org

[Implement a JDBC driver for Wayang](https://issues.apache.org/jira/browse/WAYANG-55)

**Background**

Apache Wayang is a cross-platform data processing framework that enables users to write data analytics tasks once and execute them across multiple heterogeneous execution engines (e.g., Spark, Flink, Java Streams, and others). In addition, Wayang optimizes execution plans across platforms and can split pipelines to be executed among multiple backends to optimize performance.

Currently, Wayang provides programmatic APIs (Java/Scala) and SQL support. However, it does not expose a standard **JDBC interface** that would allow external tools to connect to Wayang as if it were a relational database.

Many analytics tools rely on JDBC to communicate with query engines. Implementing a JDBC driver for Wayang would allow users to issue SQL queries to Wayang using standard database tooling.

**Project Goal**

Design and implement a **JDBC driver for Apache Wayang** that allows users to:

- Establish a JDBC connection to a Wayang instance,

- Submit SQL queries via standard JDBC interfaces,

- Retrieve results using ResultSet,

- Access metadata through DatabaseMetaData,

- Integrate Wayang with existing SQL-based tools and BI platforms.

The driver should delegate incoming SQL queries to the SQL api provided by Wayang.

**Difficulty:** Minor**Project size:** ~90 hours (small)**Potential mentors:**

- Zoi Kaoudi — zoka (at) apache.org

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Zoi Kaoudi*, mail: zkaoudi (at) apache.org

*Project Devs*, mail: dev (at) wayang.apache.org

[Support for a Dataframes API ](https://issues.apache.org/jira/browse/WAYANG-53)

**Background**

Apache Wayang is a cross-platform data processing framework that lets users write data analytics tasks once and execute them efficiently across diverse execution engines such as Apache Spark, Apache Flink, relational databases, and others. It abstracts heterogeneous backends and can enable efficient hybrid execution across different execution engines.

Currently, Wayang supports dataflow-style APIs in Java, Scala, and Python and an SQL API. However, there is **no high-level DataFrame API** — a programmatic abstraction widely used in modern data processing ecosystems (e.g., Spark DataFrames, Pandas, R DataFrames) — that lets users express relational transformations over structured datasets in a fluent, tabular style.

A DataFrame API for Wayang would dramatically improve usability for data engineers and scientists, making Wayang accessible to users familiar with DataFrame programming paradigms while preserving its powerful cross-platform optimization capabilities.

**Project Goal**

Implement a **DataFrame API for Apache Wayang** that:

- Represents structured data in a tabular abstraction (rows & columns),

- Supports common relational and analytical operations (select, filter, join, groupBy, aggregate, etc.),

- Can compile DataFrame operations into Wayang plans executed across backends transparently,

- Includes comprehensive documentation and examples.

**Outcomes & Impact**

By the end of GSoC, Wayang will have its first robust DataFrame API — a major usability milestone that bridges structured analytics with cross-platform execution. This will enhance adoption, unlock new classes of applications, and position Wayang as a friendly high-level programming environment in addition to its optimizer backend strengths.

**Difficulty:** Medium**Project size:** ~350 hours (Large)**Potential mentors:**

- Zoi Kaoudi — zkaoudi (at) apache.org

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Zoi Kaoudi*, mail: zkaoudi (at) apache.org

*Project Devs*, mail: dev (at) wayang.apache.org

# Mahout

[Add ZZFeatureMap Encoding for QDP](https://issues.apache.org/jira/browse/GSOC-312)

**Backgroud**

ZZFeatureMap is the most widely-used data encoding in quantum machine learning. It's the default in Qiskit and PennyLane for quantum kernel methods and variational classifiers.

QDP currently supports amplitude, angle, basis, and IQP encodings. Adding ZZFeatureMap completes our QML encoding suite.

**What is ZZFeatureMap?**

Maps classical features to quantum states using:

1. Hadamard gates (superposition)

2. RZ gates (single-qubit rotations)

3. ZZ interactions (two-qubit entanglement)

4. Repetition layers for expressivity

**Tracked github issue**

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Ryan Huang*, mail: hcr (at) apache.org

*Project Devs*, mail: dev (at) mahout.apache.org

[Apache Mahout Automated API Documentation Pipeline for Qumat & QDP](https://issues.apache.org/jira/browse/GSOC-313)

**Summary**

Implement an automated API documentation pipeline that generates and publishes API reference documentation from the Python (Qumat, QDP) and Rust (qdp-core) codebases, integrated into the project's Docusaurus website and CI.

**Background**

- Apache Mahout exposes
**two main API surfaces**:**Qumat**: Python library for quantum circuits (backends: Qiskit, Cirq, Amazon Braket).**QDP (Quantum Data Plane)**: GPU-accelerated encoding (Rust core + PyO3 Python bindings, qumat.qdp / _qdp).

- Manual doc updates are error-prone and don’t scale. Automating from source keeps docs accurate and reduces maintainer burden.

**Current state**

- QuMat API is maintained by hand and can drift from code.
- QDP API is waiting for new website migration to be finished.
- Rust (qdp-core) has extensive doc comments but no published rustdoc in the website.

**Goals**

1. Generate API reference from source for Python (Qumat).

2. Integrate generated docs into the existing Docusaurus site.

3. Automate the pipeline in CI so doc builds run on changes.

4. Define conventions (docstrings, public API) for future contributors.

**Deliverables**

- Python API doc pipeline for qumat and QDP.
- QuMat API reference either generated or explicitly linked.
- Rust (qdp-core) rustdoc built and linked from the website.
- CI job(s) that build Python API docs and rustdoc and fail on errors.
- Short contribution guide on docstring style and how to update API docs.

**Tracked github issue**

[https://github.com/apache/mahout/issues/1012](https://github.com/apache/mahout/issues/1012)

**Note**

Please email me(jiekaichang@apache.org) your proposal first and show me different types of approaches you considered and why you decided to do it this way.

**Difficulty:**Major

**Project size:**~175 hour (medium)

**Potential mentors:**

*Jie-Kai Chang*, mail: jiekaichang (at) apache.org

*Project Devs*, mail: dev (at) mahout.apache.org

# Beam

[Apache Beam Add Kafka Streams Runner](https://issues.apache.org/jira/browse/GSOC-305)

Sketch a working skeleton of portable Kafka Streams Runner for Apache Beam. The runner should be able to run basic portable pipelines and be a baseline implementation for further development, feature additions and performance optimization.

A more detailed design document shall be attached to the [github tracking issue](https://github.com/apache/beam/issues/18479).

**Difficulty:**Major

**Project size:**~175 hour (medium)

**Potential mentors:**

*Jan Lukavský*, mail: janl (at) apache.org

*Project Devs*, mail: dev (at) beam.apache.org

[A learning path to using accelerators with Beam](https://issues.apache.org/jira/browse/GSOC-311)

The Beam project has a few examples where hardware accelerators can be used to run models. See [https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/dataflow_tpu_examples.ipynb](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/dataflow_tpu_examples.ipynb)

This project is to improve on the available set of examples by building starter examples that allow a user to write code that slowly builds up to using these hardware accelerators. The idea would be:

- A simple python script that runs slowly without HW accelerators
- A script that shows improvements when using them
- A training job that uses accelerators
- A Beam pipeline that can train multiple models in parallel using accelerators
- A blog post that can serve as a guide for anyone learning to use hardware accelerators

These would run continuously to ensure their freshness.

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Pablo Estrada*, mail: pabloem (at) apache.org

*Project Devs*, mail: dev (at) beam.apache.org

[Simplify management of Beam infrastructure, access control and permissions via Platform features](https://issues.apache.org/jira/browse/GSOC-273)

This project consists in a series of tasks that build a sort of 'infra platform' for Beam. Some tasks include:

- Automated cleaning of infrastructure:
[[Task]: Build a cleaner for assets in the GCP test environment #33644](https://github.com/apache/beam/issues/33644) - Implement Infra-as-code for Beam infrastructure
- Implement access permissions using IaC:
[[Task]: Build a cleaner for assets in the GCP test environment #33644](https://github.com/apache/beam/issues/33644) - Implement drift detection for IaC resources for Beam
- Implement 'best-practice' key management for Beam (i.e. force key rotation for service account keys, and store in secret manager secrets)

- Implement access permissions using IaC:

A quality proposal will include a series of features beyond the ones listed above. Some ideas:

- Detection of policy breakages, and nagging to fix
- Security detections based on cloud logging
- others?

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Pablo Estrada*, mail: pabloem (at) apache.org

*Project Devs*, mail: dev (at) beam.apache.org

[Apache Beam Python SDK native streaming transforms](https://issues.apache.org/jira/browse/GSOC-315)

## Background

Apache Beam is a unified programming model for user developing data processing pipelines capable running in distributed systems. Apache Beam SDK officially supports Java, Python, and Go. While Java SDK was historically dominant, Python SDK is increasingly popular thanks to Beam ML. Python APIs are crucial for developers. We plan to port highly anticipated basic streaming transforms made convenient for Beam Python developers.

## Tasks

1. Python UnboundedSource ([https://github.com/apache/beam/issues/19137)](https://github.com/apache/beam/issues/19137))

While Splittable DoFn has been introduced as a Beam primitive transform handling IO sources, UnboundedSource arguably remains an easier API for users to author their own IOs. In the Java SDK, UnboundedSource/UnboundedReader has been (re)implemented as a wrapper of Splittable DoFn, we can follow the Java implementation and add it to Python.

Stretch goal: implement a native Python streaming IO based on UnboundedSource.

2. Python Watch Transform ([https://github.com/apache/beam/issues/21521)](https://github.com/apache/beam/issues/21521))

Currently we have a Watch transform in the Java SDK that is very useful when periodically polling for new input to a pipeline. We would like a parallel transform in Python.

Stretch goal: Update Python FileIO.readContinuously to use watch transform

## Deliverables

- Implementation of Python UnboundedSource: A functional wrapper API for UnboundedSource and UnboundedReader built on Splittable DoFn (a merged pull request to the Apache Beam repo).
- Implementation of Python Watch Transform: A parallel transform to the Java Watch API for periodic polling (a merged pull request to the Apache Beam repo).
- Unit and Integration Tests: tests for both features, specifically covering watermarks, checkpointing, and polling termination conditions.
- User Documentation: Updated SDK guides and Docstrings explaining how to author custom IOs using UnboundedSource and how to use the Watch transform in pipelines.
- Refactored FileIO.readContinuously (Stretch Goal): A pull request updating FileIO.read_continuously to utilize the new Watch transform logic.

## Recommended Skills

- Proficiency in Python, experience with pytest
- Java-to-Python Porting: Ability to read and interpret Java source code
- Version control: Git, development with GitHub
- nice to have: exposure to streaming data processing tools (e.g. Apache Beam/Flink/Spark, etc)

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Yi Hu*, mail: yhu (at) apache.org

*Project Devs*, mail: dev (at) beam.apache.org

# DolphinScheduler

[Apache DolphinScheduler Embedding the AlertServer into the API Server](https://issues.apache.org/jira/browse/GSOC-306)

**Apache DolphinScheduler**

Apache DolphinScheduler is a distributed and extensible workflow scheduler platform with powerful DAG visual interfaces, dedicated to solving complex job dependencies in the data pipeline and providing various types of jobs available out of box.

Website: [https://dolphinscheduler.apache.org/en-us/index.html](https://dolphinscheduler.apache.org/en-us/index.html)

GitHub: [https://github.com/apache/dolphinscheduler](https://github.com/apache/dolphinscheduler)

Linked GitHub Issue: [https://github.com/apache/dolphinscheduler/issues/8975](https://github.com/apache/dolphinscheduler/issues/8975)

**Background**

Currently, DolphinScheduler requires a separate alert-server to handle workflow and task alerts. Although the alert-server is lightweight, maintaining and deploying it separately adds operational complexity.

We aim to remove the standalone alert-server and embed its alerting functionality directly into the API server.

**Task**

Integrate the alert-server functionality into the API server so that it can handle workflow and task alerts natively.

**Deliverables**

- Remove the standalone alert-server.

- Enable the API server to handle all alerting tasks.
- Add Integration test case.

**Recommended Skills**

- Proficiency in Java.
- Familiarity with microservice, e.g. spring-boot.

- Familiarity with DolphinScheduler’s architecture and alerting mechanisms is a plus.

**Mentors**

- Wenjun Ruan(Apache DolphinScheduler PMC member),
[wenjun@apache.org](mailto:wenjun@apache.org) - Zihao Xiang(Apache DolphinScheduler PMC member),
[zihaoxiang@apache.org](mailto:zihaoxiang@apache.org)

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Wenjun Ruan*, mail: wenjun (at) apache.org

*Project Devs*, mail: dev (at) dolphinscheduler.apache.org

# SkyWalking

[Apache SkyWalking BanyanDB Native Data Export/Import Utility](https://issues.apache.org/jira/browse/GSOC-310)

**Background**

**BanyanDB** is the native storage engine for Apache SkyWalking, designed specifically for observability data (Traces, Metrics, and Logs). As BanyanDB matures into a production-ready storage backend, data portability becomes critical. Users need the ability to move datasets between environments (e.g., from production to staging for debugging) or export data for external analysis in tools like Python/Pandas, Spark, or specialized AI training pipelines.

Currently, BanyanDB supports disaster recovery backups and simple CSV dumps for specific models. This project aims to build a high-performance, comprehensive **Export/Import Utility** that supports multiple formats and ensures data integrity.

**Tasks**

**Multi-Format Support:**Implement export/import functionality for:

**Native Binary:**High-performance format for BanyanDB-to-BanyanDB migration.


**Plain Text/Standard:**Support for**Parquet**(optimized for metrics/measures) and**JSON/CSV**(for human readability).


**Batch & Stream Processing:**Ensure the tool can handle massive datasets by implementing chunked data reading and writing to avoid memory bottlenecks.

**Schema Evolution Handling:**Implement logic to handle cases where the schema in the exported file differs slightly from the target server's schema.

**Integration with bydbctl:**Expose these capabilities through a user-friendly CLI command suite (e.g., bydbctl data export --group=user_logs --format=parquet).

**Requirements**

- Strong knowledge of
**Go**and concurrency patterns.

- Experience with data serialization formats (Protobuf, Parquet, Apache Arrow).

- Familiarity with gRPC-based API communication.

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Hongtao Gao*, mail: hanahmily (at) apache.org

*Project Devs*, mail: dev (at) skywalking.apache.org

[Apache SkyWalking Natural Language to BydbQL](https://issues.apache.org/jira/browse/GSOC-309)

**Background**

**BanyanDB** is the native storage engine for Apache SkyWalking, designed specifically for observability data (Traces, Metrics, and Logs). It utilizes its own query language, **BydbQL**, which is SQL-like but optimized for time-series and observability schemas. While BydbQL is powerful, non-expert users or SREs in high-pressure situations may find it difficult to construct complex queries for specific traces or aggregated metrics.

The goal of this project is to build an **Intelligent Query Agent** that leverages **Large Language Models (LLMs)** to translate Natural Language (NL) into valid BydbQL.

**Tasks**

**Schema-Aware Prompting:**Develop a mechanism to extract BanyanDB metadata (Groups, Streams, Measures, Tag Families) and feed it into the LLM context (RAG - Retrieval-Augmented Generation).

**N2SQL Implementation:**Adapt state-of-the-art "Natural Language to SQL" (NL2SQL) techniques to the specific syntax and constraints of BydbQL.

**Verification Loop:**Integrate the agent with the existing BydbQL parser to validate generated queries before execution.

**CLI/UI Integration:**Implement a "chat" interface or an --ask flag in bydbctl (the BanyanDB CLI tool) to allow users to query data via plain English (e.g.,*"Show me the top 5 slowest services in the last hour"*).

**Requirements**

- Proficiency in
**Go**(BanyanDB's primary language).

- Experience with
**LLM APIs**(OpenAI, Gemini, or local models via Ollama) and orchestration frameworks (LangChain, LangGraph).

- Understanding of
**Compiler Front-ends**(Lexing, Parsing, AST).

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Hongtao Gao*, mail: hanahmily (at) apache.org

*Project Devs*, mail: dev (at) skywalking.apache.org

# IoTDB

[Compatible with TPU & integrate SOTA time series foundation models for IoTDB-AINode](https://issues.apache.org/jira/browse/GSOC-307)

**Background**

**Apache** **IoTDB** is a high-performance, IoT-native time-series database designed to manage massive volumes of time-series data generated by industrial IoT devices. It addresses challenges including high ingestion rates, complex out-of-order data handling, and real-time analytical requirements. **IoTDB-AINode** represents an endogenous node type in the IoTDB ecosystem, extending the database with native machine learning capabilities. IoTDB-AINode enables seamless integration of time series machine learning algorithms directly within the database engine, allowing users to register, manage, and execute inference tasks using simple SQL statements (e.g., *CREATE MODEL ..., SELECT * FROM FORECAST (...)*). This architecture eliminates costly data migration to external ML platforms, accelerates processing pipelines, and enhances data security by keeping computations close to the data. Currently, AINode includes built-in time series foundation models such as the Timer and Chronos for time series forecasting task.**Tensor Processing Units (TPUs)** are Google-developed AI accelerators specifically designed for neural network computations. Offering high-throughput matrix operations and energy efficiency, TPUs provide a compelling alternative to GPUs for deploying large foundation models. PyTorch/XLA enables PyTorch models to leverage TPU hardware through the XLA (Accelerated Linear Algebra) compiler, supporting both single-device and distributed training scenarios.**Time Series Foundation Models** have emerged as powerful tools for temporal analysis. These models demonstrate superior performance across diverse domains—from industrial sensor data to financial forecasting—making them ideal candidates for integration into IoTDB's analytical pipeline.

**Goal**

This project aims to enhance IoTDB-AINode with TPU hardware acceleration capabilities and integrate cutting-edge time series foundation models into the database's model inference pipeline. Specifically, the project will:

- Enable IoTDB-AINode to recognize and leverage Google TPU devices for model deployment and inference.
- Adapt the AINode packaging and compilation workflow (Maven/Java and Poetry/Python) to support TPU-specific releases.
- Survey and integrate 1-2 SOTA time series foundation models (e.g., TimesFM) into AINode's SQL-accessible model registry.
- Establish comprehensive CI pipelines for TPU environments to ensure long-term maintainability.

The ultimate outcome will empower IoTDB users to execute high-performance time series analysis on TPU hardware using state-of-the-art foundation models through simple SQL interfaces, significantly enhancing the database's analytical capabilities for industrial AI applications.

**Core Tasks（Mandatory）**

**TPU****Adaptation.**Implement TPU device recognition and tensor management within the AINode Python runtime. This involves:- Integrating PyTorch/XLA (torch_xla) to detect available TPU devices during AINode initialization.
- Implementing device abstraction layers to handle model loading and tensor operations on TPU hardware.
- Ensuring automatic fallback mechanisms to CPU/GPU when TPU is unavailable.

**Packaging for TPU Version.**Extend the existing build infrastructure to support TPU-enabled distributions:- Update Poetry configuration to manage PyTorch/XLA and TPU-specific Python dependencies.
- Create automated packaging scripts that bundle XLA compilers and TPU runtime libraries.
- Ensure the TPU version can be deployed directly in Google Cloud TPU environments and on-premise TPU pods without manual dependency resolution.

**Model Survey.**Conduct a comprehensive technical survey of SOTA time series foundation models available at project commencement. The deliverable will be a technical document analyzing each model's architecture, input requirements, computational complexity, zero-shot capabilities, and suitability for IoTDB's SQL-based inference pipeline. The survey will conclude with a justified selection of 1–2 models for integration based on deployability, inference latency, licensing, and compatibility with IoTDB’s SQL-based workflow.**Model Integration.**Integrate 1-2 selected foundation models into IoTDB-AINode's model inference framework:- Implement model wrappers conforming to AINode's model registration interface.
- Adapt models to process IoTDB's time series data format.
- Ensure compatibility with AINode's inference pipeline, supporting SQL syntax such as
*SELECT * FROM FORECAST (...)*. - Support both built-in model usage and custom model registration for integrated architectures.

**Integration Testing & CI.**Establish robust testing infrastructure for TPU functionality:- Design and implement integration tests covering device detection, model loading, tensor operations, and end-to-end inference workflows.
- Build TPU-specific CI environments using Google Cloud TPUs or TPU simulators.


**Advanced Tasks (Optional)**

**Distributed Large Model Deployment.**As an optional stretch goal, this task explores distributed deployment of large time series foundation models across multiple TPU devices. This involves:- Enabling distributed inference where large models are partitioned across TPU pods.
- Developing SQL extensions to specify distributed compute resources (e.g.,
*LOAD MODEL ... TO DEVICES ...*). - Optimizing communication patterns between DataNodes and AINode for high-throughput industrial scenarios involving thousands of time series streams.


**Deliverables**

**Fully Functional****Source Code****.**- Pull requests to Apache IoTDB repository containing TPU adaptation modules.
- Integration code for SOTA time series foundation models.
- Extended build configurations (Maven/Poetry/PyInstaller) supporting TPU distributions.

**Comprehensive Integration Tests.**- Automated test suites for TPU device detection and model execution.
- CI pipeline configurations for TPU environments.

**User Documentation.**- Deployment guide for TPU-enabled AINode (e.g. Google Cloud TPU).
- SQL reference extensions for new model types and TPU-specific configuration options.
- Tutorial documentation demonstrating time series analysis workflows using the integrated foundation models.


**Recommended Skills**

**Python >= 3.11.**Including asynchronous programming and ML pipeline development.

**Poetry & PyInstaller.**Experience with Python dependency management and executable packaging.

**PyTorch.**Known about the PyTorch/XLA integration for TPU support.

**Java & Maven.**Knowledge of multi-module Java projects, build profiles, and dependency management**.**

# Learning Material

**Apache****IoTDB.**[https://iotdb.apache.org/](https://iotdb.apache.org/)

**Time series forecasting models in HuggingFace.**[https://huggingface.co/models?pipeline_tag=time-series-forecasting&sort=trending](https://huggingface.co/models?pipeline_tag=time-series-forecasting&sort=trending)

**PyTorch****TPU****support.**[https://docs.pytorch.org/xla/master/accelerators/tpu.html](https://docs.pytorch.org/xla/master/accelerators/tpu.html)

**Difficulty:** medium**Mentor:** Yongzao Dan (Apache IoTDB PMC Member) *(yongzao@apache.org)*

**Difficulty:**Major

**Project size:**~175 hour (medium)

**Potential mentors:**

*Yongzao Dan*, mail: yongzao (at) apache.org

*Project Devs*, mail: dev (at) iotdb.apache.org

[Enhancing ThingsBoard Integration with IoTDB 2.X Table Mode](https://issues.apache.org/jira/browse/GSOC-304)

# Background

**Apache** **IoTDB** is a high-performance, open-source time-series database optimized for data management and analysis in Internet of Things (IoT) scenarios, while ThingsBoard is an open-source IoT platform for device management, data visualization, and rule-based automation.

With the release of IoTDB 2.X introducing a **dual-mode** **architecture** (tree and table), significant opportunities arise to enhance this integration. The table mode supports standard SQL syntax, JOIN operations, and user-defined functions, enabling more complex queries and analytics. This project proposes to develop an enhanced storage backend for ThingsBoard based on IoTDB's 2.X table mode, providing improved flexibility and performance for IoT data storage and analysis.

# Goal

The primary goal of this project is to design and implement a new, enhanced storage backend for ThingsBoard that strategically leverages key features of Apache IoTDB 2.X’s table mode to improve flexibility, query expressiveness, and performance for core IoT telemetry workloads. This enhancement aims to provide ThingsBoard users with more powerful SQL querying capabilities (including complex multi-device joins and time-window aggregations) and improved performance for specific workloads. Furthermore, the project seeks to strengthen the open-source ecosystem by providing a deeper, more capable integration between ThingsBoard and the Apache IoTDB project, resulting in a more robust end-to-end IoT solution for the community.


# Core Tasks (Mandatory)

**In-depth Analysis and Design**: Conduct a thorough analysis of the existing ThingsBoard-IoTDB integration architecture and ThingsBoard's storage backend interfaces (e.g., TimeseriesDao). Then, design an optimal strategy for mapping the ThingsBoard data model (devices, assets, telemetry, attributes, labels) to the IoTDB 2.X table mode. A key focus will be utilizing IoTDB's TAGS column to efficiently store and manage static device attributes (e.g., location, device type), enabling flexible device filtering and grouping based on these tags .**Implementation of Storage Backend Connector**:**Data Access Layer**: Based on the design, implement the relevant ThingsBoard storage backend interfaces to connect with IoTDB.**Write Path**: Develop efficient data writing logic that transforms device telemetry data received by ThingsBoard and performs batch writes to the corresponding tables in IoTDB.**Read/****Query****Path**: Implement query interfaces that translate data requests from ThingsBoard dashboards or the rule engine into efficient SQL queries that take full advantage of IoTDB 2.X table mode features.

**Performance Benchmarking and Comparison**: Design and execute standardized performance test cases (e.g., high-concurrency data ingestion, complex conditional queries, large-scale range queries). Produce a detailed performance comparison report between the new IoTDB 2.X table mode-based backend and ThingsBoard's existing data storage options, This report should quantify improvements in metrics like write throughput and query latency.**Testing and Documentation**: Write comprehensive integration tests to ensure the correctness and stability of the new functionality. Create detailed user documentation, including installation/configuration instructions, data model explanations, API usage guidelines, and best practices.**Community Collaboration and Upstream Contribution**: Actively communicate with the ThingsBoard open-source community at key project milestones to discuss designs and gather feedback. Submit high-quality Pull Requests (PRs) to the official ThingsBoard repository, adhering to its coding standards, with the goal of getting the implementation merged.

# Advanced Tasks (Optional)

**Leverage IoTDB UDFs**: Explore the integration of IoTDB's User-Defined Functions (UDFs) within ThingsBoard's rule engine. This could allow for performing more complex data processing and analysis (e.g., anomaly detection) directly within the database before data is pulled into ThingsBoard.

**Enhanced Data Modeling for Assets**: Extend the data mapping design to optimally support ThingsBoard's assets and the relations between entities (devices, assets, customers), exploiting the relational capabilities of the IoTDB table mode for more complex queries.

**Comprehensive Dashboard Demo**: Build a detailed ThingsBoard dashboard that showcases the advanced querying capabilities made possible by the new integration, such as visualizations based on multi-device joins or complex aggregations.

# Deliverables

- A fully functional storage backend plugin/implementation, including source code, build scripts, and configuration examples.
- A detailed design document explaining the data mapping and integration architecture between ThingsBoard and the IoTDB 2.X table mode.
- A comprehensive performance benchmark report comparing the new solution with existing options.
- Complete user and developer documentation.
- A Pull Request submitted to the ThingsBoard community containing the implementation, tests, and relevant documentation.
- A final project report summarizing work, technical challenges, learnings, and future possibilities.

# Recommended Skills

**Programming Language**: Proficiency in Java, as both ThingsBoard and IoTDB are primarily Java-based projects.

**Database Knowledge**: Understanding of SQL and fundamental database concepts. Knowledge of time-series data is a plus.

**System Integration**: Interest or experience in connecting different systems and understanding data flows.

**Learning and Communication**: Ability to quickly understand the codebases of two open-source projects and willingness to actively collaborate with community mentors and members.

# Learning Material

- Apache IoTDB Official Website:
[https://iotdb.apache.org/](https://iotdb.apache.org/) - ThingsBoard Official Documentation:
[https://thingsboard.io/docs/](https://thingsboard.io/docs/) - Integrated Reference:
[https://github.com/thingsboard/thingsboard/pull/11476](https://github.com/thingsboard/thingsboard/pull/11476) - IoTDB Table Mode Concepts:
[https://iotdb.apache.org/UserGuide/latest/Background-knowledge/Data-Model-and-Terminology_apache.html](https://iotdb.apache.org/UserGuide/latest/Background-knowledge/Data-Model-and-Terminology_apache.html) - IoTDB Table Mode Query Syntax:
[https://iotdb.apache.org/UserGuide/latest-Table/SQL-Manual/overview_apache.html](https://iotdb.apache.org/UserGuide/latest-Table/SQL-Manual/overview_apache.html)

**Difficulty:** medium**Mentor:** Xuan Wang (Apache IoTDB Committer) *(*[critas@apache.org](mailto:critas@apache.org)

*)*

**Difficulty:**Major

**Project size:**~175 hour (medium)

**Potential mentors:**

*Xuan Wang*, mail: critas (at) apache.org

*Project Devs*, mail: dev (at) iotdb.apache.org

[[GSoC] Flink connector for IoTDB 2.X Table Mode](https://issues.apache.org/jira/browse/GSOC-308)

# Background

**Apache** **IoTDB** is an open-source IoT-native time-series database designed for high-performance storage, ingestion, and analysis of massive time-series data from IoT devices. It supports deep integration with big data ecosystems like Apache Hadoop, Spark, and Flink, enabling seamless data processing workflows. IoTDB traditionally uses a tree-based data model for organizing time-series data hierarchically (e.g., root.group.device.sensor), which is efficient for device-centric IoT scenarios.

Starting with IoTDB 2.0, a dual-mode SQL architecture was introduced, adding a table mode alongside the tree mode. The table mode allows users to manage time-series data using SQL-like table structures, where each table represents a device type, with columns for timestamps, tags, and fields (e.g., measurements like temperature or humidity). This mode enhances flexibility for data analysis, supports standard SQL queries, and improves interoperability with relational tools. It is particularly useful for scenarios involving heterogeneous devices or advanced analytics, as it supports table-level schema management and retention-related configurations (e.g., TTL).**Apache** **Flink** is a powerful stream and batch processing framework for real-time data analytics. IoTDB already provides a Flink connector (flink-iotdb-connector) for reading from and writing to IoTDB using the tree mode, including IoTDBSource for data ingestion and IoTDBSink for output. There is also a Flink SQL connector (flink-sql-iotdb-connector) for SQL-based interactions and change data capture (CDC). However, these connectors primarily target the tree mode and lack full support for the table mode's features, such as table-specific metadata handling, SQL table mappings in Flink Table API, and optimized read/write operations for table-structured data. As a result, Flink users cannot natively treat IoTDB table-mode data as first-class tables in Flink SQL or the Table API. This gap limits the ability to leverage Flink's processing capabilities with IoTDB's modern table mode, especially in real-time IoT applications like predictive maintenance or anomaly detection.

This project aims to bridge this gap by developing a dedicated Flink connector for IoTDB's 2.X table mode, enabling efficient, real-time integration between Flink and IoTDB tables.

# Goal

The primary goal is to create a robust, production-ready Flink connector that supports reading from and writing to IoTDB tables using the 2.X table mode. This will allow Flink users to process IoT time-series data stored in table format, perform transformations, aggregations, and joins in real-time, and sink results back into IoTDB tables. The connector should align with Flink's DataStream and Table APIs, support fault tolerance, and handle table-specific features like tags, fields, and TTL. Ultimately, this will enhance IoTDB's ecosystem integration, making it easier for developers to build scalable IoT data pipelines.


# Core Tasks (Mandatory)

**Research and Design**: Analyze the existing flink-iotdb-connector and flink-sql-iotdb-connector to identify limitations with the table mode. Design the connector architecture, including schema and type mappings between Flink Table/RowData and IoTDB table-mode concepts (e.g., time column, tags, and fields). Define APIs for source and sink functions compatible with Flink 1.18+.

**Implement IoTDB Table Source**: Develop a Flink source connector (e.g., IoTDBTableSource) that reads data from IoTDB tables. Support filtering by time ranges, tags, and fields using IoTDB's SQL interface. Ensure it handles schema inference and dynamic table changes.

**Implement IoTDB Table Sink**: Create a Flink sink connector (e.g., IoTDBTableSink) for writing processed data back to IoTDB tables. Support batch and streaming modes, automatic schema creation (if enabled in IoTDB), and error handling for constraints like TTL or data types.

**Testing and Documentation**: Write unit and integration tests using Flink's testing utilities and IoTDB test clusters. Document usage examples, configuration options, and deployment guides in the IoTDB repository.

**Community Contributions**: Submit pull requests to upstream repositories for any required changes, and create example Flink jobs demonstrating the use cases.

# Advanced Tasks (Optional)

**Performance Optimization**: Implement optimizations like parallel reading/writing.

**Benchmarking and Comparison**: Develop benchmarks comparing the new connector's performance with the existing tree-mode connector, focusing on throughput, latency, and resource usage in IoT scenarios.

# Deliverables


Source code for the Flink connector for IoTDB table mode, including Maven artifacts (e.g., flink-iotdb-table-connector).

Comprehensive documentation, including API references, setup guides, and usage examples integrated into the IoTDB website.

Test suites covering core functionality, edge cases, and integration with Flink.

A demo application showcasing a complete Flink pipeline reading from/writing to IoTDB tables.

Optimization reports, benchmarks, and any upstream PRs.

# Recommended Skills

**Programming Language**: Proficiency in Java, as both Flink and IoTDB are primarily Java-based projects.

**Database Knowledge**: Understanding of SQL and fundamental database concepts. Knowledge of time-series data is a plus.

**System Integration**: Interest or experience in connecting different systems and understanding data flows.

**Learning and Communication**: Ability to quickly understand the codebases of two open-source projects and willingness to actively collaborate with community mentors and members.

# Learning Material


Apache IoTDB Official Website:[https://iotdb.apache.org/](https://iotdb.apache.org/)

Apache Flink Official Documentation:[https://flink.apache.org/](https://flink.apache.org/)

Integrated Reference:[https://github.com/apache/iotdb-extras/tree/master/connectors/flink-iotdb-connector](https://github.com/apache/iotdb-extras/tree/master/connectors/flink-iotdb-connector)

IoTDB Table Mode Concepts:[https://iotdb.apache.org/UserGuide/latest/Background-knowledge/Data-Model-and-Terminology_apache.html](https://iotdb.apache.org/UserGuide/latest/Background-knowledge/Data-Model-and-Terminology_apache.html)

IoTDB Table Mode Query Syntax:[https://iotdb.apache.org/UserGuide/latest-Table/SQL-Manual/overview_apache.html](https://iotdb.apache.org/UserGuide/latest-Table/SQL-Manual/overview_apache.html)

**Difficulty:** medium**Mentor:** Haonan Hou (Apache IoTDB PMC member) *(haonan@apache.org)*


**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Haonan Hou*, mail: haonan (at) apache.org

*Project Devs*, mail: dev (at) iotdb.apache.org

[Implement Trino-IoTDB Plugin to enable OLAP on time-series data](https://issues.apache.org/jira/browse/GSOC-303)

**Background**

Apache IoTDB (Internet of Things Database) is a high-performance, open-source time-series database optimized for data management and analysis in IoT scenarios. Trino (formerly PrestoSQL) is a fast distributed SQL query engine designed for running interactive analytic queries against data sources of all sizes.

Currently, while IoTDB provides strong capabilities for writing and querying time-series data, integrating it with the broader big data ecosystem for complex OLAP (Online Analytical Processing) remains a demand. A dedicated Trino connector for IoTDB will allow users to query IoTDB data using standard SQL via Trino and perform federated queries with other data sources (like Hive, MySQL, or Iceberg).

**Goal**

The goal of this project is to implement a trino-iotdb connector plugin based on the Trino SPI (Service Provider Interface). This connector will enable Trino to read data directly from IoTDB, supporting schema mapping, data projection, and predicate pushdown or maybe aggregate pushdown.


**Core Tasks（Mandatory）**

**Project Scaffolding:**Set up the Maven project structure for the trino-iotdb plugin and integrate the IoTDB JDBC API.**Metadata Implementation:**Implement ConnectorMetadata to map IoTDB’s Table Mode (relational view) to Trino’s relational metadata model:

Map IoTDB databases to Trino Schemas.

Map IoTDB Tables to Trino Tables.

Map IoTDB Data Type to Trino Data Type.

**Column Pruning (Projection Pushdown):**Ensure the connector strictly fetches only the requested columns (measurements) from IoTDB, avoiding SELECT * overhead.**Predicate Pushdown:**Implement optimization rules to push down SQL filters (especially time range filters and value filters) to the IoTDB engine to minimize data transfer.**Limit & Offset Pushdown:**Map Trino’s LIMIT and OFFSET clauses to IoTDB’s native query pagination to prevent fetching excessive data during preview or pagination queries.**Integration Testing:**Provide Docker-based integration tests to verify correctness using Trino's testing framework.

**Advanced Tasks (Optional)**

**Aggregation Pushdown:**Implement the applyAggregation method in the connector SPI.

Goal: Map Trino’s aggregate functions (e.g., COUNT, AVG, SUM, MIN, MAX) directly to IoTDB’s native aggregation queries.

Benefit: Instead of fetching raw data to Trino for calculation, the connector leverages IoTDB's pre-calculated statistics or downsampling capabilities, significantly reducing network overhead and latency.


**Deliverables**


A fully functional trino-iotdb connector source code.(a pull request to Trino Repo)

Comprehensive integration tests covering data types and query patterns.

User documentation explaining how to configure and use the connector.

**Recommended Skills**

**Java:**Proficiency in Java programming (Trino and IoTDB are both Java-based).**Database Internals:**Basic understanding of SQL execution, schema design, and database connectors.**Maven:**Experience with Java build systems.**Nice to have:**Familiarity with Trino SPI or IoTDB Session API.

# Learning Material


Apache IoTDB:[https://iotdb.apache.org/](https://iotdb.apache.org/)

Trino Connector Developer Guide:[https://trino.io/docs/current/develop/connectors.html](https://trino.io/docs/current/develop/connectors.html)

Trino PG Plugin:[https://github.com/trinodb/trino/tree/master/plugin/trino-postgresql/src/main/java/io/trino/plugin/postgresql](https://github.com/trinodb/trino/tree/master/plugin/trino-postgresql/src/main/java/io/trino/plugin/postgresql)

IoTDB Java JDBC API:[https://iotdb.apache.org/UserGuide/latest/API/Programming-JDBC_apache.html](https://iotdb.apache.org/UserGuide/latest/API/Programming-JDBC_apache.html)

IoTDB Table Model Concepts:[https://iotdb.apache.org/UserGuide/latest/Background-knowledge/Data-Model-and-Terminology_apache.html](https://iotdb.apache.org/UserGuide/latest/Background-knowledge/Data-Model-and-Terminology_apache.html)

IoTDB Table Model Query Syntax:[https://iotdb.apache.org/UserGuide/latest-Table/SQL-Manual/overview_apache.html](https://iotdb.apache.org/UserGuide/latest-Table/SQL-Manual/overview_apache.html)

**Difficulty:** medium**Mentor:** Yuan Tian (Apache IoTDB PMC Member) *(jackietien@apache.org)*


**Difficulty:**Major

**Project size:**~175 hour (medium)

**Potential mentors:**

*Yuan Tian*, mail: jackietien (at) apache.org

*Project Devs*, mail: dev (at) iotdb.apache.org

# Seata

[GSoC 2026 - Apache Seata(Incubating)Enhance the Seata framework Golang SDK’s support for multiple databases](https://issues.apache.org/jira/browse/GSOC-314)

**Project Overview**

**Title**

Enhance the Seata framework Golang SDK’s support for multiple databases

**Abstract**

Apache Seata(incubating) is a popular distributed transaction solution, providing solutions like AT, TCC, and XA for ensuring data consistency in microservice architectures.

The AT mode (Automatic Transaction) provides applications with non-intrusive distributed transaction capabilities by proxying SQL statements and parsing protocols. Although Seata-go currently supports MySQL and has initial compatibility with PostgreSQL, it still falls short in covering commonly used production databases, and precise compatibility with Oracle and MariaDB is an urgent need.

This project aims to align with the mature ecosystem of Seata Java and introduce AT mode support for Oracle and MariaDB in Seata-go. This not only involves parsing and adapting SQL dialects, but also includes metadata management, handling differences in Undo Log serialization, and integrating with the specific locking mechanisms of each database. It is a critical step in expanding the capability boundaries of Seata-go.

**Detailed Description** **Objectives**

- Console Metrics Visualization: Develop functionality to view various metrics related to the connection pool in the Seata console. The metrics should be displayed based on IP/connection pool granularity, helping users easily identify resource allocation and utilization.

- Metrics Control via Console: Allow users to control various aspects of the connection pools directly from the Seata console. This includes the ability to adjust minimum and maximum connection counts, configure connection acquisition timeout, and manage connection pool keep-alive settings.

**Deliverables**

**Complete MariaDB AT Mode Support (Priority P0)**- Implement MariaDB driver adapter layer (seata-at-mariadb Driver)
- Implement MariaDB TableMetaCache and Trigger
- Implement MariaDB UndoLogManager
- Handle dialect differences between MariaDB and MySQL (e.g., RETURNING clause, system variables)

**Complete Oracle AT Mode Support (Priority P1)**- Implement Oracle driver adapter layer (seata-at-oracle Driver)
- Implement Oracle metadata query adaptation (based on ALL_TAB_COLUMNS, ALL_INDEXES system views)
- Implement Oracle data type to JDBC type mapping (NUMBER, VARCHAR2, CLOB, DATE, etc.)
- Implement Oracle UndoLogManager with Undo Log serialization differences
- Adapt Oracle SQL dialect (ROWNUM pagination, Sequence retrieval, DUAL table, etc.)

**Integration Testing and Validation (Priority P1)**- Write comprehensive unit tests and integration tests covering single-table CRUD, multi-table join operations, and transaction rollback scenarios
- Validate accuracy of Before/After Image generation
- Validate correctness of global locks and Undo Log

**Samples and Documentation (Priority P2)**- Add Oracle and MariaDB usage demos in seata-go-samples
- Write a technical blog "Seata-Go Multi-Database Adaptation Design" explaining design concepts and implementation details


**Implementation Plan**

Phase 1: Requirement Analysis and Design

- Align scope and acceptance criteria with mentors/community: prioritize MariaDB (P0) and Oracle (confirm final priority as per topic), and define the must-cover SQL/transaction scenarios (CRUD, rollback, lock conflict, batch ops, joins where applicable).

- Study and benchmark Seata Java AT implementation: produce a gap list for Dialect, TableMeta, UndoLog, Before/After Image, and global lock integration, and decide what to port vs. re-design for Go.

- Design a pluggable multi-database architecture for Seata-Go: define clear interfaces (Dialect, MetaQuery, TypeMapper, UndoLogManager, DriverAdapter) and module boundaries for MariaDB/Oracle implementations; write a short design spec.

- Prepare baseline environments and regression safety: stand up MariaDB/Oracle test environments (local and/or CI) and create baseline test cases to ensure existing MySQL AT behavior does not regress.

Phase 2: MariaDB AT Mode Support (P0)

- Implement seata-at-mariadb driver adapter: integrate with database/sql, hook into key execution points, and ensure Seata AT context is correctly propagated.

- MariaDB dialect adaptation: handle MariaDB vs. MySQL differences (syntax/behaviors such as RETURNING-related cases, system variables, and any MariaDB-specific edge cases affecting parsing and image SQL).

- Metadata and caching: implement MariaDB TableMetaCache and metadata queries (columns, primary keys, indexes) with robust caching/invalidations as needed.

- MariaDB UndoLogManager: implement undo log write/read/delete and serialization strategy consistent with Seata-Go conventions; ensure rollback works for common and edge data types.

- Scenario-driven hardening: validate with integration tests covering single-table DML, unique key updates, batch updates, idempotent rollback, and lock conflict/retry behaviors.

Phase 3: Oracle AT Mode Support (P0/P1)

- Implement seata-at-oracle driver adapter: adapt to the chosen Oracle driver (godror / go-ora, per community decision), addressing bind variables, result set handling, and transaction boundary behaviors.

- Oracle metadata adaptation: implement metadata queries using Oracle system views (e.g., ALL_TAB_COLUMNS, ALL_INDEXES) and cache results effectively.

- Oracle type mapping: map Oracle types to Seata-Go internal types (NUMBER, VARCHAR2, CLOB, DATE, TIMESTAMP, etc.) to ensure image capture and undo serialization are consistent.

- Oracle dialect adaptation: support Oracle-specific SQL behaviors (ROWNUM pagination patterns, sequences, DUAL table usage, locking semantics where relevant).

- Oracle UndoLogManager: implement Oracle-compatible undo log persistence and serialization differences; validate large objects and time types in rollback.

Phase 4: Testing, Samples, and Documentation

- Testing: add unit tests (Dialect/TypeMapper/MetaQuery/UndoLog) and integration tests (real DB) to verify:
- Before/After Image correctness
- Global lock correctness (conflicts, concurrency, retries)
- Rollback correctness and idempotency
- No regressions for existing MySQL AT

- CI enablement (if feasible): make MariaDB/Oracle tests repeatable in CI or provide a documented script-based workflow for contributors.

- Samples: add full MariaDB and Oracle examples to incubator-seata-go-samples (config, schema, demo transactions, rollback demos).

- Documentation/blog: write “Seata-Go Multi-Database Adaptation Design” and user/developer docs covering configuration, driver selection, supported SQL patterns, and known limitations.

**Required Skills**

- Have Go language development experience, familiar with database/sql standard library and common database drivers (e.g., go-sql-driver/mysql, godror, go-ora)

- Proficient in SQL syntax, deep understanding of relational database principles, familiar with transaction isolation levels and row/table locking mechanisms

- Understand the core principles of Seata AT mode (Before/After Image, Undo Log, Global Lock)

- Have experience with Oracle or MariaDB databases, understand their dialect differences from MySQL

- Possess good documentation habits and code standards awareness, able to read Seata Java source code for reference

**Benefits to Apache Seata**

- Broader database coverage for Seata-Go AT mode: enables production adoption in enterprises that rely on MariaDB and Oracle.

- Lower migration and adoption cost: users can extend distributed transaction capability beyond MySQL with minimal application changes.

- Better maintainability and extensibility: a clean, interface-driven design (Dialect/Meta/UndoLog/TypeMapping) reduces future effort to add more databases.

- Higher reliability through verification: comprehensive integration tests and samples make correctness measurable and reduce regressions.

- Stronger community value: aligning with Seata Java’s proven approach and producing clear docs/design guidance improves contributor productivity and ecosystem confidence.

**Conclusion**

This project strengthens Seata-Go AT mode by adding robust MariaDB and Oracle support aligned with Seata Java’s mature implementation. By delivering dialect adaptation, metadata management, undo log handling, type mapping, and thorough testing plus samples and documentation, it significantly expands Seata-Go’s multi-database capabilities and improves its production readiness for real-world enterprise environments.

**Useful Link**

[https://github.com/apache/incubator-seata-go](https://github.com/apache/incubator-seata-go)

[https://github.com/apache/incubator-seata-go-samples](https://github.com/apache/incubator-seata-go-samples)

**Contact Information**

- Mentor Name: FengZhang [zfeng@apache.org], Apache Seata(incubating) PPMC member

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Feng Zhang*, mail: zfeng (at) apache.org

*Project Devs*, mail: dev (at) seata.apache.org

[GSoC 2026 - Apache Seata(Incubating)Enhance the Seata framework Golang SDK’s multi-registry support and seata-ctl capability](https://issues.apache.org/jira/browse/GSOC-316)

# Project Overview

## Title

Enhance Seata-Go Multi-Registry Support and seata-ctl Diagnostic Tool Capability

## Abstract

Apache Seata (incubating) is a popular distributed transaction solution for ensuring data consistency in microservice architectures. Seata-Go, as its Go language SDK, is responsible for implementing core TM/RM functionalities in the Go ecosystem.

Currently, Seata-Go lags behind the Java version in terms of registry support richness at the infrastructure layer, and its production-level transaction troubleshooting and operational toolchain (seata-ctl) is still in its early stages. This results in limited options for users in non-Etcd/Raft scenarios and high troubleshooting costs when transaction anomalies occur.

This project aims to align with Seata's infrastructure ecosystem by introducing support for four mainstream registries: **Nacos, ZooKeeper, Consul, and Redis** to Seata-Go. Additionally, it will significantly enhance seata-ctl's diagnostic capabilities through full-chain environment checks, transaction state insights, and an interactive terminal interface, reducing the operational threshold for distributed transactions.

## Detailed Description / Objectives

**Infrastructure Alignment**: Ensure Seata-Go can seamlessly integrate into existing enterprise-level microservice governance systems by implementing adapters for various mainstream registries.**Operational Efficiency Improvement**: Build a complete diagnostic command set enabling developers to quickly locate network, database, and transaction state anomalies, and simplify operation workflows through an interactive interface.**Community Ecosystem Contribution**: Produce high-quality design documents and technical blogs to help community users understand Seata-Go's underlying governance logic and operational best practices.

## Deliverables

### 1. Multi-Registry Cluster Support (Priority P0)

**Mainstream Registry Adapter Implementation**:

- Implement
**Nacos**and**ZooKeeper**registry adapters with support for service instance subscription, real-time listening, and multi-tenant isolation configuration. - Implement
**Consul**and**Redis**adapters with support for service registration/discovery and heartbeat monitoring mechanisms. - Bug fixes for Seata NamingServer Golang SDK.
- Ensure service registration path formats for all registries are fully compatible with Java version Seata.

- Implement
**Configuration and Initialization System Integration**:

- Extend configuration structure to standardize registry-specific configuration parameters.
- Optimize factory initialization logic to support smooth registry type switching via configuration files.


### 2. seata-ctl Diagnostic Tool Enhancement (Priority P1)

**Full-Chain Self-Check Functionality**:

- Implement automated environment checks covering network connectivity verification with the server.
- Implement database-level health checks including connection availability and validation of transaction core system table structures.
- Implement configuration file format and required field legality validation.

**Transaction State Insight Capability**:

- Implement real-time query functionality for active transaction lists.
- Implement query functionality for resource lock records corresponding to specific transaction identifiers (XID).
- Support structured output formats (e.g., table, JSON, YAML).

**Interactive Terminal Interface (TUI)**:

- Introduce a visual interactive mode for the tool, simplifying complex command input through interface guidance to enhance operational experience.


### 3. Testing, Samples, and Community Output (Priority P2)

**Testing and Validation**:

- Write unit tests and integration tests for each registry adapter to verify node change awareness capabilities.
- Validate diagnostic tool accuracy across different database dialects.

**Samples and Documentation**:

- Add complete multi-registry integration examples in seata-go-samples.
- Write technical articles:
**"Seata-Go Registry Extension Design and Practice Guide"**and**"Distributed Transaction Troubleshooting in Practice: Quickly Locating Anomalies with Diagnostic Tools"**.


## Implementation Plan

**Phase 1: Research and Architecture Design**

- Research existing Seata-Go registry implementations and study Seata NamingServer implementation logic.
- Design diagnostic tool's interaction logic and command set architecture, ensuring tool extensibility.

**Phase 2: Registry Adapter Development (P0)**

- Prioritize completion of core functionality implementation and compatibility testing for Nacos and ZooKeeper.
- Perform bug fixes for Seata NamingServer to optimize its stability in the Go SDK.
- Integrate Consul and Redis support and unify configuration initialization entry points.

**Phase 3: Diagnostic Tool and Interactive Interface Development (P1)**

- Develop core logic for environment checks and transaction state queries.
- Build interactive terminal interface (TUI), encapsulating underlying commands into intuitive visual operations.

**Phase 4: Testing Validation and Community Promotion (P2)**

- Improve test cases to ensure stability across different registry environments.
- Complete community technical article output and submit related sample code.


## Required Skills

- Have Go language development experience, familiar with concurrent programming and network communication.
- Understand service discovery principles, familiar with mainstream registries (e.g., Nacos, ZooKeeper).
- Understand basic distributed transaction principles, familiar with Seata's interaction architecture (TM/RM/TC).
- Familiar with command-line tool development, possess good code standards awareness and documentation writing skills.

## Benefits to Apache Seata

**Expand Infrastructure Boundaries**: Enable Seata-Go to adapt to more diverse enterprise production environments, eliminating selection barriers.**Improve Operational Convenience**: Fill the gap in operational diagnostic tools for the Go version, significantly reducing user learning and maintenance costs.**Enhance Ecosystem Interoperability**: Ensure consistency in governance between Go and Java versions, supporting Seata's unified multi-language ecosystem.

## Conclusion

This project addresses Seata-Go's shortcomings in infrastructure adaptation and operational troubleshooting by enhancing multi-registry support and diagnostic tool capabilities. This not only improves Seata-Go's production readiness but also strengthens the Apache Seata community ecosystem through user-friendly interactive tools and comprehensive technical documentation.

## Useful Link

[https://seata.apache.org/](https://seata.apache.org/)[https://github.com/apache/incubator-seata-go](https://github.com/apache/incubator-seata-go)[https://github.com/apache/incubator-seata-go-samples](https://github.com/apache/incubator-seata-go-samples)[https://github.com/apache/incubator-seata-ctl](https://github.com/apache/incubator-seata-ctl)

## Contact Information

- Mentor Name: TunGuo [tew@apache.org], Apache Seata(incubating) Committer

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*FinnTew*, mail: tew (at) apache.org

*Project Devs*, mail: dev (at) seata.apache.org

# HugeGraph

[[GSoC][HugeGraph] HugeGraph Query Engine Upgrade & Adaptation](https://issues.apache.org/jira/browse/GSOC-317)

**Description**

Currently, the HugeGraph core query engine is built on **Java 11 + TinkerPop 3.5.x + Groovy 3**. While this stack provides fundamental graph query capabilities, it lags behind in security, performance optimization, and support for modern features. Specifically, the built-in Groovy engine relies on complex, high-maintenance black/whitelist mechanisms for script security, which poses potential bypass risks.

The goal of this task is to comprehensively upgrade HugeGraph's underlying dependencies to **Java 17 + TinkerPop 3.7/3.8 + Groovy 4**. This is not just a version iteration, but a modern architectural transformation:

**Groovy 4 & TinkerPop 3.7/3.8**: Introduce improved syntax features and security designs. We aim to refactor HugeGraphSecurity using native, efficient sandboxing mechanisms to replace the legacy blacklist logic.**Java 17/21 Support**: Adapt to the new JDK to fully leverage features like ZGC/Shenandoah GC, Records, and Virtual Threads, significantly improving throughput and reducing long-tail latency in large-scale graph queries.

Applicants are expected to handle the full lifecycle, from dependency upgrades and code refactoring to unit test fixes and final performance benchmarking.

**Recommended Skills**

**Java Core**: Proficiency in Java development with a solid understanding of Java 17+ new features.**HugeGraph Architecture**: Basic understanding of HugeGraph's storage structure (KV Store), Schema design, and specifically the Gremlin query execution flow.**Graph Computing & Compilers**: Familiarity with the TinkerPop Gremlin framework architecture; knowledge of AST (Abstract Syntax Tree) parsing or Functional Programming (FP) mindset is a plus.**AI Coding**:**Proficiency in using AI Coding tools (e.g., Codex, Claude Code, Copilot) to assist in code refactoring, test case optimization, and source code interpretation is highly preferred.****Security Awareness**: Awareness of code security, understanding of how to prevent Script Injection, and experience designing secure sandbox environments.

### 💡 **Important Notes for Applicants**

**Authenticity Matters**: While we encourage the use of AI for coding efficiency, please**strictly control and reasonably limit**the use of LLMs when writing your project**proposal**/**emails**. We value genuine communication and mutual respect.**Proactive Engagement**: We highly recommend participating in community**Mini Tasks**early. Demonstrating your hands-on ability within the community will significantly increase your chances of selection and help build trust with mentors.

**Task List**

**Dependency Analysis & Upgrade**:- Analyze
**Breaking Changes**from TinkerPop 3.5 to 3.7/3.8. - Complete core dependency version upgrades and API adaptations following mentor confirmation.

- Analyze

**Java 17 Environment Adaptation**:- Resolve compile-time and runtime compatibility issues (e.g., reflection restrictions, module access) to ensure the Server module runs correctly on Java 17 (Java 21 is even better).
- Update Docker configurations to migrate the default runtime to Java 17 (while exploring backward compatibility with Java 11).


**PD & Store Module Upgrade (New)**:- Extend the upgrade scope to the
**PD (Placement Driver)**and**Store**modules after completing the core Server upgrade. - Ensure these modules are adapted to Java 17 to unify the runtime environment across the HugeGraph ecosystem.

- Extend the upgrade scope to the

**Security Module Refactoring**:- Refactor the HugeGraphSecurity component based on Groovy 4 features.
- Design a lightweight, secure script execution strategy and remove the performance-heavy legacy blacklist logic.


**Testing & Fixes**:- Fix Unit Test (UT) failures caused by the upgrade.
- Ensure all core functions (CRUD, complex Gremlin queries) pass verification.


**Performance Benchmarking**:- Produce a performance comparison report:
**Java 11 (Old)**vs.**Java 17 (New)**using the Twitter-14B public dataset. - Quantify improvements in
**Latency**reduction and**Throughput**increases.

- Produce a performance comparison report:

**References**

**New Contributor Guide**:[HugeGraph Contribution Guide (Issue #2212)](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2Fapache%2Fhugegraph%2Fissues%2F2212)- Environment setup & basics.

**Upgrade Docs**:[TinkerPop Upgrade Documentation](https://www.google.com/url?sa=E&q=https%3A%2F%2Ftinkerpop.apache.org%2Fdocs%2Fcurrent%2Fupgrade%2F)

**Reference Implementation**:[JanusGraph Upgrade PR (For reference only)](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2FJanusGraph%2Fjanusgraph%2Fpull%2F3914)

**Gremlin Learning**:[Practical Gremlin Guide](https://www.google.com/url?sa=E&q=https%3A%2F%2Fkelvinlawrence.net%2Fbook%2FGremlin-Graph-Guide.html)

**Project Wiki**:[HugeGraph Deepwiki](https://www.google.com/url?sa=E&q=https%3A%2F%2Fdeepwiki.com%2Fapache%2Fhugegraph%2F)

**Project Size**

**Difficulty**: Medium (Similar references available)

**Estimated Time**: ~250 Hours (~15 Weeks)

**Mentors**

- Yan Zhang:
[vaughn@apache.org](https://www.google.com/url?sa=E&q=mailto%3Avaughn%40apache.org)(Apache HugeGraph PMC)

- Imba Jin:
[jin@apache.org](https://www.google.com/url?sa=E&q=mailto%3Ajin%40apache.org)(Apache HugeGraph PMC)

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Imba Jin*, mail: jin (at) apache.org

*Project Devs*, mail:

# CloudStack

[[GSoC] [CloudStack] Improve CloudMonkey user experience by enhancing autocompletion](https://issues.apache.org/jira/browse/GSOC-295)

## Summary

Currently a lot of API parameters do not get auto-completed as cloudmonkey isn't able to deduce the probable values for those parameters based on the list APIs heuristics. A lot of these parameters are enums on CloudStack end and by finding a way to expose these and consume them on cloudmonkey side, we could improve the usability of the CLI greatly.

## Benefits to CloudStack

- Improved end user experience when using CLI
- Reduce incorrect inputs

## Deliverables

- Expose enums and all other relevant information that can be used to enhance auto-completion of parameters on CloudStack end -
- May require framework level changes and changes to APIs

- Consume these exposed details on Cloudmonkey end

## Dependent projects

[https://github.com/apache/cloudstack-cloudmonkey/](https://github.com/apache/cloudstack-cloudmonkey/)

Ref CloudStack Issue: [https://github.com/apache/cloudstack/issues/10442](https://github.com/apache/cloudstack/issues/10442)

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Pearl Dsilva*, mail: pearl11594 (at) apache.org

*Project Devs*, mail: dev (at) cloudstack.apache.org

# Apache Grails

[Author and Publish New Practical Guides for Apache Grails](https://issues.apache.org/jira/browse/GSOC-325)

Author and Publish New Practical Guides for Apache Grails on [https://guides.grails.org](https://guides.grails.org/) (will be moved to grails.apache.org soon)

## Background

The Grails Guides provide step-by-step, hands-on tutorials with accompanying GitHub repositories containing initial and complete project states. They cover core topics GORM, testing, security, frontend integrations (Vue.js, React, Angular), Micronaut features, deployment (AWS, Google Cloud, GitHub Actions), and more.

Existing guides are strong in foundational and some advanced areas but have gaps in:

- Modern frontend setups
- Broader cloud deployment
- Current DevOps practices
- Popular plugins/ecosystem updates

Creating 5-10 high-quality, up-to-date guides would directly enhance this key learning resource, making Grails more approachable and demonstrating current best practices without requiring core framework changes.

## Project Goals

**Research & Plan Topics:**Select 5-10 high-impact guide topics based on community needs (user list discussions, Slack feedback, gaps identified).**Develop Guides:**For each:- Build a complete, runnable Grails application example.
- Create initial and complete GitHub repos following the standard template.
- Write a clear, step-by-step Markdown guide with code snippets, explanations, and best-practice rationale.

**Test & Polish:**Ensure guides work with the latest stable Grails (e.g., 7.x or 8.x series), include tests where relevant, and follow accessibility/Asciidoc formatting standards.**Submit & Integrate:**Open PRs to publish guides update any related docs or grails.org links.**Optional Stretch Goals:**Add video walkthroughs (if comfortable), create a "What's New in Recent Guides" summary blog post, or contribute minor improvements to existing guides.

**Suggested Guide Topics (prioritize with mentor input):**

- Building Modern Full-Stack Apps with Grails + React/Vite (or Vue/Vite) – Update/extend older profiles with current tooling.
- Securing Grails APIs with JWT + OAuth2 (modern patterns, perhaps using Micronaut Security).
- Deploying Grails Apps to the cloud
- Advanced CI/CD
- Performance Tuning
- Using HTMX + Grails for Interactive UIs without Heavy Frontend Frameworks.

## Deliverables

- 5-10 new published guides on
[https://guides.grails.org](https://guides.grails.org/)(each with its own GitHub repo under grails-guides). - Corresponding initial and complete source code repositories.
- Well-structured Markdown/Asciidoc content with clear sections, screenshots/code blocks, and "Try it Yourself" instructions.
- PRs reviewed and merged by mentors/community.
- A short summary report or blog draft for the Grails blog announcing the new guides.
- Documentation updates if needed (e.g., category additions on the guides index page).

**Quantifiable Results for the Apache Community:**

- Fresh, relevant content that attracts and retains new developers.
- Reduced support burden on mailing lists/Slack by pointing users to modern tutorials.
- Evergreen educational assets maintained by the community.

## Proposed Timeline (12-week program)

**Community Bonding (May 2026):**Join Grails Slack/mailing list, review existing guides, discuss topic priorities with mentors, fork/clone template repo, set up local build.**Weeks 1–2:**Finalize 3–5 topics, create initial repos, outline guide structures.**Weeks 3–6:**Implement and document first 2–3 guides (focus on core features, testing).**Weeks 7–9:**Complete remaining guides, add polish (screenshots, edge-case notes), self-review for clarity.**Weeks 10–11:**Submit PRs for review, incorporate feedback, test on latest Grails version.**Week 12:**Final merges, any last tweaks, prepare announcement draft, evaluations.

## Required Skills

- Solid understanding of Grails (create-app, domains, controllers, services, GSP/JSON views).
- Experience with Groovy/Java and web basics (REST, security concepts).
- Good technical writing (clear, concise explanations).
- Git/GitHub proficiency (branching, PRs).
- Nice-to-have: Familiarity with Asciidoc/Markdown, frontend tools (Vite, npm), or deployment platforms.

## Why This Project?

This is a high-reward contribution that directly improves one of Grails' most visible learning resources. It's flexible, scope can adjust based on progress, and allows the student to master Grails while helping others. Similar documentation-focused GSoC projects have succeeded in many Apache projects.

If Grails is accepted for GSoC 2026, this would be an excellent intermediate project. Interested students should contact the Grails dev mailing list or Slack early to discuss topics and secure a mentor. The community welcomes fresh guides to keep the framework vibrant!

**Difficulty:** Medium**Project size:** ~350 hour (large)**Potential mentors:***James Fredley*

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*James Fredley*, mail: jamesfredley (at) apache.org

*Project Devs*, mail: dev (at) grails.apache.org

# Apache Fory

[Apache Fory Ruby Serialization](https://issues.apache.org/jira/browse/GSOC-321)

**Description:**

Apache Fory currently has no Ruby runtime, so Ruby services cannot participate in Fory xlang object exchange. This project implements Ruby xlang serialization with full wire compatibility to existing language runtimes, following the xlang specifications and issue #3379.

**Primary references:**

1. docs/specification/xlang_serialization_spec.md

2. docs/specification/xlang_implementation_guide.md

3. [https://github.com/apache/fory/issues/3379](https://github.com/apache/fory/issues/3379)

**Scope:**

1. Implement xlang binary format in Ruby runtime.

2. Support schema-consistent mode and compatible mode with meta share and TypeDef.

3. Implement registration model for numeric and named user types.

4. Implement deterministic struct serialization rules required by spec.

5. Implement reference tracking and reference flags behavior exactly per protocol.

6. Implement meta string encoding and dedup semantics needed by named types and TypeDef.

7. Provide cross-language interoperability with Java in both encode and decode directions.

**Expected outcomes:**

1. Ruby runtime package under ruby/ with serializer and deserializer for xlang protocol.

2. Public API centered on Fory entry point with configuration and registration APIs.

3. Core runtime modules for buffer, type resolver, ref resolver, meta string, TypeDef context, and field skipper.

4. Serializer coverage for primitives, temporal types, list, set, map, arrays, structs, and unions.

5. Struct DSL and schema metadata model for deterministic field ordering and stable schema behavior.

6. Compatibility handling for unknown fields and unknown union alternatives via safe skip logic.

7. Documentation for Ruby API usage, registration, schema evolution behavior, and constraints.

**Protocol requirements:**

1. Little-endian encoding for all multi-byte values.

2. Correct xlang header bitmap handling for null, xlang, and oob flags.

3. Exact reference flags and sequential reference ID assignment.

4. Correct type ID encoding and user type ID handling.

5. Correct namespace and type name metadata behavior for named types.

6. Deterministic struct field ordering exactly aligned with spec.

7. Meta string encoding and per-stream dedup behavior aligned with spec.

**Implementation phases:**

1. Phase 0: Ruby project skeleton, CI bootstrap, minimal smoke serialization path.

2. Phase 1: Buffer, varint and zigzag utilities, header handling, reference resolver core.

3. Phase 2: Primitive and temporal type support.

4. Phase 3: Collections and arrays support.

5. Phase 4: Type registry and schema-consistent struct serialization.

6. Phase 5: Meta string encoding and dedup.

7. Phase 6: Compatible mode and shared TypeDef.

8. Phase 7: Union and extension type support.

9. Phase 8: Performance hardening and allocation reduction.

**Testing and CI requirements:**

1. Add Ruby unit tests for protocol primitives, headers, references, and error handling.

2. Add golden vector tests for primitives, string encodings, list/set/map headers, TypeDef, and unions.

3. Add bidirectional interoperability tests:

- Ruby write to Java read.

- Java write to Ruby read.

4. Add compatibility tests for schema evolution in compatible mode, including add/remove/reorder and unknown field skipping.

5. Add tests for shared references, circular references, and ref tracking disabled behavior.

6. Add negative tests for invalid varint, unknown type ID, truncated payload, and malformed TypeDef.

7. Integrate Ruby lint and all Ruby xlang tests into CI so regressions fail CI automatically.

**Non-goals for initial delivery:**

1. Ruby-native non-xlang serialization format.

2. Decimal support.

3. Advanced runtime code generation in first iteration.

**Performance expectations:**

1. Keep hot serialization and deserialization paths allocation-conscious.

2. Add fast paths for homogeneous collections where safe.

3. Preserve protocol correctness while improving throughput and reducing allocations.

**Skills:**

Ruby, binary protocol implementation, serialization internals, cross-language compatibility testing, CI integration, performance optimization.

**Difficulty:**

Hard.

**Project size:**

Preferred 350 hours.

**Potential mentors:**

Chaokun Yang, Weipeng Wang.

**Source links:**[https://github.com/apache/fory/issues/3379](https://github.com/apache/fory/issues/3379)[https://github.com/apache/fory/blob/main/docs/specification/xlang_serialization_spec.md](https://github.com/apache/fory/blob/main/docs/specification/xlang_serialization_spec.md)[https://github.com/apache/fory/blob/main/docs/specification/xlang_implementation_guide.md](https://github.com/apache/fory/blob/main/docs/specification/xlang_implementation_guide.md)[https://github.com/apache/fory/tree/main/rust](https://github.com/apache/fory/tree/main/rust)[https://github.com/apache/fory/tree/main/java](https://github.com/apache/fory/tree/main/java)

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Chaokun Yang*, mail: chaokunyang (at) apache.org

*Project Devs*, mail: dev (at) fory.apache.org

[Apache Fory Row Format for Go, Swift, Dart, and JavaScript](https://issues.apache.org/jira/browse/GSOC-319)

**Description**:

Apache Fory already defines a cross-language row format and has standard row format implementations in Java, C++, and Python. This task adds standard row format support for Go, Swift, Dart, and JavaScript based on docs/specification/row_format_spec.md.

The implementation must follow the standard row format rules exactly, including 8-byte alignment, null bitmap behavior, fixed 8-byte field slots, relative offset plus size encoding for variable-width fields, and deterministic padding behavior.

Compact row format is explicitly out of scope for this task.

**Primary specification:**

docs/specification/row_format_spec.md

**Expected outcomes:**

1. Add standard row format read and write support in Go runtime.

2. Add standard row format read and write support in Swift runtime.

3. Add standard row format read and write support in Dart runtime.

4. Add standard row format read and write support in JavaScript runtime.

5. Implement standard row layout support for rows, arrays, maps, and nested structs according to the spec.

6. Ensure random field access without full object deserialization for supported field types.

7. Add clear API entry points for encoding typed data to row format and decoding or field-accessing from row format.

8. Update language guides and developer docs for row format usage and constraints.

**Required compatibility and test scope:**

1. Add per-language unit tests for null bitmap handling, fixed-width fields, variable-width offset and size encoding, alignment, and padding.

2. Add deterministic binary tests to verify encoded bytes for representative schemas.

3. Add cross-language compatibility tests against existing standard row format implementations, with Java as required reference endpoint.

4. Add interoperability tests for each new language reading rows produced by Java and writing rows that Java can read.

5. Add map and nested struct compatibility cases, not only primitive fields.

6. Add CI coverage for all new tests so regressions fail CI automatically.

**Non-goals:**

1. Compact row format implementation.

2. Protocol or wire format changes outside current standard row format specification.

3. Unrelated serialization runtime features not required for standard row format support.

**Skills:**

Go, Swift, Dart, JavaScript or TypeScript, binary format implementation, compiler or runtime internals, cross-language compatibility testing, performance-focused engineering.

**Difficulty**:

Hard.

Project size:

Preferred 350 hours.

**Potential mentors:**

Chaokun Yang, Weipeng Wang.

**Source links:**[https://github.com/apache/fory/tree/main/docs/specification](https://github.com/apache/fory/tree/main/docs/specification)[https://github.com/apache/fory/blob/main/docs/specification/row_format_spec.md](https://github.com/apache/fory/blob/main/docs/specification/row_format_spec.md)[https://github.com/apache/fory/tree/main/go](https://github.com/apache/fory/tree/main/go)[https://github.com/apache/fory/tree/main/swift](https://github.com/apache/fory/tree/main/swift)[https://github.com/apache/fory/tree/main/dart](https://github.com/apache/fory/tree/main/dart)[https://github.com/apache/fory/tree/main/javascript](https://github.com/apache/fory/tree/main/javascript)

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Chaokun Yang*, mail: chaokunyang (at) apache.org

*Project Devs*, mail: dev (at) fory.apache.org

[Apache Fory Lua Serialization](https://issues.apache.org/jira/browse/GSOC-323)

**Description:**

Apache Fory currently lacks a Lua runtime for xlang serialization. This project will implement Lua xlang serialization with protocol-correct wire compatibility against existing Fory runtimes.

**Primary references:**

1. docs/specification/xlang_serialization_spec.md

2. docs/specification/xlang_implementation_guide.md

**Scope:**

1. Implement Lua xlang encoder and decoder using little-endian binary format.

2. Implement type registry for numeric and named user types.

3. Implement serialization and deserialization for struct, enum, and union.

4. Support schema-consistent mode and compatible mode with meta share and TypeDef.

5. Implement metatable restoration for registered struct-like objects during deserialization.

6. Deliver cross-language interoperability with existing runtimes, with Java and Python as mandatory interoperability targets.

**Expected outcomes:**

1. New Lua module with public API:

- Fory.new(config)

- serialize(value, declared_type)

- deserialize(bytes, declared_type)

2. Core runtime modules:

- buffer and varint codecs

- header handling

- reference resolver

- type registry and type metadata

- meta string and TypeDef handling

- serializers for primitive, collection, map, enum, struct, and union

- skip-value support for unknown fields and union alternatives

3. Protocol-correct handling for:

- header bitmap flags

- reference flags and reference ID assignment

- type IDs and user_type_id encoding

- meta string encoding and dedup

- list and map headers

- deterministic struct field ordering

- union payload encoding

4. Documentation for Lua usage, registration rules, compatible mode behavior, and interoperability constraints.

**Implementation phases:**

1. Phase 0: project bootstrap and API scaffold.

2. Phase 1: core buffer, little-endian codecs, varints, and header read/write.

3. Phase 2: reference tracking and type meta core.

4. Phase 3: primitive and temporal serializers.

5. Phase 4: collection and map protocol support.

6. Phase 5: meta string and TypeDef support.

7. Phase 6: enum, struct, and union.

8. Phase 7: skip logic, compatibility hardening, malformed-input resilience.

9. Phase 8: performance optimization with pure Lua baseline and optional LuaJIT fast paths.

**Testing and CI requirements:**

1. Add Lua unit tests for buffer, varint, zigzag, tagged64, header flags, ref resolver, type meta, and TypeDef.

2. Add cross-language compatibility tests:

- Lua serialize -> Java deserialize.

- Java serialize -> Lua deserialize.

- Lua serialize -> Python deserialize.

- Python serialize -> Lua deserialize.

3. Include protocol-critical cases:

- primitives and boundary values

- UTF8, LATIN1, and UTF16 string payloads

- list, set, and map header combinations

- schema-consistent and compatible struct behavior

- known and unknown union cases

- shared and circular references

4. Add regression fixtures for deterministic protocol-critical payloads.

5. Add negative tests for malformed varint, unknown type ID, truncated payload, and malformed TypeDef.

6. Integrate Lua lint and all Lua xlang tests into CI so regressions fail automatically.

**Non-goals for initial delivery:**

1. Row format implementation.

2. Decimal support.

3. Native code generation or JIT-only dependency as a requirement.

**Performance requirements:**

1. Keep pure Lua path as canonical and fully compliant.

2. Avoid unnecessary allocations in hot encode and decode paths.

3. Ensure optimizations do not change protocol behavior.

**Skills:**

Lua 5.4 or 5.3, binary protocol implementation, serialization internals, cross-language compatibility testing, CI integration, performance optimization.

**Difficulty:**

Hard.

**Project size:**

Preferred 350 hours.

**Potential mentors:**

Chaokun Yang, Weipeng Wang.

**Source links:**

1. [https://github.com/apache/fory/issues/3380](https://github.com/apache/fory/issues/3380)

2. [https://github.com/apache/fory/blob/main/docs/specification/xlang_serialization_spec.md](https://github.com/apache/fory/blob/main/docs/specification/xlang_serialization_spec.md)

3. [https://github.com/apache/fory/blob/main/docs/specification/xlang_implementation_guide.md](https://github.com/apache/fory/blob/main/docs/specification/xlang_implementation_guide.md)

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Chaokun Yang*, mail: chaokunyang (at) apache.org

*Project Devs*, mail: dev (at) fory.apache.org

[Apache Fory Swift Schema IDL Codegen and gRPC Integration](https://issues.apache.org/jira/browse/GSOC-326)

Apache Fory has a mature compiler pipeline for FDL, Protocol Buffers, and FlatBuffers frontends, plus code generators for Java, Python, Go, Rust, and C++. The compiler also already includes service IR parsing and a `--grpc` generation path, but Swift code generation is not yet supported.

This project adds end-to-end Swift support in two layers:

1. Swift schema and model code generation from Fory IR.

2. Swift gRPC generation from service definitions, including transport bindings and a Fory-backed codec.

The implementation should follow existing compiler conventions and prioritize low-overhead, allocation-conscious runtime behavior.

**Problem Statement**

The repository already contains a Swift runtime (`swift/Sources/Fory`) but lacks compiler-generated Swift model code and Swift gRPC bindings from IDL files. This creates a gap:

- Swift users cannot use `foryc` to generate model types from `.fdl`, `.proto`, or `.fbs`.
- Service definitions parsed into compiler IR cannot yet target Swift transport code.
- There is no official Fory codec integration for grpc-swift.

**Why This Project Matters**

- Completes the Swift developer workflow: IDL -> generated models -> generated service APIs -> runnable gRPC client and server.
- Reuses existing multi-frontend service parsing support in compiler IR.
- Aligns Swift with other language targets and improves cross-language consistency.
- Enables high-performance Swift service communication using Fory serialization semantics.

**Expected Outcomes**

- Add Swift as a first-class compiler target (`
~~{~~}lang swift`, `{-}-swift_out`). - Generate Swift model code from schema definitions (messages, enums, unions, nested types).
- Generate `service_grpc.swift` from service definitions.
- Generate grpc-swift compatible async server and client wrappers.
- Implement a custom grpc-swift codec backed by Fory serialization and deserialization.
- Implement inbound zero-copy decode support with a safe copy fallback path.
- Add golden-style codegen tests for filenames and key generated signatures.
- Add cross-frontend parity tests for FDL, proto, and fbs service definitions.
- Provide runnable Swift server and client example(s) using generated code and codec.
- Document compiler usage, constraints, and integration steps.

**Detailed Scope**

1) Compiler and CLI Integration

- Add `SwiftGenerator` under `compiler/fory_compiler/generators/`.
- Register generator in `compiler/fory_compiler/generators/
*{*}init{*}*.py`. - Extend CLI output mapping and options to support `--swift_out`.
- Ensure `--lang swift` works with existing recursive import compilation flow.

2) Swift Model Code Generation

Generate Swift for:

- Enums
- Messages
- Unions
- Nested types
- Type registration helper APIs

**Requirements:**

- Follow Fory type ID behavior (explicit IDs, auto IDs, namespace/name registration fallback).
- Match existing cross-language semantics where applicable.
- Integrate with existing Swift runtime abstractions (`Serializer`, type resolver, registration APIs).

3) Swift Service and gRPC Code Generation

For each schema service:

- Generate `service.swift` containing service protocol and method shape declarations.
- Generate `service_grpc.swift` containing grpc-swift server and client transport bindings.

Required RPC support:

- Unary
- Client streaming
- Server streaming
- Bidirectional streaming

4) Fory Codec for grpc-swift

- Implement codec encode and decode using Fory Swift runtime.
- Ensure request and response types map correctly to generated Swift types.
- Provide clear error mapping for decode and type mismatch failures.

5) Zero-Copy Decode and Fallback

- Add a zero-copy-friendly decode path for inbound payload handling when safe ownership and lifecycle constraints are satisfied.
- Add a fallback path that copies payload bytes when zero-copy cannot be safely applied.
- Ensure behavior is deterministic and memory-safe.

6) Tests

Compiler tests:

- Add codegen tests validating generated Swift file names and key signatures.
- Add service generation tests for all RPC modes.
- Add cross-frontend equivalence tests for FDL/proto/fbs service definitions.

Swift runtime and integration tests:

- Codec round-trip tests.
- Error-path tests (invalid payload, type mismatch, unsupported mode).
- Zero-copy path and fallback path coverage.

7) Examples and Documentation

- Add runnable Swift gRPC server/client example using generated files.
- Update `docs/compiler/compiler-guide.md` for Swift codegen options and usage.
- Update `docs/compiler/generated-code.md` with Swift output layout and generated API shape.
- Add concise Swift integration documentation for grpc-swift + Fory codec.

**Performance and Quality Requirements**

- Keep allocation count low on encode and decode paths.
- Avoid unnecessary data copies in transport integration.
- Keep generated code predictable and stable for golden-style testing.
- Preserve compiler behavior for existing languages and frontends.

**Milestones (Recommended)**

1. Community Bonding

- Finalize generated API naming and file layout.
- Confirm Swift option strategy and dependency constraints.
- Agree on test matrix and acceptance checklist.

2. Phase 1

- Implement Swift generator base and CLI wiring.
- Generate core model types and registration helpers.
- Add baseline model codegen tests.

3. Phase 2

- Implement service generation (`service.swift`, `service_grpc.swift`).
- Support unary and all streaming RPC method shapes.
- Add service signature and transport generation tests.

4. Phase 3

- Implement and validate Fory grpc-swift codec.
- Implement zero-copy decode path and fallback path.
- Add integration example and end-to-end tests.

**Finalization**

- Documentation updates.
- Stability pass and cleanup.
- Final validation across compiler and Swift test suites.

**Acceptance Criteria**

1. `foryc` supports Swift generation through `~~{~~}lang swift` and `{-}-swift_out`.

2. Swift model code compiles and integrates with Fory Swift runtime.

3. Service generation outputs `service.swift` and `service_grpc.swift` with correct signatures.

4. Unary, client-streaming, server-streaming, and bidi-streaming methods are correctly generated.

5. Fory-backed grpc-swift codec works for request and response round-trip.

6. Zero-copy decode path exists with tested fallback behavior.

7. Added tests pass and no regressions are introduced in existing compiler suites.

8. Documentation and runnable Swift example are complete and usable.

**Skills Required**

- Swift
- grpc-swift
- Compiler and code generation
- Serialization internals
- Async and streaming APIs
- Testing and performance profiling

**Difficulty**

Hard

**Project Size**

350 hours

**Potential Mentors**

- Chaokun Yang
- Weipeng Wang

**Source Links**

[https://github.com/apache/fory/issues/3370](https://github.com/apache/fory/issues/3370)[https://fory.apache.org/docs/next/compiler/compiler_guide](https://fory.apache.org/docs/next/compiler/compiler_guide)[https://github.com/apache/fory/tree/main/compiler](https://github.com/apache/fory/tree/main/compiler)[https://github.com/apache/fory/tree/main/compiler/fory_compiler](https://github.com/apache/fory/tree/main/compiler/fory_compiler)[https://github.com/apache/fory/tree/main/compiler/fory_compiler/tests](https://github.com/apache/fory/tree/main/compiler/fory_compiler/tests)[https://github.com/apache/fory/tree/main/swift](https://github.com/apache/fory/tree/main/swift)[https://fory.apache.org/docs/guide/rust/](https://fory.apache.org/docs/guide/rust/)[https://github.com/grpc/grpc-swift](https://github.com/grpc/grpc-swift)

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Chaokun Yang*, mail: chaokunyang (at) apache.org

*Project Devs*, mail: dev (at) fory.apache.org

[Apache Fory Java & Python gRPC Integration](https://issues.apache.org/jira/browse/GSOC-318)

**Description:**

Apache Fory can already generate high-performance Java and Python model code from IDL, but end-to-end Java/Python gRPC integration is not available as a unified workflow.

This project will implement Java and Python gRPC integration in the Fory compiler by generating language-specific service and transport artifacts.

Java output artifacts: *Service.java and *Grpc.java.

Python output artifacts: *_service.py and *_grpc.py.

The implementation must use Fory serialization only, without protobuf runtime payload types. It must follow compiler conventions and keep runtime overhead low.

**Expected outcomes:**

1. Generate Java and Python gRPC service and binding code from service definitions.

2. Support unary and streaming RPC APIs based on Fory service IR.

3. Generate Fory-based request and response marshalling for both languages.

4. Implement zero-copy decode paths for inbound payloads in both Java and Python, with a safe fallback path when zero-copy cannot be applied.

5. Add golden code generation tests for output file names and key method signatures in both Java and Python generators.

6. Provide runnable Java and Python gRPC examples using generated stubs and Fory codec.

7. Update compiler documentation for Java and Python gRPC code generation usage and constraints.

**Required cross-language gRPC tests between Java and Python services:**

1. Add integration tests for Java server with Python client.

2. Add integration tests for Python server with Java client.

3. Cover request and response round-trip correctness using Fory-serialized payloads.

4. Include unary RPC coverage as required. Include streaming coverage when corresponding generated streaming APIs are in scope.

5. Validate compatibility for normal cases and key error paths, including decode errors and type mismatch.

6. Add coverage for zero-copy decode paths and fallback behavior in both Java and Python integrations.

CI end-to-end test requirements:

1. Add Java and Python gRPC end-to-end interoperability tests into CI.

2. CI must execute both directions: Java server to Python client, and Python server to Java client.

3. CI must fail on serialization compatibility regressions.

4. CI should run deterministic test cases with stable assertions for payload correctness and error handling behavior.

**Skills:**

Java, Python, gRPC Java, grpcio, compiler and code generation, serialization internals, testing, performance optimization.

**Difficulty:**

Medium to Hard.

**Project size:**

Preferred 350 hours.

**Potential mentors:**

Chaokun Yang, Weipeng Wang.

**Source links:**[https://github.com/apache/fory/issues/3272](https://github.com/apache/fory/issues/3272)[https://github.com/apache/fory/issues/3273](https://github.com/apache/fory/issues/3273)[https://fory.apache.org/docs/next/compiler/compiler_guide](https://fory.apache.org/docs/next/compiler/compiler_guide)[https://github.com/apache/fory/tree/main/compiler](https://github.com/apache/fory/tree/main/compiler)[https://github.com/apache/fory/tree/main/java](https://github.com/apache/fory/tree/main/java)[https://github.com/apache/fory/tree/main/python](https://github.com/apache/fory/tree/main/python)[https://fory.apache.org/docs/next/guide/java/](https://fory.apache.org/docs/next/guide/java/)[https://fory.apache.org/docs/guide/python/](https://fory.apache.org/docs/guide/python/)

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Chaokun Yang*, mail: chaokunyang (at) apache.org

*Project Devs*, mail: dev (at) fory.apache.org

[Apache Fory C++ & Rust gRPC Integration](https://issues.apache.org/jira/browse/GSOC-320)

**Description:**

Apache Fory can generate high-performance C++ and Rust model code from IDL, but it does not yet provide end-to-end gRPC service binding generation for both languages as one aligned workflow.

This project will add C++ and Rust gRPC code generation in the Fory compiler using Fory serialization instead of protobuf runtime payload types.

C++ generated outputs:

- service.h for service API abstractions.
- service.grpc.h for gRPC declarations.
- service.grpc.cc for gRPC implementations.

Rust generated outputs:

- service.rs for service API traits/modules.
- service_grpc.rs for tonic server/client transport bindings.

The implementation should follow Fory compiler conventions and prioritize performance-first, low-overhead runtime behavior.

**Expected outcomes:**

1. Parse service IR and generate C++ and Rust gRPC outputs from service definitions.

2. Support unary and streaming RPC method generation in both language targets.

3. Generate clear separation between language-level API abstractions and transport bindings.

4. Generate C++ abstract service interfaces and client stubs compatible with gRPC C++.

5. Generate Rust tonic-compatible async server and client wrappers.

6. Implement Fory-based request and response serialization hooks for both C++ and Rust generated bindings.

7. Implement zero-copy deserialization buffer support for inbound gRPC payloads in both languages, with safe fallback when zero-copy cannot be applied.

8. Add golden code generation tests for generated file names and key method signatures in both targets.

9. Add runtime tests for codec round-trip behavior, error handling, and fallback behavior.

10. Add interoperability tests for C++ and Rust generated services, including C++ server with Rust client and Rust server with C++ client.

11. Provide runnable C++ and Rust server/client examples using generated bindings and Fory codec.

12. Update compiler and language documentation for C++/Rust gRPC code generation usage and constraints.

**CI requirements:**

1. Add C++ and Rust gRPC code generation tests to CI.

2. Add C++ and Rust runtime tests for generated codec and service bindings to CI.

3. CI must fail on generated API signature regressions and serialization compatibility regressions.

**Skills:**

C++ 17, Rust, gRPC, tonic, compiler and code generation, serialization internals, async Rust, testing, performance optimization.

**Difficulty:**

Medium to Hard.

**Project size:**

Preferred 350 hours.

**Potential mentors:**

Chaokun Yang, Weipeng Wang.

**Source links:**[https://github.com/apache/fory/issues/3276](https://github.com/apache/fory/issues/3276)[https://github.com/apache/fory/issues/3275](https://github.com/apache/fory/issues/3275)[https://fory.apache.org/docs/next/compiler/compiler_guide](https://fory.apache.org/docs/next/compiler/compiler_guide)[https://github.com/apache/fory/tree/main/compiler](https://github.com/apache/fory/tree/main/compiler)[https://github.com/apache/fory/tree/main/cpp](https://github.com/apache/fory/tree/main/cpp)[https://github.com/apache/fory/tree/main/rust](https://github.com/apache/fory/tree/main/rust)[https://fory.apache.org/docs/guide/cpp/](https://fory.apache.org/docs/guide/cpp/)[https://fory.apache.org/docs/guide/rust/](https://fory.apache.org/docs/guide/rust/)

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Chaokun Yang*, mail: chaokunyang (at) apache.org

*Project Devs*, mail: dev (at) fory.apache.org

[Apache Fory Go & JavaScript gRPC integration](https://issues.apache.org/jira/browse/GSOC-322)

**Description:**

Apache Fory can generate high-performance model code for Go and JavaScript/TypeScript from IDL, but end-to-end gRPC service binding generation across these two ecosystems is not yet complete as a unified workflow.

This project will add Go and JavaScript/TypeScript gRPC code generation to the Fory compiler using Fory serialization instead of protobuf runtime payload types.

The implementation should follow Fory compiler conventions, remain dependency-light in runtime layers, and prioritize low-overhead, performance-first behavior.

**Potential Outcomes:**

1. Parse service IR and generate Go and JavaScript/TypeScript gRPC outputs for unary and streaming methods.

2. Generate Go outputs `**_service.go` and `**_grpc.go` with ServiceDesc, server interfaces, and client wrappers compatible with grpc-go.

3. Generate JavaScript/TypeScript service interface and gRPC binding outputs compatible with @grpc/grpc-js and existing JS/TS generator layout conventions.

4. Wire request/response payload handling through generated Fory serializer and deserializer functions in both targets.

5. Implement zero-copy deserialization buffer support for inbound gRPC payloads in both Go and JavaScript runtimes, with safe fallback paths when zero-copy cannot be applied.

6. Coordinate with JS/TS type generation so emitted message, enum, and union types are directly usable by generated gRPC stubs.

7. Add golden codegen tests for generated file names and key signatures for both language targets.

8. Add end-to-end interoperability tests between generated Go and JavaScript services, including Go server with JS client and JS server with Go client.

9. Add CI coverage for codegen tests, runtime codec tests, and Go<->JavaScript gRPC interoperability tests.

10. Provide runnable Go and JavaScript/TypeScript server-client examples using generated bindings and Fory codec.

11. Update compiler documentation for Go and JavaScript/TypeScript gRPC code generation usage and constraints.

**Skills:**

Go, JavaScript/TypeScript, Node.js, gRPC (grpc-go and @grpc/grpc-js), compiler/code generation, serialization internals, testing, performance optimization.

**Difficulty:**

Medium to Hard

**Project size:**

350 hours

**Potential mentors:**

Chaokun Yang, Weipeng Wang

**Source links:**

1. [https://github.com/apache/fory/issues/3274](https://github.com/apache/fory/issues/3274)

2. [https://github.com/apache/fory/issues/3278](https://github.com/apache/fory/issues/3278)

3. [https://github.com/apache/fory/issues/3280](https://github.com/apache/fory/issues/3280)

4. [https://fory.apache.org/docs/next/compiler/compiler_guide](https://fory.apache.org/docs/next/compiler/compiler_guide)

5. [https://github.com/apache/fory/tree/main/compiler](https://github.com/apache/fory/tree/main/compiler)

6. [https://github.com/apache/fory/tree/main/go](https://github.com/apache/fory/tree/main/go)

7. [https://github.com/apache/fory/tree/main/javascript](https://github.com/apache/fory/tree/main/javascript)

8. [https://fory.apache.org/docs/guide/go/](https://fory.apache.org/docs/guide/go/)

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Chaokun Yang*, mail: chaokunyang (at) apache.org

*Project Devs*, mail: dev (at) fory.apache.org

[Apache Fory Dart gRPC integration](https://issues.apache.org/jira/browse/GSOC-324)

**Description**

Apache Fory does not yet generate Dart gRPC service bindings.

This project will add Dart gRPC code generation to the Fory compiler. For each service definition, the compiler should generate Dart service interfaces and gRPC transport bindings that follow the existing Dart generator layout and use a Fory codec instead of protobuf runtime payload types.

The implementation must keep the Fory runtime free of gRPC dependencies. Any required gRPC glue should be emitted as generated helper code. Runtime behavior should remain low-overhead and allocation-conscious.

**Potential Outcomes**

- Generate Dart service interface and gRPC binding outputs from service definitions, aligned with current Dart generator conventions.
- Generate Dart gRPC server and client stubs for unary and streaming RPCs using Dart gRPC APIs.
- Wire request/response handling through generated Fory serializer and deserializer functions.
- Implement zero-copy deserialization buffer support for inbound gRPC payloads, with a safe fallback path when zero-copy cannot be applied.
- Coordinate with Dart type generation so emitted message, enum, and union types are directly usable by generated gRPC stubs.
- Add golden codegen tests for generated file names and key signatures.
- Provide a runnable Dart server/client example using generated bindings and the Fory codec.
- Update compiler documentation for Dart gRPC code generation usage and constraints.

**Skills：**Dart, gRPC (`grpc`), compiler/code generation, serialization internals, async programming, testing, performance optimization.

**Difficulty：** Medium**Project size：**175 hours**Potential mentors：**Chaokun Yang, Weipeng Wang**Source links：**

[https://github.com/apache/fory/issues/3279](https://github.com/apache/fory/issues/3279)[https://github.com/apache/fory/issues/3281](https://github.com/apache/fory/issues/3281)[https://fory.apache.org/docs/next/compiler/compiler_guide](https://fory.apache.org/docs/next/compiler/compiler_guide)[https://github.com/apache/fory/tree/main/compiler](https://github.com/apache/fory/tree/main/compiler)[https://github.com/apache/fory/tree/main/dart](https://github.com/apache/fory/tree/main/dart)[https://github.com/apache/fory/blob/main/dart/README.md](https://github.com/apache/fory/blob/main/dart/README.md)[https://github.com/apache/fory/tree/main/dart/packages/fory](https://github.com/apache/fory/tree/main/dart/packages/fory)

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*Chaokun Yang*, mail: chaokunyang (at) apache.org

*Project Devs*, mail: dev (at) fory.apache.org

# Spark

[SPIP Client-Side Metadata Caching for Spark Connect](https://issues.apache.org/jira/browse/SPARK-55163)

**This SPIP proposes adding a client-side schema cache for Spark Connect DataFrames.**

Currently, every call to df.columns or df.schema triggers a synchronous gRPC analysis request to the server. While these are local and near-instant in Spark Classic, in Connect they average 277 ms on standard cloud setups (like AWS t3.medium). This makes iterative work extremely slow; we've measured a 13-second lag for 50 metadata calls in a typical ETL pipeline.

This delay is forcing developers to use a "Shadow Schema" pattern, where they manually track column names in local lists to avoid the RPC overhead. Since Spark DataFrames are immutable, we can fix this by caching the resolved schema on the client after the first request. Our POC shows this reduces the 13-second lag to about 250 ms (a 51× speedup) without breaking the core Spark Connect model.


I have followed the official SPIP template for the detailed breakdown below.

**SIP**

[ https://docs.google.com/document/d/1xTvL5YWnHu1jfXvjlKk2KeSv8JJC08dsD7mdbjjo9YE/edit?tab=t.0](https://docs.google.com/document/d/1xTvL5YWnHu1jfXvjlKk2KeSv8JJC08dsD7mdbjjo9YE/edit?tab=t.0)

**Benchmark** - [https://docs.google.com/document/d/1ebX8CtTHN3Yf3AWxg7uttzaylxBLhEv-T94svhZg_uE/edit?tab=t.0](https://docs.google.com/document/d/1ebX8CtTHN3Yf3AWxg7uttzaylxBLhEv-T94svhZg_uE/edit?tab=t.0)

**Difficulty:**Major

**Project size:**~350 hour (large)

**Potential mentors:**

*vaquar khan*, mail: vaquar.khan@gmail.com (at) apache.org

*Project Devs*, mail:
