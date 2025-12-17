import pandas as pd
df = pd.read_parquet('/home/andressa/fraudflow-spark-pipeline/dados/raw/transactions__fake_us.parquet', engine='pyarrow')
print(df.head())

