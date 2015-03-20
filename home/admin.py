from django.contrib import admin
from .models import Author, Homepage


class HomeAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name']
    ordering = ['last_name']

admin.site.register(Homepage)
admin.site.register(Author, HomeAdmin)
