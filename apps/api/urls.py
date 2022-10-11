from django.urls import include, path
from rest_framework import routers

from api.views import *

router = routers.DefaultRouter()

router.register(r'SpaceX', SpaceXViewSet)
router.register(r'Results', ResultsViewSet)
router.register(r'Fairings', FairingsViewSet)
router.register(r'Links', LinksViewSet)
router.register(r'Patch', PatchViewSet)
router.register(r'Reddit', RedditViewSet)
router.register(r'Flickr', FlickrViewSet)
router.register(r'launches', ResultViewSet)
router.register(r'launches/<int:pk>', ResultViewSet)





urlpatterns = [
    path("v1/api/", include(router.urls)),
    path("", spaceX, name='spaceX'),

]