from django.urls import path

from user_profile import views as profile_views


urlpatterns = [
    path('<username>/', profile_views.get_profile)
]