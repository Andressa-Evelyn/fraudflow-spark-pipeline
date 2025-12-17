from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

with DAG(
    dag_id="fraudflow_staging",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    detect_fraud_staging = SparkSubmitOperator(
        task_id="detect_fraud_staging",
        application="/opt/airflow/dags/detect_fraud_staging.py",
        conn_id="spark_default",
        deploy_mode="client",
        verbose=True,
        conf={
            "spark.sql.parquet.enableVectorizedReader": "false",
            "spark.driver.host": "airflow-worker",
            "spark.driver.bindAddress": "0.0.0.0",
            "spark.sql.sources.commitProtocolClass":
            "org.apache.spark.sql.execution.datasources.SQLHadoopMapReduceCommitProtocol"
        }
    )
