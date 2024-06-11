from django.db.models import Model
from django.shortcuts import render

from catalog.models import Product


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
