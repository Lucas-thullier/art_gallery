from api.models import Creator
from rest_framework import serializers


class SimpleCreatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Creator
        depth = 0
        fields = [
            'id',
            'name',
            'url',
        ]
