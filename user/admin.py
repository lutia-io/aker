from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User


class CustomUserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("email",)}),)


admin.site.register(User, CustomUserAdmin)
