from django.shortcuts import render
from .models import Product
from .models import Category
# Create your views here.


def articles(request):
    articles= Product.objects.all()
    categories = Category.objects.all()
    context={
        'articles': articles,
        'categories': categories
    }
    return render(request, 'articles/products.html', context)


def articles_category(request, slug='homme'):
    articles_by_cat = Product.by_category(slug=slug)
    context = {
        'articles': articles_by_cat
    }
    return render(request, 'articles/products.html', context)


def product(request):
    return render(request, 'articles/product.html')


def search(request):
    return render(request, 'articles/search.html')