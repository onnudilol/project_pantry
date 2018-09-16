from django.urls import path
from party import views as party_views


urlpatterns = [
    path('create-party', party_views.create_party),
    path('join-party/', party_views.join_party),
    path('add-item', party_views.add_item_to_list),
    path('vote-item', party_views.vote_item)
]
