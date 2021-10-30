import json
from django.test import TestCase, Client
from rest_framework import status
from chef.models import Chef
from chef.serializers import ChefSerializers
from recipe.models import Recipe, GroupRecipe
from recipe.serializers import RecipeSerializers


client = Client()


def params_search(chefname='', name='', groupname=''):
    """chefname,name,groupname"""
    return {'chefname': chefname, 'name': name, 'groupname': ''}


class ChefTestCase(TestCase):
    """Tests for Chefs """
    def setUp(self):
        self.URLCHEF = '/api/chefs/'
        self.geralda = Chef.objects.create(name='Geralda')
        self.leandra = Chef.objects.create(name='Leandra')

        self.valid_chef = {'name': 'Charlie Brown'}
        self.invalid_chef = {'name': ''}

    def test_get_chefs(self):
        """Test create recipe"""
        response = client.get(self.URLCHEF)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_chef(self):
        """Test get chef"""
        response = client.get(self.URLCHEF + str(self.leandra.pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        chef = Chef.objects.get(pk=self.leandra.pk)
        serializer = ChefSerializers(chef)
        self.assertEqual(response.data, serializer.data)

    def test_valid_update_chef(self):
        """Test update recipe"""
        response = client.put(
            self.URLCHEF + str(self.leandra.pk) + '/',
            json.dumps(self.valid_chef),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        chef = Chef.objects.get(pk=self.leandra.pk)
        self.assertEqual(chef.name, self.valid_chef.get('name'))

    def test_invalid_update_chef(self):
        """Test invalid update chef"""
        response = client.put(
            self.URLCHEF + str(self.leandra.pk) + '/',
            json.dumps(self.invalid_chef),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_chef(self):
        """Test delete chef"""
        response = client.delete(self.URLCHEF + str(self.leandra.pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_opstions_chef(self):
        """Test options chef"""
        response = client.options(self.URLCHEF)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
