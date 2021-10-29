from rest_framework import viewsets
from rest_framework.generics import ListAPIView

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
    def get_queryset(self):
        params = self.request.query_params
        queryset = Recipe.objects.filter(
            name__icontains=params.get('name', ''),
            chef__name__icontains=params.get('chef', ''),
            group__name__icontains=params.get('group', ''),
        )
        print(self.request.query_params)
        print(queryset)
        return queryset


class GroupRecipeViewSet(viewsets.ModelViewSet):

    serializer_class = GroupRecipeSerializers
    queryset = GroupRecipe.objects.all()
    http_method_names = ['get',
                         'post',
                         'put',
                         'options',
                         'delete']


class SearchRecipes(ListAPIView):

    serializer_class = RecipeSerializers

    def get_queryset(self):
        params = self.request.query_params
        queryset = Recipe.objects.filter(
            name__icontains=params.get('name', ''),
            chef__name__icontains=params.get('chef', ''),
            group__name__icontains=params.get('group', ''),
        )
        print(self.request.query_params)
        print(queryset)
        return queryset
