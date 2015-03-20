from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email', 'message']
    ordering = ['email']

admin.site.register(Message, MessageAdmin)