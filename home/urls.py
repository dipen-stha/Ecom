from .views import *
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', Categories.as_view(), name = 'category'),
    path('search', SearchView.as_view(), name = 'search'),
    path('product-details/<slug>', DetailView.as_view(), name = 'product-details'),
    path('reviews', review, name = 'reviews'),
    path('signup', signup, name = 'signup'),
    path('add_to_cart/<slug>', add_to_cart, name = 'add_to_cart'),
    path('cart/', CartView.as_view(),name = 'cart'),
    path('remove_cart/<slug>', remove_cart, name='remove_cart'),
    path('delete_cart/<slug>', delete_cart, name='delete_cart'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('add_to_wishlist/<slug>', add_to_wishlist, name='add_to_wishlist'),
    path('delete_wishlist/<slug>', delete_wishlist, name='delete_wishlist'),
]
