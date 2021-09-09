from django.urls import path
from User.views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('/', HomeView.as_view(), name='home'),
]