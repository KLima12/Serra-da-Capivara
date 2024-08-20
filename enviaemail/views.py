from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# funcao da informacao do email


def envia_email(request):
    # Assunto : Conteudo : Email ativo : Email passivo
    send_mail('****Assunto: ****', '**** Conteudo do email ****',
              'contato.adealencar@mail.com', ['dinhoalencaraa@gmail.com'])
    return HttpResponse('*email enviado*')


# LEMBRAR DE TROCAR OS EMAILS
