from django import forms
from .models import leads

class leadmodelform(forms.ModelForm):
    class Meta:
        model  = leads
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
        )

class leadform(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)