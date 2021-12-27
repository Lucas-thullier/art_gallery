from rest_framework import serializers
from api.models import Location

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = [
            'id',
            'name',
            'paintings'
        ]