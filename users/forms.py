from django.contrib.auth.forms import UserCreationForm, AdminUserCreationForm, UserChangeForm
from .models import User

class CustomAdminUserCreationForm(AdminUserCreationForm):
    class Meta(AdminUserCreationForm.Meta):
        model = User
        fields = ('username', 'balance')


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('balance','first_name', 'last_name', 'email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('balance', 'first_name', 'last_name', 'email',)