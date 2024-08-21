from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('galeria/', views.galeria, name='galeria'),
    path('confirmacaoProduto/<int:product_id>/', views.confirmacaoProduto, name='confirmacaoProduto'),
    path('confirmacaoCategoria/<int:category_id>/', views.confirmacaoCategoria, name='confirmacaoCategoria'),
    path('cadastroCategoria/', views.cadastroCategoria, name='cadastroCategoria'),
    path('editar/<int:product_id>/', views.editar, name='editar'),
    path('editarCategoria/<int:category_id>/', views.editarCategoria, name='editarCategoria'),
    path('remove-photo/', views.remove_photo, name='remove_photo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)