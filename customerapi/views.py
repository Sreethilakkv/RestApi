from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .models import Customer,Product,Basket
from .serializer import CustomerSerializer,ProductSerializer,BasketSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response, responses
from rest_framework import status
from rest_framework.views import APIView

class CustomerAPIView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers,many=True)
        return Response(serializer.data)
    def post(post,request):
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Customerdetails(APIView):
    def get_object(self,id):
        try:
            return Customer.objects.get(id=id)

        except Customer.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        customer = self.get_object(id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, id):
        customer = self.get_object(id)
        serializer = CustomerSerializer(customer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        customer = self.get_object(id)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def customer_details(request,pk):
    try:
         customer = Customer.objects.get(pk=pk)

    except Customer.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
         customer.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)

#product

@api_view(['GET','POST'])
def product_list(request):
     if request.method == 'GET':
         products = Product.objects.all()
         serializer = ProductSerializer(products,many=True)
         return Response(serializer.data)
     elif request.method == 'POST':
         serializer = ProductSerializer(data=request.data)

         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def product_details(request,pk):
    try:
        product = Product.objects.get(pk=pk)

    except Product.DoesNotExist:
         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
         serializer = ProductSerializer(product)
         return Response(serializer.data)
    elif request.method == 'PUT':
         serializer = ProductSerializer(product,data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
         product.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)


 #Basket

@api_view(['GET','POST'])
def basket_list(request):
    if request.method == 'GET':
         basket = Basket.objects.all()
         serializer = BasketSerializer(basket,many=True)
         return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BasketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def basket_details(request,pk):
     try:
         basket = Basket.objects.get(pk=pk)

     except Product.DoesNotExist:
         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

     if request.method == 'GET':
         serializer = BasketSerializer(basket)
         return Response(serializer.data)
     elif request.method == 'PUT':
         serializer = BasketSerializer(basket,data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     elif request.method == 'DELETE':
         basket.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)