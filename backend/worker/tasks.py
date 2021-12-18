import logging
import json
from api.models import Movement, Location, Creator, Depiction, Genre, Material, Painting
from django.db import models
from .worker import app
from .sparql_wrapper import get_paintings_with_columns, get_painting_count

logger = logging.getLogger('import_paintings_logger')
creations_errors_logger = logging.getLogger('creations_errors_logger')


@app.task(bind=True, name='populate_database')
def populate_database(self, offset=0):
    try:
        painting_count = get_painting_count()

        limit = 20
        while offset <= painting_count:
            app.send_task('import_from_paintings_interval', args=[limit, offset])
            offset += limit
    except Exception as e:
        log = {'error': e, 'offset': offset, 'painting_count': painting_count}
        logger.warning(log)


@app.task(bind=True, name='import_from_paintings_interval', rate_limit='0.5/s')
def import_from_paintings_interval(self, limit, offset):
    paintings_with_full_data = get_paintings_with_columns(limit, offset)
    paintings: list = paintings_with_full_data['paintings']

    mappings = get_mappings()

    for painting in paintings:
        models_to_fill = remap_data_for_model(painting, mappings)

        logs = handle_creation(models_to_fill, mappings)
        logger.info(json.dumps(logs))


def get_mappings() -> dict:
    return {
        'Painting': {
            'model': Painting,
            'relation_name': False,
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


def remap_data_for_model(painting: dict, mappings: dict) -> dict:
    models_names = list(mappings)
    models_to_fill = {model_name: {} for model_name in models_names}

    for model_name, property in mappings.items():
        for sparql_name, art_gallery_name in property['mappings'].items():
            if sparql_name in painting:
                models_to_fill[model_name][art_gallery_name] = painting[sparql_name]['value']

    return models_to_fill


def handle_creation(models_to_fill: dict, mappings: dict) -> dict:
    painting = None
    relations = {}
    logs = {
        'painting': {
            'id': None,
            'is_new': None
        },
        'relations': {},
    }

    for model_name, data in models_to_fill.items():
        if len(data) > 0:
            model = mappings[model_name]['model']

            try:
                model_instance, is_new = model.objects.get_or_create(
                    wikidata_url=data['wikidata_url'],
                    defaults=data
                )

                if is_new:
                    model_instance.save()
                
                if isinstance(model, Painting):
                    painting: Painting = model_instance
                    logs['painting']['id'] = painting.id
                    logs['painting']['is_new'] = is_new
                else:
                    relations[model_name] = model_instance
                    logs['relations'][model_name] = {}
                    logs['relations'][model_name]['id'] = model_instance.id
                    logs['relations'][model_name]['is_new'] = is_new
            except Exception as e:
                creations_errors_logger.warning({'error': e, 'model': ''})

    for relation_name, relation_model in relations.items():
        if painting is not None:
            painting_relation = getattr(painting, mappings[relation_name]['relation_name'])
            painting_relation.add(relation_model)

    if painting is not None:
        painting.save()

    return logs
