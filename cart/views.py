from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url='login')
def addtocart(request,item_id):
    cart,created=Cart.objects.get_or_create(user=request.user)
    item = get_object_or_404(FoodItem, id=item_id)
    cartitem,created=AddToCart.objects.get_or_create(user=request.user,items=item)
    if not created:
        cartitem.quantity += 1
        cartitem.save()
    return redirect('Restaurants:home')


@login_required(login_url='login')
def viewcart(request):
    cartitems=AddToCart.objects.filter(user=request.user)
    if not cartitems:
        return render(request,'emptycart.html')
    return render(request,'viewcart.html',{'cartitems':cartitems})


@login_required(login_url='login')
def update_quantity(request, item_id):
    cart_item = get_object_or_404(AddToCart, id=item_id, user=request.user)

    # Increase or decrease quantity based on the action button clicked
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'increase':
            cart_item.quantity += 1
        elif action == 'decrease' and cart_item.quantity > 1:
            cart_item.quantity -= 1
        cart_item.save()
    return redirect('Cart:viewcart')  # Redirect back to the cart page

@login_required(login_url='login')
def delete_item(request, item_id):
    cart_item = get_object_or_404(AddToCart, id=item_id, user=request.user)

    # Delete the cart item
    cart_item.delete()

    return redirect('Cart:viewcart')  # Redirect back to the cart page

