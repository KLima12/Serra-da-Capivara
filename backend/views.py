from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from gestao.models import Product, Category
from urllib.parse import quote
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


def form(request, id):
    produto = get_object_or_404(Product, id=id)
    name = produto.name
    code = produto.code
    nome_codificado = quote(name)
    codigo_codificado = quote(code)
    messagem = f"{name}, Codigo: {code}"
    whatsapp_url = (
    f"https://wa.me/5581998288213?text="
    f"Olá,%20estou%20interessado%20nos%20seguintes%20produtos:%0A"
    f"-%20{nome_codificado}%20({codigo_codificado})%0A"
    " - Outros%20produtos%20aqui"
)

    return redirect(whatsapp_url)
    
    

