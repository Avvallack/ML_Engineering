from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['avvallack@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=30),
    'max_active_runs': 1
}
with DAG(
        'yfinance_daily_analisys',
        default_args=default_args,
        description='A simple yfinance DAG',
        schedule_interval=timedelta(hours=1),
        start_date=days_ago(0),
        tags=['ml_eng'],
) as dag:
    # t1, t2 and t3 are examples of tasks created by instantiating operators
    step1 = BashOperator(
        task_id='get_data',
        bash_command='python /opt/airflow/src/get_data.py --date {{macros.datetime.now().strftime("%Y-%m-%d-%H")}}',
    )

    step2 = BashOperator(
        task_id='calculate_mean',
        depends_on_past=False,
        bash_command='python /opt/airflow/src/calculate_mean.py  --date {{macros.datetime.now().strftime("%Y-%m-%d-%H")}}',

    )

    step31 = BashOperator(
        task_id='calculate_5sma',
        depends_on_past=False,
        bash_command='python /opt/airflow/src/calculate_5sma.py --date {{macros.datetime.now().strftime("%Y-%m-%d-%H")}}',

    )

    step32 = BashOperator(
        task_id='calculate_20sma',
        depends_on_past=False,
        bash_command='python /opt/airflow/src/calculate_20sma.py --date {{macros.datetime.now().strftime("%Y-%m-%d-%H")}}',
        retries=3,
    )

    step4 = BashOperator(
        task_id='plot_results',
        depends_on_past=False,
        bash_command='python /opt/airflow/src/plot_results.py --date {{macros.datetime.now().strftime("%Y-%m-%d-%H")}}',
        retries=3,
    )

    step1 >> step2 >> [step31, step32] >> step4
