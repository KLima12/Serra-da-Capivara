from django import forms

class ContatoEmail(forms.Form):
    nome = forms.CharField(max_length=50, label="Nome")
    email = forms.EmailField(label="Email")
    assunto = forms.CharField(max_length=100,label="Assunto")
    mensagem = forms.CharField(widget=forms.Textarea, label="Mensagem")


    
        