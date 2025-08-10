import django_filters
from .models import *
from django_filters import FilterSet


class CourseFilter(FilterSet):
     class Meta:
        model = Course
        fields = {
             'category': ['exact'],
             'level': ['exact'],
             'price_type': ['exact'],
             'price': ['gt', 'lt'],
        }