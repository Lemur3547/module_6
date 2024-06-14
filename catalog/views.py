from django.shortcuts import render

from catalog.models import Product, Category


def index(request):
    context = {
        'products_list': Product.objects.all()
    }
    return render(request, 'main/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        print(name, email, phone)
    return render(request, 'main/contacts.html')


def product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk)
    }
    return render(request, 'main/product.html', context)


def add_product(request):
    context = {
        'category_list': Category.objects.all()
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        preview = request.FILES.get('preview')
        category = request.POST.get('category')
        price = request.POST.get('price')
        Product.objects.create(name=name, description=description, preview=preview, category=Category.objects.get(pk=category), price=price)
    return render(request, 'main/add_product.html', context)
