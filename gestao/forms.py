from django import forms
from .models import Product, Category
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.html import format_html

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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'edit-label'}),
            'size': forms.TextInput(attrs={'class': 'edit-label'}),
            'code': forms.TextInput(attrs={'class': 'edit-label'}),
            'category': forms.Select(attrs={'class': 'edit-label'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.label:
                field.label = format_html('<span class="input-label">{}</span>', field.label)
                
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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'edit-label'}),
            'size': forms.TextInput(attrs={'class': 'edit-label'}),
            'code': forms.TextInput(attrs={'class': 'edit-label'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.label:
                field.label = format_html('<span class="input-label">{}</span>', field.label)
        

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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'edit-label'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.label:
                field.label = format_html('<span class="input-label">{}</span>', field.label)

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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'edit-label'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.label:
                field.label = format_html('<span class="input-label">{}</span>', field.label)
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Nome do Usúario', max_length=50)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        
        #Autentifica o usuário
        user = authenticate(username=username, password=password)
        
        if user is None:                    
            raise forms.ValidationError("Usuário ou senha errados")
        
        self.cleaned_data['user'] = user
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.label:
                field.label = format_html('<span class="input-label">{}</span>', field.label)