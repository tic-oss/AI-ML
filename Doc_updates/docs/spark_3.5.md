# Apache Spark 3.5.0 Release Notes

Highlights

    Scala and Go client support in Spark Connect SPARK-42554 SPARK-43351
    PyTorch-based distributed ML Support for Spark Connect SPARK-42471
    Structured Streaming support for Spark Connect in Python and Scala SPARK-42938
    Pandas API support for the Python Spark Connect Client SPARK-42497
    Introduce Arrow Python UDFs SPARK-40307
    Support Python user-defined table functions SPARK-43798
    Migrate PySpark errors onto error classes SPARK-42986
    PySpark Test Framework SPARK-44042
    Add support for Datasketches HllSketch SPARK-16484
    Built-in SQL Function Improvement SPARK-41231
    IDENTIFIER clause SPARK-43205
    Add SQL functions into Scala, Python and R API SPARK-43907
    Add named argument support for SQL functions SPARK-43922
    Avoid unnecessary task rerun on decommissioned executor lost if shuffle data migrated SPARK-41469
    Distributed ML <> spark connect SPARK-42471
    DeepSpeed Distributor SPARK-44264
    Implement changelog checkpointing for RocksDB state store SPARK-43421
    Introduce watermark propagation among operators SPARK-42376
    Introduce dropDuplicatesWithinWatermark SPARK-42931
    RocksDB state store provider memory management enhancements SPARK-43311

Spark Connect

    Refactoring of the sql module into sql and sql-api to produce a minimum set of dependencies that can be shared between the Scala Spark Connect client and Spark and avoids pulling all of the Spark transitive dependencies. SPARK-44273
    Introducing the Scala client for Spark Connect SPARK-42554
    Pandas API support for the Python Spark Connect Client SPARK-42497
    PyTorch-based distributed ML Support for Spark Connect SPARK-42471
    Structured Streaming support for Spark Connect in Python and Scala SPARK-42938
    Initial version of the Go client SPARK-43351
    Lot’s of compatibility improvements between Spark native and the Spark Connect clients across Python and Scala
    Improved debugability and request handling for client applications (asynchronous processing, retries, long-lived queries)

Spark SQL
Features

    Add metadata column file block start and length SPARK-42423
    Support positional parameters in Scala/Java sql() SPARK-44066
    Add named parameter support in parser for function calls SPARK-43922
    Support SELECT DEFAULT with ORDER BY, LIMIT, OFFSET for INSERT source relation SPARK-43071
    Add SQL grammar for PARTITION BY and ORDER BY clause after TABLE arguments for TVF calls SPARK-44503
    Include column default values in DESCRIBE and SHOW CREATE TABLE output SPARK-42123
    Add optional pattern for Catalog.listCatalogs SPARK-43792
    Add optional pattern for Catalog.listDatabases SPARK-43881
    Callback when ready for execution SPARK-44145
    Support Insert By Name statement SPARK-42750
    Add call_function for Scala API SPARK-44131
    Stable derived column aliases SPARK-40822
    Support general constant expressions as CREATE/REPLACE TABLE OPTIONS values SPARK-43529
    Support subqueries with correlation through INTERSECT/EXCEPT SPARK-36124
    IDENTIFIER clause SPARK-43205
    ANSI MODE: Conv should return an error if the internal conversion overflows SPARK-42427

Functions

    Add support for Datasketches HllSketch SPARK-16484
    Support the CBC mode by aes_encrypt()/aes_decrypt() SPARK-43038
    Support TABLE argument parser rule for TableValuedFunction SPARK-44200
    Implement bitmap functions SPARK-44154
    Add the try_aes_decrypt() function SPARK-42701
    array_insert should fail with 0 index SPARK-43011
    Add to_varchar alias for to_char SPARK-43815
    High-order function: array_compact implementation SPARK-41235
    Add analyzer support of named arguments for built-in functions SPARK-44059
    Add NULLs for INSERTs with user-specified lists of fewer columns than the target table SPARK-42521
    Adds support for aes_encrypt IVs and AAD SPARK-43290
    DECODE function returns wrong results when passed NULL SPARK-41668
    Support udf ‘luhn_check’ SPARK-42191
    Support implicit lateral column alias resolution on Aggregate SPARK-41631
    Support implicit lateral column alias in queries with Window SPARK-42217
    Add 3-args function aliases DATE_ADD and DATE_DIFF SPARK-43492

