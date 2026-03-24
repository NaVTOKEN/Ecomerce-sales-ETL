from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'etl')))

from main import run_etl

default_args = {
    'owner': 'naveen',
    'start_date': datetime(2025, 1, 1),
    'retries': 1
}

with DAG(
    'ecommerce_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    etl_task = PythonOperator(
        task_id='run_etl',
        python_callable=run_etl
    )

    etl_task
