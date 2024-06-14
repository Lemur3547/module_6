from django.urls import path

from catalog.views import index, contacts, product, add_product

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product, name='name_url'),
    path('add_product/', add_product, name='add_product')
]
