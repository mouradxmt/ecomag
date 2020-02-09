
from datetime import datetime
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from pages import views as pages_views
from ecomag import forms
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   #path('', pages_views.index),
    path('', include('pages.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
