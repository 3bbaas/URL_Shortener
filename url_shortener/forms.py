from django import forms
from .models import shorten

class get_url(forms.ModelForm):
    class Meta:
        model = shorten
        fields = ['url']
