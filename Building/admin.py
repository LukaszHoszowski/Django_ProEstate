from django.contrib import admin
from Building.models import Building, Cartography, HousingCooperative, Flat


# @admin.action(description='Dodaj mieszkania')
# def create_flats(modeladmin, request, queryset):
#     queryset.update(status='p')


class BuildingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('street', 'building_no')}
    ordering = ['street']
    # actions = [create_flats]


class FlatAdmin(admin.ModelAdmin):
    ordering = ['building', 'number', 'number_suffix']
    exclude = ('building',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Cartography)
admin.site.register(HousingCooperative)
