from django.shortcuts import render
from .models import Product
from django.views.generic import ListView


def main(request):
    return render(request, 'main/main.html')


def shop(request):
    return render(request, 'main/shop.html')


class ProductListView(ListView):
    model = Product
    template_name = 'main/shop.html'
    context_object_name = 'product_list'
