import os
import logging
import requests

from .worker import app


logger = logging.getLogger(__name__)


@app.task(bind=True, name='fetch_data_from_quandl')
def fetch_data_from_quandl(self, database_code, dataset_code):
    url = f'https://www.quandl.com/api/v3/datasets/{database_code}/{dataset_code}/data.json'
    response = requests.get(url)
    logger.info(f'GET {url} returned status_code {response.status_code}')
    