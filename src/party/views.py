from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import status

from party.models import Party, FoodList, FoodListItem, FoodListItemVote
from restaurant.models import Restaurant, FoodItem
from party.serializers import PartySerializer, FoodListSerializer

User = get_user_model()


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_party(request):
    leader = request.user
    restaurant = Restaurant.objects.get(name=request.data['restaurant'])
    title = request.data['title']
    description = request.data['description']
    dictator = request.data['dictator'].lower() == 'true'
    start_time = request.data['start_time']

    party = Party.objects.create(leader=leader, title=title, description=description, dictator=dictator, start_time=start_time)
    party.restaurant.set([restaurant])
    party.users.add(leader)
    FoodList.objects.create(party=party)
    serializer = PartySerializer(data=party)
    serializer.is_valid()

    return Response(serializer.data, status=status.HTTP_201_CREATED)

# {"restaurant": "Popeyes", "title": "test title", "description": "test description", "dictator": "true", "start_time": "2010-04-20T20:08:21.634121"}


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def join_party(request):
    user = request.user
    party = Party.objects.get(id=request.data['party_id'])

    if party not in user.party_set.all():
        user.party_set.add(party)

    serializer = PartySerializer(data=party)
    serializer.is_valid()

    return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def add_item_to_list(request):
    user = request.user
    party = Party.objects.get(id=request.data['party_id'])
    food_item = FoodItem.objects.get(id=request.data['food_item_id'])

    if party.dictator is False and user in party.users.all():

        try:
            food_list_item = FoodListItem.objects.create(list=party.foodlist, item=food_item)
            serializer = FoodListSerializer(food_list_item.list)
            serializer.is_valid()

        except IntegrityError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)

    else:
        return Response(status=status.HTTP_403_FORBIDDEN)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def vote_item(request):
    user = request.user
    food_list_item = FoodListItem.objects.get(id=request.data['food_list_item_id'])

    if request.user in food_list_item.list.party.users.all():
        FoodListItemVote.objects.create(user=user, item=food_list_item, vote_type=request.data['vote_type'])

    serializer = FoodListSerializer(food_list_item.list)
    serializer.is_valid()

    return Response(serializer.data, response=status.HTTP_201_CREATED)