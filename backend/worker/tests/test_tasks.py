from django.test import TestCase

from ..tasks import import_from_paintings_interval, get_mappings, remap_data_for_model, handle_creation
from ..sparql_wrapper import get_paintings_with_columns, get_painting_count


class TasksTestCase(TestCase):
    def test_get_mappings_is_str(self):
        mappings = get_mappings()
        self.assertIsInstance(mappings, dict)

    def test_get_mappings_is_well_structured(self):
        mappings = get_mappings()

        for model_infos in mappings.values():
            self.assertIn('model', model_infos)
            self.assertIn('relation_name', model_infos)
            self.assertIn('mappings', model_infos)

    def test_remap_data_for_model_is_dict(self):
        paintings_with_full_data = get_paintings_with_columns(20, 0)
        painting = paintings_with_full_data['paintings'][0]

        mappings = get_mappings()

        model_data = remap_data_for_model(painting, mappings)

        self.assertIsInstance(model_data, dict)
    
    def test_handle_creation_is_dict(self):
        paintings_with_full_data = get_paintings_with_columns(20, 0)
        painting = paintings_with_full_data['paintings'][0]

        mappings = get_mappings()

        model_data = remap_data_for_model(painting, mappings)

        logs = handle_creation(model_data, mappings)
        self.assertIsInstance(logs, dict)

        