Data Sources

    Char/Varchar Support for JDBC Catalog SPARK-42904
    Support Get SQL Keywords Dynamically Thru JDBC API and TVF SPARK-43119
    DataSource V2: Handle MERGE commands for delta-based sources SPARK-43885
    DataSource V2: Handle MERGE commands for group-based sources SPARK-43963
    DataSource V2: Handle UPDATE commands for group-based sources SPARK-43975
    DataSource V2: Allow representing updates as deletes and inserts SPARK-43775
    Allow jdbc dialects to override the query used to create a table SPARK-41516
    SPJ: Support partially clustered distribution SPARK-42038
    DSv2 allows CTAS/RTAS to reserve schema nullability SPARK-43390
    Add spark.sql.files.maxPartitionNum SPARK-44021
    Handle UPDATE commands for delta-based sources SPARK-43324
    Allow V2 writes to indicate advisory shuffle partition size SPARK-42779
    Support lz4raw compression codec for Parquet SPARK-43273
    Avro: writing complex unions SPARK-25050
    Speed up Timestamp type inference with user-provided format in JSON/CSV data source SPARK-39280
    Avro to Support custom decimal type backed by Long SPARK-43901
    Avoid shuffle in Storage-Partitioned Join when partition keys mismatch, but join expressions are compatible SPARK-41413
    Change binary to unsupported dataType in CSV format SPARK-42237
    Allow Avro to convert union type to SQL with field name stable with type SPARK-43333
    Speed up Timestamp type inference with legacy format in JSON/CSV data source SPARK-39281

Query Optimization

    Subexpression elimination support shortcut expression SPARK-42815
    Improve join stats estimation if one side can keep uniqueness SPARK-39851
    Introduce the group limit of Window for rank-based filter to optimize top-k computation SPARK-37099
    Fix behavior of null IN (empty list) in optimization rules SPARK-44431
    Infer and push down window limit through window if partitionSpec is empty SPARK-41171
    Remove the outer join if they are all distinct aggregate functions SPARK-42583
    Collapse two adjacent windows with the same partition/order in subquery SPARK-42525
    Push down limit through Python UDFs SPARK-42115
    Optimize the order of filtering predicates SPARK-40045

Code Generation and Query Execution

    Runtime filter should supports multi level shuffle join side as filter creation side SPARK-41674
    Codegen Support for HiveSimpleUDF SPARK-42052
    Codegen Support for HiveGenericUDF SPARK-42051
    Codegen Support for build side outer shuffled hash join SPARK-44060
    Implement code generation for to_csv function (StructsToCsv) SPARK-42169
    Make AQE support InMemoryTableScanExec SPARK-42101
    Support left outer join build left or right outer join build right in shuffled hash join SPARK-36612
    Respect RequiresDistributionAndOrdering in CTAS/RTAS SPARK-43088
    Coalesce buckets in join applied on broadcast join stream side SPARK-43107
    Set nullable correctly on coalesced join key in full outer USING join SPARK-44251
    Fix IN subquery ListQuery nullability SPARK-43413

Other Notable Changes

    Set nullable correctly for keys in USING joins SPARK-43718
    Fix COUNT(*) is null bug in correlated scalar subquery SPARK-43156
    Dataframe.joinWith outer-join should return a null value for unmatched row SPARK-37829
    Automatically rename conflicting metadata columns SPARK-42683
    Document the Spark SQL error classes in user-facing documentation SPARK-42706

PySpark
Features

    Support positional parameters in Python sql() SPARK-44140
    Support parameterized SQL by sql() SPARK-41666
    Support Python user-defined table functions SPARK-43797
    Support to set Python executable for UDF and pandas function APIs in workers during runtime SPARK-43574
    Add DataFrame.offset to PySpark SPARK-43213
    Implement dir() in pyspark.sql.dataframe.DataFrame to include columns SPARK-43270
    Add option to use large variable width vectors for arrow UDF operations SPARK-39979
    Make mapInPandas / mapInArrow support barrier mode execution SPARK-42896
    Add JobTag APIs to PySpark SparkContext SPARK-44194
    Support for Python UDTF to analyze in Python SPARK-44380
    Expose TimestampNTZType in pyspark.sql.types SPARK-43759
    Support nested timestamp type SPARK-43545
    Support UserDefinedType in createDataFrame from pandas DataFrame and toPandas [SPARK-43817]SPARK-43702
    Add descriptor binary option to Pyspark Protobuf API SPARK-43799
    Accept generics tuple as typing hints of Pandas UDF SPARK-43886
    Add array_prepend function SPARK-41233
    Add assertDataFrameEqual util function SPARK-44061
    Support arrow-optimized Python UDTFs SPARK-43964
    Allow custom precision for fp approx equality SPARK-44217
    Make assertSchemaEqual API public SPARK-44216
    Support fill_value for ps.Series SPARK-42094
    Support struct type in createDataFrame from pandas DataFrame SPARK-43473

