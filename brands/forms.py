from django import forms
from .models import Brand


class BrandCreationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name',
        'type': 'text'
    }))

    class Meta:
        model = Brand
        fields = ['name',]
