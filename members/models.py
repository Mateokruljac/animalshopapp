from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from pets.models import Animal
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,blank = True, null = True)
    name = models.CharField(max_length = 100,null = True, blank = True)
    email = models.CharField(max_length = 100,null = True, blank = True)
    
    def __str__(self):
        return f"{self.user}"
    
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE,blank = True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    # if complete is False, customer can add new items to box
    complete = models.BooleanField(default = False)
    transaction_id = models.CharField(max_length = 100)
    
    def __str__(self):
        return f'{self.id}' 
    
    
    @property 
    def get_total_items(self):
        items = self.orderitem_set.all()
        total_items = sum([item.quantity for item in items ])
        return total_items
    
    @property
    def get_cart_total(self):
        items = self.orderitem_set.all()
        total_items = sum([item.total_price for item in items])
        return total_items
    
class OrderItem(models.Model):
    product = models.ForeignKey(Animal,on_delete = models.CASCADE, blank = True)
    order = models.ForeignKey(Order,on_delete = models.CASCADE, blank = True)
    quantity = models.IntegerField(default = 0,null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)

    @property
    def total_price(self):
        return self.product.price * self.quantity
    
    
#customer address
#this class represents shipping address
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE,blank = True)
    order = models.ForeignKey(Order,on_delete = models.CASCADE, blank = True)
    address = models.CharField(max_length = 100,blank = False)
    city = models.CharField(max_length = 100,blank = False)
    state = models.CharField(max_length = 100,blank = False)
    zip_code = models.CharField(max_length = 100,blank = False)
    
    def __str__(self):
        return self.address 
    

