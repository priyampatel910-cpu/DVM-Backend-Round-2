from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomAdminUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomAdminUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'email', 'balance', 'is_staff']

    fieldsets = UserAdmin.fieldsets + (
        ("Balance", {"fields": ("balance",)}),
    )

admin.site.register(User, CustomUserAdmin)   