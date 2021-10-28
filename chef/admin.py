from django.contrib import admin
# Register your models here.
from chef.models import Chef


class ChefAdmin(admin.ModelAdmin):
    #Chef
    pass


admin.site.register(Chef)