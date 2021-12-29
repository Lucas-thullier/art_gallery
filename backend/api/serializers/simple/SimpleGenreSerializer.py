from api.models import Genre
from rest_framework import serializers


class SimpleGenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        depth = 0
        fields = [
            'id',
            'name',
            'url',
        ]
