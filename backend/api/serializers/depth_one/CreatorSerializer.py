from api.models import Creator
from api.serializers.simple import SimplePaintingSerializer
from rest_framework import serializers


class CreatorSerializer(serializers.HyperlinkedModelSerializer):
    paintings = SimplePaintingSerializer(many=True, read_only=True)
    paintings_count = serializers.SerializerMethodField()

    class Meta:
        model = Creator
        depth = 1
        fields = [
            'id',
            'name',
            'url',
            'picture_url',
            'paintings',
            'paintings_count'
        ]

    def get_paintings_count(self, obj):
        return obj.paintings.count()
