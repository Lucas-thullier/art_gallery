from api.models import Creator
from api.serializers.simple import SimplePaintingSerializer
from rest_framework import serializers


class CreatorSerializer(serializers.HyperlinkedModelSerializer):
    paintings = SimplePaintingSerializer(many=True, read_only=True)

    class Meta:
        model = Creator
        depth = 1
        fields = [
            'id',
            'name',
            'url',
            'paintings'
        ]
