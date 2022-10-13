from django.urls import include, path
from rest_framework import routers

from api.views import *

router = routers.DefaultRouter()

router.register(r'message', SpaceXViewSet, basename='message')
router.register(r'launches', ResultsViewSet, basename='launches')
router.register(r'stats', StatsViewSet, basename='stats')
# router.register(r'Cores', CoresViewSet)
# router.register(r'Fairings', FairingsViewSet)
# router.register(r'Links', LinksViewSet)
# router.register(r'Patch', PatchViewSet)
# router.register(r'Reddit', RedditViewSet)
# router.register(r'Flickr', FlickrViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
