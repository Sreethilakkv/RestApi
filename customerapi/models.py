  
from django.db import models
from django.db.models.fields import DateTimeField, EmailField
from django.db.models.fields.related import ForeignKey
from django.utils import module_loading
from django.utils.translation import activate
import datetime


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

class Product(models.Model):
     product_name = models.CharField(max_length=100)
     product_id = models.IntegerField(primary_key=True)
     description = models.CharField(max_length=100)
     price = models.IntegerField(null=False)
     created_date = models.DateTimeField(auto_now_add=True)


class Basket(models.Model):
     id = models.IntegerField(primary_key=True)
     customer_id = models.ForeignKey(to=Customer,on_delete=models.CASCADE)
     product_id = models.ForeignKey(to=Product,on_delete=models.CASCADE)
     quantity = models.IntegerField(null=False)
     created_date = models.DateTimeField(auto_now_add=True)
     active = models.BooleanField(default=True)

