# Apache Spark 3.4.0 Release Notes

## Highlight

    Python client for Spark Connect (SPARK-39375)
    Implement support for DEFAULT values for columns in tables (SPARK-38334)
    Support TIMESTAMP WITHOUT TIMEZONE data type (SPARK-35662)
    Support “Lateral Column Alias References” (SPARK-27561)
    Harden SQLSTATE usage for error classes (SPARK-41994)
    Enable Bloom filter Joins by default (SPARK-38841)
    Better Spark UI scalability and Driver stability for large applications (SPARK-41053)
    Async Progress Tracking in Structured Streaming (SPARK-39591)
    Python Arbitrary Stateful Processing in Structured Streaming (SPARK-40434)
    Pandas API coverage improvements (SPARK-42882) and NumPy input support in PySpark (SPARK-39405)
    Provide a memory profiler for PySpark user-defined functions (SPARK-40281)
    Implement PyTorch Distributor (SPARK-41589)
    Publish SBOM artifacts (SPARK-41893)
    Support IPv6-only environment (SPARK-39457)
    Customized K8s Scheduler (Apache YuniKorn and Volcano) GA (SPARK-42802)

## Spark SQL

## Features

    Implement support for DEFAULT values for columns in tables (SPARK-38334)
    Add Dataset.as(StructType) (SPARK-39625)
    Support parameterized SQL (SPARK-41271, SPARK-42702)
    Add unpivot / melt (SPARK-38864, SPARK-39876)
    Support “lateral column alias references” (SPARK-27561)
    Support result offset clause (SPARK-28330, SPARK-39159)
    Support Timestamp without time zone data type (SPARK-35662)
    Support scalar subquery in time travel (SPARK-39306)
    Make Catalog API be compatible with 3-layer-namespace (SPARK-39235)
    Support timestamp in seconds for TimeTravel using Dataframe options (SPARK-39633)
    Add SparkSession.config(Map) (SPARK-40163)
    Support changing session catalog’s default database (SPARK-35242)
    Protobuf support for Spark - from_protobuf AND to_protobuf (SPARK-40654)
    Add WHEN NOT MATCHED BY SOURCE clause to MERGE INTO (SPARK-40921)
    Relax ordering constraint for CREATE TABLE column options (SPARK-40944)
    SQL Equivalent for Dataframe overwrite command (SPARK-40956)
    Support Generate with no required child output to host outer references (SPARK-41441)
    ORDER BY ALL (SPARK-41637)
    GROUP BY ALL (SPARK-41635)
    Add flatMapSortedGroups and cogroupSorted (SPARK-38591)
    Support subqueries with correlated non-equality predicates (SPARK-36114)
    Support subqueries with correlation through UNION/INTERSECT/EXCEPT (SPARK-36124)

## ANSI Compliance

    ANSI SQL mode: always return null on invalid access to map column (SPARK-40066)
    Support double quoted identifiers (SPARK-40585)
    ANSI SQL mode: Round/Bround should return an error on integer overflow (SPARK-42045)
    Support casting of integrals to ANSI intervals (SPARK-40008)
    Support cast of decimals to ANSI intervals (SPARK-40014)
    Return wider ANSI interval types from the percentile functions (SPARK-40151)
    Support cast of ANSI intervals to decimals (SPARK-39470)
    Support casting intervals to integrals in ANSI mode (SPARK-39451)
    Harden SQLSTATE usage for error classes (SPARK-41994)

