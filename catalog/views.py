from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView

from catalog.models import Product, BlogPost


class ProductListView(ListView):
    model = Product


class ContactsView(View):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            print(name, email, phone)
        return render(request, 'catalog/contacts.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        print(name, email, phone)
    return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'preview', 'category', 'price')
    success_url = reverse_lazy('catalog:index')


class PostCreateView(CreateView):
    model = BlogPost
    fields = ('name', 'body', 'preview', 'is_published',)
    success_url = reverse_lazy('catalog:blog')


class PostListView(ListView):
    model = BlogPost


class PostDetailView(DetailView):
    model = BlogPost


class PostUpdateView(UpdateView):
    model = BlogPost
    fields = ('name', 'body', 'preview', 'is_published',)
    success_url = reverse_lazy('catalog:blog')


class PostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('catalog:blog')
