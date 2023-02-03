from django.contrib import admin
from .models import Articles, ArticleViewersData
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin
from django.utils.safestring import mark_safe


class ViewerDataInline(admin.StackedInline):
    model = ArticleViewersData
    extra = 0
    fields = ('ip_address',)


class ArticlesAdmin(SummernoteModelAdmin, TranslationAdmin):
    list_display = ('__str__', 'article_type', 'get_image',
                    'created_at', 'updated_at', 'views', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('__str__', 'text')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ViewerDataInline,]

    summernote_fields = ('text')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="100px"')

    get_image.short_description = "Image:"


admin.site.register(Articles, ArticlesAdmin)


class ArticleViewersDataAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'ip_address')
    search_fields = ('__str__', 'ip_address')


admin.site.register(ArticleViewersData, ArticleViewersDataAdmin)
