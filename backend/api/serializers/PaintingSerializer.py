from rest_framework import serializers
from api.models import Painting

class PaintingSerializer(serializers.HyperlinkedModelSerializer):
    creators = serializers.HyperlinkedIdentityField(many=True, view_name='creator-detail', read_only=True)
    depicts = serializers.HyperlinkedIdentityField(many=True, view_name='depiction-detail', read_only=True)
    genres = serializers.HyperlinkedIdentityField(many=True, view_name='genre-detail', read_only=True)
    locations = serializers.HyperlinkedIdentityField(many=True, view_name='location-detail', read_only=True)
    materials = serializers.HyperlinkedIdentityField(many=True, view_name='material-detail', read_only=True)
    movements = serializers.HyperlinkedIdentityField(many=True, view_name='movement-detail', read_only=True)


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