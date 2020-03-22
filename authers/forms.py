from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class AutherRegisterForm(UserCreationForm):
    email = forms.EmailField()
    captcha = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']