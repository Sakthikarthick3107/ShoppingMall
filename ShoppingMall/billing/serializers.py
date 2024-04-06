from rest_framework import serializers
from .models import Product , Customer , Bill , Bill_Details

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

class BillDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill_Details
        fields = '__all__'