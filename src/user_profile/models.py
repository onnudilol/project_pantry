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


class Allergen(models.Model):
    name = models.CharField(max_length=300)
    list = models.ForeignKey(DietaryRestriction, on_delete=models.CASCADE)


class UserRating(models.Model):
    ENDORSEMENT = (
        ('TASTE', 'Excellent Taste'),
        ('HELP', 'Helpful'),
        ('LEADER', 'Good Leadership')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    review_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_author')
    text = models.TextField()
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    endorsement = models.CharField(max_length=25, choices=ENDORSEMENT, blank=True, null=True)

    class Meta:
        unique_together = ('user', 'review_author')
