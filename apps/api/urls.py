from django.urls import include, path
from rest_framework import routers
from api.views import *


router = routers.DefaultRouter()
router.register(r'message', SpaceXViewSet, basename='message')
router.register(r'launches', ResultsViewSet, basename='launches')
router.register(r'stats', StatsViewSet, basename='stats')


urlpatterns = [
    path("", include(router.urls)),
]
