from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Product
from .models import Category, Comment, UserProfileInfo
from django.core.paginator import Paginator
from .forms import addComment


# Create your views here.


def articles(request):
    articles = Product.objects.order_by('-date')
    categories = Category.objects.all()
    paginator = Paginator(articles, 3)  # show 6 articles per page
    page = request.GET.get('page')
    paged_articles = paginator.get_page(page)
    context = {
        'articles': paged_articles,
        'categories': categories
    }
    return render(request, 'articles/products.html', context)


# TODO : REPAIR SHOW BY CATEGORY HIERARCHIC FILTER

def show_category(request, hierarchy=None):
    category_slug = hierarchy.split('/')
    category_queryset = list(Category.objects.all())
    all_slugs = [x.slug for x in category_queryset]
    parent = None
    categories = Category.objects.all()
    for slug in category_slug:
        if slug in all_slugs:
            filteredArticels = Product.by_category(slug=slug)
            paginator = Paginator(filteredArticels, 3)  # show 6 articles per page
            page = request.GET.get('page')
            paged_articles = paginator.get_page(page)
        else:
            instance = get_object_or_404(Product, slug=slug)
            breadcrumbs_link = instance.get_cat_list()
            category_name = [' '.join(i.split('/')[-1].split('-')) for i in breadcrumbs_link]
            try:
                comments = Comment.objects.filter(ProductId=instance)
            except Comment.DoesNotExist:
                comments = None
            breadcrumbs = zip(breadcrumbs_link, category_name)
            comments.addComment = addComment
            if request.method == 'POST':
                form = addComment(data=request.POST)
                if form.is_valid():
                    comment = form.save(commit=False)
                    comment.UserId = request.user
                    comment.ProductId = instance
                    comment.save()
                    return redirect(request.get_full_path())

            return render(request, 'articles/product.html', {'instance': instance, 'comments': comments, 'breadcrumbs': breadcrumbs})

    return render(request, 'articles/products.html',
                  {'articles': paged_articles, 'categories': categories})


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
