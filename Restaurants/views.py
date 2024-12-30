from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages


# Create your views here.
def home(request):
    Restaurants=Restaurant.objects.all()
    Categories=Category.objects.all()
    FoodItems=FoodItem.objects.all()
    context={'Restaurants':Restaurants,'Categories':Categories,'FoodItems':FoodItems}
    return render(request,'home.html',context)

def restaurants(request,restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    fooditems = FoodItem.objects.filter(restaurant=restaurant)
    context = {'restaurant': restaurant, 'fooditems': fooditems}
    return render(request, 'restaurant.html', context)

def category(request,category_id):
    category_item = Category.objects.get(cat_id=category_id)
    fooditems = FoodItem.objects.filter(category_name_id=category_item)
    context = {'category': category_item, 'fooditems': fooditems}
    return render(request, 'category.html', context)


# def category_view(request, category_id):
#     category = Category.objects.get(cat_id=category_id)
#     # Now you can fetch all items that belong to this category
#     items = category.items.all()  # Adjust according to your model relations
#     return render(request, 'Restaurants/category_detail.html', {'category': category, 'items': items})


def menu(request):
    categories=Category.objects.all()
    context={'categories':categories,}
    return render(request,'menu.html',context)

def search_category(request):
    items=FoodItem.objects.filter(name__icontains=request.GET['search'])
    data=Category.objects.filter(name__icontains=request.GET['search'])
    return render(request,'search.html',{'data':data,'items':items,})