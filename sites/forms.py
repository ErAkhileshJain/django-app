from django import forms
from  django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    email=forms.EmailField()

class LoginForm(forms.Form):
    username=forms.CharField();
    password=forms.CharField(widget=forms.PasswordInput)

