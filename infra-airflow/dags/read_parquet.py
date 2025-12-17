from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ReadParquetManual") \
    .config("spark.sql.parquet.enableVectorizedReader", "false") \
    .getOrCreate()

df = spark.read.parquet("/opt/spark-data/raw/transactions__fake_us.parquet")

df.show(5, truncate=False)
df.printSchema()

spark.stop()
