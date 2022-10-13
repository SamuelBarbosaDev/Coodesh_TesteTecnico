from django.contrib import admin
from api.models import *


@admin.register(SpaceX)
class SpaceXAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    exclude = ()


# @admin.register(Fairings)
# class FairingsAdmin(admin.ModelAdmin):
#     exclude = ()


@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(Patch)
class PatchAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(Reddit)
class RedditAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(Flickr)
class FlickrAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(Cores)
class CoresAdmin(admin.ModelAdmin):
    exclude = ()
