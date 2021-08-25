from django.db.models import fields
from rest_framework import serializers
from .models import Basket, Customer, Product 

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        #fields=['id','fullname','email','mobile','address']
        fields = '__all__'
    # fullname = serializers.CharField(max_length=100)
    # email = serializers.EmailField(max_length=100)
    # mobile = serializers.CharField(max_length=15)
    # address = serializers.CharField(max_length=100)

    # def create(self, validated_data):
    #     return Customer.objects.create(**validated_data)
    # def update(self, instance, validated_data):
    #     instance.fullname = validated_data.get('fullname', instance.fullname)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.mobile = validated_data.get('mobile', instance.mobile)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.save()
    #     return instance

class ProductSerializer(serializers.ModelSerializer):
     class Meta:
         model = Product
         fields=['product_name','product_id','description','price','created_date']
#         fields = '__all__'
    # product_name = serializers.CharField(max_length=100)
    # product_id = serializers.CharField(max_length=100)
    # description = serializers.CharField(max_length=100)

    # def create(self, validated_data):
    #     return Product.objects.create(**validated_data)
    # def update(self, instance, validated_data):
    #     instance.product_name = validated_data.get('product_name', instance.product_name)
    #     instance.product_id = validated_data.get('product_id', instance.product_id)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.save()
    #     return instance
class BasketSerializer(serializers.ModelSerializer):
     class Meta:
         model = Basket
         fields=['product_name','product_id','price','created_date']
#         fields = '__all__'