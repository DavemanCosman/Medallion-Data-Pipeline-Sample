from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="setup_minio",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["setup", "minio"]
):

    create_structure = BashOperator(
        task_id="create_minio_structure",
        bash_command="python /opt/airflow/scripts/minio_setup.py"
    )
