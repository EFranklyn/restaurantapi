from rest_framework import viewsets
from recipe.models import Recipe
from recipe.serializers import RecipeSerializers


class RecipeViewSet(viewsets.ModelViewSet):

    serializer_class = RecipeSerializers
    queryset = Recipe.objects.all()
    http_method_names = ['get',
                         'post',
                         'put',
                         'options',
                         'delete']