Other Notable Changes

    Add autocomplete support for df[ 	] in pyspark.sql.dataframe.DataFrame [SPARK-43892]
    Deprecate & remove the APIs that will be removed in pandas 2.0 [SPARK-42593]
    Make Python the first tab for code examples - Spark SQL, DataFrames and Datasets Guide SPARK-42493
    Updating remaining Spark documentation code examples to show Python by default SPARK-42642
    Use deduplicated field names when creating Arrow RecordBatch [SPARK-41971]
    Support duplicated field names in createDataFrame with pandas DataFrame [SPARK-43528]
    Allow columns parameter when creating DataFrame with Series [SPARK-42194]

Core

    Schedule mergeFinalize when push merge shuffleMapStage retry but no running tasks SPARK-40082
    Introduce PartitionEvaluator for SQL operator execution SPARK-43061
    Allow ShuffleDriverComponent to declare if shuffle data is reliably stored SPARK-42689
    Add max attempts limitation for stages to avoid potential infinite retry SPARK-42577
    Support log level configuration with static Spark conf SPARK-43782
    Optimize PercentileHeap SPARK-42528
    Add reason argument to TaskScheduler.cancelTasks SPARK-42602
    Avoid unnecessary task rerun on decommissioned executor lost if shuffle data migrated SPARK-41469
    Fixing accumulator undercount in the case of the retry task with rdd cache SPARK-41497
    Use RocksDB for spark.history.store.hybridStore.diskBackend by default SPARK-42277
    Support spark.kubernetes.setSubmitTimeInDriver SPARK-43014
    NonFateSharingCache wrapper for Guava Cache SPARK-43300
    Improve the performance of MapOutputTracker.updateMapOutput SPARK-43043
    Allowing apps to control whether their metadata gets saved in the db by the External Shuffle Service SPARK-43179
    Port executor failure tracker from Spark on YARN to K8s SPARK-41210
    Parameterize the max number of attempts for driver props fetcher in KubernetesExecutorBackend SPARK-42764
    Add SPARK_DRIVER_POD_IP env variable to executor pods SPARK-42769
    Mounts the hadoop config map on the executor pod SPARK-43504

Structured Streaming

    Add support for tracking pinned blocks memory usage for RocksDB state store SPARK-43120
    Add RocksDB state store provider memory management enhancements SPARK-43311
    Introduce dropDuplicatesWithinWatermark SPARK-42931
    Introduce a new callback onQueryIdle() to StreamingQueryListener SPARK-43183
    Add option to skip commit coordinator as part of StreamingWrite API for DSv2 sources/sinks SPARK-42968
    Introduce a new callback “onQueryIdle” to StreamingQueryListener SPARK-43183
    Implement Changelog based Checkpointing for RocksDB State Store Provider SPARK-43421
    Add support for WRITE_FLUSH_BYTES for RocksDB used in streaming stateful operators SPARK-42792
    Add support for setting max_write_buffer_number and write_buffer_size for RocksDB used in streaming SPARK-42819
    RocksDB StateStore lock acquisition should happen after getting input iterator from inputRDD SPARK-42566
    Introduce watermark propagation among operators SPARK-42376
    Cleanup orphan sst and log files in RocksDB checkpoint directory SPARK-42353
    Expand QueryTerminatedEvent to contain error class if it exists in exception SPARK-43482

ML

    Support Distributed Training of Functions Using Deepspeed SPARK-44264
    Base interfaces of sparkML for spark3.5: estimator/transformer/model/evaluator SPARK-43516
    Make MLv2 (ML on spark connect) supports pandas >= 2.0 SPARK-43783
    Update MLv2 Transformer interfaces SPARK-43516
    New pyspark ML logistic regression estimator implemented on top of distributor SPARK-43097
    Add Classifier.getNumClasses back SPARK-42526
    Write a Deepspeed Distributed Learning Class DeepspeedTorchDistributor SPARK-44264
    Basic saving / loading implementation for ML on spark connect SPARK-43981
    Improve logistic regression model saving SPARK-43097
    Implement pipeline estimator for ML on spark connect SPARK-43982
    Implement cross validator estimator SPARK-43983
    Implement classification evaluator SPARK-44250
    Make PyTorch Distributor compatible with Spark Connect SPARK-42993

UI

    Add a Spark UI page for Spark Connect SPARK-44394
    Support Heap Histogram column in Executors tab SPARK-44153
    Show error message on UI for each failed query SPARK-44367
    Display Add/Remove Time of Executors on Executors Tab SPARK-44309

