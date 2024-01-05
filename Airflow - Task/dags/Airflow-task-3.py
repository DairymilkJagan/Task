from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Jagan',
    'start_date': datetime(2024, 1, 4),
    'retries': 1,
}

dag = DAG(
    'Task4',
    default_args=default_args,
    schedule_interval='*/2 * * * *',  # Run every 2 minutes
)

# Query to insert into Orders table with ON CONFLICT to handle duplicates
query_orders = """
    INSERT INTO Orders (customer_id, order_date)
    VALUES
        (1, NOW()),
        ( 2, NOW())
"""

# Query to insert into Product_returns table with ON CONFLICT to handle duplicates
query_product_returns = """
    INSERT INTO Product_returns ( customer_id, return_date)
    VALUES
        (1, NOW()),
        (2, NOW())
"""

# Task to insert into Orders table
insert_orders_task = PostgresOperator(
    task_id="insert_into_orders",
    postgres_conn_id="postgres_localhost",
    sql=query_orders,
    dag=dag,
)

# Task to insert into Product_returns table
insert_product_returns_task = PostgresOperator(
    task_id="insert_into_product_returns",
    postgres_conn_id="postgres_localhost",
    sql=query_product_returns,
    dag=dag,
)

insert_orders_task >> insert_product_returns_task
