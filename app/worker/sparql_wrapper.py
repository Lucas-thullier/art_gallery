from wikibaseintegrator import wbi_functions
from .sparql_repository import paintings_full_data, count_paintings_full_data


def get_painting_count() -> int:
    query = count_paintings_full_data()

    response = wbi_functions.execute_sparql_query(query)
    painting_count = response['results']['bindings'][0]['painting_count']['value']

    return int(painting_count)


def get_paintings_with_columns(limit: int = 20, offset: int = 20) -> dict:
    query = paintings_full_data(limit, offset)

    response = wbi_functions.execute_sparql_query(query)

    columns = response['head']['vars']
    paintings = response['results']['bindings']

    paintings_with_full_data = {
        'columns': columns,
        'paintings': paintings
    }

    return paintings_with_full_data