## Functions

    Support table-valued generator functions in the FROM clause (SPARK-41594)
    Support ANSI Aggregate Function: REGR_SXY (SPARK-37681)
    Support ANSI Aggregate Function: REGR_R2 (SPARK-37641)
    Support ANSI Aggregate Function: REGR_SXX (SPARK-37672)
    Support ANSI Aggregate Function: REGR_SYY (SPARK-37702)
    Support ANSI Aggregate Function: REGR_SLOPE (SPARK-39230)
    Support ANSI Aggregate Function: REGR_INTERCEPT (SPARK-37623)
    Support ANSI aggregation function PERCENTILE_CONT as window function (SPARK-38219)
    Support ANSI Aggregation Function: PERCENTILE_DISC (SPARK-37691)
    Support SPLIT_PART function (SPARK-38063)
    Support TRY_AVG function (SPARK-38589)
    Support TRY_TO_BINARY function (SPARK-38590)
    Support the TO_NUMBER and TRY_TO_NUMBER SQL functions according to a new specification (SPARK-38796)
    Support ANSI general value specification and function - USER (SPARK-39138)
    Support TO_CHAR and TRY_TO_CHAR functions to format Decimal values as strings (SPARK-28516)
    Support ANY_VALUE aggregate function (SPARK-39213)
    Support EQUAL_NUL function (SPARK-39305)
    Support aggregate function MEDIAN (SPARK-39320)
    Support REGEXP_COUNT function (SPARK-39618)
    Support REGEXP_INSTR function (SPARK-39744)
    Support REGEXP_SUBSTR function (SPARK-39695)
    Support UNPIVOT function (SPARK-39876)
    Support TRY_TO_TIMESTAMP function (SPARK-39795)
    Support url encode/decode as built-in function and tidy up url-related functions (SPARK-39741)
    Support aggregate function MODE (SPARK-39808)
    Support GET function (SPARK-40109)
    Add function aliases: LEN, DATEPART, DATEADD, DATE_DIFF, CURDATE (SPARK-40352)
    Improve the TO_BINARY function (SPARK-40112)
    Support CURRENT_SCHEMA (SPARK-41323)
    Support data masking built-in function MASK (SPARK-40687)
    Support high-order function: ARRAY_COMPACT (SPARK-41235)
    Support ARRAY_APPEND function (SPARK-41232)
    Support ARRAY_INSERT function (SPARK-41234)
    Support LUHN_CHECK function (SPARK-42191)
    Support ARRAY_SORT(column, comparator) (SPARK-39925)

## Data Sources

    Support Column Stats in DS v2 (SPARK-41378)
    Storage Partitioned Join (SPJ) in DS v2 (SPARK-37375)
    Row-level operations in DS v2 (SPARK-35801)
    Add SupportsReportOrdering mix in interface for DS v2 Scan (SPARK-38647)
    Infer DATE type for CSV schema inference (SPARK-39469)
    Support driver metrics in DS v2 custom metric API (SPARK-39635)
    Distribution and ordering support DS v2 function in writing (SPARK-39607)
    StringEndsWith/Contains support push down to Parquet so that we can leverage dictionary filter (SPARK-39002)
    Support UDT in Spark Parquet vectorized reader (SPARK-39086)
    Extend METADATA column to support row indexes for Parquet files (SPARK-37980)
    Support reading parquet FIXED_LEN_BYTE_ARRAY type (SPARK-41096)
    Optimize the order of filtering predicates (SPARK-40045)
    Support CTE and temp table queries with MSSQL JDBC (SPARK-37259)
    Support ignoreCorruptFiles and ignoreMissingFiles in Data Source options (SPARK-38767)
    Pull out v1 write to WriteFiles (SPARK-41407)
    Add read-side char padding to cover external data files (SPARK-40697)

