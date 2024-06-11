from django.urls import path

from catalog.views import index, contacts, product

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('product/<int:pk>/', product, name='name_url')
]
