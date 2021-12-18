from django.db import models
from django.utils.timezone import now


from .Creator import Creator
from .Depiction import Depiction
from .Genre import Genre
from .Location import Location
from .Material import Material
from .Movement import Movement
from ..repository import PaintingQuerySet


class Painting(models.Model):
    def __init__(self, *args, **kwargs):
        if 'width' in kwargs:
            kwargs['width'] = float(kwargs['width'])
        else:
            kwargs['width'] = None

        if 'height' in kwargs:
            kwargs['height'] = float(kwargs['height'])
        else:
            kwargs['height'] = None
        super().__init__(*args, **kwargs)

    name = models.CharField(max_length=500, null=True)
    native_name = models.CharField(max_length=500, null=True)
    wikidata_url = models.CharField(max_length=500, unique=True, null=False)

    title = models.CharField(max_length=500, null=True)
    picture_url = models.CharField(max_length=500, null=True)
    owned_by = models.CharField(max_length=500, null=True)
    inception_at = models.DateTimeField(null=True)
    width = models.PositiveIntegerField(null=True)
    height = models.PositiveIntegerField(null=True)
    described_at = models.CharField(max_length=500, null=True)

    creators = models.ManyToManyField(Creator)
    movements = models.ManyToManyField(Movement)
    genres = models.ManyToManyField(Genre)
    depicts = models.ManyToManyField(Depiction)
    materials = models.ManyToManyField(Material)
    locations = models.ManyToManyField(
        Location, related_name='actual_location')

    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    objects: models.Manager = PaintingQuerySet.as_manager()
