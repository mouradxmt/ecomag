from django.urls import path
from .import views
# /articles/
urlpatterns = [
    path('', views.articles, name='articles'),
    path('<str:hierarchy>', views.show_category, name='category'),
    path('search', views.search, name='search'),
]