from rest_framework import viewsets
from rest_framework.views import APIView
from chef.models import Chef
from chef.serializers import ChefSerializers


class ChefViewSet(viewsets.ModelViewSet):
    serializer_class = ChefSerializers
    queryset = Chef.objects.all()
    http_method_names = ['get', 'post', 'put', 'options']
