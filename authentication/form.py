from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import CustomUser


class CustomInitMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'form-control py-4'})


class CustomAuthenticationForm(CustomInitMixin, AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class UserRegistrationForm(CustomInitMixin, UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError(
                'Пользователь с таким адресом электронной почты уже существует')
        return email

        # self.fields['username'].widget.attrs.update(
        #     {'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'})
        # self.fields['first_name'].widget.attrs.update(
        #     {'class': 'form-control py-4', 'placeholder': 'Введите имя'})
        # self.fields['last_name'].widget.attrs.update(
        #     {'class': 'form-control py-4', 'placeholder': 'Введите фамилию'})
        # self.fields['email'].widget.attrs.update(
        #     {'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'})
        # self.fields['password1'].widget.attrs.update(
        #     {'class': 'form-control py-4', 'placeholder': 'Введите пароль'})
        # self.fields['password2'].widget.attrs.update(
        #     {'class': 'form-control py-4', 'placeholder': 'Повторите пароль'})


# class UserRegistrationForm(ModelForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'first_name', 'last_name', 'email')

#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'
#     }))
#     first_name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите имя'
#     }))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите фамилию'
#     }))
#     email = forms.CharField(widget=forms.EmailInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'
#     }))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите пароль'
#     }))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Повторите пароль'
#     }))
