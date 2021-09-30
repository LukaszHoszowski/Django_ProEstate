from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from User.views import MainView, AboutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('about/', AboutView.as_view(), name='about'),
    path('accounts/', include('User.urls')),
    path('buildings/', include('Building.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
