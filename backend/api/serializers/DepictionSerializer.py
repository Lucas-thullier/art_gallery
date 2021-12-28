from api.models import Depiction
from api.serializers.DynamicDepthSerializer import DynamicDepthSerializer


class DepictionSerializer(DynamicDepthSerializer):
    class Meta:
        model = Depiction
        depth = 1
        fields = [
            'id',
            'name',
            'paintings'
        ]
