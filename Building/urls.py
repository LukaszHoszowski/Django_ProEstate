from django.urls import path

from Building.views import BuildingListView, BuildingDetailView, \
    BuildingCartographyView, BuildingCoopView, BuildingPhotosView, BuildingDocsView, BuildingPhotosCreate, \
    BuildingDocsCreate, BuildingFlatsView, FlatDetailView, FlatUpdateView, FlatAddUserUpdate, FlatDeleteUserUpdate, \
    MeasureUpdateView

app_name = 'Building'

urlpatterns = [
    # Building urls
    path('', BuildingListView.as_view(), name='buildings'),
    path('<slug:slug>/', BuildingDetailView.as_view(), name='building_details'),
    path('<slug:slug>/flats/', BuildingFlatsView.as_view(), name='building_flats'),
    path('<slug:slug>/cartography/', BuildingCartographyView.as_view(), name='building_cartography'),
    path('<slug:slug>/coop/', BuildingCoopView.as_view(), name='building_coop'),
    path('<slug:slug>/photos/', BuildingPhotosView.as_view(), name='building_photos'),
    path('<slug:slug>/add_photos/', BuildingPhotosCreate.as_view(), name='building_photos_add'),
    path('<slug:slug>/documents/', BuildingDocsView.as_view(), name='building_documents'),
    path('<slug:slug>/add_docs/', BuildingDocsCreate.as_view(), name='building_docs_add'),
    # Flat urls
    path('<slug:slug>/<int:pk>', FlatDetailView.as_view(), name='flat_details'),
    path('<slug:slug>/<int:pk>/update', FlatUpdateView.as_view(), name='flat_update'),
    path('add/user_to_flat/<int:pk>/', FlatAddUserUpdate.as_view(), name='flat_add_user'),
    path('del/user_from_flat/<int:pk>/', FlatDeleteUserUpdate.as_view(), name='flat_delete_user'),
    path('update/measure/<int:pk>/', MeasureUpdateView.as_view(), name='measure_update'),
]
