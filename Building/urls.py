from django.urls import path

from Building.views import BuildingListView, BuildingDetailView

app_name = 'Building'
urlpatterns = [
    path('building_list/', BuildingListView.as_view(), name='buildings'),
    path('<slug:slug>/', BuildingDetailView.as_view(), name='building_details'),
]
