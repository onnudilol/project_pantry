from django.contrib import admin
from user_profile.models import UserProfile, UserLocation, DietaryRestriction, UserRating


models = [UserProfile, UserLocation, DietaryRestriction, UserRating]
admin.site.register(models)
