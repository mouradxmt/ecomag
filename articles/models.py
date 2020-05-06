import itertools

from django.db import models
from datetime import datetime
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.contrib.auth.models import User
from ecomag import settings
from pages.models import UserProfileInfo


class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=50,
    )
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

    def _generate_slug(self):
        max_length = self._meta.get_field('slug').max_length
        value = self.name
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Category.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)


# Product Model
class Product(models.Model):
    mainImage = models.ImageField(upload_to='photos/', blank=True, verbose_name='Main Image')
    SecondImage = models.ImageField(upload_to='photos/', blank=True, verbose_name='Second Image')
    ThirdImage = models.ImageField(upload_to='photos/', blank=True, verbose_name='Third Image')
    name = models.CharField(max_length=50, verbose_name='Nom de produit')
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=50,
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200, verbose_name='Description courte')
    detail_text = models.TextField(max_length=1000, verbose_name='Desciption du produit')
    price = models.FloatField()
    date = models.DateTimeField(default=datetime.now, blank=True)

    def overallRating(self):
        ratings=[rat.Rating for rat in list(Comment.objects.filter(ProductId=self))]
        if len(ratings):
            return sum(ratings) / len(ratings)
        return 0

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        get_latest_by = ['-date']

    def get_cat_list(self):
        k = self.category

        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb) - 1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i - 1:-1])
        return breadcrumb[-1:0:-1]

    def _generate_slug(self):
        max_length = self._meta.get_field('slug').max_length
        value = self.name
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Product.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)

    @staticmethod
    def by_category(slug):
        category_queryset = Category.objects.filter(slug=slug)
        return Product.objects.filter(category=category_queryset[0]).order_by('-date')[:3]

#Comments
class Comment(models.Model):
    UserId = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name=_('User'))
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'))
    title = models.CharField(max_length=50, default='', verbose_name=_('Title'))
    Rating = models.IntegerField(verbose_name=_('Rating'))
    content = models.TextField(max_length=250, verbose_name=_('Comment'))
    date = models.DateTimeField(default=datetime.now, editable=False)

    def __str__(self):
        return self.UserId.__str__() + ' on ' + self.ProductId.__str__()

#panier
class Cart(models.Model):
    UserId = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='amount', default=1)

    def getPriceUnit(self):
        return self.amount * self.ProductId.price

