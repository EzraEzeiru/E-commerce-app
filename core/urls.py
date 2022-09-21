from django.urls import path
from .views import (ItemsView, ItemDetailView, CheckoutView,
                    add_to_cart, remove_from_cart, home_page_view,
                    OrderSummaryView, remove_single_item_from_cart)

app_name = "core"

urlpatterns = [
    path('', home_page_view, name='home'),
    path('products/', ItemsView.as_view(), name='products'),
    path('order-summary/', OrderSummaryView.as_view(), name="order-summary"),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>', remove_from_cart, name='remove-from-cart'),
    path("remove-single-item-from-cart/<slug>", remove_single_item_from_cart, name="remove-item-from-cart")
]