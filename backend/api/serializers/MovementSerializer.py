from rest_framework import serializers
from api.models import Movement

class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = [
            'id',
            'name',
        ]