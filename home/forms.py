from .models import * 
from django import forms


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        labels = {
            'name':'Name',
            'phone':'Phone',
            'email':'email',
            'address':'address',
            'born':'born',
        }
