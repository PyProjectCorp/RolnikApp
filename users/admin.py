from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NormalUser

class NormalUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}), (('Personal info'), {'fields': ('first_name', 'last_name')}),
        (('Permissions'), {'fields': ('is_active',)}), (('Additional info'), {'fields': ('avatar', 'phone')})
    )
admin.site.register(NormalUser, NormalUserAdmin)