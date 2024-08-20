from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'size', 'code']
        labels = {
            'name': 'Nome',
            'size': 'Tamanho',
            'code': 'Código',
        }
