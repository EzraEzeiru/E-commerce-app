from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Item, OrderItem, Order
from django.utils import timezone
from django.contrib import messages

# Create your views here.


def checkout_view(request):
    return render(request, 'checkout-page.html')


class ItemsView(ListView):
    model = Item
    template_name = "items-page.html"


def home_page_view(request):
    return render(request, 'home.html')


class ItemDetailView(DetailView):
    model = Item
    template_name = 'product-page.html'


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item,
                                                 user=request.user,
                                                 ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")
        else:
            messages.info(request, "This item was added to you cart")
            order.items.add(order_item)

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user,
                                     ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to you cart")
    return redirect("core:product", slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item,
                                                  user=request.user,
                                                  ordered=False)[0]
            order.items.remove(order_item)
            messages.info(request, "This item removed from your cart")
        else:
            # add message saying order does not contain this item
            messages.info(request, "This item is not in your cart")
            return redirect("core:product", slug=slug)

    else:
        # message saying the user does not have an order
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)

    return redirect("core:product", slug=slug)
