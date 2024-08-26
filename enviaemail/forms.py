from django import forms

class EmailForm(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField()
    
        