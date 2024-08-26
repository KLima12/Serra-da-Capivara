from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class EmailForm(forms.Form):
    email = forms.CharField(label='email:', max_length=50)
    password = forms.CharField(label='senha:', widget=forms.PasswordInput)
    
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