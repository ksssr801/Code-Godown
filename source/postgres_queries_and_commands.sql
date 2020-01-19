-- tbl backup
pg_dump --column-inserts --data-only --table=tblimsconfig master_db > c:\my_dump.sql
PostgreSQL\9.6\bin>pg_dump --column-inserts --data-only --table=tblimsconfig -Upostgres -W everest_db > my_dump.sql
pg_dump --format plain --schema-only --verbose	--file "/tmp/everest_db.sql" "everest_db"

# restor ref
https://dba.stackexchange.com/a/76902
http://blog.endpoint.com/2010/04/restoring-individual-table-data-from.html

select * from pg_stat_activity 

-- select * from pg_stat_activity where state ='active' and query != '' and query != 'COMMIT'order by backend_start desc limit 5;

datid |  datname   |  pid  | usesysid | usename | application_name | client_addr  | client_hostname | client_port |       backend_start           |            xact_start            |           query_start            |           state_change           | wait_event_type | wait_event | state  | backend_xid | backend_xmin |                                                                       query          

--select pid, client_addr, backend_start, query_start, query from pg_stat_activity where state ='active' and query != '' and query != 'COMMIT' and client_addr = '202.92.239.3' order by backend_start desc limit 5
--
-- check active queries
select pid, client_addr, backend_start, query_start, query from pg_stat_activity where state ='active' and query != '' and query != 'COMMIT'  order by backend_start desc limit 50

SELECT pg_cancel_backend(__pid__);

-- check for locks:
SELECT l.*,a.*
  FROM pg_locks l
  JOIN pg_stat_activity a USING (pid)
 WHERE NOT granted;

SELECT a.pid, a.client_addr, a.backend_start, a.query_start, l.locktype, l.database,
  a.query 
  FROM pg_locks l
  JOIN pg_stat_activity a USING (pid)
 WHERE NOT granted;

--You'll see a list of waiting sessions. 

-- list of blocking sessions
SELECT l.*,a.*
  FROM pg_locks l
  JOIN pg_stat_activity a USING (pid)
 WHERE granted
   AND (database,relation) IN (SELECT database,relation
                                 FROM pg_locks WHERE NOT granted);


--Find blocking sessions:
    SELECT 
        pl.pid as blocked_pid
        ,psa.usename as blocked_user
        ,pl2.pid as blocking_pid
        ,psa2.usename as blocking_user
        ,psa.query as blocked_statement
    FROM pg_catalog.pg_locks pl
    JOIN pg_catalog.pg_stat_activity psa
        ON pl.pid = psa.pid
    JOIN pg_catalog.pg_locks pl2
    JOIN pg_catalog.pg_stat_activity psa2
        ON pl2.pid = psa2.pid
        ON pl.transactionid = pl2.transactionid 
            AND pl.pid != pl2.pid
    WHERE NOT pl.granted;

-- search tables like
SELECT table_catalog, table_name FROM information_schema.tables WHERE table_name ilike 'tblhour%%'

-- standards

-- show running queries (9.2)
SELECT pid, age(query_start, clock_timestamp()), usename, query 
FROM pg_stat_activity 
WHERE query != '<IDLE>' AND query NOT ILIKE '%pg_stat_activity%' 
ORDER BY query_start desc;

-- show running queries (pre 9.2)
SELECT procpid, age(query_start, clock_timestamp()), usename, current_query 
FROM pg_stat_activity 
WHERE current_query != '<IDLE>' AND current_query NOT ILIKE '%pg_stat_activity%' 
ORDER BY query_start desc;


-- kill running query
SELECT pg_cancel_backend(procpid);

-- kill idle query
SELECT pg_terminate_backend(procpid);

-- vacuum command
VACUUM (VERBOSE, ANALYZE);

-- all database users

-- pgstats  - query activity
select * from pg_stat_activity 


-- DB Size
select datname, pg_size_pretty(pg_database_size(datname))
from pg_database
order by pg_database_size(datname) desc;

-- Table size
SELECT
   table_catalog as DB, relname as "Table", pg_size_pretty(pg_total_relation_size(relid)) As "Total Size", 
   pg_size_pretty(pg_relation_size(table_name)) as "Table Size",
   pg_size_pretty(pg_total_relation_size(relid) - pg_relation_size(relid)) as "Index Size"
   FROM pg_catalog.pg_statio_user_tables inner join information_schema.tables on relname = table_name  
   --and relname = 'tblhour2017215_p4'
   ORDER BY pg_total_relation_size(relid) DESC;

-- Index Size of each table
SELECT idx.relname as table,
       idx.indexrelname as index, pg_index.indisunique "Unique", pg_index.indisprimary "Primary",
       pg_size_pretty(pg_relation_size(idx.indexrelname::text)),
       cls.relpages as pages, cls.reltuples as tuples, idx.idx_scan as scanned,
       idx.idx_tup_read as read, idx.idx_tup_fetch as fetched 
       FROM pg_stat_user_indexes idx, pg_class cls, pg_index
 WHERE cls.relname = idx.relname
   AND idx.indexrelid = pg_index.indexrelid
   and idx.relname = 'tblhour2017300_p5'
ORDER BY idx.relname, idx.indexrelname;

-- row size

select a.*,  octet_length(a.*::text) octectlength,  pg_column_size(a.*) from tblaudit2019101 a order by timestamp desc


-- Drop Index
DROP INDEX tblhour2017273_p5.tblhour2017273_p5_poller_id


-- cache hit rates (should not be less than 0.99)
SELECT sum(heap_blks_read) as heap_read, sum(heap_blks_hit)  as heap_hit, (sum(heap_blks_hit) - sum(heap_blks_read)) / sum(heap_blks_hit) as ratio
FROM pg_statio_user_tables;

-- table index usage rates (should not be less than 0.99)
SELECT relname, 100 * idx_scan / (seq_scan + idx_scan) percent_of_times_index_used, n_live_tup rows_in_table
FROM pg_stat_user_tables 
ORDER BY n_live_tup DESC;

-- how many indexes are in cache
SELECT sum(idx_blks_read) as idx_read, sum(idx_blks_hit)  as idx_hit, (sum(idx_blks_hit) - sum(idx_blks_read)) / sum(idx_blks_hit) as ratio
FROM pg_statio_user_indexes;

-- Dump database on remote host to file
$ pg_dump -U username -h hostname databasename > dump.sql

-- Import dump into existing database
$ psql -d newdb -f dump.sql
