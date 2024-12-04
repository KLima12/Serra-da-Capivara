from . import views
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView


urlpatterns = [
    path('home/', views.inicio, name='inicio'),
    path('categorias/', views.categorias, name='categorias'),
    re_path(r'produtos/?$', views.produtos, name='produtosDefault'), 
    path('produtos/<int:category_id>/', views.produtos, name='produtos'),
    
    path('produto/<int:category_id>/<int:product_id>/', views.produto, name='produto'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('get-cart-items/', views.get_cart_items, name='get_cart_items'),
    path('save_cart/', views.save_cart, name='save_cart'),
    path('message/', views.message, name='message'),
    path('update-views/<int:product_id>/', views.update_views, name='update_views'),
    path('contatos/', views.formulario, name='formulario-email'),
    path('processaremail/', views.processaremail, name='processar-email'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^.*$', RedirectView.as_view(url='home/', permanent=False), name='index'),
]

