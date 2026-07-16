from __future__ import annotations

import os
import subprocess
from datetime import datetime
from pathlib import Path

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator


AIRFLOW_HOME = Path("/opt/airflow")


def run_spark_job(script_name: str) -> None:
    script_path = AIRFLOW_HOME / "jobs" / "pyspark" / script_name
    env = os.environ.copy()
    env["PYTHONPATH"] = f"{AIRFLOW_HOME}{os.pathsep}{env.get('PYTHONPATH', '')}"
    command = ["spark-submit", str(script_path)]
    subprocess.run(command, check=True, env=env)


with DAG(
    dag_id="ecommerce_analytics_pipeline",
    description="Bronze, silver, and gold ETL for e-commerce analytics",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["spark", "ecommerce", "analytics"],
) as dag:
    start = EmptyOperator(task_id="start")

    bronze = PythonOperator(
        task_id="bronze_ingestion",
        python_callable=run_spark_job,
        op_kwargs={"script_name": "bronze_ingestion.py"},
    )

    silver = PythonOperator(
        task_id="silver_transform",
        python_callable=run_spark_job,
        op_kwargs={"script_name": "silver_transform.py"},
    )

    gold = PythonOperator(
        task_id="gold_analytics",
        python_callable=run_spark_job,
        op_kwargs={"script_name": "gold_analytics.py"},
    )

    finish = EmptyOperator(task_id="finish")

    start >> bronze >> silver >> gold >> finish
