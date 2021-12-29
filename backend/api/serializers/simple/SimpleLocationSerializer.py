from api.models import Location
from rest_framework import serializers


class SimpleLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        depth = 0
        fields = [
            'id',
            'name',
            'url',
        ]
