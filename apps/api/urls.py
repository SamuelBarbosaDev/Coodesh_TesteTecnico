from django.urls import include, path
from rest_framework import routers

from api.views import *

router = routers.DefaultRouter()

router.register(r'SpaceX', SpaceXViewSet)
router.register(r'Results', ResultsViewSet)


urlpatterns = [
    path("routes/", include(router.urls)),
]