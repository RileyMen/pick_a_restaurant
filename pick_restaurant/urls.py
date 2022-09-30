from django.urls import path
from . import views
app_name = 'pick_restaurant'
urlpatterns = [
    path('', views.index,name='index'),
    path('restaurant/',views.restaurant, name='restaurant')
]
