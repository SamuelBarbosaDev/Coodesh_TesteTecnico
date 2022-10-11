from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import generics
from api.models import *
from api.serializers import *


class SpaceXViewSet(viewsets.ModelViewSet):
    queryset = SpaceX.objects.all()
    serializer_class = SpaceXSerializer


class ResultsViewSet(viewsets.ModelViewSet):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer


class FairingsViewSet(viewsets.ModelViewSet):
    queryset = Fairings.objects.all()
    serializer_class = FairingsSerializer


class LinksViewSet(viewsets.ModelViewSet):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer


class PatchViewSet(viewsets.ModelViewSet):
    queryset = Patch.objects.all()
    serializer_class = PatchSerializer


class RedditViewSet(viewsets.ModelViewSet):
    queryset = Reddit.objects.all()
    serializer_class = RedditSerializer


class FlickrViewSet(viewsets.ModelViewSet):
    queryset = Flickr.objects.all()
    serializer_class = FlickrSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Launches.objects.all()
    serializer_class = LaunchesSerializer

class StatsViewSet(viewsets.ModelViewSet):
    queryset = Launches.objects.all()
    serializer_class = LaunchesSerializer


def spaceX(request):
    data = list(SpaceX.objects.values())

    return JsonResponse(data, safe=False)
