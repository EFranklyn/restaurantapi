from rest_framework import serializers

from chef.models import Chef
from chef.serializers import ChefSerializers
from recipe.models import Recipe, GroupRecipe


class GroupRecipeSerializers(serializers.ModelSerializer):
    """Serializer to Model GroupRecipe"""
    class Meta:
        model = GroupRecipe
        fields = (
            'id',
            'name',)


class RecipeSerializers(serializers.ModelSerializer):
    """Serializer to Model Recipe"""
    chef = ChefSerializers(read_only=True)
    chef_put = serializers.PrimaryKeyRelatedField(queryset=Chef.objects.all(),
                                                  write_only=True, source='chef')
    group = GroupRecipeSerializers(read_only=True)
    group_put = serializers.PrimaryKeyRelatedField(queryset=GroupRecipe.objects.all(),
                                                   write_only=True, source='group')

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
            'chef_put',
            'group',
            'group_put')
