from api.serializers import CreatorSerializer, GenreSerializer, DepictionSerializer, LocationSerializer, MaterialSerializer, MovementSerializer
from api.serializers.DynamicDepthSerializer import DynamicDepthSerializer
from api.models import Painting


class PaintingSerializer(DynamicDepthSerializer):
    creators = CreatorSerializer(many=True, read_only=True, nest=True)
    depicts = DepictionSerializer(many=True, read_only=True, nest=True)
    genres = GenreSerializer(many=True, read_only=True, nest=True)
    locations = LocationSerializer(many=True, read_only=True, nest=True)
    materials = MaterialSerializer(many=True, read_only=True, nest=True)
    movements = MovementSerializer(many=True, read_only=True, nest=True)

    class Meta:
        model = Painting
        depth = 1
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
