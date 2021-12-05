def count_paintings_full_data():
    query = """
    SELECT (COUNT(*) AS ?painting_count) WHERE {
        ?painting p:P31 ?statement0.
        ?statement0 (ps:P31/(wdt:P279*)) wd:Q3305213.
    }"""

    return query


def paintings_full_data(limit=20, offset=20):
    query = """
    SELECT ?painting ?paintingLabel ?pic ?inception ?movement ?movementLabel ?location ?locationLabel ?owned_by ?native_label ?title ?genre ?genreLabel ?creator ?creatorLabel ?made_from_material ?made_from_materialLabel ?depicts ?depictsLabel ?width ?height ?described_at WHERE {
        {
            SELECT DISTINCT ?painting WHERE {
                ?painting p:P31 ?statement0.
                ?statement0 (ps:P31/(wdt:P279*)) wd:Q3305213.
            }
            LIMIT """+str(limit)+"""
            OFFSET """+str(offset)+"""
        }
        OPTIONAL { ?painting wdt:P18 ?pic. }
        OPTIONAL { ?painting wdt:P1705 ?native_label. }
        OPTIONAL { ?painting wdt:P571 ?inception. }
        OPTIONAL { ?painting wdt:P135 ?movement. }
        OPTIONAL { ?painting wdt:P276 ?location. }
        OPTIONAL { ?painting wdt:P127 ?owned_by. }
        OPTIONAL { ?painting wdt:P1476 ?title. }
        OPTIONAL { ?painting wdt:P136 ?genre. }
        OPTIONAL { ?painting wdt:P170 ?creator. }
        OPTIONAL { ?painting wdt:P495 ?country_of_origin. }
        OPTIONAL { ?painting wdt:P186 ?made_from_material. }
        OPTIONAL { ?painting wdt:P180 ?depicts. }
        OPTIONAL { ?painting wdt:P1071 ?location_of_creation. }
        OPTIONAL { ?painting wdt:P2049 ?width. }
        OPTIONAL { ?painting wdt:P2048 ?height. }
        OPTIONAL { ?painting wdt:P973 ?described_at. }

        SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }"""

    return query
