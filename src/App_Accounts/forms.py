from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, error_messages={'required':"Please Enter Username"})
    password = forms.CharField(max_length=65, widget=forms.PasswordInput, error_messages={'required':"Please Enter Password"})


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(max_length=65, widget=forms.PasswordInput, error_messages={'required':"Please Enter Password"},help_text='Please Enter Password Good', label='Password')
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')