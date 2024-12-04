from django import forms
from django.core.exceptions import ValidationError
import re

def validate_phone_number(value):
    digits = re.sub(r'\D', '', value)

    if len(digits) not in [8, 9, 10, 11]:
        raise ValidationError('Número Inválido')

    if len(digits) == 8:
        value = f"{digits[:4]}-{digits[4:]}"
    elif len(digits) == 9:
        value = f"{digits[:5]}-{digits[4:]}"
    elif len(digits) == 10:
        value = f"({digits[:2]}) {digits[2:6]}-{digits[6:]}"
    elif len(digits) == 11:
        value = f"({digits[:2]}) {digits[2:7]}-{digits[7:]}"

    return value

class ContatoEmail(forms.Form):
    nome = forms.CharField(
        max_length=50, 
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Nome", "class":"f1"})
    )
    celular = forms.CharField(
        label="Celular", 
        validators=[validate_phone_number],
        widget=forms.TextInput(attrs={"id": "celular-input", "maxlength": "19", "inputmode": "numeric", "placeholder": "Celular", "class":"f1"})
    )
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Email", "class":"f2"})
    )
    assunto = forms.CharField(
        max_length=100,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Assunto", "class":"f2"})
    )
    mensagem = forms.CharField(
        max_length=2500, 
        label="",
        widget=forms.Textarea(attrs={"placeholder": "Sua Mensagem", "class":"f3"})
    )


    
        