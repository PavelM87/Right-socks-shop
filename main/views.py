from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

def catalog(request):
    return render(request, 'main/catalog.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def classic(request):
    return render(request, 'main/classic.html')

def funeral(request):
    return render(request, 'main/funeral.html')

def cat_face(request):
    return render(request, 'main/cat_face.html')