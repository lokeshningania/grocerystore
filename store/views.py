from django.http import HttpResponse
from django.shortcuts import render
from .models import Product_attributes , Product

from math import ceil

def home(request):
    product_details = Product_attributes.objects.all()
    n = len(product_details)
    nSlides= n//4+ceil((n/4) - (n//4))
    print(product_details)
    params = {'no_of_slides':nSlides , 'range':range(1,nSlides) , 'products':product_details}
    return render(request , 'store/home.html' , params)
    


def offers(request):
    return render(request , 'store/home.html')

def account(request):
    return render(request , 'store/home.html')

def wallet(request):
    return render(request , 'store/home.html')


def orders(request):
    return render(request , 'store/home.html')

def cart(request):
    return render(request , 'store/home.html')

def checkout(request):
    return render(request , 'store/home.html')
