from api.models import Depiction
from rest_framework import serializers


class SimpleDepictionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Depiction
        depth = 0
        fields = [
            'id',
            'name',
            'url',
        ]
