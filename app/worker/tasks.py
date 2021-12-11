import logging
from api.models import Movement, Location, Creator, Depiction, Genre, Material, Painting
from django.db import models
from .worker import app
from .sparql_wrapper import get_paintings_with_full_data, get_painting_count
logger = logging.getLogger(__name__)


@app.task(bind=True, name='populate_database')
def populate_database(self):
    return 'hahaha'
    # painting_count = get_painting_count()

    # cache_path = os.getcwd()+'/worker/tmp/cache.json'
    # with open(cache_path, 'r') as file:
    #     cache = json.load(file)

    # cache['painting_count'] = painting_count

    # with open(cache_path, 'w') as file:
    #     json.dump(cache, file)

    # offset = 0
    # limit = 20
    # while offset <= 10000:
    #     # while offset <= int(cache['painting_count']):
    #     app.send_task('get_painting_interval', args=[limit, offset])
    # # get_painting_interval(limit, offset)
    #     offset += limit


@app.task(bind=True, name='get_painting_interval', rate_limit='0.5/s')
def get_painting_interval(self, limit, offset):
    paintings_with_full_data = get_paintings_with_full_data(limit, offset)
    paintings: list = paintings_with_full_data['paintings']

    mappings = get_mappings()

    for painting in paintings:
        models_to_fill = extract_data_from_mapping(painting, mappings)

        handle_creation(models_to_fill, mappings)


def get_mappings() -> dict:
    return {
        'Painting': {
            'model': Painting,
            'mappings':
            {
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
        },
        'Movement': {
            'model': Movement,
            'relation_name': 'movements',
            'mappings':
            {
                'movement': 'wikidata_url',
                'movementLabel': 'name'
            }
        },
        'Location': {
            'model': Location,
            'relation_name': 'locations',
            'mappings': {
                'location': 'wikidata_url',
                'locationLabel': 'name'
            }
        },
        'Genre': {
            'model': Genre,
            'relation_name': 'genres',
            'mappings': {
                'genre': 'wikidata_url',
                'genreLabel': 'name'
            }
        },
        'Creator':
        {
            'model': Creator,
            'relation_name': 'creators',
            'mappings': {
                'creator': 'wikidata_url',
                'creatorLabel': 'name'
            }
        },
        'Material':
        {
            'model': Material,
            'relation_name': 'materials',
            'mappings': {
                'made_from_material': 'wikidata_url',
                'made_from_materialLabel': 'name'
            }
        },
        'Depiction':
        {
            'model': Depiction,
            'relation_name': 'depicts',
            'mappings': {
                'depicts': 'wikidata_url',
                'depictsLabel': 'name'
            }
        }
    }


def extract_data_from_mapping(painting: dict, mappings: dict) -> dict:
    models_names = list(mappings)
    models_to_fill = {model_name: {} for model_name in models_names}

    for model_name, property in mappings.items():
        for sparql_name, art_gallery_name in property['mappings'].items():
            if sparql_name in painting:
                models_to_fill[model_name][art_gallery_name] = painting[sparql_name]['value']

    return models_to_fill


def handle_creation(models_to_fill: dict, mappings: dict) -> None:
    painting = None
    relations = {}
    for model_name, data in models_to_fill.items():
        if len(data) > 0:
            model: models.Model = mappings[model_name]['model']

            collection = model.objects.filter(
                wikidata_url=data['wikidata_url'])
            if len(collection) > 0:
                already_existing_model = collection[0]
                if isinstance(already_existing_model, Painting):
                    painting = already_existing_model
                else:
                    relations[model_name] = already_existing_model
            else:
                new_model: models.Model = model(**data)
                new_model.save()
                if isinstance(new_model, Painting):
                    painting = new_model
                else:
                    relations[model_name] = new_model

    for relation_name, model in relations.items():
        painting_relation = getattr(
            painting, mappings[relation_name]['relation_name'])
        painting_relation.add(model)

    painting.save()
