from django.urls import include, path
from rest_framework import routers

from api.views import *

router = routers.DefaultRouter()

router.register(r'message', SpaceXViewSet)
router.register(r'launches', ResultsViewSet)
# router.register(r'Fairings', FairingsViewSet)
# router.register(r'Links', LinksViewSet)
# router.register(r'Patch', PatchViewSet)
# router.register(r'Reddit', RedditViewSet)
# router.register(r'Flickr', FlickrViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
