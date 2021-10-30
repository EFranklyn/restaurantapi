from django.contrib import admin
# Register your models here.
from chef.models import Chef


class ChefAdmin(admin.ModelAdmin):
    """class responsible for customizing the model in admin"""
    list_display = ('id', 'name',)
    list_display_links = ('id',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_editable = ('name',)


admin.site.register(Chef, ChefAdmin)
