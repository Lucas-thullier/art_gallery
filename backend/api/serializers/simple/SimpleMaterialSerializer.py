from api.models import Material
from rest_framework import serializers


class SimpleMaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Material
        depth = 0
        fields = [
            'id',
            'name',
            'url',
        ]
