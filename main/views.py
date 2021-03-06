from django.shortcuts import render
from .models import Product, Specification


def index(request):
    return render(request, 'main/index.html')

def catalog(request):
    product = Product.objects.all()
    return render(request, 'main/catalog.html', {'product': product})

def contacts(request):
    return render(request, 'main/contacts.html')


def item(response, item_slug):
    item = Product.objects.get(slug = item_slug)
    specific = Specification.objects.get(product = item.id)
    return render(response, 'main/item_base.html', {'item': item,'specific': specific})