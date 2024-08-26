from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm


def formulario(request):
    form = EmailForm()
    return render(request, 'formulario.html', {'form': form})


def processa_formulario(request):
    form = EmailForm(request.POST)
    return HttpResponse(form)


def envia_email(request):
    # Assunto : Conteudo : Email ativo : Email passivo
    send_mail('****Assunto: ****', '**** Conteudo do email ****',
              'contato.adealencar@mail.com', ['dinhoalencaraa@gmail.com'])
    return HttpResponse('O email foi enviado. ')
    # LEMBRAR DE TROCAR OS EMAILS
