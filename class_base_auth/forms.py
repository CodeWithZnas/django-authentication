from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username Here'}))


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email Here'})
        }



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')