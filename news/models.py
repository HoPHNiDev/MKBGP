from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Articles(models.Model):

    title = models.CharField('Title:', max_length=100)
    slug = models.SlugField('URL', max_length=100, unique=True, null=True)
    anons = models.CharField('Anons:', max_length=300)
    article_type = models.CharField(
        'Article type:', max_length=50, default='Новость')
    text = models.TextField(
        'Article:', max_length=5000)
    photo = models.ImageField('Article photo:', upload_to=f"Articles/{str(datetime.now()).split(' ')[0]}/",
                              null=True, blank=True)
    status = models.BooleanField('Status', default=True)
    author = models.ForeignKey(
        User, related_name="Author", on_delete=models.SET_NULL, null=True)
    views = models.IntegerField('Views:', default=0)

    created_at = models.DateTimeField('Created:', auto_now_add=True)
    updated_at = models.DateTimeField('Updated:', auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.slug}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class ArticleViewersData(models.Model):
    article = models.ForeignKey(
        Articles, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(
        'Viewer IP:', default="45.243.82.169")

    def __str__(self):
        return self.article.title

    class Meta:
        verbose_name = 'Viewers Data'
        verbose_name_plural = 'Viewers Data'
