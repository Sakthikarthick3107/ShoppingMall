from django.urls import path
from .views import (ProductListAPIView , 
                    ProductRetrieveUpdateDestroyAPIView , 
                    CustomerListAPIView , 
                    CustomerRetrieveUpdateDestroyAPIView,
                    BillListAPIView,
                    BillRetrieveUpdateDestroyAPIView,
                    BillDetailsListAPIView,
                    BillDetailsRetrieveUpdateDestroyAPIView
                    )

urlpatterns = [
    path('products/', ProductListAPIView.as_view() , name="product_list"),
    path('products/<int:product_id>' , ProductRetrieveUpdateDestroyAPIView.as_view() , name='product-retrieve-update-destroy'),
    path('customers/' , CustomerListAPIView.as_view() , name="customer_list" ),
    path('customers/<int:customer_id>' , CustomerRetrieveUpdateDestroyAPIView.as_view(), name="customer-retrieve-update-destroy"),
    path('checkout/bill/' , BillListAPIView.as_view() , name="Bill_List"),
    path('checkout/bill/<int:bill_id>' , BillRetrieveUpdateDestroyAPIView.as_view() , name='Bill List Individual'),
    path('checkout/bill_details/' , BillDetailsListAPIView.as_view() , name="Bill_List"),
    path('checkout/bill_details/<int:id>' , BillDetailsRetrieveUpdateDestroyAPIView.as_view() , name='Bill List Individual'),
]
