from rest_framework import serializers
from api.models import Painting, Creator

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = [
            'id',
            'name',
        ]