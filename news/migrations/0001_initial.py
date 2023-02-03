# Generated by Django 4.1.5 on 2023-02-03 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title:')),
                ('title_ru', models.CharField(max_length=100, null=True, verbose_name='Title:')),
                ('title_en', models.CharField(max_length=100, null=True, verbose_name='Title:')),
                ('slug', models.SlugField(max_length=100, null=True, unique=True, verbose_name='URL')),
                ('slug_ru', models.SlugField(max_length=100, null=True, unique=True, verbose_name='URL')),
                ('slug_en', models.SlugField(max_length=100, null=True, unique=True, verbose_name='URL')),
                ('anons', models.CharField(max_length=300, verbose_name='Anons:')),
                ('anons_ru', models.CharField(max_length=300, null=True, verbose_name='Anons:')),
                ('anons_en', models.CharField(max_length=300, null=True, verbose_name='Anons:')),
                ('article_type', models.CharField(default='Новость', max_length=50, verbose_name='Article type:')),
                ('article_type_ru', models.CharField(default='Новость', max_length=50, null=True, verbose_name='Article type:')),
                ('article_type_en', models.CharField(default='Новость', max_length=50, null=True, verbose_name='Article type:')),
                ('text', models.TextField(max_length=5000, verbose_name='Article:')),
                ('text_ru', models.TextField(max_length=5000, null=True, verbose_name='Article:')),
                ('text_en', models.TextField(max_length=5000, null=True, verbose_name='Article:')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Articles/2023-02-03/', verbose_name='Article photo:')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('views', models.IntegerField(default=0, verbose_name='Views:')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created:')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated:')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='ArticleViewersData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(default='45.243.82.169', verbose_name='Viewer IP:')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.articles')),
            ],
            options={
                'verbose_name': 'Viewers Data',
                'verbose_name_plural': 'Viewers Data',
            },
        ),
    ]