from django.db.models.query import QuerySet


class CreatorQuerySet(QuerySet):
    def with_picture(self) -> QuerySet:
        return self.filter(picture_url__isnull=False)

    def with_readable_name(self) -> QuerySet:
        return self.exclude(name__regex=r"http.+")
