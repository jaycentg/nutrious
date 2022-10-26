from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from home.models import *
from django.forms import ModelForm, Textarea

class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = AppUser
        fields = ['username', 'nickname', 'description', 'profile_pict_url']


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = AppUser
        fields = ['username', 'nickname', 'description', 'profile_pict_url']

class MessageForm(ModelForm):
    class Meta(ModelForm):
        model = Message
        fields = ['message']
        widgets = {
            'message': Textarea(attrs={'rows': 1, 'class': 'form-control', 'placeholder': 'Message'}),
        }
        labels = {
           'message' : '',
        }