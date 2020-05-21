from django import forms
from django.forms import SelectDateWidget
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class MyLoginForm(AuthenticationForm, forms.ModelForm):
    """Форма для авторизации пользователей"""

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        """Переопределяем метод init для формы, чтобы задать нужные классы"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control mb-2'


class MyRegisterForm(forms.ModelForm):
    """Форма для регистрации пользователей"""

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        labels = {
            'username': ('Имя пользователя (Логин)'),
        }
        help_texts = {
            'username': ('',),
        }

    def __init__(self, *args, **kwargs):
        """Переопределяем метод init для формы, чтобы задать нужные классы"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit = True):
        """переопределяем Save чтобы правильно сохранять пароли пользователей"""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

