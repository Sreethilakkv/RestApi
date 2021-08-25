from rest_framework import viewsets
from . import models
from . import serializer

class CustomerViewset(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializer.CustomerSerializer

class ProductViewset(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializer.CustomerSerializer

