from api.models import Location
from api.serializers.DynamicDepthSerializer import DynamicDepthSerializer


class LocationSerializer(DynamicDepthSerializer):
    class Meta:
        model = Location
        depth = 1
        fields = [
            'id',
            'name',
            'url',
            'paintings'
        ]
