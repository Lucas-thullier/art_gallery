from api.models import Location
from api.serializers.simple import SimplePaintingSerializer
from rest_framework import serializers


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    paintings = SimplePaintingSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        depth = 1
        fields = [
            'id',
            'name',
            'url',
            'paintings'
        ]
