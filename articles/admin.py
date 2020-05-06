from django.contrib import admin
from articles.models import Category, Product, Comment, Cart


admin.site.site_title = 'ECOMAG'
admin.site.site_header='ECOMAG'

admin.site.register(Category)
admin.site.register(Product)

admin.site.register(Comment)
admin.site.register(Cart)

