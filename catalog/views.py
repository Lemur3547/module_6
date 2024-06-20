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

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class PostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostUpdateView(UpdateView):
    model = BlogPost
    fields = ('name', 'body', 'preview', 'is_published',)
    success_url = reverse_lazy('catalog:blog')


class PostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('catalog:blog')
