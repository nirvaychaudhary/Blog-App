from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    # email = forms.EmailField()
    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2']