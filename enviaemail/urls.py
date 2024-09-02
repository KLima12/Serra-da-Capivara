from django.urls import path
from . import views
from django.urls import re_path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('formulario/', views.formulario, name='formulario-email'),
    path('processaremail/', views.processaremail, name='processar-email'),
]

urlpatterns += [
    re_path(r'^.*$', RedirectView.as_view(url='formulario/', permanent=False), name='index'),
]