try:
    from datetime import timedelta
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    from datetime import datetime
    import pandas as pd

    print("All Dag modules are ok ......")
except Exception as e:
    print("Error  {} ".format(e))


def first_function_dag(**kwargs):
    print("This is the first function")
    kwargs['ti'].xcom_push(key='mkey', value="first_function_dag says hello")


# Second function to have a relation with first function
def second_function_dag(**kwargs):
    print("This is the second function")
    data = {"name" : "Dibyaranjan", "title": "Airflow Tutorial"}
    print("#" * 20)
    df = pd.DataFrame(data=data, index=[0])
    print(df.head())
    instance = kwargs.get('ti').xcom_pull(key='mkey')
    return f"Hello World ! My name is {instance}"

with DAG(
        dag_id='first_dag',
        schedule_interval="@daily",
        default_args={
            "owner": "airflow",
            "retries": 1,
            "retry_delay": timedelta(minutes=5),
            "start_date": datetime(2022, 12, 3)
        },
        catchup=False
) as f:
    first_function_execute = PythonOperator(
        task_id="first_function_execute",
        python_callable=first_function_dag,
        provide_context = True, # This flag enables to ex-chagne data between functions
        op_kwargs={"name": "Dibyaranjan"} # This is how pass an argument to the function "first_function_dag"
    )

    second_function_execute = PythonOperator(
        task_id="second_function_execute",
        provide_context=True,  # This flag enables to ex-chagne data between functions
        python_callable=second_function_dag
    )

first_function_execute >> second_function_execute