from django.db import models
from Accounts.models import User_details
from Restaurants.models import FoodItem
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User_details, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
    
class AddToCart(models.Model):
    user=models.ForeignKey(User_details,on_delete=models.CASCADE)
    items=models.ForeignKey(FoodItem,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.items.name} (x{self.quantity})"