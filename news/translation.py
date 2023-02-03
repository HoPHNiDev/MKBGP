from modeltranslation.translator import register, TranslationOptions
from .models import Articles


@register(Articles)
class ArticleTranslationOption(TranslationOptions):
    fields = ['title', 'slug', 'anons', 'article_type', 'text']
