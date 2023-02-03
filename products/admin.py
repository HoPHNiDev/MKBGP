from django.contrib import admin
from .models import Products, ProductsCategory
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from django.utils.safestring import mark_safe


class ProductsAdmin(SummernoteModelAdmin, TranslationAdmin):
    list_display = ('__str__', 'get_image', 'category',
                    'created_at', 'updated_at', 'hasDescription', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('__str__', 'description', 'details')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('get_image',)

    summernote_fields = ('description', 'details')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="100px"')

    get_image.short_description = "Image"


admin.site.register(Products, ProductsAdmin)


class ProductsInline(admin.StackedInline):
    model = Products
    extra = 0
    fields = ('title', 'photo', 'status')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="100px"')

    get_image.short_description = "Image:"


class ProductsCategoryAdmin(SummernoteModelAdmin, TranslationAdmin):
    list_display = ('__str__', 'slug', 'text', 'get_image', 'status')
    list_filter = ['status']
    search_fields = ('__str__', 'text')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductsInline]

    summernote_fields = ('text')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="100px"')

    get_image.short_description = "Image:"


admin.site.register(ProductsCategory, ProductsCategoryAdmin)
