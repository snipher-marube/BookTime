from django.db import models
from django.db.models import manager


class ProductTag(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=48)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def natural_key(self):
        return str(self.slug,)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(max_length=48)
    active = models.BooleanField(default=False)
    in_stock = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(ProductTag, blank=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='product-thumbnails', null=True)
    image = models.ImageField(upload_to='product-images')

    def __str__(self):
        return str(self.product)



