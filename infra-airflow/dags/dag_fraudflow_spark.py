from datetime import datetime
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

default_args = {
    'start_date': datetime(2025, 1, 1),
}

with DAG(
    dag_id="fraudflow_spark_pipeline",
    default_args=default_args,
    schedule=None,
    catchup=False,
    tags=["spark"],
) as dag:

    run_generate = SparkSubmitOperator(
        task_id="run_generate_transactions",
        application="/opt/airflow/dags/generate_transactions.py",
        conn_id="spark_default",
        verbose=True,
        conf={
            'spark.driver.memory': '1g',
            'spark.executor.memory': '1g'
        },
    )

    run_generate

