from django.contrib import admin
from api.models import *


@admin.register(SpaceX)
class SpaceXAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    exclude = ()


