# START REPLICA UNTIL

**Parent:** MariaDB — Project Ideas
**Source:** https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/replication-statements/start-replica
**Scraped:** 2026-02-22T23:28:47.611435

---

# START REPLICA

## Syntax

```
START { SLAVE | REPLICA } ["connection_name"] [thread_type [, thread_type] ... ]
START { SLAVE | REPLICA } ["connection_name"] [SQL_THREAD] UNTIL
MASTER_LOG_FILE = 'log_name', MASTER_LOG_POS = log_pos
START { SLAVE | REPLICA } ["connection_name"] [SQL_THREAD] UNTIL
RELAY_LOG_FILE = 'log_name', RELAY_LOG_POS = log_pos
START { SLAVE | REPLICA } ["connection_name"] [SQL_THREAD] UNTIL
MASTER_GTID_POS = <GTID position>
START ALL { SLAVES | REPLICAS } [thread_type [, thread_type]]
thread_type: IO_THREAD | SQL_THREAD
```


## Description

#### START REPLICA UNTIL

#### connection_name

#### START ALL REPLICAS

## See Also

Last updated

Was this helpful?
