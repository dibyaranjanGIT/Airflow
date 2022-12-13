# Airflow
Airflow demo

![download](https://user-images.githubusercontent.com/45364252/205421705-b391207b-91f4-4a91-9910-e0231d8cdafa.png)


├───dags
│   │
│   ├───project_1
│   │     dag_1.py
│   │     dag_2.py
│   │
│   └───project_2
│         dag_1.py
│         dag_2.py
│
├───plugins
│   ├───hooks
│   │      pysftp_hook.py
|   |      servicenow_hook.py
│   │   
│   ├───sensors
│   │      ftp_sensor.py
|   |      sql_sensor.py
|   |
│   ├───operators
│   │      servicenow_to_azure_blob_operator.py
│   │      postgres_templated_operator.py
│   |
│   ├───scripts
│       ├───project_1
|       |      transform_cases.py
|       |      common.py
│       ├───project_2
|       |      transform_surveys.py
|       |      common.py
│       ├───common
|             helper.py
|             dataset_writer.py
| .airflowignore
| Dockerfile
| docker-stack-airflow.yml
