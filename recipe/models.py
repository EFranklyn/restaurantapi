from django.db import models

# Create your models here.
from chef.models import Chef


class TimesMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, null=True,verbose_name='Data Modificação')

    class Meta:
        abstract = True


class GroupRecipe(TimesMixin, models.Model):

    name = models.CharField(max_length=50, verbose_name='nome do grupo')
    details = models.TextField(verbose_name='Detalhes do grupo de receitas')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Grupo de receita'
        verbose_name_plural = 'Grupos de receita'


class Recipe(TimesMixin, models.Model):

    name = models.CharField(max_length=50, verbose_name='Receita')
    details = models.TextField(verbose_name='Detalhes da Receita')
    ingredients = models.TextField(verbose_name='Ingredientes')
    method_of_preparation = models.TextField(default='', verbose_name='Modo de Preparo')
    time = models.IntegerField(verbose_name='Preparo (em minutos)')
    chef = models.ForeignKey(Chef, on_delete=models.PROTECT, verbose_name='Chefe da receita')
    group = models.ForeignKey(GroupRecipe, on_delete=models.PROTECT, verbose_name='Grupo de receitas')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'