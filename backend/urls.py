from . import views
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^home/?$', views.inicio, name='inicio'),
    re_path(r'^produtos/?$', views.produtos, name='produtos'),
    re_path(r'^carrinho/?$', views.carrinho, name='carrinho'),
    re_path(r'^get-cart-items/?$', views.get_cart_items, name='get_cart_items'),
    re_path(r'^save_cart/?$', views.save_cart, name='save_cart'),
    re_path(r'^message/?$', views.message, name='message'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

