from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('produtos/', views.produtos, name='produtos'),
    path('form/<int:id>/', views.form, name='form'),
]
