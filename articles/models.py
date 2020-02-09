from django.db import models
# TODO : try and catch the 404 error !

class Category(models.Model):
    name = models.CharField(max_length=300)
    # primaryCategory = models.BooleanField(default=False)
    slug = models.SlugField(default='', verbose_name='Identifiant')
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


# Product Model
class Product(models.Model):
    mainImage = models.ImageField(upload_to='photos/', blank=True, verbose_name='Image')
    name = models.CharField(max_length=300, verbose_name='Nom de produit')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200, verbose_name='Description courte')
    detail_text = models.TextField(max_length=1000, verbose_name='Desciption du produit')
    price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def get_cat_list(self):
        k = self.category

        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb) - 1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i - 1:-1])
        return breadcrumb[-1:0:-1]

    @staticmethod
    def by_category(slug):
        return Product.objects.filter(category=Category.objects.get(slug=slug)).all()
