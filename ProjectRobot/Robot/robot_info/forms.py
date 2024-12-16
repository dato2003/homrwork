from django import forms
from .models import Robot

class RobotForm(forms.ModelForm):
    class Meta:
        model = Robot
        fields = ['name', 'last_name', 'email', 'intelligence']
