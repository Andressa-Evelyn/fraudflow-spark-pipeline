import pandas as pd
df = pd.read_parquet("/home/andressa/fraudflow-spark-pipeline/dados/staging/transactions_fraud_staging/part-00000-6328524b-94a5-4508-9c1a-96a5c0338005-c000.snappy.parquet")
print(df.head())