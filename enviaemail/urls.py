from django.urls import path
from . import views

urlpatterns = [
    #path('enviaemail/', views.enviar_email, name='enviar-email'),
    path('formulario/', views.formulario, name='formulario-email'),
    path('processaremail/', views.processaremail,
         name='processar-email'),

]
