from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        print(name, email, phone)
    return render(request, 'main/contacts.html')
