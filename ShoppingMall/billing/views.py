from django.shortcuts import render
from .models import Product, Customer , Bill , Bill_Details
from .serializers import ProductSerializer , CustomerSerializer , BillSerializer , BillDetailSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
# Create your views here.


class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'product_id'

class CustomerListAPIView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'customer_id'
    
class BillListAPIView(ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    
class BillRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    lookup_field = 'bill_id'
    
class BillDetailsListAPIView(ListCreateAPIView):
    queryset = Bill_Details.objects.all()
    serializer_class = BillDetailSerializer
    
class BillDetailsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Bill_Details.objects.all()
    serializer_class = BillDetailSerializer
    lookup_field = 'id'