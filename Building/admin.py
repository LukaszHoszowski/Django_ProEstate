from django.contrib import admin
from Building.models import Building, Cartography, HousingCooperative


@admin.action(description='Dodaj mieszkania')
def create_flats(modeladmin, request, queryset):
    queryset.update(status='p')


class BuildingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('street', 'building_no')}
    ordering = ['street']
    actions = [create_flats]


admin.site.register(Building, BuildingAdmin)
admin.site.register(Cartography)
admin.site.register(HousingCooperative)
