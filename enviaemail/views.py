from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# funcao da informacao do email


def envia_email(request):
    send_mail('Assunto: ', 'Esse e o email teste!',
              'contato.adealencar@mail.com', ['dinhoalencaraa@gmail.com'])
    return HttpResponse('ola')