Build and Others

    Remove Python 3.7 Support SPARK-43347
    Increate PyArrow minimum version to 4.0.0 SPARK-44183
    Support R 4.3.1 SPARK-43447 SPARK-44192
    Add JobTag APIs to SparkR SparkContext SPARK-44195
    Add math functions to SparkR SPARK-44349
    Upgrade Parquet to 1.13.1 SPARK-43519
    Upgrade kubernetes-client to 6.7.2 SPARK-42362 SPARK-42761 SPARK-42885 SPARK-43355 SPARK-43581 SPARK-43950 SPARK-43990
    Upgrade ASM to 9.5 SPARK-43537 SPARK-43588
    Upgrade rocksdbjni to 8.3.2 SPARK-41569 SPARK-42718 SPARK-43007 SPARK-43436 SPARK-44256
    Upgrade Netty to 4.1.93 SPARK-42218 SPARK-42417 SPARK-42487 SPARK-43609 SPARK-44128
    Upgrade zstd-jni to 1.5.5-5 SPARK-42409 SPARK-42625 SPARK-43080 SPARK-43294 SPARK-43737 SPARK-43994 SPARK-44465
    Upgrade dropwizard metrics 4.2.19 SPARK-42654 SPARK-43738 SPARK-44296
    Upgrade gcs-connector to 2.2.14 SPARK-42888 SPARK-43842
    Upgrade commons-crypto to 1.2.0 SPARK-42488
    Upgrade scala-parser-combinators from 2.1.1 to 2.2.0 SPARK-42489
    Upgrade protobuf-java to 3.23.4 SPARK-41711 SPARK-42490 SPARK-42798 SPARK-43899 SPARK-44382
    Upgrade commons-codec to 1.16.0 SPARK-44151
    Upgrade Apache Kafka to 3.4.1 SPARK-42396 SPARK-44181
    Upgrade RoaringBitmap to 0.9.45 SPARK-42385 SPARK-43495 SPARK-44221
    Update ORC to 1.9.0 SPARK-42820 SPARK-44053 SPARK-44231
    Upgrade to Avro 1.11.2 SPARK-44277
    Upgrade commons-compress to 1.23.0 SPARK-43102
    Upgrade joda-time from 2.12.2 to 2.12.5 SPARK-43008
    Upgrade snappy-java to 1.1.10.3 SPARK-42242 SPARK-43758 SPARK-44070 SPARK-44415 SPARK-44513
    Upgrade mysql-connector-java from 8.0.31 to 8.0.32 SPARK-42717
    Upgrade Apache Arrow to 12.0.1 SPARK-42161 SPARK-43446 SPARK-44094
    Upgrade commons-io to 2.12.0 SPARK-43739
    Upgrade Apache commons-io to 2.13.0 SPARK-43739 SPARK-44028
    Upgrade FasterXML jackson to 2.15.2 SPARK-42354 SPARK-43774 SPARK-43904
    Upgrade log4j2 to 2.20.0 SPARK-42536
    Upgrade slf4j to 2.0.7 SPARK-42871
    Upgrade numpy and pandas in the release Dockerfile SPARK-42524
    Upgrade Jersey to 2.40 SPARK-44316
    Upgrade H2 from 2.1.214 to 2.2.220 SPARK-44393
    Upgrade optionator to ^0.9.3 SPARK-44279
    Upgrade bcprov-jdk15on and bcpkix-jdk15on to 1.70 SPARK-44441
    Upgrade mlflow to 2.3.1 SPARK-43344
    Upgrade Tink to 1.9.0 SPARK-42780
    Upgrade silencer to 1.7.13 SPARK-41787 SPARK-44031
    Upgrade Ammonite to 2.5.9 SPARK-44041
    Upgrade Scala to 2.12.18 SPARK-43832
    Upgrade org.scalatestplus:selenium-4-4 to org.scalatestplus:selenium-4-7 SPARK-41587
    Upgrade minimatch to 3.1.2 SPARK-41634
    Upgrade sbt-assembly from 2.0.0 to 2.1.0 SPARK-41704
    Update maven-checkstyle-plugin from 3.1.2 to 3.2.0 SPARK-41714
    Upgrade dev.ludovic.netlib to 3.0.3 SPARK-41750
    Upgrade hive-storage-api to 2.8.1 SPARK-41798
    Upgrade Apache httpcore to 4.4.16 SPARK-41802
    Upgrade jetty to 9.4.52.v20230823 SPARK-45052
    Upgrade compress-lzf to 1.1.2 SPARK-42274

Removals, Behavior Changes and Deprecations
Upcoming Removal

The following features will be removed in the next Spark major release

    Support for Java 8 and Java 11, and the minimal supported Java version will be Java 17
    Support for Scala 2.12, and the minimal supported Scala version will be 2.13
