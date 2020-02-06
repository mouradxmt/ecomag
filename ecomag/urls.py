
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
    path('login/', LoginView.as_view
        (
        template_name='pages/login.html',
        authentication_form=forms.BootstrapAuthenticationForm,
        extra_context=
        {
            'title': 'Log in',
            'year': datetime.now().year,
        }
    ),
                                      name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
