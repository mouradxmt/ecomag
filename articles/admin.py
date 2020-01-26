from django.contrib import admin
from articles.models import Category, Product

admin.site.site_header='ECOMAG'

admin.site.register(Category)
admin.site.register(Product)
