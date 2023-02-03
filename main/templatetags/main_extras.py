from django import template
register = template.Library()


@register.simple_tag
def split_url(url, language):
    return url.split(f'/{language}/')[1]
