from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()

def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)

class RegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Your name')
        add_placeholder(self.fields['last_name'], 'Your surname')
        add_placeholder(self.fields['password'],'Type your password here')
        add_placeholder(self.fields['password2'],'Repeat your password')

    first_name = forms.CharField(
        error_messages={'required': 'Write your first name'},
        label='First name'
    )

    last_name = forms.CharField(
        error_messages={'required': 'Write your last name'},
        label='Last name'
    )

    email = forms.EmailField(
        error_messages={'required': 'E-mail is required'},
        label='E-mail'
    )

    password = forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput(),
        error_messages={'required': 'Password must not be empty'}
    )

    password2 = forms.CharField(
        required=True,
        label='Password2',
        widget=forms.PasswordInput(),
        error_messages={'required': 'Please, repeat your password'}
    )
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        labels = {
            'username': 'Username',
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'E-mail',
            'password': 'Password',
        }

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'Password and password2 must be equal',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })
 