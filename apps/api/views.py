from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response

from api.models import SpaceX
from api.serializers import SpaceXSerializer


class SpaceXViewSet(viewsets.ModelViewSet):
    queryset = SpaceX.objects.all()
    serializer_class = SpaceXSerializer

