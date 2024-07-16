from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='previews/', verbose_name='Превью')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, **NULLABLE)
    price = models.IntegerField(verbose_name='Цена')
    author = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'price', 'name']
        permissions = [
            ('can_cancel_publication', 'Может отменять публикацию продукта'),
            ('can_edit_description', 'Может менять описание продукта'),
            ('can_edit_category', 'Может менять категорию продукта')
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    build = models.FloatField(verbose_name='Номер версии')
    name = models.CharField(max_length=100, verbose_name='Название версии', **NULLABLE)
    is_current = models.BooleanField(verbose_name='Текущая версия')

    def __str__(self):
        if self.name:
            return f'{self.name} (v.{self.build})'
        else:
            return f'{self.build}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'


class BlogPost(models.Model):
    name = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.CharField(max_length=255, verbose_name='slug')
    body = models.TextField(verbose_name='Текст')
    preview = models.ImageField(upload_to='blog/previews/', verbose_name='Превью', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
