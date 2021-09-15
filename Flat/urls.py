from django.urls import path


app_name = 'Flat'
urlpatterns = [
    path('flat_list/', FlatListView.as_view(), name='flats'),
    path('<slug:slug>/', FlatDetailView.as_view(), name='flat_details'),
]
