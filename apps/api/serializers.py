from rest_framework import serializers
from api.models import *


class SpaceXSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceX
        fields = ['message']


class FairingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fairings
        fields = [
            'reused', 'recovery_attempt',
            'recovered', 'ships',
        ]


class PatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patch
        fields = ['small', 'large']


class RedditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reddit
        fields = ['campaign', 'launch', 'media', 'recovery']


class FlickrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flickr
        fields = ['small', 'original']


class LinksSerializer(serializers.ModelSerializer):
    patch = PatchSerializer(required=False)
    reddit = RedditSerializer(required=False)
    flickr = FlickrSerializer(required=False)

    class Meta:
        model = Links
        fields = [
            'patch', 'reddit', 'flickr',
            'presskit', 'webcast', 'youtube_id',
            'article', 'wikipedia',
        ]


class ResultsSerializer(serializers.ModelSerializer):
    links = LinksSerializer(required=False)
    fairings = FairingsSerializer(required=False)

    class Meta:
        model = Results
        fields = [
            'fairings', 'links', 'static_fire_date_utc',
            'static_fire_date_unix', 'net', 'window',
            'rocket', 'success', 'failures',
            'details', 'crew', 'ships',
            'capsules', 'payloads', 'launchpad',
            'flight_number', 'name', 'date_utc',
            'date_unix', 'date_local', 'date_precision',
            'upcoming', 'cores', 'auto_update',
            'tbd', 'launch_library_id', 'id',
        ]
