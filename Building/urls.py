from django.urls import path

from Building.views import BuildingListView, BuildingDetailView, FlatListView, FlatDetailView, \
    BuildingCartographyView

app_name = 'Building'
urlpatterns = [
    path('', BuildingListView.as_view(), name='buildings'),
    path('<slug:slug>/', BuildingDetailView.as_view(), name='building_details'),
    path('flat_list/', FlatListView.as_view(), name='flats'),
    path('<slug:slug>/', FlatDetailView.as_view(), name='flat_details'),
    path('cartography/<slug:slug>', BuildingCartographyView.as_view(), name='building_cartography'),
]
