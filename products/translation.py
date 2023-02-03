from modeltranslation.translator import register, TranslationOptions
from .models import Products, ProductsCategory


@register(Products)
class ProductsTranslationOption(TranslationOptions):
    fields = ['title', 'slug', 'anons', 'description', 'details']


@register(ProductsCategory)
class ProductsCategoryTranslationOption(TranslationOptions):
    fields = ['title', 'slug', 'text']
