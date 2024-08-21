from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'size', 'code', 'category']
        labels = {
            'name': 'Nome',
            'size': 'Tamanho',
            'code': 'Código',
            'category': 'Categoria',
        }
        error_messages = {
            'name': {
                'unique': 'Um produto com este nome já existe.',
            },
            'code': {
                'unique': 'Um produto com este código já existe.',
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['name'].error_messages['required'] = 'Por favor, insira o nome do produto.'

        self.fields['size'].required = True
        self.fields['size'].error_messages['required'] = 'Por favor, insira o tamanho do produto.'

        self.fields['code'].required = True
        self.fields['code'].error_messages['required'] = 'Por favor, insira o código do produto.'

        self.fields['category'].required = True
        self.fields['category'].error_messages['required'] = 'Por favor, insira a categoria do produto.'



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
                'required': 'Por favor, insira o nome do produto',
            },
            'size': {
                'required': 'Por favor, insira o tamanho do produto',
            },
            'code': {
                'unique': 'Um produto com este código já existe.',
                'required': 'Por favor, insira o código do produto',
            },
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'photo']
        labels = {
            'name': 'Nome da Categoria',
            'photo': 'Foto',
        }
        error_messages = {
            'name': {
                'unique': 'Uma categoria com este nome já existe.',
            }
        }

class EditFormCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'photo']
        labels = {
            'name': 'Nome',
            'photo': 'Foto',
        }
        error_messages = {
            'name': {
                'unique': 'Uma categoria com este nome já existe.',
                'required': 'Por favor, insira o nome da categoria',
            },
            'photo': {
                'required': 'Por favor, insira uma foto',
            },
        }