from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Product_attributes)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Address)
admin.site.register(Discount)
admin.site.register(Categorie)
admin.site.register(Subcategorie)
admin.site.register(Cart)