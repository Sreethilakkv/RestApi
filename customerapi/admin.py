from django.contrib import admin
from customerapi.models import  Customer,Product,Basket

class CustomerAdmin(admin.ModelAdmin):
     pass
admin.site.register(Customer)

class ProductAdmin(admin.ModelAdmin):
     pass
admin.site.register(Product)

admin.site.register(Basket)