<<<<<<< HEAD
from django.shortcuts import render

=======
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from gestao.models import Product, Category
from urllib.parse import quote
from django.http import JsonResponse
import json
>>>>>>> 2e3be4ad8a2fed32f82ed14cd9f4813c7e1e22e2

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

    
    

