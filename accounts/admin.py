from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from accounts.models import User, Profile


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    ordering = ["email"]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["fullname", "telno"]
