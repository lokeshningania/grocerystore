from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('list' , views.listproducts , name='listproducts'),
    path('category/<str:cname>' , views.showcategory , name='showcategory'),
    path('category/<str:cname>/<str:pname>' , views.showproduct , name='showproduct')
]