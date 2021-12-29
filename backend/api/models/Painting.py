from django.db import models
from django.utils.timezone import now
import re
from django.db.models.signals import pre_save
from django.dispatch import receiver
from . import Creator, Depiction, Genre, Location, Material, Movement
from ..repositories import PaintingQuerySet


class Painting(models.Model):
    name = models.CharField(max_length=500, null=True)
    native_name = models.CharField(max_length=500, null=True)
    wikidata_url = models.CharField(max_length=500, unique=True, null=False)

    title = models.CharField(max_length=500, null=True)
    picture_url = models.CharField(max_length=1000, null=True)
    owned_by = models.CharField(max_length=500, null=True)
    inception_at = models.CharField(max_length=10, null=True)
    width = models.PositiveIntegerField(null=True)
    height = models.PositiveIntegerField(null=True)
    described_at = models.CharField(max_length=500, null=True)

    creators = models.ManyToManyField(Creator, related_name='paintings')
    movements = models.ManyToManyField(Movement, related_name='paintings')
    genres = models.ManyToManyField(Genre, related_name='paintings')
    depicts = models.ManyToManyField(Depiction, related_name='paintings')
    materials = models.ManyToManyField(Material, related_name='paintings')

    locations = models.ManyToManyField(
        Location, related_name='paintings')

    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    objects: models.Manager = PaintingQuerySet.as_manager()


@receiver(pre_save, sender=Painting)
def painting_pre_save(sender, instance, *args, **kwargs):
    if instance.width is not None:
        instance.width = float(instance.width)
    else:
        instance.width = None

    if instance.height is not None:
        instance.height = float(instance.height)
    else:
        instance.height = None

    if type(instance.inception_at) is str:
        if instance.inception_at.startswith('http'):
            instance.inception_at = None
        else:
            year_regex = r"^-?\d+(?=-)"
            match = re.match(year_regex, instance.inception_at)
            if match is not None:
                instance.inception_at = match.group(0)
