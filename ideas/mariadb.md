# MariaDB — Project Ideas

**Source:** https://mariadb.com/docs/general-resources/community/contributing-participating/google-summers-of-code/google-summer-of-code-2026
**Scraped:** 2026-02-22T23:28:47.610725

---

# Google Summer of Code 2026

In 2026, we are again participating in the [Google Summer of Code](https://summerofcode.withgoogle.com/). We, joined with the [MariaDB Foundation](https://www.mariadb.org), believe we are making a better database that remains application-compatible with MySQL. We also work on making LGPL connectors (currently [C](/ideas/mariadb/docs-connectors-mariadb-connector-c), [C++](/ideas/mariadb/docs-connectors-mariadb-connector-cpp), [ODBC](/ideas/mariadb/docs-connectors-mariadb-connector-odbc), [Java](/ideas/mariadb/docs-connectors-mariadb-connector-j), [Node.js](/ideas/mariadb/docs-connectors-mariadb-connector-nodejs)) and on [MariaDB Galera Cluster](/ideas/mariadb/docs-galera-cluster), which allows you to scale your reads & writes. And we have [MariaDB ColumnStore](/ideas/mariadb/docs-analytics-mariadb-columnstore), which is a columnar storage engine, designed to process petabytes of data with real-time response to analytical queries.

## Where to Start

Please join us on [Zulip](https://mariadb.zulipchat.com/#narrow/channel/118760-New-Members/topic/GSoC.202026.3A.20welcome.20here!/) to mingle with the community. You should also subscribe to the [developers mailing list](https://lists.mariadb.org/postorius/lists/developers.lists.mariadb.org) (this is the main list where we discuss development - there are also [other mailing lists](/ideas/mariadb/docs-general-resources-community-joining-the-community)).

To improve your chances of being accepted, it is a good idea to submit a pull request with a bug fix to the server.

Also see the [List of beginner friendly issues](https://jira.mariadb.org/issues/?jql=status%20%3D%20Confirmed%20AND%20labels%20%3D%20beginner-friendly%20ORDER%20BY%20updated%20DESC) from the MariaDB Issue Tracker.

## List of Tasks (work in progress, check again tomorrow)

### MariaDB Server

[MDEV-28395](https://jira.mariadb.org/browse/MDEV-28395) LOAD DATA plugins

[MDEV-28395](https://jira.mariadb.org/browse/MDEV-28395)LOAD DATA plugins

**Full-time project 350h**

`LOAD DATA INFILE`

can flexibly load data into a table from CSV-like files accessible by the mariadbdb process. `LOAD XML INFILE`

can do it for XML files. `LOAD DATA LOCAL INFILE`

and `LOAD XML LOCAL INFILE`

can do it with files accessible by the client, but not by the server. But there are requests to support loading more file formats and from other locations, for example, from S3.

This project is to implement support for LOAD plugins and refactor the current LOAD code accordingly. There are two kind of plugins — data parser plugin (CSV-like and XML) and transfer plugin (file and LOCAL). Implementing new plugins is not in the scope of this task, this task is mainly about moving existing code around, creating a *possibility* for new plugins (like JSON or S3).

**Skills needed:** C++, bison
**Mentors:** Sergei Golubchik

[MDEV-7924](https://jira.mariadb.org/browse/MDEV-7924) START SLAVE UNTIL to Support Timestamps

[MDEV-7924](https://jira.mariadb.org/browse/MDEV-7924)START SLAVE UNTIL to Support Timestamps

**Part-time project 175h**

Users can control a point at which a replica will automatically stop applying events from the primary via [START REPLICA UNTIL](/ideas/mariadb/docs-server-reference-sql-statements-administrative-sql-statements-replication-s). Currently, this only allows [GTIDs](/ideas/mariadb/docs-server-ha-and-performance-standard-replication-gtid) and log-offsets (file-name, binlog offset), which usually requires users to manually examine the binary log on the master to find the exact transaction one wants to stop at. Often, users won't care about the specifics on the exact transaction to stop at, but rather the goal is to create a known/consistent state, e.g. across multiple different slaves (possibly of different masters). That is, it currently requires users to use [mariadb-binlog](/ideas/mariadb/docs-server-clients-and-utilities-logging-tools-mariadb-binlog-using-mariadb-bin) to manually analyze the binary log files in the master server's binlog directory, find the transaction identifier (GTID or log-offset) of some transaction at the timestamp they want to stop the slaves at, and input that into their `STOP SLAVE UNTIL`

statement. With multiple masters, this process would need to be repeated for each master.

This project is to implement support for timestamps in `START SLAVE UNTIL`

, to simplify the aforementioned process. To define inclusive/exclusive behaviors, it would be good to be consistent with the existing GTID-based keywords `SQL_BEFORE_GTIDS`

and `SQL_AFTER_GTIDS`

, i.e. to define `SQL_BEFORE_TIMESTAMP`

and `SQL_AFTER_TIMESTAMP`

, respectively.

**Skills needed:** C++, Lex/Yacc
**Mentors:** Brandon Nesterenko

[MDEV-38721](https://jira.mariadb.org/browse/MDEV-38721) one-pass HNSW search

[MDEV-38721](https://jira.mariadb.org/browse/MDEV-38721)one-pass HNSW search

**Full-time project 350h**

The idea here is to treat HNSW graph as a flat one-level non-hierarchical graph and search on all layers at once. Without actual flattening, so let's call it VF-HNSW, Virtually Flattened Hierarchical Navigable Small World.

This project is to implement this algorithm and benchmark it using ann-benchmarks.

**Skills needed:** C++, Python
**Mentors:** Sergei Golubchik

[MDEV-33411](https://jira.mariadb.org/browse/MDEV-33411) OPTIMIZE TABLE for graph indexes

[MDEV-33411](https://jira.mariadb.org/browse/MDEV-33411)OPTIMIZE TABLE for graph indexes

**Full-time project 350h**

Bulk insert into mHNSW index. There are various optimizations we can implement when all vectors are available in advance.

**Skills needed:** C++
**Mentors:** Sergei Golubchik

[MDEV-31342](https://jira.mariadb.org/browse/MDEV-31342) I_S optimization: avoid temp table

[MDEV-31342](https://jira.mariadb.org/browse/MDEV-31342)I_S optimization: avoid temp table

**Part-time project 175h** or can be combined with MDEV-31535 for a Full-time project 350h

Currently information_schema tables work like:

prepare information_schema table

this creates a temporary table


call the information_schema implementation code

it sets values using

`Field::store()`

and calls`schema_table_store_record()`

per row`schema_table_store_record()`

uses`handler::ha_write_row()`

to store the row in he temporary table

when the temporary table is filled with data, it's used in the query.


For queries like `SELECT f1, f2, ... FROM INFORMATION_SCHEMA.tbl`

the above adds a lot of overhead. The server can recognize that case, not create a temporary table in the step 1. And modify `schema_table_store_record()`

to send results directly to the client.

**Skills needed:** C++
**Mentors:** Oleksandr Byelkin

[MDEV-31535](https://jira.mariadb.org/browse/MDEV-31535) optimize directory listing for information_schema tables based on privileges

[MDEV-31535](https://jira.mariadb.org/browse/MDEV-31535)optimize directory listing for information_schema tables based on privileges

**Part-time project 175h** or can be combined with MDEV-31342 for a Full-time project 350h

Usually when `INFORMATION_SCHEMA.TABLES`

(or any other table that is implemented via `get_all_tables()`

function) is queried, it creates a list of all schemas first, then for every schema it creates a list of all files in that schema.

In certain cases the above is optimized:

when a specific table is requested via

`TABLE_SCHEMA=xxx AND TABLE_NAME=yyy`

in the`WHERE`

clase — in this case only that one table is openedwhen a specific schema is requested via

`TABLE_SCHEMA=xxx`

— tables for only that schema are listed, the list of all schemas is not createdwhen privileges only allow access to certain schemas — the list of all schemas is created, but tables are listed only for those schemas that pass the privilege check


Note that in the last case the server still creates a list of all schemas. This can be expensive, if there're thousands of them and the privileges only allow access to one specific schema. It makes sense to treat this case as if the schema name was explicitly specified on the `WHERE`

clause. Almost, because the user will also have access to the `INFORMATION_SCHEMA`

itself, but it's already treated specially anyway.

That is:

if the user does not have global grants that allow to see all schemas, then

for every schema-level (and table-level?) grant:

if the schema name is not a pattern (does not contain wildcards), directly append this schema name to the list, if the schema exists


append "INFORMATION_SCHEMA"


if the above isn't true — fallback to the directory listing.

**Skills needed:** C++
**Mentors:** Oleksandr Byelkin

[MDEV-38329](https://jira.mariadb.org/browse/MDEV-38329) Named parameters in invocation of stored routines

[MDEV-38329](https://jira.mariadb.org/browse/MDEV-38329)Named parameters in invocation of stored routines

**Full-time project 350h**

Add support for the syntax like

not explicitly mentioned parameters get their default values.

**Skills needed:** C++
**Mentors:** Alexander Barkov

[MDEV-12320](https://jira.mariadb.org/browse/MDEV-12320) configurable default authentication plugin for the server

[MDEV-12320](https://jira.mariadb.org/browse/MDEV-12320)configurable default authentication plugin for the server

**Full-time project 350h**

configurable default authentication plugin for the server.

"default" applies to the plugin name that the server uses for the first handshake packet, what plugin the server uses when no username is yet known.

**Skills needed:** C, C++
**Mentors:** Nikita Malyavin

[MDEV-13594](https://jira.mariadb.org/browse/MDEV-13594) Support for JSON operators column->path and column->>path

[MDEV-13594](https://jira.mariadb.org/browse/MDEV-13594)Support for JSON operators column->path and column->>path

**Part-time project 175h** or can be combined with MDEV-38591 for a Full-time project 350h

Implement this syntax sugar in MariaDB for MySQL compatibility

**Skills needed:** C++
**Mentors:** Rucha Deodhar

[MDEV-38591](https://jira.mariadb.org/browse/MDEV-38591) MEMBER OF json operator

[MDEV-38591](https://jira.mariadb.org/browse/MDEV-38591)MEMBER OF json operator

**Part-time project 175h** or can be combined with MDEV-13594 for a Full-time project 350h

Implement {{MEMBER OF}} operator for MySQL compatibility.

**Skills needed:** C++
**Mentors:** Rucha Deodhar

[MDEV-37591](https://jira.mariadb.org/browse/MDEV-37591) Binlog Table Map Event to be a Sequential Index

[MDEV-37591](https://jira.mariadb.org/browse/MDEV-37591)Binlog Table Map Event to be a Sequential Index

**Part-time project 175h**

The mapping defined by a binary log `Table_map_log_event`

can be revamped to improve slave efficiency. Currently, when a transaction is binlogged using `binlog_format=ROW`

, a `Table_map`

event is written in the binary log to declare a table that the transaction is updating, and includes information to identify this table on the slave. In particular, this information includes an identification number (`table_id`

) that is used by a `Rows log event`

in this transactions, which specifies that the given row event is targeting that given table. This `table_id`

is only applicable for the server which actually logged the event, and is meaningless to the slave for execution, outside of its use to identify the table to target. However, when the slave uses this `table_id`

to identify a table, it does so by searching/iterating through a list of all tables targeted by the transaction.

This search for a table can be optimized by changing the assignment strategy of the `table_id`

to effectively work as an index into the list of tables targeted by the transaction. That is, instead of using the actual `table_id`

of the given table on the master server, the value can be filled in using some 0-indexed counter. Then when the slave needs to find the table that a given row event is targeting, it would use this index to simply access the table directly (rather than iteratively search).

**Skills needed:** C++
**Mentors:** Brandon Nesterenko

## Suggest a Task

Do you have an idea of your own, not listed above? Do let us know in the comments below (Click 'Login' on the top of the page first)!

*This page is licensed: CC BY-SA / Gnu FDL*

Last updated

Was this helpful?
