import django_filters
from django import forms
from .models import Conference, Country, EventStatus, ParticipantStatus

myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})


class ConferenceFilter(django_filters.FilterSet):
    naimenovanie = django_filters.CharFilter(field_name='naimenovanie', lookup_expr='icontains')
    strana = django_filters.ModelMultipleChoiceFilter(field_name='strana',
                                                      queryset=Country.objects.all())
    status_meropriatia = django_filters.ModelMultipleChoiceFilter(field_name='status_meropriatia',
                                                                  queryset=EventStatus.objects.all())
    status_uchastnikov = django_filters.ModelMultipleChoiceFilter(field_name='status_uchastnikov',
                                                                  queryset=ParticipantStatus.objects.all())
    data_podachi_gte = django_filters.DateFilter(field_name='data_podachi', lookup_expr='gte')
    data_podachi_lte = django_filters.DateFilter(field_name='data_podachi', lookup_expr='lte')
    data_provedenia_gte = django_filters.DateFilter(field_name='data_provedenia', lookup_expr='gte')
    data_provedenia_lte = django_filters.DateFilter(field_name='data_provedenia', lookup_expr='lte')

    class Meta:
        model = Conference
        fields = []
