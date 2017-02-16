from django.forms import ModelForm, CharField, PasswordInput, TextInput, EmailInput
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class EditForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': TextInput(attrs={'class': 'validate'}),
            'first_name': TextInput(attrs={'class': 'validate'}),
            'last_name': TextInput(attrs={'class': 'validate'}),
            'email': EmailInput(attrs={'class': 'validate'})
        }


class RegisterForm(UserCreationForm):
    password1 = CharField(
        label=_("Password"),
        strip=False,
        widget=PasswordInput(attrs={'class': 'validate', 'required': 'true'})
    )
    password2 = CharField(
        label=_("Password confirmation"),
        strip=False,
        widget=PasswordInput(attrs={'class': 'validate', 'required': 'true'}),
        help_text=_("Enter the same password as before, for verification.")
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': TextInput(attrs={'class': 'validate', 'required': 'true'}),
            'email': EmailInput(attrs={'class': 'validate', 'required': 'true'})
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(
        max_length=254,
        widget=TextInput(attrs={'class': 'validate', 'required': 'true'}),
    )
    password = CharField(
        label=_("Password"),
        strip=False,
        widget=PasswordInput(attrs={'class': 'validate', 'required': 'true'}),
    )


class PasswordForm(PasswordChangeForm):
    old_password = CharField(
        label=_("Old password"),
        strip=False,
        widget=PasswordInput(attrs={'class': 'validate', 'required': 'true'}),
    )
    new_password1 = CharField(
        label=_("New password"),
        widget=PasswordInput(attrs={'class': 'validate', 'required': 'true'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=PasswordInput(attrs={'class': 'validate', 'required': 'true'}),
    )
