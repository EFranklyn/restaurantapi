from django.urls import path, include
from rest_framework import routers
from chef.api import ChefViewSet
from recipe.api import RecipeViewSet

app_name = 'recipe'
router = routers.DefaultRouter()
router.register('', RecipeViewSet)  # router name

urlpatterns = [
    path('', include(router.urls)),
]

