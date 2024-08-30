from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('produtos/', views.produtos, name='produtos'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('get-cart-items/', views.get_cart_items, name='get_cart_items'),
    path('save_cart/', views.save_cart, name='save_cart'),
    path('message/', views.message, name='message'),
]
