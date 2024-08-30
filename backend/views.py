from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from gestao.models import Product, Category
from urllib.parse import quote
from django.http import JsonResponse
from django.core.serializers import serialize
import json

def inicio(request):
    return render(request, 'inicio.html')

def produtos(request):
    categories = Category.objects.all().order_by('name')
    products = Product.objects.all()
    category_products = {
        category: Product.objects.filter(category=category).order_by('name')
        for category in categories
    }

    context = {
        'categories': categories,
        'products': products,
        'category_products': category_products,
    }

    return render(request, 'produtos.html', context)


def carrinho(request):
    categories = Category.objects.all().order_by('name')
    products = Product.objects.all()
    category_products = {
        category: Product.objects.filter(category=category).order_by('name')
        for category in categories
    }

    cart = []
    if request.method == 'POST':
        data = json.loads(request.body)
        cart = data.get('cart', [])

    if request.method == 'GET':
        cart = [] 

    products_data = [
        {
            "pk": product.pk,
            "fields": {
                "name": product.name,
                "code": product.code,
                "size": product.size,
                "views": product.views,
            }
        }
        for product in products
    ]

    context = {
        'categories': categories,
        'products_json': json.dumps(products_data), 
        'category_products': category_products,
        'cart': cart
    }

    return render(request, 'carrinho.html', context)



def get_cart_items(request):
    if request.method == "POST":
        data = json.loads(request.body)
        cart_items = data.get('cart', [])
        product_ids = [item['id'] for item in cart_items]
        products = Product.objects.filter(id__in=product_ids)

        products_data = []
        for product in products:
            cart_item = next((item for item in cart_items if item['id'] == product.id), None)
            products_data.append({
                'id': cart_item['id'],
                'name': product.name,
                'code': product.code,
                'size': product.size,
                'views': product.views,
                'photos': [photo.url for photo in product.photos.all()],
                'quantity': cart_item['quantity'] if cart_item else 0,
            })

        return JsonResponse({'products': products_data})

    return JsonResponse({'error': 'Invalid request method'}, status=400)

    


def save_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cart = data.get('cart', [])
        request.session['cart'] = cart 
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failure'}, status=400)

def message(request):
    cart = request.session.get('cart', []) 
    if not cart:
        return redirect('produtos')  

    message_lines = ["Olá, eu estou interessado(a) nos seguintes produtos:"]

    for item in cart:
        product = get_object_or_404(Product, id=item['id'])
        name = product.name
        code = product.code
        quantity = item['quantity']
        nome_codificado = quote(name)
        codigo_codificado = quote(code)

        message_lines.append(f"•{quantity}x {nome_codificado} ({codigo_codificado})")

    message_text = "%0A".join(message_lines)
    whatsapp_url = f"https://wa.me/5581983664652?text={message_text}"

    return redirect(whatsapp_url)

    
    

