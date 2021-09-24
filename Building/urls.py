from django.urls import path

from Building.views import BuildingListView, BuildingDetailView, FlatListView, FlatDetailView, \
    BuildingCartographyView, BuildingCoopView, BuildingPhotosView, BuildingDocsView, BuildingPhotosCreate

app_name = 'Building'
urlpatterns = [
    path('', BuildingListView.as_view(), name='buildings'),
    path('<slug:slug>/', BuildingDetailView.as_view(), name='building_details'),
    path('<slug:slug>/flat_list/', FlatListView.as_view(), name='building_flats'),
    path('<slug:slug>/', FlatDetailView.as_view(), name='flat_details'),
    path('<slug:slug>/cartography/', BuildingCartographyView.as_view(), name='building_cartography'),
    path('<slug:slug>/coop/', BuildingCoopView.as_view(), name='building_coop'),
    path('<slug:slug>/photos/', BuildingPhotosView.as_view(), name='building_photos'),
    path('<slug:slug>/add_photos/', BuildingPhotosCreate.as_view(), name='building_photos_add'),
    path('<slug:slug>/documents/', BuildingDocsView.as_view(), name='building_documents'),
]
