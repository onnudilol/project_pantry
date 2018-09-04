from django.db import models
from django.contrib.auth import get_user_model

from restaurant.models import Restaurant, FoodItem


User = get_user_model()


class Party(models.Model):
    restaurant = models.ManyToManyField(Restaurant)
    title = models.CharField(max_length=300)
    description = models.TextField()
    users = models.ManyToManyField(User)
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='party_leader')
    dictator = models.BooleanField(default=False)
    start_time = models.DateTimeField()

    def __str__(self):
        return self.title


class FoodList(models.Model):
    party = models.OneToOneField(Party, on_delete=models.CASCADE)


class FoodListItem(models.Model):
    list = models.ForeignKey(FoodList, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.item.name

    class Meta:
        unique_together = ('list', 'item')


class FoodListItemVote(models.Model):
    VOTE_TYPE = (
        ('YES', 'Yes'),
        ('NO', 'No')
    )

    item = models.ForeignKey(FoodListItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_type = models.CharField(choices=VOTE_TYPE, max_length=25)

    class Meta:
        unique_together = ('item', 'user')
