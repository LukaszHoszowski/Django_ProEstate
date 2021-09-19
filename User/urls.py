from django.urls import path

from User.views import SignUpView, ProfileView, UserLoginView, UserLogoutView, UpdatePassword, \
    ProfileCreateBuildingView, ProfileCreateFlatView

app_name = 'User'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile_creation_building/', ProfileCreateBuildingView.as_view(), name='profile_create_building'),
    path('profile_creation_flat/', ProfileCreateFlatView.as_view(), name='profile_create_flat'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('pass_change/', UpdatePassword.as_view(), name='pass_change'),
]