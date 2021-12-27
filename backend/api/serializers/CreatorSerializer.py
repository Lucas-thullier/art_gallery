from rest_framework import serializers
from api.models import Creator

class CreatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Creator

        fields = [
            'id',
            'name',
            'paintings'
        ]