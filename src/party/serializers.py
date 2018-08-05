from rest_framework import serializers

from party.models import Party, FoodList, FoodListItem


class PartySerializer(serializers.ModelSerializer):

    class Meta:
        model = Party
        exclude = ('user',)


class FoodItemSerializer(serializers.ModelSerializer):
    item =  serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = FoodListItem
        fields = ('item')


class FoodListSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Party
