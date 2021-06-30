from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Address(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    house_no = models.PositiveSmallIntegerField()
    street = models.CharField(max_length=30)
    area = models.CharField(max_length=30)


class Discount(models.Model):
    discount_choices = (
        ('p', 'Percent'),
        ('a', 'Amount'), 
    )
    name = models.CharField(max_length=50)
    discount_type = models.CharField(max_length=1 , choices=discount_choices)
    discount = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class Categorie(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    discount = models.ForeignKey(Discount , on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000 , default="")
    discount = models.ForeignKey(Discount , on_delete=models.DO_NOTHING , default=2)
    category = models.ForeignKey(Categorie , on_delete=models.DO_NOTHING , default=1)

    def __str__(self):
        return self.name

    

class Product_attributes(models.Model):
    size_units = (
        ('ml', 'Millilitre'),
        ('l', 'Litre'),
        ('gm', 'Gram'),
        ('kg', 'Kilogram'),
       
    )
    product_id = models.ForeignKey(Product , on_delete=models.CASCADE)
    product_size = models.PositiveSmallIntegerField()
    size_unit = models.CharField(max_length=2 , choices=size_units)
    price = models.DecimalField(max_digits=8 , decimal_places=2 , default=0.00)

    def __str__(self):
        return self.product_id.name + " " + str(self.product_size) + self.size_unit





class Order(models.Model):
    order_status = (
        ('Y', 'Shipped'),
        ('N', 'Not Shipped'),
       
    )
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    shipped = models.CharField(max_length=1 , choices=order_status)
    datetime_ordered = models.DateTimeField()
    datetime_shipped = models.DateTimeField()

class Item(models.Model):
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product_attributes , on_delete=models.CASCADE , default="")

    
class Cart(models.Model):
    user = models.ForeignKey(Customer , on_delete=models.CASCADE)
    