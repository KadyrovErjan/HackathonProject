'''from .models import Product
from modeltranslation.translator import TranslationOptions,register

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')(example)
'''


'''from django.contrib import admin
from .models import Product
from modeltranslation.admin import TranslationAdmin

class ImageInlines(admin.TabularInline):
    model = Images
    extra = 1

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [ImageInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
'''