from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response

from api.models import *
from api.serializers import *


class SpaceXViewSet(viewsets.ModelViewSet):
    queryset = SpaceX.objects.all()
    serializer_class = SpaceXSerializer

class ResultsViewSet(viewsets.ModelViewSet):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer