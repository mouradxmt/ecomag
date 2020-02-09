from django.shortcuts import render
from .models import Product
from .models import Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def articles(request,cat=None):

    articles= Product.objects.order_by('name')
    paginator = Paginator(articles,2)
    page_number = request.GET.get('page')
    paged_articles = paginator.get_page(page_number)

    context={
        'articles': paged_articles,
    }
    return render(request, 'articles/products.html', context)

def product(request,product_id):
    product=get_objects_or_404(Product, pk=product_id)
    context = {
        'article': product
    }
    return render(request, 'articles/product.html', context)

def search(request):
    return render(request, 'articles/search.html')