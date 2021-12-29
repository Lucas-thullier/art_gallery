from api.models import Movement
from api.serializers.simple import SimplePaintingSerializer
from rest_framework import serializers


class MovementSerializer(serializers.HyperlinkedModelSerializer):
    paintings = SimplePaintingSerializer(many=True, read_only=True)

    class Meta:
        model = Movement
        depth = 1
        fields = [
            'id',
            'name',
            'url',
            'paintings'
        ]
