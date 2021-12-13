from django.test import TestCase

from ..sparql_repository import count_paintings_full_data, paintings_full_data


class SparqlRepositoryTestCase(TestCase):
    def test_count_paintings_full_data_is_str(self):
        query = count_paintings_full_data()
        return self.assertIsInstance(query, str)

    def test_paintings_full_data_is_str(self):
        query = paintings_full_data()
        return self.assertIsInstance(query, str)

