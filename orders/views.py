from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .views import *
from cart.views import *


# Create your views here.

@login_required(login_url='login')
def create_order(request):
    cart=AddToCart.objects.filter(user=request.user)

    if cart:
        total_price = sum(item.items.price * item.quantity for item in cart)
        order = Order.objects.create(user=request.user, total_price=total_price)
        for item in cart:
            Order_item.objects.create(order=order, item=item.items, quantity=item.quantity)
        cart.delete()
    else:
        return redirect('Restaurants:home')
    return redirect('orders:order_details', order_id=order.id)

@login_required(login_url='login')
def order_detail(request, order_id):
    order=Order.objects.get(id=order_id)
    order_items=Order_item.objects.filter(order=order)
    return render(request,'order_detail.html',{'order':order,'order_items':order_items})

@login_required(login_url='login')
def confrim_order(request,id):
    order=Order.objects.get(user=request.user,id=id)
    user=User_details.objects.get(id=request.user.id)
    order_items=Order_item.objects.filter(order=order,order_id=id)
    action = request.POST.get('action')
    if action=='confirm':
        order.status='Confirmed'
        return render(request,'confirm_order.html',{'order':order,'user':user,'order_items':order_items})
    elif action=='cancel':
        order.status='Cancelled'
    order.save()
    return redirect('Restaurants:home')
    





def show_map(request):
    # Ensure you use the correct field names from your model
    restaurants = Restaurant.objects.values('Restaurant_name', 'address', 'rating')  # Adjust fields as needed
    markers = [
        {
            "lat": 51.505,  # Placeholder latitude
            "lng": -0.09,  # Placeholder longitude
            "label": r["Restaurant_name"],
        }
        for r in restaurants
    ]
    return render(request, 'map.html', {'markers': markers})
