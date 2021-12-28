from rest_framework import serializers
from api.models import Movement


class MovementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movement
        fields = [
            'id',
            'name',
            'paintings'
        ]
