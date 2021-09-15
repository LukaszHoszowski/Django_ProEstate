from django.contrib import admin
from Flat.models import Flat


class FlatAdmin(admin.ModelAdmin):
    ordering = ['building', 'number', 'number_suffix']


admin.site.register(Flat, FlatAdmin)
