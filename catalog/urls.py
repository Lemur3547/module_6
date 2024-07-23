from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.views import ProductListView, ProductDetailView, ProductCreateView, PostCreateView, PostListView, \
    PostDetailView, PostUpdateView, PostDeleteView, ContactsView, ProductUpdateView, ProductDeleteView, CategoryView

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('add_product/', never_cache(ProductCreateView.as_view()), name='add_product'),
    path('edit_product/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='edit_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

    path('categories/', CategoryView.as_view(), name='categories'),

    path('blog/', PostListView.as_view(), name='blog'),
    path('blog/post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('blog/add_post/', never_cache(PostCreateView.as_view()), name='add_post'),
    path('blog/edit_post/<int:pk>', never_cache(PostUpdateView.as_view()), name='edit_post'),
    path('blog/delete_post/<int:pk>', PostDeleteView.as_view(), name='delete_post'),
]
