from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests
import boto3
import json

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023,5,18),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def put_data_in_s3(num_results,current_date):
        try:
                s3 = boto3.client('s3')
                bucket_name = 'dag-run-edf'
                file_key = f'dag_runs/file_{current_date}.json'
                x = {"date":current_date,"totalresults":num_results}
                s3.put_object(Body=json.dumps(x), Bucket = bucket_name, Key=file_key)
        except Exception as e:
                raise Exception(f'Failed to put data in S3: {e}')
