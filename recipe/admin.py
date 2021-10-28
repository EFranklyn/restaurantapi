from django.contrib import admin

# Register your models here.
from recipe.models import Recipe


class RecipeAdmin(admin.ModelAdmin):

    FIELDS_ADMIN = ('name',
                    'details',
                    'ingredients',
                    'method_of_preparation',
                    'time chef group')
    list_display = FIELDS_ADMIN
    list_display_links = ('name',)
    list_filter = FIELDS_ADMIN
    search_fields = FIELDS_ADMIN
    list_editable = FIELDS_ADMIN


admin.site.register(Recipe, RecipeAdmin)
