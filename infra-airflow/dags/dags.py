from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

with DAG(
    dag_id="fraudflow_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    spark_raw = SparkSubmitOperator(
        task_id="spark_raw_processing",
        application="/opt/airflow/dags/detect_fraud_raw.py",
        conn_id="spark_default",
        deploy_mode="client",
    )

    spark_staging = SparkSubmitOperator(
        task_id="spark_staging_processing",
        application="/opt/airflow/dags/detect_fraud_staging.py",
        conn_id="spark_default",
        deploy_mode="client",
    )

    spark_raw >> spark_staging
