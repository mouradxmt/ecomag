from django.urls import path
from .import views
# /articles/
urlpatterns = [
    path('', views.articles, name='articles'),
    path('<int:article_id>', views.product, name='article'),
    path('category/<slug:slug>/', views.articles_category, name='category'),
    path('search', views.search, name='search'),
]