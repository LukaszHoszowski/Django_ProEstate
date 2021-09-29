from django.urls import path

from User import views
from User.views import SignUpView, ProfileView, UserLoginView, UserLogoutView, UpdatePassword, \
    ProfileCreateAdditionalView, FlatUserUpdateView, FlatFormView, DeleteUser, ReportFailureView, ContactNeighbourView, \
    ProfileUpdateView

app_name = 'User'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile_creation_additional/', ProfileCreateAdditionalView.as_view(), name='profile_create_additional'),
    path('profile_creation_flat/', FlatFormView.as_view(), name='profile_creation_flat'),
    # path('profile_creation_flat/<int:pk>/', FlatUserUpdateView.as_view(), name='profile_create_flat'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/pass_change/', UpdatePassword.as_view(), name='pass_change'),
    path('profile/delete_user/', DeleteUser.as_view(), name='delete_user'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('report_failure/', ReportFailureView.as_view(), name='report_failure'),
    path('contact_neighbour/', ContactNeighbourView.as_view(), name='contact_neighbour'),
]
