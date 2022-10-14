from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

DEF_PICT_URL = 'https://uxwing.com/wp-content/themes/uxwing/download/peoples-avatars/no-profile-picture-icon.png'


class AppUser(AbstractUser):
    nickname = models.CharField(max_length=30)
    description = models.TextField()
    profile_pict_url = models.URLField(default=DEF_PICT_URL)
    is_admin = models.BooleanField(default=False)
    is_verified_user = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
