from api.models import Creator
from api.serializers.DynamicDepthSerializer import DynamicDepthSerializer


class CreatorSerializer(DynamicDepthSerializer):
    class Meta:
        model = Creator
        depth = 1
        fields = [
            'id',
            'name',
            'paintings'
        ]
