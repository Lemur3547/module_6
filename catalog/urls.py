from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ProductCreateView, PostCreateView, PostListView, \
    PostDetailView, PostUpdateView, PostDeleteView, ContactsView

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='name_url'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('blog/add_post/', PostCreateView.as_view(), name='add_post'),
    path('blog/', PostListView.as_view(), name='blog'),
    path('blog/post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('blog/edit_post/<int:pk>', PostUpdateView.as_view(), name='edit_post'),
    path('blog/delete_post/<int:pk>', PostDeleteView.as_view(), name='delete_post'),
]
