from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    age = models.IntegerField()


class UserLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.PointField()
    date = models.DateTimeField(auto_created=True)


class DietaryRestriction(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    milk = models.BooleanField(default=False)
    nuts = models.BooleanField(default=False)
    peanuts = models.BooleanField(default=False)
    tree_nuts = models.BooleanField(default=False)
    soy = models.BooleanField(default=False)
    wheat = models.BooleanField(default=False)
    fish = models.BooleanField(default=False)
    shellfish = models.BooleanField(default=False)


class UserRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    review_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_author')
    text = models.TextField()
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('user', 'review_author')
