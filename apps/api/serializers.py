from rest_framework import serializers

from api.models import *


class SpaceXSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceX
        fields = '__all__'

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = '__all__'