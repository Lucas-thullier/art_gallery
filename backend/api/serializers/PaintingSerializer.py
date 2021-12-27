from rest_framework import serializers
from api.models import Painting, Creator
from . import CreatorSerializer, DepictionSerializer, GenreSerializer, LocationSerializer, MaterialSerializer, MovementSerializer

class PaintingSerializer(serializers.ModelSerializer):
    creators = CreatorSerializer(many=True)
    depicts = DepictionSerializer(many=True)
    genres = GenreSerializer(many=True)
    locations = LocationSerializer(many=True)
    materials = MaterialSerializer(many=True)
    movements = MovementSerializer(many=True)

    class Meta:
        model = Painting
        fields = [
            'id',
            'name',
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