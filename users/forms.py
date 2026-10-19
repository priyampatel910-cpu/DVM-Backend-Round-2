from django.contrib.auth.forms import UserCreationForm, AdminUserCreationForm, UserChangeForm
from .models import User

class CustomAdminUserCreationForm(AdminUserCreationForm):
    class Meta(AdminUserCreationForm.Meta):
        model = User
        fields = ("email", "username", "balance")


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email','username', 'balance')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('email', 'username', 'balance')