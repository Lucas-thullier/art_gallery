from wikibaseintegrator import wbi_functions
from .sparql_repository import paintings_full_data, count_paintings_full_data


def get_painting_count():
    query = count_paintings_full_data()

    response = wbi_functions.execute_sparql_query(query)
    painting_count = response['results']['bindings'][0]['painting_count']['value']

    return painting_count


def get_paintings_with_full_data(limit=20, offset=20):
    query = paintings_full_data(limit, offset)

    response = wbi_functions.execute_sparql_query(query)
    paintings = response['results']['bindings']

    columns = response['head']['vars']

    paintings_with_full_data = {'columns': columns, 'paintings': paintings}
    
    return paintings_with_full_data
