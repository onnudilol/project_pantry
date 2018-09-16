from rest_framework import serializers

from user_profile.models import UserProfile, DietaryRestriction, Allergen, UserRating


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    allergens = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    def get_allergens(self, obj):
        diet = DietaryRestriction.objects.get(user=obj.user)
        sick = Allergen.objects.filter(list=diet)
        serializer = AllergenSerializer(sick, many=True)

        return serializer.data

    def get_avg_rating(self, obj):
        return obj.avg_rating

    class Meta:
        model = UserProfile
        fields = ('username', 'age', 'allergens', 'avg_rating')


class AllergenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Allergen
        fields = ('name',)

