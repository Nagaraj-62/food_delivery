from django.urls import path
from .views import *


app_name='Restaurants'
urlpatterns = [
    path('',home,name='home'),
    path('restaurant/<int:restaurant_id>/', restaurants, name='restaurant_menu'),
    path('search/', search_category, name='search'),
    path('menu/', menu, name='menu'),
    path('category/<str:category_id>/', category, name='category'),
    # path('category_view/<str:category_id>/', category_view, name='category_detail'),
]
