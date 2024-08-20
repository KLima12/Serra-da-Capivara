from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('galeria/', views.galeria, name='galeria'),
    path('confirmacao/<int:product_id>/', views.confirmacao, name='confirmacao'),
    path('editar/<int:product_id>/', views.editar, name='editar'),
]