
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.core.validators import  MinLengthValidator
from django.contrib.auth.password_validation import NumericPasswordValidator, CommonPasswordValidator
from captcha.fields import CaptchaField
from .models import Projects

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'registration-input'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'registration-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'registration-input'}),
                                validators=[MinLengthValidator(8, message='Пароль слишком короткий(не менее 8 символов)')])
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'registration-input', 'name': 'password2'}), validators=[MinLengthValidator(8, 'Пароль слишком короткий(не менее 8 символов)')])
    captcha = CaptchaField(label='Капча')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Такой пользователь уже существует!")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают!")
        return cd['password2']


    class Meta:
        model = User
        fields = ('username', 'email' ,'password1', 'password2')





class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'authorization-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'authorization-input'}))
    captcha = CaptchaField(label='Капча')

    class Meta:
        model = User
        fields = ['username', 'password']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['name']
        labels = {"name": "Название проекта: "}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-ctp'}),
        }
    


