from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ProductCreateView, contacts

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    # path('contacts/', ContactsView.as_view(), name='contacts'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='name_url'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
]
