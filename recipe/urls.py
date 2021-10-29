from django.urls import path, include
from rest_framework import routers
from chef.api import ChefViewSet
from recipe.api import RecipeViewSet, GroupRecipeViewSet

app_name = 'recipe'
router_recipes = routers.DefaultRouter()
router_recipes.register('recipes', RecipeViewSet)  # router name
router_groups = routers.DefaultRouter()
router_groups.register('groups', GroupRecipeViewSet)

urlpatterns = [
    path('', include(router_recipes.urls)),
    path('', include(router_groups.urls)),
]

