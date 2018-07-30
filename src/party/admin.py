from django.contrib import admin
from party.models import Party, FoodList, FoodListItem, FoodListItemVote


models = [Party, FoodListItemVote, FoodList, FoodListItem]
admin.site.register(models)
