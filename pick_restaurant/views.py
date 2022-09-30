from django.http import HttpResponse
from django.shortcuts import render
from .models import Restaurants
import random

def index(request):
    return render(request,'pick_restaurant/index.html')

list1 = list(Restaurants.objects.values_list('restaurantname','rate'))
def restaurant(request):
    return render(request,'pick_restaurant/restaurant.html',{'list1': list1})

