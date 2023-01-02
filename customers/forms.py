from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        UserCreationForm.Meta.model = User
        UserCreationForm.Meta.fields += ("email",) # ("email", "first_name", "last_name",)