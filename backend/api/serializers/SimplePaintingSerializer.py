from rest_framework import serializers
from api.models import Painting


class SimplePaintingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Painting
        depth = 0
        fields = [
            'id',
            'name',
            'url',
            'picture_url',
            'height',
            'width',
            'inception_at',
        ]
