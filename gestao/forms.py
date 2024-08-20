from django import forms
from .models import Product, Category

class EditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'size', 'code']
        labels = {
            'name': 'Nome',
            'size': 'Tamanho',
            'code': 'Código',
        }
        error_messages = {
            'name': {
                'unique': 'Um produto com este nome já existe.',
            },
            'code': {
                'unique': 'Um produto com este código já existe.',
            }
        }

class EditFormCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Nome da Categoria',
        }
        error_messages = {
            'name': {
                'unique': 'Uma categoria com este nome já existe.',
            }
        }