import django_filters
from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter
from django.forms import DateInput
from .models import Post, Category


class PostFilter(FilterSet):
    model = Post
    add_title = CharFilter(
        field_name='title',
        lookup_expr='iregex',
        label='Заголовок'
    )
    date = DateFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Дата',
        widget=DateInput(
            attrs={'type': 'date'},
        ),
    )
    add_category = ModelChoiceFilter(
        field_name='postcategory__categoryThrough',
        queryset=Category.objects.all(),
        label='Категория поста',
        empty_label='all'
    )
