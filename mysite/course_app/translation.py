from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', )


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')


@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title', 'content' )


@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('text', 'name_question')


@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('title', 'questions')



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