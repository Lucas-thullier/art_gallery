from django.db import models
from django.utils.timezone import now

from .Creator import Creator
from .Depiction import Depiction
from .Genre import Genre
from .Location import Location
from .Material import Material
from .Movement import Movement


class Painting(models.Model):
    name = models.CharField(max_length=500)
    native_name = models.CharField(max_length=500)
    wikidata_url = models.CharField(max_length=500, null=False)

    title = models.CharField(max_length=500)
    picture_url = models.CharField(max_length=500)
    owned_by = models.CharField(max_length=500)
    inception_at = models.DateTimeField()
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    described_at = models.CharField(max_length=500)

    creators = models.ManyToManyField(Creator)
    movements = models.ManyToManyField(Movement)
    genres = models.ManyToManyField(Genre)
    depicts = models.ManyToManyField(Depiction)
    materials = models.ManyToManyField(Material)
    locations = models.ManyToManyField(Location, related_name='actual_location')
    location_of_creations = models.ManyToManyField(Location, related_name='creation_location')

    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)
