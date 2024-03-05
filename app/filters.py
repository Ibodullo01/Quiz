import django_filters
from .models import Result
from django.forms import  DateInput


class ResultFilter(django_filters.FilterSet):
    score_gt = django_filters.NumberFilter(field_name='score' , lookup_expr='gt')
    score_lt = django_filters.NumberFilter(field_name='score' , lookup_expr='lt')
    date_gt = django_filters.DateFilter(field_name='created_at', lookup_expr='gt' , widget = DateInput( attrs={'type':'date'}))
    date_lt = django_filters.DateFilter(field_name='created_at', lookup_expr='lt', widget = DateInput( attrs={'type':'date'}))
    class Meta:
        model = Result
        fields = ['user__phone' , 'score_gt' , 'score_lt' , 'date_gt' , 'date_lt']