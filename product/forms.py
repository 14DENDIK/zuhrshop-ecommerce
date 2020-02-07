from django import forms
from .models import Phone, Accessory, ProductImage, Product
from brands.models import Brand

class MyCustomModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class GeneralProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Galaxy S100',
        'type': 'text'
    }))
    price = forms.DecimalField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '1234.32',
        'step': "0.01",
        'type': 'number'
    }))
    is_on_sale = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
        'type': 'checkbox',
    }))
    on_sale_price = forms.DecimalField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'On Sale Price',
        'step': "0.01",
        'type': 'number',
        'disabled': 'disabled'
    }))
    is_available = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
        'type': 'checkbox',
    }))
    main_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'class': 'form-control-file',
        'type': 'file'
    }))

    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'is_on_sale',
            'on_sale_price',
            'is_available',
            'main_image'
        ]


class PhoneCreationForm(GeneralProductForm):
    condition = forms.ChoiceField(choices=Phone.Condition.choices ,widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    ram = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': '4',
        'type': 'number'
    }))
    memory = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': '32',
        'step': "0.01",
        'type': 'number'
    }))
    camera = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': '12',
        'type': 'number'
    }))
    screen_dimension = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': '4.12',
        'step': "0.01",
        'type': 'number'
    }))
    screen = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Gorilla',
        'type': 'text'
    }))
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(),
                                   widget=forms.Select(attrs={
                                                    'class': 'form-control'
                                                    }))

    class Meta:
        model = Phone
        fields = [
            'name', 'price', 'is_on_sale', 'on_sale_price', 'is_available',
            'main_image', 'condition', 'ram', 'memory', 'camera',
            'screen_dimension', 'screen', 'brand']


class AccessoryCreationForm(GeneralProductForm):
    phone = MyCustomModelMultipleChoiceField(queryset=Phone.objects.all(),
                                           widget=forms.SelectMultiple(attrs={
                                                'class': 'form-control'
                                           }))
    material = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Leather',
        'type': 'text'
    }))

    class Meta:
        model = Accessory
        fields = [
            'name', 'price', 'is_on_sale', 'on_sale_price', 'is_available',
            'main_image', 'phone', 'material']


ProductImageFormset = forms.modelformset_factory(
            ProductImage,
            fields=('image',),
            extra=4,
            max_num=4,
            widgets={'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})}
            )
