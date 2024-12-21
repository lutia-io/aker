from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.forms import CustomUserChangeForm
from user.models import User


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("profile",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("email",)}),)


admin.site.register(User, CustomUserAdmin)
