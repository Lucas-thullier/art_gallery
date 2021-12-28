from api.models import Movement
from api.serializers.DynamicDepthSerializer import DynamicDepthSerializer


class MovementSerializer(DynamicDepthSerializer):
    class Meta:
        model = Movement
        depth = 1
        fields = [
            'id',
            'name',
            'url',
            'paintings'
        ]
