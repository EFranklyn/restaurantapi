from django.contrib import admin
# Register your models here.
from chef.models import Chef


class ChefAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_editable = ('name',)


admin.site.register(Chef, ChefAdmin)
