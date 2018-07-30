from django.contrib import admin
from restaurant.models import Restaurant, RestaurantRating, FoodItem, FoodItemRating


models = [RestaurantRating, Restaurant, FoodItemRating, FoodItem]
admin.site.register(models)
