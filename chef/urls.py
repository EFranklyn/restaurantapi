"""chef app routes"""
from django.urls import path, include
from rest_framework import routers
from chef.api import ChefViewSet

app_name = 'chef'
router = routers.DefaultRouter()
router.register('api/chefs', ChefViewSet)  # router name

urlpatterns = [
    path('', include(router.urls), name='chefs'),
]
