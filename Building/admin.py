from django.contrib import admin
from Building.models import Building, Cartography, HousingCooperative


class BuildingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('street', 'building_no')}


admin.site.register(Building, BuildingAdmin)
admin.site.register(Cartography)
admin.site.register(HousingCooperative)
