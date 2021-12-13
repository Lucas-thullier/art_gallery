from django.db import models
from django.utils.timezone import now


class Material(models.Model):
    name = models.CharField(max_length=255)
    wikidata_url = models.CharField(max_length=500, unique=True, null=False)

    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)
