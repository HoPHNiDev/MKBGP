from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class ProductsCategory(models.Model):
    title = models.CharField('Title:', max_length=100)
    slug = models.SlugField('URL', max_length=100, unique=True, null=True)
    text = models.TextField(
        'Description:', max_length=5000)
    photo = models.ImageField(
        'Category photo:', upload_to=f"ProductsCategory/{str(datetime.now()).split(' ')[0]}/")
    status = models.BooleanField('Status', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/products/category/{self.slug}'

    class Meta:
        verbose_name = 'Products Category'
        verbose_name_plural = 'Products Categories'


class Products(models.Model):
    title = models.CharField('Title:', max_length=100)
    slug = models.SlugField('URL', max_length=100, unique=True, null=True)
    anons = models.CharField('Anons:', max_length=300, null=True)
    description = models.TextField(
        'Description:', max_length=20000, null=True)
    details = models.TextField(
        'Details:', max_length=20000, null=True)
    photo = models.ImageField('Product photo:', upload_to=f"Products/{str(datetime.now()).split(' ')[0]}/",
                              null=True, blank=True)
    status = models.BooleanField('Status', default=True)
    hasDescription = models.BooleanField('hasDescription', default=True)
    author = models.ForeignKey(
        User, related_name="Product_Author", on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        ProductsCategory, related_name="Category", on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField('Created:', auto_now_add=True)
    updated_at = models.DateTimeField('Updated:', auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/products/{self.slug}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
