from django.db import models

# Create your models here.

class Restaurant(models.Model):
    Restaurant_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    logo = models.ImageField(upload_to='restaurant_logos/', blank=True, null=True)
    rating = models.FloatField(default=0.0)
    total_reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.Restaurant_name
    
class Category(models.Model):
    cat_id=models.CharField(max_length=15,primary_key=True)
    name=models.CharField(max_length=100)
    description=models.TextField()
    images=models.ImageField(upload_to='category')

    def __str__(self):
        return self.name
    

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE,)

    def __str__(self):
        return self.name