from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('galeria/', views.galeria, name='galeria'),
    path('confirmacaoProduto/<int:product_id>/', views.confirmacaoProduto, name='confirmacaoProduto'),
    path('confirmacaoCategoria/<int:category_id>/', views.confirmacaoCategoria, name='confirmacaoCategoria'),
    path('cadastroCategoria/', views.cadastroCategoria, name='cadastroCategoria'),
    path('editar/<int:product_id>/', views.editar, name='editar'),
]