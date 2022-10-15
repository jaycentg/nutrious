from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import AppUser


class AppUserCreationForm(UserCreationForm):
    nickname = forms.CharField(required=True)
    # is_admin = forms.BooleanField()

    class Meta(UserCreationForm):
        model = AppUser
        fields = ('username', 'nickname', 'description', 'profile_pict_url')


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = AppUser
        fields = ('username', 'nickname', 'description', 'profile_pict_url')
