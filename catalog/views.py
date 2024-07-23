from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, BlogPost, Version, Category
from catalog.send_email import send_email
from catalog.services import get_categories, get_products


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        active_version = Version.objects.filter(is_current=True)
        context_data['active_version'] = active_version
        context_data['product_list'] = get_products()
        return context_data


class ContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            print(name, email, phone)
        return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        versions = Version.objects.filter(is_current=True, product=Product.objects.get(pk=self.object.pk))
        if len(versions) > 1:
            form.add_error(None, 'У продукта не может быть более одной активной версии.')
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.author:
            return ProductForm
        if user.has_perms(['catalog.can_cancel_publication', 'catalog.can_edit_description', 'catalog.can_edit_category']):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


class CategoryView(ListView):
    model = Category

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['category_list'] = get_categories()
        return context_data


class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = BlogPost
    fields = ('name', 'body', 'preview', 'is_published',)
    permission_required = 'catalog.add_blogpost'
    success_url = reverse_lazy('catalog:blog')

    def form_valid(self, form):
        self.object = form.save()
        if form.is_valid():
            post = form.save()
            post.slug = slugify(post.name)
            post.save()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


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

        if self.object.views_count == 100:
            obj = self.object
            send_email(obj)

        return self.object


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = BlogPost
    permission_required = 'catalog.change_blogpost'
    fields = ('name', 'body', 'preview', 'is_published',)

    def form_valid(self, form):
        if form.is_valid():
            post = form.save()
            post.slug = slugify(post.name)
            post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:post', args=[self.kwargs.get('pk')])


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('catalog:blog')
    permission_required = 'catalog.delete   _blogpost'
