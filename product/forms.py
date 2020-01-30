from django import forms
from .models import Phone, Accessory, ProductImage, Product


class PhoneCreationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name',
        'type': 'text'
    }))
    price = forms.DecimalField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '1234.32',
        'type': 'number'
    }))
    is_on_sale = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
        'placeholder': 'Name',
        'type': 'checkbox'
    }))
    on_sale_price = forms.DecimalField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Sale Price',
        'type': 'number'
    }))
    is_available = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
        'type': 'checkbox'
    }))
    main_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'class': 'form-control-file',
        'type': 'file'
    }))
    condition = forms.ChoiceField(choices=Phone.Condition.choices ,widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    ram = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'RAM',
        'type': 'number'
    }))
    memory = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Memory',
        'type': 'number'
    }))
    camera = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Camera',
        'type': 'number'
    }))
    screen_dimension = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Screen Dimension',
        'type': 'number'
    }))
    screen = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Memory',
        'type': 'text'
    }))

    class Meta:
        model = Phone
        fields = [
            'name', 'price', 'is_on_sale', 'on_sale_price', 'is_available',
            'main_image', 'condition', 'ram', 'memory', 'camera',
            'screen_dimension', 'screen']


ProductImageFormset = forms.modelformset_factory(
            ProductImage,
            fields=('image',),
            extra=4,
            max_num=4,
            widgets={'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})}
            )
