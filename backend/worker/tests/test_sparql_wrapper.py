from django.test import TestCase

from ..sparql_wrapper import get_painting_count, get_paintings_with_columns
from ..sparql_repository import count_paintings_full_data
from wikibaseintegrator import wbi_functions


class SparqlWrapperTestCase(TestCase):
    def test_is_endpoint_available(self):
        query = count_paintings_full_data()
        response = wbi_functions.execute_sparql_query(query, max_retries=2)

        self.assertIsInstance(response, dict)

    def test_get_painting_count_is_int(self):
        painting_count = get_painting_count()
        self.assertIsInstance(painting_count, int)

    def test_get_paintings_with_columns_is_dict(self):
        paintings = get_paintings_with_columns(20, 0)
        self.assertIsInstance(paintings, dict)
