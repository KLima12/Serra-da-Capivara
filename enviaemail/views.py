from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContatoEmail


def formulario(request):
    form = ContatoEmail()
    return render(request, 'formulario.html', {'form': form})


def processaremail(request):
    form = ContatoEmail(request.POST)
    if form.is_valid():
        nome = form.data['nome']
        email = form.data['email']
        assunto = form.data['assunto']
        mensagem = form.data['mensagem']

    send_mail(
        assunto,
        f"Mensagem de {nome} \nEmail: {email} \nMensagem: {mensagem}",
        'contato.adealencar@gmail.com',
        ['dinhoalencaraa@gmail.com', email],
        fail_silently=False,  # para o codigo nao falhar "silenciosamente"
    )
    return HttpResponse('Email enviado com sucesso.')
