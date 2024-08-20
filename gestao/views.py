from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product, ProductPhoto
from .forms import ProductForm 
from PIL import Image
import os
from django.conf import settings


#Teste de git
def home(request):
    return render(request, 'home.html')

def cadastro(request):
    categories = Category.objects.all()
    if request.method == 'GET':
        return render(request, 'cadastro.html', {'categories':categories})
    elif request.method == 'POST':
        name = request.POST.get('name')
        size = request.POST.get('size')
        code = request.POST.get('code')
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)

        product = Product.objects.create(name=name, size=size, code=code, category=category)

        if 'photos' in request.FILES:
            photos = request.FILES.getlist('photos')
            for photo in photos:
                ProductPhoto.objects.create(product=product, photo=photo)
                
    return HttpResponse('Salvo com sucesso')

def galeria(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    category_products = {category: products.filter(category=category) for category in categories}

    context = {
        'categories': categories,
        'products': products,
        'category_products': category_products,
    }

    return render(request, 'galeria.html', context)

def confirmacao(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('galeria') 

    return render(request, 'confirmar.html', {'product': product})

def editar(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('galeria') 
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'editar.html', {'form': form, 'product': product})

def apagar(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        product.delete()
    return redirect('galeria')  