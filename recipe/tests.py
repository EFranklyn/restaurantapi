import json
from django.test import TestCase, Client
from rest_framework import status
from chef.models import Chef
from recipe.models import Recipe, GroupRecipe
from recipe.serializers import RecipeSerializers, GroupRecipeSerializers

client = Client()


def params_search(chefname='', name='', groupname=''):
    """function used to return parameters for searchrecipes
    Args:
        chefname (str): Value for search in chefname.
        name (str): value for search in name.
        groupname (str): value for search in groupname
    Returns:
        params_search(dict): dict with values"""
    return {'chefname': chefname, 'name': name, 'groupname': ''}


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
        """Test update recipe"""
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
        """test update false data recipe"""
        response = client.put(
            self.URLRECIPES + str(self.escondidinho.pk) + '/',
            json.dumps(self.invalid),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_recipe(self):
        """Test delete recipe"""
        response = client.delete(self.URLRECIPES + str(self.escondidinho.pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_search_recipe_no_param(self):
        """Test all searchrecipes"""
        response = client.get(self.URLSEARCHRECIPES, params_search(), HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_search_recipe_param_name(self):
        """Test searchrecipes param recipe name"""
        response = client.get(self.URLSEARCHRECIPES, params_search(name=self.escondidinho.name[5: 10]),
                              HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(response.data[0]).get('name'), self.escondidinho.name)

    def test_get_search_recipe_param_chef_name(self):
        """Test searchrecipes param chef name"""
        response = client.get(self.URLSEARCHRECIPES, params_search(chefname=self.Ernane.name[0:5]),
                              HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(response.data[0]).get('chef').get('name'), self.Ernane.name)

    def test_get_search_recipe_param_group_name(self):
        """Test searchrecipes param group name"""
        response = client.get(self.URLSEARCHRECIPES, params_search(groupname=self.escondidinho.name[0: 5]),
                              HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(response.data[0]).get('group').get('name'), self.pratos_de_domingo.name)

    def test_get_groups(self):
        """test get Groups"""
        response = client.get(self.URLGROUPS)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_specify_group(self):
        """Test get specify group"""
        response = client.get(self.URLGROUPS + str(self.pratos_de_domingo.pk) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        group = GroupRecipe.objects.get(pk=self.pratos_de_domingo.pk)
        serializer = GroupRecipeSerializers(group)
        self.assertEqual(response.data, serializer.data)

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

    def test_opstions_recipes(self):
        """Test options recipes"""
        response = client.options(self.URLRECIPES)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_opstions_groups(self):
        """Test options groups"""
        response = client.options(self.URLGROUPS)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




