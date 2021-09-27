from django.contrib import admin
from Building.models import Building, Cartography, HousingCooperative, Flat, BuildingDocs, BuildingPhotos, \
    PaymentPeriod, Measure


# @admin.action(description='Dodaj wskazania liczików')
# def create_flats(modeladmin, request, queryset):
#     queryset.update(status='p')


class BuildingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('street', 'number')}
    ordering = ['street']


class FlatAdmin(admin.ModelAdmin):
    ordering = ['building', 'number', 'number_suffix']
    exclude = ('building',)


class MeasureAdmin(admin.ModelAdmin):
    exclude = ('flat',)

    list_filter = [
        "flat",
        "flat__building",
        "payment_period__year",
        "payment_period__month",
    ]
    search_fields = (
        "flat__number",
        "flat__building__street",
    )


admin.site.register(Flat, FlatAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(BuildingDocs)
admin.site.register(BuildingPhotos)
admin.site.register(Cartography)
admin.site.register(HousingCooperative)
admin.site.register(PaymentPeriod)
admin.site.register(Measure, MeasureAdmin)
