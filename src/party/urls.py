from django.urls import path
from party import views as party_views


urlpatterns = [
    path('create-party', party_views.create_party)
]