## Query Optimization

    Merge non-correlated scalar subqueries (SPARK-34079)
    Enable Bloom filter Joins by default (SPARK-38841)
    Remove unnecessary distinct in aggregate expression by distinctKeys (SPARK-38832)
    Support predicate pushdown and column pruning for de-duped CTEs (SPARK-37670)
    Remove outer join if aggregate functions are duplicate agnostic on streamed side (SPARK-38886)
    Remove left/right outer join if only left/right side columns are selected and the join keys on the other side are unique (SPARK-39172)
    Optimize global Sort to RepartitionByExpression (SPARK-39911)
    Optimize TransposeWindow rule (SPARK-38034)
    Enhance EliminateSorts to support removing sorts via LocalLimit (SPARK-40050)
    Push local limit to both sides if join condition is empty (SPARK-40040)
    Add PushProjectionThroughLimit for Optimizer (SPARK-40501)
    Support PIVOT/UNPIVOT with join children (SPARK-41195)
    Support column pruning with multiple nondeterministic Filters (SPARK-41017)
    Improve output partitioning and ordering with AQE cache (SPARK-41048)
    Improve multi like performance by creating a balanced expression tree predicate (SPARK-41167)
    Remove the Sort if it is the child of RepartitionByExpression (SPARK-36703)
    Use available column statistics from completed query stages (SPARK-39991)
    Reuse expressions in WindowSpecDefinition (SPARK-41805)
    Improve AliasAwareOutputPartitioning and AliasAwareQueryOutputOrdering to take all aliases into account (SPARK-40086, SPARK-42049)
    Push down limit through Python UDFs (SPARK-42115)

## Code Generation and Query Execution

    Make defaultJoin in BroadcastNestedLoopJoinExec running in parallel (SPARK-40487)
    Codegen Support for HiveGenericUDF (SPARK-42051)
    Introduce shuffle on SinglePartition (SPARK-41986)
    Makes DPP support the pruning side has Union (SPARK-39217)

## Other Notable Changes

    Support Auto Partition Statistics Collection (SPARK-38573)
    Format error messages in the Thrift Server (SPARK-40098)
    Add an extension API to do plan normalization for caching (SPARK-41183)
    Refactor Spark types by introducing physical types (SPARK-41226)
    OneOf field support and recursion checks (SPARK-41396)
    Centralize the column resolution logic (SPARK-41405)
    Improve the plan change validation (SPARK-42081)
    Introduce SparkPath for typesafety (SPARK-41970)
    Throw Exception for db_name.view_name when creating temp view by Dataset API (SPARK-41090)
    Change the default value of argument of Mask function from -1 to NULL (SPARK-42070)

## Spark Core

## Decommission

    Avoid unnecessary task rerun on decommissioned executor lost if shuffle data migrated (SPARK-41469)
    Ignore stage fetch failure caused by decommissioned executor (SPARK-40481)
    Enable spark.storage.decommission.(rdd 	shuffle)Blocks.enabled by default (SPARK-40198)
    Add support for YARN decommissioning when ESS is disabled (SPARK-30835)

## Scheduler

    Make stage scheduling support local-cluster mode (SPARK-41949)
    Support stage level task resource profile for standalone cluster when dynamic allocation disabled (SPARK-39853)
    Delay onDisconnected to enable Driver receives ExecutorExitCode (SPARK-39957)
    Improve the speculation through the stage task metrics (SPARK-32170)
    Add stage level resource scheduling support for standalone cluster (SPARK-39062)
    Improve LaunchTask process to avoid Stage failures caused by fail-to-send LaunchTask messages (SPARK-39955)

## Shuffle

    Add Push Based Shuffle client side read metrics (SPARK-36620)
    Shuffle server side metrics for Push-based shuffle (​​SPARK-33573)
    Ensure mergedShuffleCleaner have been shutdown before db close (SPARK-40186)
    Add RocksDB support for shuffle service state store (SPARK-38888)
    Encapsulate LevelDB used to store remote/external shuffle state as DB (SPARK-38909)
    Enable spark.dynamicAllocation.shuffleTracking.enabled by default (SPARK-3984)
    Enable Push-based shuffle service to store state in NM level DB for work preserving restart (SPARK-33236)
    Remove shuffle blocks using the shuffle service for released executors (SPARK-37618)

