from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login as auth_login
from .forms import EmailForm


def envia_email(request):
    # Assunto : Conteudo : Email ativo : Email passivo
    send_mail('****Assunto: ****', '**** Conteudo do email ****',
              'contato.adealencar@mail.com', ['dinhoalencaraa@gmail.com'])
    return HttpResponse('O email foi enviado. ')
    # LEMBRAR DE TROCAR OS EMAILS


def formulario(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            auth_login(request, user)
            return redirect('enviaemail')
    else:
        form = EmailForm()
    return render(request, 'formulario.html', {'form': form})
