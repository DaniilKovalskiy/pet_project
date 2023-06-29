from django.shortcuts import render
from .models import Product
from django.views.generic import ListView


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    for el in products:
        print(f"{el.name}: {el.price} руб.")
    return render(request, "product_list.html", context)


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
