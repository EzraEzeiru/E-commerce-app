from django.urls import path
from .views import ItemsView, ItemDetailView, checkout_view, add_to_cart, remove_from_cart, home_page_view

app_name = "core"

urlpatterns = [
    path('', home_page_view, name='home'),
    path('products', ItemsView.as_view(), name='products'),
    path('checkout', checkout_view, name='checkout'),
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>', remove_from_cart, name='remove-from-cart')
]