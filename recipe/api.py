from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from recipe.models import Recipe, GroupRecipe
from recipe.serializers import RecipeSerializers, GroupRecipeSerializers


class RecipeViewSet(viewsets.ModelViewSet):
    """Endpoint used to list, create and delete recipes."""

    serializer_class = RecipeSerializers
    queryset = Recipe.objects.all()
    http_method_names = ['get',
                         'post',
                         'put',
                         'options',
                         'delete']


class GroupRecipeViewSet(viewsets.ModelViewSet):
    """Endpoint used to list, create and delete Groups."""
    serializer_class = GroupRecipeSerializers
    queryset = GroupRecipe.objects.all()
    http_method_names = ['get',
                         'post',
                         'put',
                         'options',
                         'delete']


class SearchRecipes(ListAPIView):
    """
    Class of endpoint used to list recipes,
    to list specific recipes use the parameter search.
    Args:
        name (str): recipe name
        chefname (str): name chef
        groupname (str): name group
    return:
        SearchRecipes: queryset
    """

    serializer_class = RecipeSerializers

    def get_queryset(self):
        params = self.request.query_params
        queryset = Recipe.objects.filter(
            name__icontains=params.get('name', ''),
            chef__name__icontains=params.get('chefname', ''),
            group__name__icontains=params.get('groupname', ''),
        )
        return queryset
