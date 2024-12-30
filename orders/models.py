from django.db import models
from Accounts.models import User_details
from Restaurants.models import *
# Create your models here.

class Order(models.Model):
    user=models.ForeignKey(User_details,on_delete=models.CASCADE)
    total_price=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=50,default='Pending')
    Created_at=models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return f"Order #{self.id} - {self.status}"
    
class Order_item(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    item=models.ForeignKey(FoodItem,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return f"{self.item.name} - {self.quantity}"
