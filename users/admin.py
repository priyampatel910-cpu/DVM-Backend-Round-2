from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomAdminUserCreationForm

@admin.action(description="Add user as an organizer")
def add_organizer(modeladmin, request, queryset):
    queryset.update(is_organizer=True)

class CustomUserAdmin(UserAdmin):
    add_form = CustomAdminUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'email', 'balance', 'is_staff',] #'is_organizer']

    fieldsets = UserAdmin.fieldsets + (
        ("Balance", {"fields": ("balance",)}),
        ("Organizer Access", {"fields": ("is_organizer",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Balance", {"fields": ("balance",)}),
        ("Organizer Access", {"fields": ("is_organizer",)}),
    )
    actions = [add_organizer]

admin.site.register(User, CustomUserAdmin)