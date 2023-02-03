from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Articles


class ArticlesSummernoteForm(forms.Form):
    text = forms.CharField(
        'Article', widget=SummernoteWidget(), max_length=5000)
    text_ru = forms.CharField(
        'Article', widget=SummernoteWidget(), max_length=5000)
    text_en = forms.CharField(
        'Article', widget=SummernoteWidget(), max_length=5000)


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'article_type', 'text', 'photo']
        widgets = {
            'text': SummernoteWidget()
        }


def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field,
                                   'label') else 'Error', error)
    return msg
