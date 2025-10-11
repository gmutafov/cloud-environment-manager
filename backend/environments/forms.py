from django import forms
from environments.models import Environment


class EnvironmentForm(forms.ModelForm):
    class Meta:
        model = Environment
        fields = ['name', 'description', 'environment_type', 'status']