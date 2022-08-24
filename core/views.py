from django.shortcuts import render
from .models import Item

# Create your views here.


def item_list(request):
    context = {
        "items": Item.objects.all()
    }
    return render(request, "home-page.html", context)


def checkout_view(request):
    return render(request, 'checkout-page.html')


def products_view(request):
    return render(request, 'product-page.html')