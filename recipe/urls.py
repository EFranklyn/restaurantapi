"""recipe app routes"""


from django.urls import path, include
from rest_framework import routers
from recipe.api import RecipeViewSet, GroupRecipeViewSet, SearchRecipes

app_name = 'recipe'
router_recipes = routers.DefaultRouter()
router_recipes.register('api/recipes', RecipeViewSet)  # router name
router_groups = routers.DefaultRouter()
router_groups.register('api/groups', GroupRecipeViewSet)

urlpatterns = [
    path('', include(router_recipes.urls), name='recipes'),
    path('', include(router_groups.urls), name='groups'),
    path('api/searchrecipes/', SearchRecipes.as_view(), name='searchrecipes'),
]

