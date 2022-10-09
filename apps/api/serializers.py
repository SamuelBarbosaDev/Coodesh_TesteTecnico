from rest_framework import serializers

from api.models import SpaceX


class SpaceXSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceX
        fields = '__all__'

