from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible,label='')

    class Meta:
        model = User  # Interacts with User model
        fields = ["first_name", "last_name", "username",
                  "email", "password1", "password2"]