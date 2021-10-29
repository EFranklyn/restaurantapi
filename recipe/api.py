from rest_framework import viewsets
from recipe.models import Recipe, GroupRecipe
from recipe.serializers import RecipeSerializers, GroupRecipeSerializers


class RecipeViewSet(viewsets.ModelViewSet):

    serializer_class = RecipeSerializers
    queryset = Recipe.objects.all()
    http_method_names = ['get',
                         'post',
                         'put',
                         'options',
                         'delete']


class GroupRecipeViewSet(viewsets.ModelViewSet):

    serializer_class = GroupRecipeSerializers
    queryset = GroupRecipe.objects.all()
    http_method_names = ['get',
                         'post',
                         'put',
                         'options',
                         'delete']
