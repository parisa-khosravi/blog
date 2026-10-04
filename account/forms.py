from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import authenticate

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields=('email','password1','password2')


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            user = authenticate(
                username=email,
                password=password
            )

            if user is None:
                raise forms.ValidationError(
                    "ایمیل یا رمز عبور اشتباه است."
                )

            cleaned_data["user"] = user

        return cleaned_data