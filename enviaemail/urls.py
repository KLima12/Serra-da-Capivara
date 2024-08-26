from django.urls import path
from . import views

urlpatterns = [
    path('enviaemail/', views.envia_email, name='envia_email'),
    path('formulario/', views.formulario, name='formulario'),

]
