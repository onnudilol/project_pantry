from django.contrib import admin
from user_profile.models import UserProfile, UserLocation, DietaryRestriction, UserRating, Allergen


models = [UserProfile, UserLocation, DietaryRestriction, UserRating, Allergen]
admin.site.register(models)
