from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import generics
from api.models import *
from api.serializers import *


class SpaceXViewSet(viewsets.ModelViewSet):
    queryset = SpaceX.objects.all()
    serializer_class = SpaceXSerializer


class StatsViewSet(viewsets.ModelViewSet):
    queryset = Results.objects.all()
    serializer_class = StatsSerializer


class FairingsViewSet(viewsets.ModelViewSet):
    queryset = Fairings.objects.all()
    serializer_class = FairingsSerializer


class CoresViewSet(viewsets.ModelViewSet):
    queryset = Cores.objects.all()
    serializer_class = CoresSerializer


class PatchViewSet(viewsets.ModelViewSet):
    queryset = Patch.objects.all()
    serializer_class = PatchSerializer


class RedditViewSet(viewsets.ModelViewSet):
    queryset = Reddit.objects.all()
    serializer_class = RedditSerializer


class FlickrViewSet(viewsets.ModelViewSet):
    queryset = Flickr.objects.all()
    serializer_class = FlickrSerializer


class LinksViewSet(viewsets.ModelViewSet):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer


class ResultsViewSet(viewsets.ModelViewSet):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer


# def space_x(request):
#     data = list(SpaceX.objects.values())

#     return JsonResponse(data, safe=False)
