from django.contrib import admin
from django.urls import path, include
from User.views import SignUpView, ProfileCreateView, UpdatePassword, UserLoginView, UserLogoutView, MainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/profile_creation/', ProfileCreateView.as_view(), name='profile_create'),
    path('accounts/login/', UserLoginView.as_view(), name='user_login'),
    path('accounts/logout/', UserLogoutView.as_view(), name='user_logout'),
    path('accounts/pass_change/', UpdatePassword.as_view(), name='pass_change'),

]