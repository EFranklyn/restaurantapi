import json

from django.test import TestCase, Client
from rest_framework import status
from rest_framework.reverse import reverse

from chef.models import Chef
from recipe.models import Recipe, GroupRecipe
from recipe.serializers import RecipeSerializers


client = Client()


class RecipeTestCase(TestCase):
    """Class for test the functionalities of the api"""
    def setUp(self):
        self.gordon = Chef.objects.create(name='Ernane')
        self.jacquin = Chef.objects.create(name='Leandra')
        self.sobremesas = GroupRecipe.objects.create(name='sobremesas')
        self.pratos_de_domingo = GroupRecipe.objects.create(name='Pratos de domingo')

        self.feijoada = Recipe.objects.create(
            name='Feijoada',
            short_description='A feijoada é um prato típico do Rio de Janeiro e é muito consumido em todo Brasil.',
            ingredients='1 Kg de feijão preto, 100 g de carne seca, 70 g de orelha de porco, 70 g de rabo de porco...',
            method='Coloque as carnes de molho por 36 horas ou mais, vá trocando a água várias vezes...',
            difficulty=1,
            chef=self.gordon,
            time=60
        )
        self.strogonoff = Recipe.objects.create(
            name='Strogonoff de camarão',
            short_description='Sirva com arroz e batata palha, palito ou chips',
            ingredients='500 gramas de camarão cinza ou rosa, 1 colher de sobremesa rasa de margarina, 1 lata...',
            method='Limpe os camarões tirando a cabeça e a tripa., Coloque em uma panela a manteiga.',
            difficulty=1,
            chef=self.jacquin,
            time=50
        )
        self.valid = {
            'name': 'Feijoada',
            'short_description': 'Comida tipica brasileira',
            'ingredients': '1 Kg de feijão preto, 100 g de carne seca, 70 g de orelha de porco, 70 g de rabo de porco',
            'method': 'Coloque as carnes de molho por 36 horas ou mais, vá trocando a água várias vezes',
            'difficulty': 1,
            'chef': 1,
            'time': 60
        }
        self.invalid = {
            'name': '',
            'short_description': 'Comida tipica brasileira',
            'ingredients': '1 Kg de feijão preto, 100 g de carne seca, 70 g de orelha de porco, 70 g de rabo de porco',
            'method': 'Coloque as carnes de molho por 36 horas ou mais, vá trocando a água várias vezes',
            'difficulty': 1,
            'chef': 1,
            'time': 60
        }

        self.chef = {'name': 'Douglas'}

    def test_create_recipe(self):
        """Testing the creation of a recipe"""
        response = client.post(reverse('create_recipe'), self.valid)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_single_recipe(self):
        """Testing the retrieve of information from a single recipe"""
        response = client.get(reverse('detail_recipe', kwargs={'pk': self.feijoada.pk}))

        recipe = Recipe.objects.get(pk=self.feijoada.pk)
        serializer = RecipeSerializer(recipe)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_update_recipe(self):
        """Testing update from a valid information"""
        response = client.put(
            reverse(
                'detail_recipe',
                kwargs={'pk': self.feijoada.pk}
            ),
            json.dumps(self.valid),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_recipe(self):
        """Testing update from a invalid information"""
        response = client.put(
            reverse(
                'detail_recipe',
                kwargs={'pk': self.feijoada.pk}
            ),
            json.dumps(self.invalid),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_recipe(self):
        """Testing the deletion of a recipe"""
        response = client.delete(reverse('detail_recipe', kwargs={'pk': self.feijoada.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_all_recipes(self):
        """Testing the retrieve of all recipes"""
        response = client.get(
            reverse('search_recipes'),
            {'name': '', 'difficulty': ''},
            HTTP_ACCEPT='application/json'
        )

        recipes = Recipe.objects.all().order_by('created')

        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_recipes_by_name(self):
        """Testing the retrieve of recipes filtered by name"""
        response = client.get(
            reverse('search_recipes'), {'name': 'f'}, HTTP_ACCEPT='application/json')

        recipes = Recipe.objects.filter(
            name__icontains='f'
        ).order_by('created')

        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_recipes_by_difficulty(self):
        """Testing the retrieve of recipes filtered by difficulty"""
        response = client.get(
            reverse('search_recipes'), {'difficulty': '1'}, HTTP_ACCEPT='application/json')

        recipes = Recipe.objects.filter(
            difficulty__icontains='1'
        ).order_by('created')

        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_recipes_by_chef(self):
        """Testing the retrieve of recipes filtered by chef name"""
        response = client.get(reverse('search_recipes'), {'chef': 'Gordon'}, HTTP_ACCEPT='application/json')

        recipes = Recipe.objects.filter(chef__name__icontains='Gordon').order_by('created')

        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_recipes_by_name_and_difficulty(self):
        """Testing the retrieve of recipes filtered by name, difficulty and chef"""
        response = client.get(
            reverse('search_recipes'),
            {'name': 'f', 'difficulty': '1', 'chef': 'Jacquin'},
            HTTP_ACCEPT='application/json'
        )

        recipes = Recipe.objects.filter(
            name__icontains='f',
            difficulty__icontains='1',
            chef__name__icontains='Jacquin'
        ).order_by('created')

        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_chef(self):
        """Testing the creation of a chef"""
        response = client.post(reverse('create_chef'), json.dumps(self.chef), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)