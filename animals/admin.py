from django.contrib import admin
from .models import Animals


class AnimalsAdmin(admin.ModelAdmin):
    search_fields = ['oznaczenie', 'typ']
    ordering = ['oznaczenie']

admin.site.register(Animals, AnimalsAdmin)