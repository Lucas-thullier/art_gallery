from api.serializers.simple import SimpleMovementSerializer, SimpleCreatorSerializer, SimpleDepictionSerializer, SimpleGenreSerializer, SimpleLocationSerializer, SimpleMaterialSerializer
from api.models import Painting
from rest_framework import serializers


class PaintingSerializer(serializers.HyperlinkedModelSerializer):
    creators = SimpleCreatorSerializer(many=True, read_only=True)
    depicts = SimpleDepictionSerializer(many=True, read_only=True)
    genres = SimpleGenreSerializer(many=True, read_only=True)
    locations = SimpleLocationSerializer(many=True, read_only=True)
    materials = SimpleMaterialSerializer(many=True, read_only=True)
    movements = SimpleMovementSerializer(many=True, read_only=True)

    class Meta:
        model = Painting
        depth = 1
        fields = [
            'id',
            'name',
            'url',
            'picture_url',
            'height',
            'width',
            'inception_at',
            'creators',
            'depicts',
            'genres',
            'locations',
            'materials',
            'movements',
        ]
