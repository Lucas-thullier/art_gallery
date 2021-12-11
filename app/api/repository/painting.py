from django.db.models.query import QuerySet


def with_picture(query_set: QuerySet):
    query_set.filter(picture_url__isnull=False)

    return query_set

def with_readable_name(query_set: QuerySet):
    query_set.filter(name__regex=r'[^(Q[0-9]+)]')

    return query_set