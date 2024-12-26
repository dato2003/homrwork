# santa_list/forms.py
from django import forms
from .models import Kid , SantaList

class KidForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = ['name', 'niceness_coefficient', 'gift']

