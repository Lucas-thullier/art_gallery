from rest_framework import serializers
from api.models import Genre


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = [
            'id',
            'name',
            'paintings'
        ]
