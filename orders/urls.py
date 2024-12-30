from django.urls import path
from .views import *

app_name='orders'

urlpatterns = [
    path('create_order/',create_order, name='create_order'),
    path('order_details/<int:order_id>/', order_detail, name='order_details'),
    path('confrim_order/<int:id>/', confrim_order, name='confrim_order')
]
