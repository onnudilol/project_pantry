from django.contrib import admin
from user_profile.models import UserProfile, UserLocation, DietaryRestriction, UserRating, Allergen, FriendList


models = [UserProfile, UserLocation, DietaryRestriction, UserRating, Allergen, FriendList]
admin.site.register(models)
