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


class CoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cores
        fields = [
            'core', 'flight', 'gridfins',
            'legs', 'reused', 'landing_attempt',
            'landing_success', 'landing_type', 'landpad',
        ]


class StatsSerializer(serializers.ModelSerializer):
    cores = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='reused'
    )

    class Meta:
        model = Results
        fields = [
            'success', 'cores', 'rocket'
        ]

        depth = 1


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
    cores = CoresSerializer(many=True)
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
        depth = 1
