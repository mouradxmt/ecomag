from django.urls import path
from .import views
# /articles/
urlpatterns = [
    path('', views.articles, name='articles'),
    path('<str:Category_name>', views.articles,name='type'),
    path('<int:product_id>',views.product,name='article'),
    path('search', views.search, name='search'),
]