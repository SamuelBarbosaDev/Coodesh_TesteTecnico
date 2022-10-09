from django.urls import include, path
from rest_framework import routers

from api.views import SpaceXViewSet

router = routers.DefaultRouter()

router.register(r'', SpaceXViewSet)

urlpatterns = [
    path("", include(router.urls)),
]