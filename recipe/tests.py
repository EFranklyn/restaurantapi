import json

from django.conf.urls import url
from django.test import TestCase, Client
from rest_framework import status
from rest_framework.reverse import reverse

from chef.models import Chef
from recipe.models import Recipe, GroupRecipe
from recipe.serializers import RecipeSerializers


client = Client()


def params_search(chefname='', name='', groupname=''):
    """chefname,name,groupname"""
    return {'chefname':chefname,'name':name,'groupname':''}


class RecipeTestCase(TestCase):
    """Tests for Recipes """
    def setUp(self):
        self.URLRECIPES = '/api/recipes/'
        self.URLSEARCHRECIPES = '/api/searchrecipes/'
        self.URLGROUPS = '/api/groups/'
        self.Ernane = Chef.objects.create(name='Ernane')
        self.pratos_de_domingo = GroupRecipe.objects.create(name='Pratos de domingo')

        self.Leandra = Chef.objects.create(name='Leandra')
        self.sobremesas = GroupRecipe.objects.create(name='sobremesas')

        self.escondidinho = Recipe.objects.create(
            name='Escondidinho de carne ',
            details='Escondinho de carne com purê de mandioca',
            ingredients='3 Kg de carne seca, 800g de mandioca',
            method_of_preparation='Coloque a carne e a mandioca depois leve ao forno ...',
            time=50,
            chef=self.Ernane,
            group=self.pratos_de_domingo
        )
        self.canjica = Recipe.objects.create(
            name='Canjica ',
            details='Deliciosa canjica com run',
            ingredients='15 mls de run, quatro latas de leite condençado, canjica',
            method_of_preparation='cozinhe a canjica e adicione o leite condensado e o run',
            time=50,
            chef=self.Leandra,
            group=self.sobremesas
        )

        self.valid_recipe = {
            "name":'Escondidinho de carne',
            "details":'Escondinho de carne com purê de mandioca',
            "ingredients":'3 Kg de carne seca, 800g de mandioca',
            "method_of_preparation":'Coloque a carne e a mandioca depois leve ao forno ...',
            "time":50,
            "chef":1,
            "chef_put":1,
            "group":2,
            "group_put":2
        }

        self.invalid = {
            'name':'',
            'details':'Deliciosa canjica com run',
            'ingredients':'15 mls de run, quatro latas de leite condençado, canjica',
            'method_of_preparation':'cozinhe a canjica e adicione o leite condensado e o run',
            'time':50,
            'chef':1,
            'group':None

        }

        self.valid_group = {'name': 'Pratos de domingo'}

        self.invalid_group = {'name': ''}

    def test_create_recipe(self):
        """Test create recipe"""
        response = client.post('/api/recipes/', self.valid_recipe)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_recipes(self):
        """Test get recipes"""
        response = client.get(self.URLRECIPES)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_recipe(self):
        """Test get recipe"""
        response = client.get(self.URLRECIPES + str(self.escondidinho.pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        recipe = Recipe.objects.get(pk=self.escondidinho.pk)
        serializer = RecipeSerializers(recipe)
        self.assertEqual(response.data, serializer.data)

    def test_valid_update_recipe(self):
        """Test update"""
        response = client.put(
            self.URLRECIPES + str(self.escondidinho.pk) + '/',
            json.dumps(self.valid_recipe),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        recipe = Recipe.objects.get(pk=self.escondidinho.pk)
        self.assertEqual(recipe.chef.pk, self.valid_recipe.get('chef'))
        self.assertEqual(recipe.group.pk, self.valid_recipe.get('group'))

    def test_invalid_update_recipe(self):
        """test update false data"""
        response = client.put(
            self.URLRECIPES + str(self.escondidinho.pk) + '/',
            json.dumps(self.invalid),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_recipe(self):
        """Test delete"""
        response = client.delete(self.URLRECIPES + str(self.escondidinho.pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_search_recipes(self):
        """Test all searcherecipes"""
        response = client.get(self.URLSEARCHRECIPES, params_search(), HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get(self.URLSEARCHRECIPES, params_search(name=self.escondidinho.name[5: 10]),
                              HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get(self.URLSEARCHRECIPES, params_search(chefname=self.escondidinho.name[0: 5]),
                              HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get(self.URLSEARCHRECIPES, params_search(groupname=self.escondidinho.name[0: 5]),
                              HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_groups(self):
        """test get Groups"""
        response = client.get(self.URLGROUPS)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_specify_group(self):
        response = client.get(self.URLGROUPS + str(self.pratos_de_domingo.pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_group(self):
        """Test create group"""
        response = client.post(self.URLGROUPS, self.valid_group)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = client.post(self.URLGROUPS, self.invalid_group)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_group(self):
        """Test update Group"""
        response = client.put(
            self.URLGROUPS + str(self.sobremesas.pk) + '/',
            json.dumps(self.valid_group),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        group = GroupRecipe.objects.get(pk=self.sobremesas.pk)
        self.assertEqual(group.name, self.valid_group.get('name'))

    def test_delete_group(self):
        """Test delete group"""
        response = client.delete(self.URLRECIPES + str(self.canjica.pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = client.delete(self.URLGROUPS + str(self.sobremesas.pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



