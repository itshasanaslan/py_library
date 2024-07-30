from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products':products})

def deneme(request):
    return render(request, "deneme.html")

def new(request):
    return HttpResponse("New Product")
