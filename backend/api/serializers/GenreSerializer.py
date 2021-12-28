from api.models import Genre
from api.serializers.DynamicDepthSerializer import DynamicDepthSerializer


class GenreSerializer(DynamicDepthSerializer):
    class Meta:
        model = Genre
        depth = 1
        fields = [
            'id',
            'name',
            'paintings'
        ]
