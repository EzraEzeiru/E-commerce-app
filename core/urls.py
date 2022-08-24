from django.urls import path
from .views import item_list, products_view, checkout_view

app_name = "core"

urlpatterns = [
    path('', item_list, name='item-list'),
    path('checkout', checkout_view, name='checkout'),
    path('products', products_view, name='products')
]