from django.contrib import admin

# Register your models here.
from recipe.models import Recipe, GroupRecipe


class RecipeAdmin(admin.ModelAdmin):
    """class responsible for customizing the model in admin"""

    FIELDS_ADMIN = ('id',
                    'name',
                    'time',
                    'chef',
                    'group')
    list_display = FIELDS_ADMIN
    list_display_links = ('id',)
    list_filter = FIELDS_ADMIN
    list_editable = (
                    'name',
                    'time',
                    'chef',
                    'group')


class GroupRecipeAdmin(admin.ModelAdmin):
    """class responsible for customizing the model in admin"""

    FIELDS_ADMIN = (
                    'id',
                    'name',
                    'details',
                    )
    list_display = FIELDS_ADMIN
    list_display_links = ('id',)
    list_filter = FIELDS_ADMIN
    search_fields = FIELDS_ADMIN
    list_editable = (
                    'name',
                    'details',
                    )


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(GroupRecipe, GroupRecipeAdmin)
