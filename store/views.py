from django.http import HttpResponse
from django.shortcuts import render
from .models import Categorie

from math import ceil

def home(request):
    categories = Categorie.objects.all()
    n = len(categories)
    print(categories)
    params = {'range':range(1,n) , 'categories':categories}
    return render(request , 'store/home.html' , params)
    

def listproducts(request):
    return render(request , 'store/listproducts.html')


def showcategory(request , cname):
    return HttpResponse(cname + "is the given category")

def showproduct(request,cname,pname):
    return HttpResponse(pname + " is a product of " + cname + " category")

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
