from rest_framework import serializers
from api.models import Material

class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Material
        fields = [
            'id',
            'name',
            'paintings'
        ]