from rest_framework import serializers
from api.models import Depiction


class DepictionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Depiction
        fields = [
            'id',
            'name',
            'paintings'
        ]
