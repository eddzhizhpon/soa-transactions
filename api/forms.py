from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

'''Clase para inicio de sesión mediante un formulario, donde se realizan ciertas validaciones'''
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    dni = forms.CharField(max_length=10, required=True)
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')