from api.models import Material
from api.serializers.simple import SimplePaintingSerializer
from rest_framework import serializers


class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    paintings = SimplePaintingSerializer(many=True, read_only=True)

    class Meta:
        model = Material
        depth = 1
        fields = [
            'id',
            'name',
            'url',
            'paintings'
        ]
