from rest_framework import serializers
from chef.models import Chef


class ChefSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = ('id', 'name')
        