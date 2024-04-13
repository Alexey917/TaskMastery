
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'registration-input'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'registration-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'registration-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'registration-input'}))


    class Meta:
        model = User
        fields = ('username', 'email' ,'password1', 'password2')