from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': 'Jagan',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'Task-3',
    default_args=default_args,
    description='DAG for math operations',
    schedule_interval=None,
)

def add_values(a, b):
    result = a + b
    print(f"Addition Result: {result}")
    return result

def subtract_values(c, d):
    result = c - d
    print(f"Subtraction Result: {result}")
    return result

def multiply_values(e, f):
    result = e * f
    print(f"Multiplication Result: {result}")
    return result

# Values for the operations
a, b, c, d, e, f = 5, 3, 8, 4, 6, 2

# Task 1: Add two values (a + b)
task_add = PythonOperator(
    task_id='add_values',
    python_callable=add_values,
    op_args=[a, b],
    dag=dag,
)

# Task 2: Subtract two values (c - d)
task_subtract = PythonOperator(
    task_id='subtract_values',
    python_callable=subtract_values,
    op_args=[c, d],
    dag=dag,
)

# Task 3: Multiply two values (e * f)
task_multiply = PythonOperator(
    task_id='multiply_values',
    python_callable=multiply_values,
    op_args=[e, f],
    dag=dag,
)

# Set task dependencies for sequential execution
# task_add >> task_subtract >> task_multiply
# Set tasks to run in parallel
[task_add,task_subtract, task_multiply]