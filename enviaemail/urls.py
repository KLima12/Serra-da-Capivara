from django.urls import path
from . import views

urlpatterns = [
    path('enviaemail/', views.envia_email, name='enviar-email'),
    path('formulario/', views.formulario, name='formulario-email'),
    path('processaformulario/', views.processa_formulario,
         name='processa-formulario'),


]
