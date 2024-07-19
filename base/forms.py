from django.forms import ModelForm
from .models import Conference, Podpiska
from django import forms

myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})


class ConferenceForm(ModelForm):
    class Meta:
        model = Conference
        fields = '__all__'
        widgets = {'data_podachi': myDateInput, 'data_provedenia': myDateInput, 'naimenovanie':
            forms.Textarea(attrs={'class': "form-control"}),
                   'uchregdenie': forms.Textarea(attrs={'class': "form-control"})}


class PodpiskaForm(ModelForm):
    class Meta:
        model = Podpiska
        fields = '__all__'

