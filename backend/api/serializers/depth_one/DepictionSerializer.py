from api.models import Depiction
from api.serializers.simple import SimplePaintingSerializer
from rest_framework import serializers


class DepictionSerializer(serializers.HyperlinkedModelSerializer):
    paintings = SimplePaintingSerializer(many=True, read_only=True)

    class Meta:
        model = Depiction
        depth = 1
        fields = [
            'id',
            'name',
            'url',
            'paintings'
        ]
