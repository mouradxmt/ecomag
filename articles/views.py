from django.shortcuts import render
from .models import Product
from .models import Category
from django.core.paginator import Paginator
# Create your views here.


def articles(request):
    articles= Product.objects.all()
    categories=Category.objects.all()
    paginator = Paginator(articles, 3) # show 6 articles per page
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)
    context = {
        'articles': paged_articles,
        'categories': categories
    }
    return render(request, 'articles/products.html', context)

def articles_category(request, slug='homme'):
    articles_by_cat = Product.by_category(slug=slug)
    categories = Category.objects.all()
    paginator = Paginator(articles_by_cat, 3)  # show 6 articles per page
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)
    context = {
        'articles': paged_articles,
        'categories': categories
    }
    return render(request, 'articles/products.html', context)


def product(request):
    return render(request, 'articles/product.html')


def search(request):
    return render(request, 'articles/search.html')