## Other Notable Changes

    Support IPv6-only environment (SPARK-39457)
    Enable spark.kryo.unsafe by default (SPARK-42137)
    Disallow arbitrary custom classpath with proxy user in cluster mode (SPARK-41958)
    Avoid BlockManager re-registration if the executor has been lost (SPARK-41360)
    Remove the limitation that single task result must fit in 2GB (SPARK-40622)
    Remove the support of deprecated spark.akka.* configs (SPARK-40401)
    Change default logging to stderr to consistent with the behavior of log4j (SPARK-40406)
    Exclude DirectTaskResult metadata when calculating result size (SPARK-40261)
    Allow customize initial partitions number in take() behavior (SPARK-40211)
    Use interruptible lock instead of synchronized in Executor.updateDependencies() (SPARK-40235)
    Task failure should always trigger task failure listeners (SPARK-40106)
    Add the ability to selectively disable watching or polling (SPARK-36462)
    Do not cache unserialized broadcast relations on the driver (SPARK-39983)
    Fix deadlock between TaskMemoryManager and UnsafeExternalSorter.SpillableIterator (SPARK-39283)
    Expose the number partitions in a stage to TaskContext (SPARK-38679)
    Make memory overhead factor configurable (SPARK-38194)
    Avoid using bash -c in ShellBasedGroupsMappingProvider (SPARK-38992)

## Structured Streaming

## Major Features

    Async Progress Tracking (SPARK-39591)
    Python Arbitrary Stateful Processing in Structured Streaming (SPARK-40434)
    Protobuf Support in Structured Streaming (SPARK-40653)
    Fix late record filtering to support chaining of stateful operators (SPARK-40925)

## Other Notable Changes

    Introducing a streaming checkpoint file manager based on Hadoop’s Abortable interface (SPARK-40039)
    Deprecate Trigger.Once and Promote Trigger.AvailableNow (SPARK-39805)
    Expose the information of catalog table to the logical plan in streaming query (SPARK-39564)
    Support collecting metrics from streaming sinks (SPARK-38564)
    Deprecate DStream API (SPARK-42075)
    Flip the default value of Kafka offset fetching config (SPARK-40844)
    Provide cloned spark session in DataFrame in user function for foreachBatch sink in PySpark (SPARK-41379)

## Spark Connect

## Python Client

    Implement DataFrame API (SPARK-41279)
    Implement Column API (SPARK-41282)
    Implement Functions API (SPARK-41283)
    Implement SparkSession API (SPARK-41281)
    Implement I/O API (SPARK-41284)
    Implement Catalog API (SPARK-41289)
    Support for User-defined Functions in Python (SPARK-41661)
    Support for Pandas/Arrow Function API (SPARK-42393)
    Support for Runtime SQL configuration (SPARK-42499)
    Build, package and infrastructure for Spark Connect (SPARK-41286)
    Type annotations for Spark Connect Python Client (SPARK-40451)

## Scala Client

    Implement basic Scala Client (SPARK-41534, SPARK-42133, SPARK-42043, SPARK-41822)
    Implement SparkSession API (SPARK-42639, SPARK-42581, SPARK-42564, SPARK-42544, SPARK-42631)
    Implement Dataframe API (SPARK-42440, SPARK-42559, SPARK-42558, SPARK-42556, SPARK-42468, SPARK-42529, SPARK-42561, SPARK-42894, SPARK-41874, SPARK-42691, SPARK-42692, SPARK-42481, SPARK-42541, SPARK-42542, SPARK-42520, SPARK-41823)
    Implement Column API (SPARK-42441, SPARK-42560)
    Implement Functions API (SPARK-42461, SPARK-42579, SPARK-42527, SPARK-42531, SPARK-42495, SPARK-42557)
    Implement I/O API (SPARK-42457, SPARK-42555, SPARK-42690, SPARK-42878, SPARK-42757, SPARK-42482, SPARK-42733, SPARK-42518)
    Implement Runtime SQL configuration (SPARK-42586)
    Basic User Defined Function support (SPARK-42283, SPARK-42653, SPARK-42543)
    Basic Typed API support (SPARK-42580, SPARK-42605)
    Test infrastructure for Spark Connect (SPARK-42172, SPARK-42377, SPARK-42599)
    Implement REPL Support (SPARK-42656, SPARK-42884)

## PySpark

