# from airflow.sensors.external_task import ExternalTaskSensor
# from airflow import DAG
# from airflow.operators.postgres_operator import PostgresOperator
# from airflow.operators.sensors import ExternalTaskSensor
# from airflow.operators.trigger_dagrun import TriggerDagRunOperator
# from datetime import datetime, timedelta



# # External task to check if Purchase_details cache is stale
# check_cache_task = ExternalTaskSensor(
#     task_id='check_cache_task',
#     external_dag_id='Task5_Cache_Check',
#     external_task_id='check_cache',
#     mode='poke',  # This means the sensor will keep poking the external task until the condition is met
#     timeout=600,  # Set a timeout value
#     poke_interval=60,  # The interval between pokes
#     dag=DAG,
# )

# default_args = {
#     'owner': 'Jagan',
#     'start_date': datetime(2024, 1, 1),
#     'depends_on_past': False,
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }

# dag = DAG(
#     'Task6',
#     default_args=default_args,
#     description='every 4 minutes',
#     schedule_interval='*/4 * * * *',  # Run every 4 minutes
# )



# # SQL query to calculate total_orders and total_returns for each customer
# calculate_purchase_details_sql = """
# INSERT INTO Purchase_details (customer_id, total_orders, total_returns, created_time)
# SELECT
#     o.customer_id,
#     COUNT(DISTINCT o.order_id) AS total_orders,
#     COUNT(DISTINCT pr.return_id) AS total_returns,
#     NOW() AS created_time
# FROM
#     Orders o
# LEFT JOIN
#     Product_returns pr ON o.customer_id = pr.customer_id
# GROUP BY
#     o.customer_id;
# """

# # Operator to execute the SQL query and insert rows into the Purchase_details table
# calculate_purchase_details_task = PostgresOperator(
#     task_id='calculate_purchase_details_task',
#     postgres_conn_id='postgres_localhost',
#     sql=calculate_purchase_details_sql,
#     dag=dag,
# )

# # Trigger the DAG to run only if the cache is stale
# trigger_purchase_details_dag = TriggerDagRunOperator(
#     task_id='trigger_purchase_details_dag',
#     trigger_dag_id='Task6',
#     dag=dag,
# )

# # Define the task sequence
# check_cache_task >> calculate_purchase_details_task >> trigger_purchase_details_dag
