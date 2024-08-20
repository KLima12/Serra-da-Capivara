from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Product
from .forms import EditForm, EditFormCategory, ProductForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from PIL import Image
import io
import os
from django.conf import settings


def home(request):
    return render(request, 'home.html')

from django.core.files.storage import default_storage
from django.shortcuts import redirect, render
from .forms import ProductForm
from .models import Category, Product

def cadastro(request):
    categories = Category.objects.all().order_by('name')

    category_id = request.GET.get('category_id')
    initial_category = None
    if category_id:
        try:
            initial_category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            initial_category = None

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            photos = []

            if 'photos[]' in request.FILES:
                for index, photo in enumerate(request.FILES.getlist('photos[]')):
                    image = Image.open(photo)
                    image = image.convert('RGB') 

                    filename, _ = os.path.splitext(photo.name)
                    new_filename = f"img-{product.name.replace(' ', '-')}-{index+1}.jpg"

                    in_memory_file = io.BytesIO()
                    image.save(in_memory_file, format='WEBP')
                    in_memory_file.seek(0)

                    path = default_storage.save(f'produtos_fotos/{new_filename}', ContentFile(in_memory_file.read(), new_filename))
                    photos.append(path)

            product.photos = photos
            product.save()

            return redirect('galeria')
    else:
        form = ProductForm(initial={'category': initial_category})

    return render(request, 'cadastro.html', {'form': form, 'categories': categories})

    

def galeria(request):
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

    return render(request, 'galeria.html', context)

def confirmacaoProduto(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('galeria') 

    return render(request, 'confirmarProduto.html', {'product': product})

def confirmacaoCategoria(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('galeria') 

    return render(request, 'confirmarCategoria.html', {'category': category})

def editar(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = EditForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('galeria') 
    else:
        form = EditForm(instance=product)
    
    return render(request, 'editar.html', {'form': form, 'product': product})

def cadastroCategoria(request):
    if request.method == 'POST':
        form = EditFormCategory(request.POST,)
        if form.is_valid():
            form.save()
            return redirect('galeria') 
    else:
       form = EditFormCategory()

    return render(request, 'cadastroCategoria.html', {'form': form})


