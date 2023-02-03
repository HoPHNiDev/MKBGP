from django import template

from ..models import Articles

register = template.Library()


@register.simple_tag
def get_last_article():

    article = Articles.objects.order_by('-id')[:1]

    return article


@register.simple_tag
def article_or_not(url, language):
    slug = url.split('/')[-1]
    if language == 'ru':
        return Articles.objects.filter(slug_ru=slug).exists()
    elif language == 'en':
        return Articles.objects.filter(slug_en=slug).exists()
    else:
        return False


@register.simple_tag
def get_article_slug(url, language):
    slug = url.split('/')[-1]
    if language == 'ru':
        article = Articles.objects.get(slug_ru=slug)
        return url.split(f'/{language}/')[1].replace(slug, article.slug_en)
    elif language == 'en':
        article = Articles.objects.get(slug_en=slug)
        return url.split(f'/{language}/')[1].replace(slug, article.slug_ru)