## Pandas API on Spark

    Major improvement
        Python Arbitrary Stateful Processing in Structured Streaming (SPARK-40434)
        Implement pandas API missing parameters (SPARK-42883)
        Pandas 1.5 support (SPARK-40576)
    Major feature
        Implement Series.searchsorted (SPARK-40330)
        Implement Series.autocorr (SPARK-38774)
        Implement DataFrame.mode (SPARK-40138)
        Implement DataFrame.boxplot and DataFrame.plot.box (SPARK-38993)
        Implement DataFrame.corrwith (SPARK-38907)
        Implement DataFrame.resample and Series.resample (SPARK-39081)
        Implement DataFrame.interpolate and Series.interpolate (SPARK-38844)
        Implement DataFrame.ewm and Series.ewm (SPARK-38785)
        Implement GroupBy.prod (SPARK-40334)
        Implement GroupBy.nth (SPARK-40333)
        Implement GroupBy.quantile (SPARK-40332)
        Implement GroupBy.sem (SPARK-40305)
        Implement GroupBy.mad (SPARK-39284)
        Implement GroupBy.skew (SPARK-39246)
        Implement GroupBy.ewm (SPARK-39129)
        Support GroupBy positional indexing (SPARK-38947)

## Other Notable Changes

    Major improvements
        Provide a memory profiler for PySpark user-defined functions (SPARK-40281)
        Make Catalog API be compatible with 3-layer-namespace (SPARK-39235)
        NumPy input support in PySpark (SPARK-39405)
        PySpark error improvements (SPARK-41597)
    Major features
        Support parameterized SQL in PySpark (SPARK-41666)
        Implement ‘median’ function (SPARK-40003)
        Implement ‘mode’ function (SPARK-40007)
        Implement ‘unpivot/melt’ function (SPARK-39877)
        Support Varchar in PySpark (SPARK-39760)
        Support CharType in PySpark (SPARK-39809)

## MLLIB

    Implement PyTorch Distributor (SPARK-41589)
    Unify the data validation (SPARK-38584)
    Reduce the shuffle size of ALS (SPARK-40476, SPARK-40745)
    Dedup isotonic regression duplicate features (SPARK-41008)
    KMeans blockify input vectors (SPARK-30661)
    Add relevance score for nDCG evaluation (SPARK-39446)

## SparkR

    Add unpivot / melt (SPARK-41267)
    Add array_sort(column, comparator) (SPARK-40167)
    Support multiple “Column” drop in R (SPARK-40087)
    Arrow 9.0.0 support with SparkR (SPARK-40114)
    Make Catalog API be compatible with 3-layer-namespace (SPARK-39579, SPARK-39646, SPARK-39645, SPARK-39236, SPARK-39716, SPARK-39719)
    Support R 4.2.0 (SPARK-39372)

## Live UI and History Server Service

    Better Spark UI scalability and Driver stability for large applications(SPARK-41053)
    Use RocksDB for spark.history.store.hybridStore.diskBackend by default (SPARK-42277)
    Group nested executions under the root execution(SPARK-41752)
    Show metrics properties in the environment tab(SPARK-39110)
    Fix StagePage input size/records not show when records greater than zero(SPARK-34777)
    Improve event logging JsonProtocol performance by using Jackson instead of Json4s (SPARK-39489)
    Support spark.history.fs.update.batchSize (SPARK-39225)

## Build

    Update cloudpickle to v2.2.0 (SPARK-40991)
    Deprecate Python 3.7 Support (SPARK-39861)
    Support Python 3.11 (SPARK-41454)
    Update dev.ludovic.netlib to 3.0.2 (SPARK-40251)
    Update breeze to 2.0 (SPARK-39616)
    Update slf4j version to 2.0.6 (SPARK-41561)
    Update kubernetes-client version to 6.4.1 (SPARK-42362)
    Update rocksdbjni to 7.9.2 ( SPARK-42129)
    Update Apache Arrow to 11.0.0 (SPARK-42161)
    Upgrade Apache Kafka to 3.3.2 (SPARK-42109)
