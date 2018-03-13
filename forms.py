from django import forms
from .models import Tutorial


class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        exclude = ('author',)
        widgets = {
            'file': forms.FileInput(attrs={'accept': 'video/*,image/*'}),
        }
