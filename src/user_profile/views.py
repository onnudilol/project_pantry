from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg
from django.contrib.auth import get_user_model

from user_profile.models import UserProfile, UserRating
from user_profile.serializers import ProfileSerializer
from rest_framework import status


User = get_user_model()


@api_view(['GET'])
def get_profile(request, username):
    person = User.objects.get(username=username)
    avg_rating = UserRating.objects.filter(user=person).annotate(rating_avg=Avg('score'))
    profile = UserProfile.objects.filter(user=person).annotate(avg_rating=avg_rating)

    print(profile)

    serializer = ProfileSerializer(profile)

    return Response(serializer.data, status=status.HTTP_200_OK)