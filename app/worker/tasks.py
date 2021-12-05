import os
import logging
import requests
import json
import celery

from .worker import app
from .sparql_wrapper import get_paintings_with_full_data, get_painting_count


logger = logging.getLogger(__name__)



@app.task(bind=True, name='populate_database')
def populate_database(self):
    painting_count = get_painting_count()

    cache_path = os.getcwd()+'/worker/tmp/cache.json'
    with open(cache_path, 'r') as file:
        cache = json.load(file)
    
    cache['painting_count'] = painting_count

    with open(cache_path, 'w') as file:
        json.dump(cache, file)
    
    offset = 0
    limit = 20
    # while offset <= 19:
    # while offset <= int(cache['painting_count']):
    app.send_task('get_painting_interval', args=[limit, offset])
        # get_painting_interval(limit, offset)
    offset += limit

@app.task(bind=True, name='get_painting_interval', rate_limit='0.5/s')
def get_painting_interval(self, limit, offset):
    paintings_with_full_data = get_paintings_with_full_data(limit, offset)
    
    columns = paintings_with_full_data['columns']
    paintings = paintings_with_full_data['paintings']
    return paintings
    
    

    

        
    

    
    
    