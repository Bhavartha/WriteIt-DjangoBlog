from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Custom register form that extends basic UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class': 'input'}))
    first_name = forms.CharField(required=True, max_length=30, widget=forms.TextInput(
        attrs={'class': 'input'}))
    last_name = forms.CharField(required=True, max_length=30, widget=forms.TextInput(
        attrs={'class': 'input'}))
    username = forms.CharField(required=True, max_length=30, widget=forms.TextInput(
        attrs={'class': 'input'}))
    password1 = forms.CharField(required=True, label='Password', widget=forms.TextInput(
        attrs={'class': 'input', 'type': 'password'}))
    password2 = forms.CharField(required=True, label='Confirm Password', widget=forms.TextInput(
        attrs={'class': 'input', 'type': 'password'}))

    class Meta:
        model = User  # Interacts with User model
        fields = ["first_name", "last_name", "username",
                  "email", "password1", "password2"]
