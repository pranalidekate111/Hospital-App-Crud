from django import forms
from .models import patient

class patienForm(forms.ModelForm):
    class Meta:
        model = patient
        fields = ['name','age','gender']
