from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms
from django.core import validators
from myapp.models import Image_Post


class SignForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Password (again)", widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs=({'class': 'form-control'})),
            'first_name': forms.TextInput(attrs=({'class': 'form-control'})),
            'last_name': forms.TextInput(attrs=({'class': 'form-control'})),
            'email': forms.EmailInput(attrs=({'class': 'form-control'})),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if (User.objects.filter(email=email).exists()):
            raise forms.ValidationError("Email Already Exists")

        return email


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class EditProfileChange(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs=({'class': 'form-control'})),
            'first_name': forms.TextInput(attrs=({'class': 'form-control'})),
            'last_name': forms.TextInput(attrs=({'class': 'form-control'})),
            'email': forms.EmailInput(attrs=({'class': 'form-control'})),
        }


class PasswordChange(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(
        label="New Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(
        label="Confirm New Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User


class Upload_Image(forms.ModelForm):
    class Meta:
        model = Image_Post
        fields = ['title', 'image']

        widgets = {
            'title': forms.TextInput(attrs=({'class': 'form-control'})),
        }


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email", widget=forms.EmailInput({'class': 'form-control'}))


class MysetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(
        label="Confirm New Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
