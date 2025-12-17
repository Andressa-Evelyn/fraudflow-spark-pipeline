from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, hour, lit, avg

spark = (
    SparkSession.builder
    .appName("FraudDetectionStaging")
    .config("spark.sql.parquet.enableVectorizedReader", "false")
    .getOrCreate()
)

INPUT_PATH = "file:///opt/spark-data/raw/transactions__fake_us.parquet"
OUTPUT_PATH = "file:///opt/spark-data/staging/transactions_fraud_staging"

df = spark.read.parquet(INPUT_PATH)

avg_amount = df.select(avg("amount")).collect()[0][0]

df = df.withColumn(
    "score_high_amount",
    when(col("amount") > avg_amount * 3, 0.4).otherwise(0.0)
).withColumn(
    "score_high_risk_country",
    when(col("is_high_risk_country") == True, 0.3).otherwise(0.0)
).withColumn(
    "score_international",
    when(col("is_international") == True, 0.2).otherwise(0.0)
).withColumn(
    "score_suspicious_hour",
    when(hour(col("timestamp")).isin([2, 3, 4]), 0.1).otherwise(0.0)
).withColumn(
    "fraud_score",
    col("score_high_amount") +
    col("score_high_risk_country") +
    col("score_international") +
    col("score_suspicious_hour")
).withColumn(
    "fraud_detected",
    when(col("fraud_score") >= 0.6, True).otherwise(False)
).withColumn(
    "fraud_reason",
    when(col("score_high_amount") > 0, lit("HIGH_AMOUNT"))
    .when(col("score_high_risk_country") > 0, lit("HIGH_RISK_COUNTRY"))
    .when(col("score_suspicious_hour") > 0, lit("SUSPICIOUS_HOUR"))
    .otherwise(lit("NORMAL"))
)

# ✅ UMA ÚNICA ESCRITA
df.write.mode("overwrite").parquet(OUTPUT_PATH)

spark.stop()
