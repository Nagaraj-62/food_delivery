from django.urls import path
from .models import *
from .views import *

app_name='Cart'

urlpatterns = [
    path('add-to-cart/<int:item_id>/', addtocart, name='addtocart'),
    path('viewcart/', viewcart, name='viewcart'),
    path('update-quantity/<int:item_id>/', update_quantity, name='update_quantity'),
    path('delete-item/<int:item_id>/', delete_item, name='delete_item'),
    # path('order-now/', order_now, name='order_now'),
]


