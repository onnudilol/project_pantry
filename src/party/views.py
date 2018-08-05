from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import status

from party.models import Party, FoodList, FoodListItem
from restaurant.models import Restaurant, FoodItem
from party.serializers import PartySerializer

User = get_user_model()


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_party(request):
    leader = request.user
    restaurant = Restaurant.objects.get(request.data['restaurant'])
    title = request.data['title']
    description = request.data['description']
    dictator = request.data['dictator']
    start_time = request.data['start_time']

    party = Party.objects.create(leader=leader, restaurant=restaurant, title=title, description=description,
                                 dictator=dictator, start_time=start_time)
    FoodList.objects.create(party=party)
    serializer = PartySerializer(data=party)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def join_party(request):
    user = request.user
    party = Party.objects.get(id=request.data['party_id'])

    if party not in user.party_set.all():
        user.party.add(party)

    serializer = PartySerializer(data=party)

    return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def add_item_to_list(request):
    user = request.user
    party = Party.objects.get(id=request.data['party_id'])
    food_item = FoodItem.objects.get(id=request.data['food_item_id'])

    if party.dictator is False and user in party.user_set.all():
        food_list_item = FoodListItem.objects.create(list=party.foodlist, item=food_item)

        return Response

    else:
        return


