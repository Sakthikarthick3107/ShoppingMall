from django.db import models
from django.db.models import Sum,F
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_delete
from django.dispatch import receiver

phone_regex = RegexValidator(regex=r'^\d{10}$',
                             message="Phone number must be entered in the format: '9999999999'. Exactly 10 digits allowed.")

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    
class Customer(models.Model): 
    
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    mobile = models.CharField(validators=[phone_regex], max_length=10)

class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(User,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_amt = models.IntegerField(default=0)
    
    def update_total_amt(self):
        total = self.bill_details_set.aggregate(
            total = Sum('price',output_field=models.IntegerField())
        )['total'] or 0
        self.total_amt = total
        self.save()

class Bill_Details(models.Model):
    bill_id = models.ForeignKey(Bill , related_name='bill_details_set',on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField(editable=False)
    
    def save(self,*args , **kwargs):
        self.price = self.product_id.price * self.quantity
        super().save(*args , **kwargs)
        if self.bill_id:
            self.bill_id.update_total_amt()

@receiver(post_delete, sender=Bill_Details)
def bill_detail_post_delete_handler(sender, instance, **kwargs):
    if instance.bill_id:
        instance.bill_id.update_total_amt()
