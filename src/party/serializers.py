from rest_framework import serializers

from party.models import Party, FoodList, FoodListItem


class PartySerializer(serializers.ModelSerializer):

    class Meta:
        model = Party
        exclude = ('user',)


class FoodItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodListItem
        fields = ('item')



class FoodListSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True)

    class Meta:
        model = Party
