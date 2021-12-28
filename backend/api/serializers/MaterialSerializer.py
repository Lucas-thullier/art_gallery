from api.models import Material
from api.serializers.DynamicDepthSerializer import DynamicDepthSerializer


class MaterialSerializer(DynamicDepthSerializer):
    class Meta:
        model = Material
        depth = 1
        fields = [
            'id',
            'name',
            'url',
            'paintings'
        ]
