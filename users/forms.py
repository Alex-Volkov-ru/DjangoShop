from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']

    """ username = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={"autofocus": True,
                                      'class': 'form-control',
                                      'placeholder': 'Введите Ваше имя пользователя'})
    )
    password = forms.CharField(
        label= 'Пароль',
        strip=False,
        widget= forms.PasswordInput(attrs={"autocomplete": "current-password",
                                        'class': 'form-control',
                                        'placeholder': 'Введите Ваш пароль'}),
    ) """
    