"""
This DAG provides an example of using the Qubole Operator
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.qubole_operator import QuboleOperator
from datetime import datetime, timedelta
from airflow.models import Variable


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 5, 6),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'qubole_example', default_args=default_args, schedule_interval=timedelta(hours=1), catchup=False)

# Running Example Qubole Query
t1 = QuboleOperator(
    task_id='hive_example',
    command_type='hivecmd',
    script_location="s3://sovrn-datascience/qubole_scripts/test_query.hql",
    macros='[{"dt": "{{ execution_date.strftime("%Y%m%d%H") }}"}]',
    cluster_label='default',
    fetch_logs=True, # If true, will fetch qubole command logs and concatenate them into corresponding airflow task logs
    tags='aiflow_example_run',  # To attach tags to qubole command, auto attach 3 tags - dag_id, task_id, run_id
    qubole_conn_id='qubole_default',  # Connection id to submit commands inside QDS, if not set "qubole_default" is used
    dag=dag)
