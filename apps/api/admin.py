from django.contrib import admin

from api.models import SpaceX


@admin.register(SpaceX)
class SpaceXAdmin(admin.ModelAdmin):
    exclude = ()

