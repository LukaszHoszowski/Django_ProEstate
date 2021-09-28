from django.urls import path

from User import views
from User.views import SignUpView, ProfileView, UserLoginView, UserLogoutView, UpdatePassword, \
    ProfileCreateAdditionalView, FlatUserUpdateView, FlatFormView, DeleteUser

app_name = 'User'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile_creation_additional/', ProfileCreateAdditionalView.as_view(), name='profile_create_additional'),
    # path('profile_creation_building/', ProfileCreateBuildingView.as_view(), name='profile_create_building'),
    path('profile_creation_flat/', FlatFormView.as_view(), name='profile_create_flat'),
    # path('profile_creation_flat/<int:pk>/', FlatUserUpdateView.as_view(), name='profile_create_flat'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('pass_change/', UpdatePassword.as_view(), name='pass_change'),
    path('delete_user/', DeleteUser.as_view(), name='delete_user'),
    # path('ajax/load-flats/', views.load_flats, name='ajax_load_flats'),
]
