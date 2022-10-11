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


class FairingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fairings
        fields = '__all__'


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = '__all__'


class PatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patch
        fields = '__all__'


class RedditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reddit
        fields = '__all__'


class FlickrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flickr
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
