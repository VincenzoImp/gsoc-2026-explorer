# PostgreSQL — Project Ideas

**Source:** https://wiki.postgresql.org/wiki/GSoC_2026
**Scraped:** 2026-02-22T23:28:47.569554

---

# GSoC 2026

[Jump to navigation](https://wiki.postgresql.org#column-one)

[Jump to search](https://wiki.postgresql.org#searchInput)

This page is for Google Summer of Code 2026 project ideas.

IF YOU ARE A MENTOR: there is a top-level GSoC page for PostgreSQL here:[PostgreSQL General GSoC Page]-please read this first before proceeding to contact the admins! PLEASE make sure you have read everything thoroughly.

IF YOU ARE A CONTRIBUTOR: there is a top-level GSoC page for PostgreSQL here:[PostgreSQL General GSoC Page]-please read this first before proceeding to contact mentors! Contribution guidelines, channels and communication methods are in this page too. PLEASE make sure you have read everything thoroughly.

**Note on Project Selection and Mentor Availability**

Please be aware that the list of ideas below is a starting point. Due to the competitive nature of GSoC:

- Not all ideas will be funded. Google provides us with a limited number of "slots," and we can only accept the highest-quality proposals as determined by our mentors.
- Mentor Bottlenecks: Primary mentors will only take on one contributor. If several people apply for ideas listed under the same mentor, only the strongest application will be selected.
- Be Selective: We encourage you to check our communication channels (e.g., Slack) to see if many other contributors are already targeting a specific idea

**Mentors mailing list for proposals**: gsoc-mentors@lists.postgresql.org

## Status

PostgreSQL has been accepted for Google Summer of Code 2026

## Admins

- Jesper Pedersen <jesperpedersen (dot) db (at) gmail (dot) com>
- Pavlo Golub <pavlo (dot) golub (at) gmail (dot) com>

## Mentors

The following individuals have been listed as mentors on the below projects:

- Pavlo Golub
- Jesper Pedersen
- Mark Wong
- Ahmed Gouda
- Luca Ferrari
- Tejas Tyagi
- Haoran Zhang
- Mohab Yassar
- Ashutosh Sharma
- Bassam Adnan
- Konstantina Skovola
- Akshat Jaimini
- Sachin Beniwal
- Arth Thapa
- Nik Samokhvalov
- Kirk Wolak
- Andrei Lepikhov
- Andreas Karlsson

## Timeline

- March 16 - GSoC contributor application period begins
- March 31 - GSoC contributor application deadline
- April 21 - GSoC contributor proposal rankings due from Org Admins
- April 30 - Accepted GSoC contributor projects announced
- May 4 - GSoC 2026 begins !

## Test Development in C/C++: Implementing event-driven concurrency in OLTP test tool (dbt5)

### Project Description

This project is a learning exercise in developing event-driven code by converting a thread-based concurrency model in a C++ application to use an event-driven model. DBT-5 is the application that is an open source implementation of the TPC Benchmark(TM) E Specification. This specification is an OLTP workload modeling a brokerage house. DBT-5 is currently using a thread (pthreads) based model in several programs and we want to convert that to a concurrency model that has shown itself to be significantly less resource intensive.

The general outline of the project, which can be adapted depending on the contributor's skill level:

- Learn how to program a simple event-driven program using libev
- Learn how to use DBT-5 to run a small scale test against PostgreSQL
- Replace the threaded model in the DBT-5, one program at a time

### Skills needed

- C
- C++

### Difficulty level

Moderate

### Project size

Long (350 hours)

### Mentors

- Mark Wong <markwkm (at) gmail (dot) com>
- Akshat Jaimini

### Expected outcomes

- Successful and working event-driven code.

### References

- DBT-5 code:
[https://github.com/osdldbt/dbt5](https://github.com/osdldbt/dbt5) - libev homepage:
[https://software.schmorp.de/pkg/libev.html](https://software.schmorp.de/pkg/libev.html) - Code example of using libev to convert DBT-2 (another OLTP test kit):
[https://github.com/osdldbt/dbt2/commit/0e6214381867dd608221a2ec30b37e560115d4e3](https://github.com/osdldbt/dbt2/commit/0e6214381867dd608221a2ec30b37e560115d4e3) - TPC Benchmark(TM) E Specification, DBT-5 implements this:
[https://www.tpc.org/tpce/](https://www.tpc.org/tpce/)

## Adding features to the Julia Procedural Language: pl/julia

### Project Description

This project is a learning exercise in how procedural languages get implemented. pl/Julia allows stored procedures and user defined functions to be created using the Julia programming language. pl/Julia currently supports:

- Triggers functions
- Event triggers
- Anonymous code blocks
- Directly access the database
- Some, but not all, PostgreSQL data types

The general outline of the project, which can be adapted depending on the contributor's area of interests:

- Updating pl/Julia to build and with the current version of Julia's C API's
- Support additional datatypes:
- DateTime / Time / Timestamp
- bytea

- Handle arrays passed as IN parameters
- Additional suggestions by contributor allowed here

### Skills needed

- C
- Julia may be helpful

### Difficulty level

Intermediate

### Project size

Long (350 hours)

### Mentors

- Konstantina Skovola
- Mark Wong <markwkm (at) gmail (dot) com>

### Expected outcomes

- Successful and working extension.

### References

- pl/Julia project page:
[https://github.com/pljulia/pljulia](https://github.com/pljulia/pljulia) - Previous
[pl/Julia status report](https://docs.google.com/presentation/d/1cTnsUWiH6o0YH6MlZoPLofna3eNT3P3r9HSL9Dyte5U/edit?usp=sharing) - Julia language homepage:
[https://julialang.org/](https://julialang.org/) - Julia documentation for embedding in C:
[https://docs.julialang.org/en/v1/manual/embedding/](https://docs.julialang.org/en/v1/manual/embedding/)

## Implement AI copilot for pgwatch

### Project Description

This project proposes building a standalone, CLI-based AI copilot for PostgreSQL monitoring, designed to work with metrics collected by pgwatch.

pgwatch is a mature, PostgreSQL-specific monitoring system that stores a rich set of performance metrics and statistics. However, analyzing these metrics during incidents still requires significant manual effort: navigating dashboards, correlating multiple data sources, and relying on expert knowledge.

The goal of this project is to allow engineers to use pgwatch and analyze its metrics using natural language prompts.

### Skills needed

- Go
- PostgreSQL

### Difficulty level

- Moderate

### Project size

- Large (350 hours).

### Mentors

- Ahmed Gouda <gouda0x (at) gmail (dot) com>
- Pavlo Golub

### Expected outcomes

- A CLI-based AI copilot for PostgreSQL monitoring that works with pgwatch.

### References

- pgwatch:
[https://github.com/cybertec-postgresql/pgwatch](https://github.com/cybertec-postgresql/pgwatch) - GitHub Copilot CLI (conceptual inspiration):
[https://github.com/features/copilot/cli](https://github.com/features/copilot/cli)

## pgagroal: High-available (HA) functionality

### Project Description

The goal of this project is to allow pgagroal operate in a high-available environment.

This project requires to analyze, design and implement a solution where read-only queries can be executed on a replica instance. Or even be delegated from the primary instance to a replica.

The final solution should describe the architecture of a solution where 2 pgagroal instances works against a PostgreSQL cluster in a primary/replica setup - including the additional components needed (if necessary) in a bare metal / container / Kubernetes environment.

### Skills needed

- C
- PostgreSQL

### Difficulty level

- Hard

### Project size

- Large (350 hours).

### Mentors

- Luca Ferrari <fluca1978 <at> gmail (dot) com>
- Jesper Pedersen <jesperpedersen (dot) db (at) gmail (dot) com

Contact mentors for submission requirements.

### Expected outcomes

- Using a replica for read-only queries.

### References

- pgagroal:
[https://github.com/pgagroal/pgagroal](https://github.com/pgagroal/pgagroal)

## pgagroal: Advanced security

### Project Description

The goal of this project is to add advanced security functionality to pgagroal.

The main focus is to add full pooling support for pgagroal to PostgreSQL communication. Note, that this might require a clean-room TLSv1.2+ implementation where we can cache and update the security context. Additionally areas such as client certificate authentication, SCRAM-SHA-256-PLUS and enhanced vault security can be investigated.

### Skills needed

- C
- Transport Layer Security (TLS)
- PostgreSQL

### Difficulty level

- Hard

### Project size

- Large (350 hours).

### Mentors

- Tejas Tyagi <tejastyagi (dot) tt (at) gmail (dot) com>
- Luca Ferrari <fluca1978 <at> gmail (dot) com>

Contact mentors for submission requirements.

### Expected outcomes

- End-to-end TLS communication from client to PostgreSQL with pooling support

### References

- pgagroal:
[https://github.com/pgagroal/pgagroal](https://github.com/pgagroal/pgagroal)

## pgmoneta: Model Context Server implementation

### Project Description

The goal of this project is to enhance the Model Context Protocol server for pgmoneta.

The main focus is to support all the commands of pgmoneta, and their parameters. And, the requirements outside the commands such as security.

Part of the implementation should make it easy to test the functionality when new functionality is added to pgmoneta

### Skills needed

- Rust
- PostgreSQL

### Difficulty level

- Moderate

### Project size

- Large (350 hours).

### Mentors

- Haoran Zhang <andrewzhr9911 (at) gmail (dot) com>
- Jesper Pedersen <jesperpedersen (dot) db <at> gmail (dot) com>

Contact mentors for submission requirements.

### Expected outcomes

- A MCP server that support all the pgmoneta CLI commands

### References

## pgmoneta: Write-Ahead Log (WAL) & Model Context Server (MCP)

### Project Description

The goal of this project is to enhance the Write-Ahead Log (WAL) functionality of pgmoneta and its tools. Especially pgmoneta-walfilter. This work will include expanding the test cases, and making sure that PostgreSQL 14 to PostgreSQL 19 are fully supported.

This project also need to implement WAL functionality into the Model Context Protocol (MCP) server in order to create WAL streams for recovery in an easy way.

### Skills needed

- C
- Rust
- PostgreSQL

### Difficulty level

- Moderate

### Project size

- Large (350 hours).

### Mentors

- Mohab Yaser <mohabyaserofficial2003 (at) gmail (dot) com>
- Haoran Zhang <andrewzhr9911 (at) gmail (dot) com>

Contact mentors for submission requirements.

### Expected outcomes

- Enhance pgmoneta-walfilter, increase code coverage of WAL generation and support WAL based commands in the MCP server

### References

## pgmoneta: Legacy incremental backup

### Project Description

The goal of this project is to complete the support of incremental backups of PostgreSQL version before 17.

The main focus is to get tablespaces supported, and expand the test suite to cover for the different scenarios between PostgreSQL 14 and PostgreSQL 16.

This project should complete full support for full and incremental backup and restore for legacy PostgreSQL versions.

### Skills needed

- C
- PostgreSQL

### Difficulty level

- Moderate

### Project size

- Large (350 hours).

### Mentors

- Ashutosh Sharma <ash2003sharma (at) gmail (dot) com>
- Haoran Zhang <andrewzhr9911 (at) gmail (dot) com>

Contact mentors for submission requirements.

### Expected outcomes

- Support PostgreSQL 14-16 incremental backups with tablespaces

### References

- pgmoneta:
[https://github.com/pgmoneta/pgmoneta](https://github.com/pgmoneta/pgmoneta)

## pgmoneta: Storage engines

### Project Description

The goal of this project is to implement support for using external storage engines - such as SSH and S3 - for all of pgmoneta's commands.

The main focus is to create a unified interface that can be used across all storage engines to minimize integration into the pgmoneta infrastructure.

It should be possible to use one or more storage engines per cluster setup.

### Skills needed

- C
- PostgreSQL

### Difficulty level

- Hard

### Project size

- Large (350 hours).

### Mentors

- Jesper Pedersen <jesperpedersen (dot) db (at) gmail (dot) com>
- Haoran Zhang <andrewzhr9911 (at) gmail (dot) com>

Contact mentors for submission requirements.

### Expected outcomes

- Unified storage engine interface, and a full implementation of one or more engines

### References

- pgmoneta:
[https://github.com/pgmoneta/pgmoneta](https://github.com/pgmoneta/pgmoneta)

## pgexporter: Historic data

### Project Description

The goal of this project to add a history to pgexporter such that metrics are stored over time based on the configuration. Backends should be sqlite, PostgreSQL or TimescaleDB.

This data can then be used to look at trends through reports or UIs, or even a Model Context Protocol (MCP) server.

### Skills needed

- C
- Prometheus
- PostgreSQL

### Difficulty level

- Moderate

### Project size

- Large (350 hours).

### Mentors

- Bassam Adnan <mailbassam (at) gmail (dot) com>
- Jesper Pedersen <jesperpedersen (dot) db (at) gmail (dot) com>

Contact mentors for submission requirements.

### Expected outcomes

- Infrastructure for historic data that can be retrieved through various UIs

### References

- pgexporter:
[https://github.com/pgexporter/pgexporter](https://github.com/pgexporter/pgexporter)

## pg_ai_query: Improving AI Query Generation Accuracy and Configuration

### Project Description

pg_ai_query is a PostgreSQL extension that generates SQL queries from natural language using AI models. While functional, production usage reveals that LLMs frequently hallucinate PostgreSQL syntax generating non-existent functions or version-incompatible queries.

This project aims to dramatically improve query accuracy by integrating real-time PostgreSQL documentation context (e.g., Context7 MCP), and to solve configuration challenges where PostgreSQL extensions cannot access environment variables or secrets managers.

Students will design and implement an architecture that decouples AI logic from the extension, enabling accurate, version-aware query generation with flexible configuration.

### Skills needed

- C (PostgreSQL extension development, SPI)
- Python/Go/Rust (optional)
- HTTP/REST API integration
- Basic understanding of LLM behavior

### Difficulty level

Moderate

### Project size

Medium

### Mentors

- Sachin Beniwal <sachinbeniwal0101 (at) gmail (dot) com>
- Arth Thapa <probablyarth (at) gmail (dot) com>

### Expected outcomes

- Measurable improvement in query generation accuracy
- Flexible configuration support (environment variables, secrets)
- Decoupled architecture enabling independent updates and testing
- Documentation and test suite

### References

[https://github.com/benodiwal/pg_ai_query](https://github.com/benodiwal/pg_ai_query)[https://benodiwal.github.io/pg_ai_query/](https://benodiwal.github.io/pg_ai_query/)[https://github.com/upstash/context7](https://github.com/upstash/context7)

## Join Removal Based on Foreign Key Constraints

### Project Description

The project focuses on adding the ability to remove joins to tables when the join is on a foreign key column and only the child table columns are needed in the query result.

This is a common optimization in enterprise databases (Oracle, DB2) that PostgreSQL currently lacks. When a view joins multiple tables but a query only needs columns from some of them, the optimizer should be able to eliminate unnecessary joins if foreign key constraints guarantee referential integrity.

Example scenario:

-- View joining orders to customers CREATE VIEW order_summary AS SELECT o.* FROM orders o JOIN customers c ON o.customer_id = c.id; -- Query only uses order columns - join should be eliminated SELECT order_id, amount FROM order_summary;

The optimizer should recognize that the join to customers table is unnecessary since:

- Only columns from orders are selected
- The foreign key constraint guarantees the join will succeed
- No filtering on customers columns exists

### Skills needed

- C programming
- SQL
- PostgreSQL

### Difficulty level

Hard

### Project size

Large: approximately ~350 hours of work.

### Mentors

- Nik Samokhvalov <nik (at) postgres (dot) ai>
- Kirk Wolak <wolakk (at) gmail (dot) com>
- Andrei Lepikhov <lepihov (at) gmail (dot) com>

### Expected outcomes

- A working implementation of FK-based join elimination in the query optimizer
- Updated cost estimation to account for eliminated joins
- Comprehensive regression tests covering various join patterns
- Documentation outlining the optimization rules and limitations
- Performance benchmarks demonstrating query speedups

### References

## B-tree Index Bloat Reduction (Page Merge)

### Project Description

The project focuses on implementing efficient B-tree index bloat reduction through page merging. B-tree indexes can become severely bloated after heavy UPDATE/DELETE workloads - in production systems, indexes with 90%+ bloat are common.

Current solutions have significant drawbacks:

**REINDEX**: Requires AccessExclusiveLock for entire duration (blocks all access)**REINDEX CONCURRENTLY**: Very long duration, requires 2x disk space**pg_repack**: External tool, complex setup, requires double space

This project would implement in-core page merging that:

- Merges sparsely populated leaf pages with their neighbors
- Uses two-phase locking (light lock for planning, brief exclusive lock for execution)
- Provides crash safety through WAL logging
- Achieves 30-50% bloat reduction with minimal disruption

A prototype extension (pg_btree_compact) has been developed demonstrating the approach. This project would work toward integrating similar functionality into core PostgreSQL, potentially as part of VACUUM or as a new REINDEX variant.

### Skills needed

- C programming
- PostgreSQL
- B-Tree structures

### Difficulty level

Hard

### Project size

Large: approximately ~350 hours of work.

### Mentors

- Kirk Wolak <wolakk (at) gmail (dot) com>
- Nik Samokhvalov <nik (at) postgres (dot) ai>
- Andrei Lepikhov <lepihov (at) gmail (dot) com>

### Expected outcomes

- Working implementation of B-tree page merging
- Integration with VACUUM or as standalone command
- Proper WAL logging for crash safety
- Minimal exclusive lock duration (<1ms per 100 page merges)
- Performance benchmarks and bloat reduction measurements
- Comprehensive tests using amcheck for index integrity verification

### References

## Monitoring Tools Performance: pg_stat_statements and LWLock Contention

### Project Description

The project focuses on improving the performance and reducing lock contention in PostgreSQL's monitoring infrastructure, particularly pg_stat_statements and related statistics collectors. Keeping in mind that the more executing backends you have running queries need to lock this structure for writing. Then monitoring software needs to lock this structure for reading. The faster the system, the more locking/unlocking takes up most of the time. Also, as the number of statements being tracked increases, the reading takes longer. Finally, sampling could reduce some of this.

pg_stat_statements is essential for query performance analysis, but it has known scalability issues:

**Lock contention**: High-frequency queries cause contention on the shared hash table**Memory pressure**: Limited entries (default 5000) cause eviction churn on busy systems**Reset overhead**: pg_stat_statements_reset() can cause significant pauses

Similar issues affect other monitoring tools:

- pg_stat_activity updates
- pg_stat_user_tables/indexes statistics
- Custom statistics collectors

Goals of this project:

- Analyze and profile current lock contention patterns
- Implement lock-free or reduced-lock data structures where possible
- Add partitioned/sharded hash tables for better scalability
- Consider/test ideas on timing out (and not logging) if having to wait too long for the lock
- Consider/test a secondary queue for things to add when we have time
- Consider/test a circular buffer so reading always returns the previous portion of the buffer w/o locking
- Improve statistics aggregation efficiency
- Reduce impact on production workloads

This work is critical for observability in high-throughput PostgreSQL deployments where monitoring overhead must be minimized.

### Skills needed

- C programming
- Performance profiling
- Concurrency/locking patterns
- PostgreSQL

### Difficulty level

Hard

### Project size

Large: approximately ~350 hours of work.

### Mentors

- Kirk Wolak <wolakk (at) gmail (dot) com>
- Nik Samokhvalov <nik (at) postgres (dot) ai>
- Andrei Lepikhov <lepihov (at) gmail (dot) com>

### Expected outcomes

- Measurable reduction in lock contention for pg_stat_statements
- Improved scalability under high query rates (target: 100k+ queries/sec)
- Benchmarks comparing before/after performance
- Documentation of new architecture and trade-offs
- Regression tests ensuring correctness of statistics collection

### References

## Wait Event Coverage Improvements

### Project Description

The project focuses on improving PostgreSQL's wait event coverage to provide more accurate observability into what the database is doing at any given moment. More importantly, what the database is waiting on. While PostgreSQL has many waits being properly recorded, this project is designed to find as many places as possible where we wait, and we should clarify what we are waiting on/for. This project will add the code required to track those new wait areas properly.

Many monitoring tools that implement wait event analysis (AWS RDS Performance Insights, pgsentinel, pg_wait_sampling, and others) visualize samples where "wait_event IS NULL" as "CPU" time, typically shown in green. This convention originated from Oracle and has become widespread.

However, this assumption can make analysis inaccurate because there are many places in PostgreSQL code that are not covered by wait events but technically should be - and such places cannot accurately be labeled as "CPU". When a backend shows NULL wait_event, it might be:

- Actually doing CPU work (legitimate)
- Performing I/O that isn't instrumented
- Waiting on internal synchronization not covered by wait events
- Executing extension code without proper instrumentation

This project would:

- Systematically analyze PostgreSQL source code to identify non-instrumented waits
- Categorize gaps by type (I/O, synchronization, extension hooks, etc.)
- Propose and implement new wait events for significant gaps
- Ensure backward compatibility with existing monitoring tools
- Document the new wait events and their meanings

Initial analysis has identified potential gaps in areas like:

- Some file I/O operations
- Internal memory allocation paths
- Extension hook execution
- Background worker coordination
- Certain replication scenarios

### Skills needed

- C programming
- PostgreSQL
- Basic understanding of performance analysis

### Difficulty level

Moderate

### Project size

Large: approximately ~350 hours of work.

### Mentors

- Nik Samokhvalov <nik (at) postgres (dot) ai>
- Kirk Wolak <wolakk (at) gmail (dot) com>
- Andreas Karlsson <andreas (at) proxel (dot) se>

### Expected outcomes

- Comprehensive analysis of current wait event coverage gaps
- Implementation of new wait events for significant uninstrumented code paths
- Improved accuracy of "CPU" vs "waiting" distinction in monitoring tools
- Documentation of all new wait events
- Regression tests ensuring wait events fire correctly
- Backward compatibility with existing monitoring infrastructure
- Getting and applying feedback (especially on naming) from the Hackers group
