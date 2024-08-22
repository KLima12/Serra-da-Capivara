from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Product
from .forms import EditForm, EditFormCategory, ProductForm, CategoryForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from PIL import Image
import io
import os
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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
                    new_filename = f"img-{product.name.replace(' ', '-')}-{index+1}.webp"

                    in_memory_file = io.BytesIO()
                    image.save(in_memory_file, format='WEBP')
                    in_memory_file.seek(0) 

                    path = default_storage.save(f'produtos_fotos/{new_filename}', ContentFile(in_memory_file.read(), new_filename))
                    photos.append(path)

            product.photos = photos
            product.save()
            messages.success(request, 'Produto adicionado com sucesso!')
        
            return redirect('cadastro')
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
        for photo_path in product.photos:
            if default_storage.exists(photo_path):
                default_storage.delete(photo_path)
        
        product.delete()
        return redirect('galeria')

    return render(request, 'confirmarProduto.html', {'product': product})


def confirmacaoCategoria(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        if category.photo:
            photo_path = category.photo.name
            if default_storage.exists(photo_path):
                default_storage.delete(photo_path)

        category.delete()
        return redirect('galeria') 

    return render(request, 'confirmarCategoria.html', {'category': category})


def editar(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = EditForm(request.POST, instance=product)
        if form.is_valid():
            form.save()

            if 'photo_order' in request.POST:
                photo_order = json.loads(request.POST['photo_order'])
                product.photos = photo_order
                product.save()

            if 'removed_photos' in request.POST:
                removed_photos = json.loads(request.POST['removed_photos'])
                for photo in removed_photos:
                    if default_storage.exists(photo):
                        default_storage.delete(photo)
                product.photos = [p for p in product.photos if p not in removed_photos]
                product.save()

            if 'photos[]' in request.FILES:
                photos = product.photos if product.photos else []
                for index, photo in enumerate(request.FILES.getlist('photos[]')):
                    image = Image.open(photo)
                    image = image.convert('RGB')

                    filename, _ = os.path.splitext(photo.name)
                    new_filename = f"img-{product.name.replace(' ', '-')}-{len(photos) + index + 1}.webp"

                    in_memory_file = io.BytesIO()
                    image.save(in_memory_file, format='WEBP')
                    in_memory_file.seek(0)

                    path = default_storage.save(f'produtos_fotos/{new_filename}', ContentFile(in_memory_file.read(), new_filename))
                    photos.append(path)
                product.photos = photos
                product.save()

            return redirect('galeria')
    else:
        form = EditForm(instance=product)
    
    return render(request, 'editar.html', {'form': form, 'product': product})


def editarCategoria(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        form = EditFormCategory(request.POST, instance=category)
        if form.is_valid():
            form.save()

            if 'photo' in request.FILES:
                if category.photo:
                    photo_path = category.photo.name
                    if default_storage.exists(photo_path):
                        default_storage.delete(photo_path)

                photo = request.FILES['photo']
                image = Image.open(photo)
                image = image.convert('RGB') 

                new_filename = f"img-{category.name.replace(' ', '-')}.webp"
                in_memory_file = io.BytesIO()
                image.save(in_memory_file, format='WEBP')
                in_memory_file.seek(0)

                path = default_storage.save(f'categorias_fotos/{new_filename}', ContentFile(in_memory_file.read(), new_filename))
                category.photo = path

            category.save()
            return redirect('galeria')
    else:
        form = EditFormCategory(instance=category)

    return render(request, 'editarCategoria.html', {'form': form, 'category': category})



@csrf_exempt
def remove_photo(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        photo_path = data.get('photo')
        if photo_path:
            full_path = os.path.join('produtos_fotos', photo_path)
            if default_storage.exists(full_path):
                default_storage.delete(full_path)
                return JsonResponse({'success': True})
        return JsonResponse({'success': False}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


def cadastroCategoria(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                image = Image.open(photo)
                image = image.convert('RGB') 

                new_filename = f"img-{category.name.replace(' ', '-')}.webp"
                in_memory_file = io.BytesIO()
                image.save(in_memory_file, format='WEBP')
                in_memory_file.seek(0)

                path = default_storage.save(f'categorias_fotos/{new_filename}', ContentFile(in_memory_file.read(), new_filename))
                category.photo = path

            category.save()
            return redirect('galeria')
    else:
        form = CategoryForm()
    
    return render(request, 'cadastroCategoria.html', {'form': form})
