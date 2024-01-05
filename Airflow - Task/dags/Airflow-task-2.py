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
    'Task-2',
    default_args=default_args,
    description='DAG for Math Operations',
    schedule_interval=None,  # Set to None for manual triggering
)

# Values for the operations
a, b, c, d, e, f = 5, 3, 8, 4, 6, 2

# Task 1: Add two values (a + b)
def add_values():
    result = a + b
    print(f"Addition Result: {a} + {b} = {result}")

add_task = PythonOperator(
    task_id='add_task',
    python_callable=add_values,
    dag=dag,
)

# Task 2: Subtract two values (c - d)
def subtract_values():
    result = c - d
    print(f"Subtraction Result: {c} - {d} = {result}")

subtract_task = PythonOperator(
    task_id='subtract_task',
    python_callable=subtract_values,
    dag=dag,
)

# Task 3: Multiply two values (e * f)
def multiply_values():
    result = e * f
    print(f"Multiplication Result: {e} * {f} = {result}")

multiply_task = PythonOperator(
    task_id='multiply_task',
    python_callable=multiply_values,
    dag=dag,
)

# Set up task dependencies for sequential execution
add_task >> subtract_task >> multiply_task

# Alternatively, for parallel execution, you can remove the dependencies
# add_task and subtract_task can run in parallel with multiply_task
# add_task >> multiply_task
# subtract_task >> multiply_task


# Parallel Execution 
            # (add_task >> multiply_task and subtract_task >> multiply_task):
            # add_task and subtract_task are set to run in parallel with multiply_task. 
            # They can execute concurrently.


# Sequential Execution (add_task >> subtract_task >> multiply_task):
            # add_task is set to run first, followed by subtract_task, and finally multiply_task.
            # The >> operator ensures the sequential execution. 
            # Each task will run only if the previous task completes successfully.