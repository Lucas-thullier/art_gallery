from django.db import models
from django.utils.timezone import now

from ..repositories import CreatorQuerySet


class Creator(models.Model):
    name = models.CharField(max_length=255)
    wikidata_url = models.CharField(max_length=500, unique=True, null=False)
    picture_url = models.CharField(max_length=1000, null=True)

    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    objects: models.Manager = CreatorQuerySet.as_manager()
