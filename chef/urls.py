from django.urls import path, include
from rest_framework import routers
from chef.api import ChefViewSet

app_name = 'chef'
router = routers.DefaultRouter()
router.register('', ChefViewSet)  # router name

urlpatterns = [
    path('api/', include(router.urls)),
]
