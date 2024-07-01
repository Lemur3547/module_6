from django.contrib import admin

from catalog.models import Category, Product, BlogPost, Version


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'build', 'name', 'is_current',)
    list_filter = ('product', 'build', 'name', 'is_current',)
    search_fields = ('product', 'build', 'name',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    fields = ('name', 'body', 'preview', 'is_published',)
    list_display = ('id', 'name', 'is_published', 'views_count',)
    list_filter = ('is_published', 'views_count', 'name', 'created_at')
    search_fields = ('name', 'body',)
