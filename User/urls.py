from django.urls import path

from User.views import SignUpView, ProfileCreateView, ProfileView, UserLoginView, UserLogoutView, UpdatePassword

app_name = 'User'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile_creation/', ProfileCreateView.as_view(), name='profile_create'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('pass_change/', UpdatePassword.as_view(), name='pass_change'),
]