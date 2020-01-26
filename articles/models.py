from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=300)
    primaryCategory = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"


# Product Model
class Product(models.Model):
    mainimage = models.ImageField(upload_to='products/', blank=True, verbose_name='Image')
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
