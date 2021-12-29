from api.models import Movement
from rest_framework import serializers


class SimpleMovementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movement
        depth = 0
        fields = [
            'id',
            'name',
            'url',
        ]
