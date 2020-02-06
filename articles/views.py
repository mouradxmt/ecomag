from django.shortcuts import render
from .models import Product
# Create your views here.

def articles(request):
    articles= Product.objects.all()
    context={
        'articles':articles
    }
    return render(request, 'articles/products.html', context)

def product(request):
    return render(request, 'articles/product.html')

def search(request):
    return render(request, 'articles/search.html')