from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from customer.models import Orders, Profile, FeedBack


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2"
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),

        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


class PasswordResetForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        if new_password != confirm_password:
            msg = "incorrect password"
            self.add_error("confirm_password", msg)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ["address"]
        widgets = {
            "address": forms.Textarea(attrs={"class": "form-control"})
        }


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = [
            "comment",
            "rating"
        ]
        widgets = {
            "comment": forms.Textarea(attrs={"class": "form-control"}),
            "rating": forms.Select(attrs={"class": "form-select"})

        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("user", )
