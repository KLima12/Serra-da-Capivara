from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home/', views.inicio, name='inicio'),
    path('categorias/', views.categorias, name='categorias'),
    path('produtos/<int:category_id>/', views.produtos, name='produtos'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('get-cart-items/', views.get_cart_items, name='get_cart_items'),
    path('save_cart/', views.save_cart, name='save_cart'),
    path('message/', views.message, name='message'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


