from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Custom register form that extends basic UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)

    class Meta:
        model = User  # Interacts with User model
        fields = ["first_name", "last_name", "username",
                  "email", "password1", "password2"]