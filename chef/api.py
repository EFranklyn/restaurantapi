from rest_framework import viewsets
from chef.models import Chef
from chef.serializers import ChefSerializers


class ChefViewSet(viewsets.ModelViewSet):
    """
    chef class used to change, create, and delete also provides options. to delete or change an object
    add the desired id(pk) to the end of the endpoint example:api/chefs/id
    """
    serializer_class = ChefSerializers
    queryset = Chef.objects.all()
    http_method_names = ['get',
                         'post',
                         'put',
                         'options',
                         'delete']

