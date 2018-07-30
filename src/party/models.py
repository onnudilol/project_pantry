from django.db import models
from django.contrib.auth import get_user_model

from restaurant.models import Restaurant, FoodItem


User = get_user_model()


class Party(models.Model):
    restaurant = models.ManyToManyField(Restaurant)
    user = models.ManyToManyField(User)
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='party_leader')
    availability = models.BooleanField(default=False)
    start_time = models.DateTimeField()


class FoodList(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    price_max = models.DecimalField(max_digits=6, decimal_places=2)


class FoodListItem(models.Model):
    list = models.ForeignKey(FoodList, on_delete=models.CASCADE)
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)


class FoodListItemVote(models.Model):
    item = models.ForeignKey(FoodListItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('item', 'user')
