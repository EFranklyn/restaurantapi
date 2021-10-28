from rest_framework import serializers
from recipe.models import Recipe


class RecipeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'id',
            'name',
            'details',
            'ingredients',
            'method_of_preparation',
            'time',
            'chef',
            'group')
