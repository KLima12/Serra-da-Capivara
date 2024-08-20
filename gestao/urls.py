from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('galeria/', views.galeria, name='galeria'),
]