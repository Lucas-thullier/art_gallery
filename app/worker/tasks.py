import os
import logging
import requests
import json
import celery

from api.models import Movement, Location, Creator, Depiction, Genre, Material, Painting

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
    while offset <= 10000:
        # while offset <= int(cache['painting_count']):
        app.send_task('get_painting_interval', args=[limit, offset])
    # get_painting_interval(limit, offset)
        offset += limit


@app.task(bind=True, name='get_painting_interval', rate_limit='0.5/s')
def get_painting_interval(self, limit, offset):
    paintings_with_full_data = get_paintings_with_full_data(limit, offset)

    # columns = paintings_with_full_data['columns']
    paintings = paintings_with_full_data['paintings']

    painting_mapping = {
        'painting': 'wikidata_url',
        'paintingLabel': 'name',
        'pic': 'picture_url',
        'inception': 'inception_at',
        'owned_by': 'owned_by',
        'native_label': 'native_name',
        'title': 'title',
        'width': 'width',
        'height': 'height',
        'described_at': 'described_at',
    }

    relation_mappings = {
        'Movement': {
            'movement': 'wikidata_url',
            'movementLabel': 'name'
        },
        'Location': {
            'location': 'wikidata_url',
            'locationLabel': 'name'
        },
        'Genre': {
            'genre': 'wikidata_url',
            'genreLabel': 'name'
        },
        'Creator': {
            'creator': 'wikidata_url',
            'creatorLabel': 'name'
        },
        'Material': {
            'made_from_material': 'wikidata_url',
            'made_from_materialLabel': 'name'
        },
        'Depiction': {
            'depicts': 'wikidata_url',
            'depictsLabel': 'name'
        }
    }

    for painting in paintings:
        relations_attributes = {
            'Movement': {},
            'Location': {},
            'Genre': {},
            'Creator': {},
            'Material': {},
            'Depiction': {}
        }

        painting_attributes = {}
        for relation, mapping in relation_mappings.items():
            for sparql_name, art_gallery_name in mapping.items():
                if sparql_name in painting:
                    relations_attributes[relation][art_gallery_name] = painting[sparql_name]['value']

        for sparql_name, art_gallery_name in painting_mapping.items():
            if sparql_name in painting:
                painting_attributes[art_gallery_name] = painting[sparql_name]['value']

        painting_relations = {
            'movements': None,
            'locations': None,
            'locations': None,
            'creators': None,
            'genres': None,
            'materials': None,
            'depicts': None
        }
        for relation, properties in relations_attributes.items():
            if 'wikidata_url' in properties and properties['wikidata_url'] is not None:
                if relation == 'Movement':
                    dynamic_class = Movement
                elif relation == 'Location':
                    dynamic_class = Location
                elif relation == 'Creator':
                    dynamic_class = Creator
                elif relation == 'Depiction':
                    dynamic_class = Depiction
                elif relation == 'Genre':
                    dynamic_class = Genre
                elif relation == 'Material':
                    dynamic_class = Material

                collection = dynamic_class.objects.filter(
                    wikidata_url=properties['wikidata_url'])
                if len(collection) > 0:
                    relation_model = collection[0]
                else:
                    relation_model = dynamic_class(**properties)
                    relation_model.save()

                if relation == 'Movement':
                    painting_relations['movements'] = relation_model
                elif relation == 'Location':
                    painting_relations['locations'] = relation_model
                elif relation == 'Creator':
                    painting_relations['creators'] = relation_model
                elif relation == 'Depiction':
                    painting_relations['depicts'] = relation_model
                elif relation == 'Genre':
                    painting_relations['genres'] = relation_model
                elif relation == 'Material':
                    painting_relations['materials'] = relation_model

        if 'wikidata_url' in painting_attributes and painting_attributes['wikidata_url'] is not None:
            collection = Painting.objects.filter(
                wikidata_url=painting_attributes['wikidata_url'])
            if len(collection) > 0:
                painting_model = collection[0]
                if painting_relations['movements'] is not None:
                    painting_model.movements.add(
                        painting_relations['movements'])
                if painting_relations['locations'] is not None:
                    painting_model.locations.add(
                        painting_relations['locations'])
                if painting_relations['creators'] is not None:
                    painting_model.creators.add(painting_relations['creators'])
                if painting_relations['depicts'] is not None:
                    painting_model.depicts.add(painting_relations['depicts'])
                if painting_relations['genres'] is not None:
                    painting_model.genres.add(painting_relations['genres'])
                if painting_relations['materials'] is not None:
                    painting_model.materials.add(
                        painting_relations['materials'])

                painting_model.save()
            else:
                painting_model = Painting(**painting_attributes)
                painting_model.save()

                if painting_relations['movements'] is not None:
                    painting_model.movements.add(
                        painting_relations['movements'])
                if painting_relations['locations'] is not None:
                    painting_model.locations.add(
                        painting_relations['locations'])
                if painting_relations['creators'] is not None:
                    painting_model.creators.add(painting_relations['creators'])
                if painting_relations['depicts'] is not None:
                    painting_model.depicts.add(painting_relations['depicts'])
                if painting_relations['genres'] is not None:
                    painting_model.genres.add(painting_relations['genres'])
                if painting_relations['materials'] is not None:
                    painting_model.materials.add(
                        painting_relations['materials'])

                painting_model.save()
