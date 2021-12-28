from rest_framework import serializers


class DynamicDepthSerializer(serializers.HyperlinkedModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields", None)
        exclude = kwargs.pop("exclude", None)
        nest = kwargs.pop("nest", None)

        if nest is not None:
            if nest == True:
                self.Meta.depth = 0

        super(DynamicDepthSerializer, self).__init__(*args, **kwargs)
