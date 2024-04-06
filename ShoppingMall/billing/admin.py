from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name' , 'price' , 'stock',]

admin.site.register(Product , ProductAdmin)
admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(Bill_Details)
