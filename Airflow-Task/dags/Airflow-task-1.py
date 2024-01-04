from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable

default_args = {
    'owner': 'Jagan',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'Task-1',
    default_args=default_args,
    description='Airflow Task DAG',
    schedule_interval=timedelta(days=1),
    # schedule_interval=None,
)

def create_airflow_variable(input_list):
    for word in input_list:
        Variable.set(word, word)

create_variable_task = PythonOperator(
    task_id='create_variable_task',
    python_callable=create_airflow_variable,
    op_args=[["DAG", "variable", "preset"]],
    dag=dag,
)

def print_word_lengths(input_list):
    word_lengths = {}
    for word in input_list:
        variable_value = Variable.get(word, default_var=None)
        if variable_value:
            word_lengths[word] = len(variable_value)

    print(word_lengths)

print_lengths_task = PythonOperator(
    task_id='print_lengths_task',
    python_callable=print_word_lengths,
    op_args=[["DAG", "variable", "preset"]],
    dag=dag,
)

create_variable_task >> print_lengths_task
