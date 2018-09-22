from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg
from django.contrib.auth import get_user_model

from user_profile.models import UserProfile, UserRating, FriendList
from user_profile.serializers import ProfileSerializer, FriendListSerializer
from rest_framework import status


User = get_user_model()


@api_view(['GET'])
def get_profile(request, username):
    person = User.objects.get(username=username)
    avg_rating = UserRating.objects.aggregate(rating_avg=Avg('score'))
    profile = UserProfile.objects.get(user=person)

    profile.avg_rating = avg_rating
    serializer = ProfileSerializer(profile)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_friends_list(request, username):
    person = User.objects.get(username=username)
    friend_list = FriendList.objects.get(owner=person)

    serializer = FriendListSerializer(friend_list)
    print(friend_list)

    return Response(serializer.data, status=status.HTTP_200_OK)