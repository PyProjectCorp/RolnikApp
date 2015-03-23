from django import forms
from .models import Animals

class AnimalsForm(forms.ModelForm):
    class Meta:
        model = Animals
        fields = ('oznaczenie', 'typ', 'old', 'weight', 'price', 'user')