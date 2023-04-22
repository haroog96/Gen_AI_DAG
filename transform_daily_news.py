from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 16),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def fetch_news():
    # Set up the NewsAPI request
    url = ('https://newsapi.org/v2/everything?q=Generative%20AI&'
           'sortBy=popularity&apiKey=YOUR_API_KEY')
    response = requests.get(url)

    # Get the number of articles about Generative AI
    if response.status_code == 200:
        data = response.json()
        article_count = data['totalResults']
        print(f'Number of articles about Generative AI: {article_count}')
    else:
        print('Error fetching data from NewsAPI')

dag = DAG(
    'fetch_generative_ai_news',
    default_args=default_args,
    description='Fetches the number of articles about Generative AI using NewsAPI',
    schedule_interval=timedelta(days=1)
)

fetch_news_task = PythonOperator(
    task_id='fetch_news',
    python_callable=fetch_news,
    dag=dag
)
