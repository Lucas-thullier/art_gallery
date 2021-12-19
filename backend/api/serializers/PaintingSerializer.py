from rest_framework import serializers
from api.models import Painting

class PaintingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = [
            'id',
            'name',
            'picture_url',
            'height',
            'width'
        ]