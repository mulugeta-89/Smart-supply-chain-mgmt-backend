from django.shortcuts import render
from rest_framework import generics
from .models import Buyer, Seller, Driver
from .serializers import BuyerSerializer, SellerSerializer, DriverSerializer

# Create Buyer views here.
class BuyerCreateView(generics.CreateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer

class BuyerRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer 
    lookup_field = "pk"

# Create Seller views here
class SellerCreateView(generics.CreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SellerRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer 
    lookup_field = "pk"



# Create Driver views here
class DriverCreateView(generics.CreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class DriverRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer 
    lookup_field = "pk"
