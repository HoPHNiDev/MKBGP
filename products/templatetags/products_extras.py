from django import template

from ..models import Products

register = template.Library()


@register.simple_tag
def get_products():

    products = Products.objects.filter(status=True).filter(category=2).order_by(
        'id')[0:4]

    return products


@register.simple_tag
def product_or_not(url, language):
    slug = url.split('/')[-1]
    if language == 'ru':
        return Products.objects.filter(slug_ru=slug).exists()
    elif language == 'en':
        return Products.objects.filter(slug_en=slug).exists()
    else:
        return False


@register.simple_tag
def get_product_slug(url, language):
    slug = url.split('/')[-1]
    if language == 'ru':
        product = Products.objects.get(slug_ru=slug)
        return url.split(f'/{language}/')[1].replace(slug, product.slug_en)
    elif language == 'en':
        product = Products.objects.get(slug_en=slug)
        return url.split(f'/{language}/')[1].replace(slug, product.slug_ru)
