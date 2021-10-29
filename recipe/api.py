from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from recipe.models import Recipe, GroupRecipe
from recipe.serializers import RecipeSerializers, GroupRecipeSerializers


class RecipeViewSet(viewsets.ModelViewSet):
    """Endpoint used to list, create and delete recipes,
    to list specific recipes use /id(pk)
    example:
    api/recipes/id"""

    serializer_class = RecipeSerializers
    queryset = Recipe.objects.all()
    http_method_names = ['get',
                         'post',
                         'put',
                         'options',
                         'delete']


class GroupRecipeViewSet(viewsets.ModelViewSet):
    """Endpoint used to list, create and delete recipes,
        to list specific groups use /id(pk)
        example:
        api/groups/id"""
    serializer_class = GroupRecipeSerializers
    queryset = GroupRecipe.objects.all()
    http_method_names = ['get',
                         'post',
                         'put',
                         'options',
                         'delete']


class SearchRecipes(ListAPIView):
    """Endpoint used to list recipes,
    to list specific recipes use the parameter search.
    search parameters:
    recipe name: name
    chef name: chefname
    group name:groupname
    example:
    api/searchrecipes/?name=value"""

    serializer_class = RecipeSerializers

    def get_queryset(self):
        params = self.request.query_params
        queryset = Recipe.objects.filter(
            name__icontains=params.get('name', ''),
            chef__name__icontains=params.get('chefname', ''),
            group__name__icontains=params.get('groupname', ''),
        )
        return queryset
