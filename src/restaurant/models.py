from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator


User = get_user_model()


class Restaurant(models.Model):
    name = models.CharField(max_length=300)
    location = models.PointField()

    def __str__(self):
        return self.name


class RestaurantRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    text = models.TextField()
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('user', 'restaurant')


class FoodItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class FoodItemRating(models.Model):
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommend = models.BooleanField(default=False)

    class Meta:
        unique_together = ('item', 'user')
