from django.db import models
from django.contrib.auth.models import AbstractUser
from blog.models import Post

# Create your models here.
class AppUser(AbstractUser):
    nickname = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    profile_pict_url = models.URLField(blank=True)
    is_admin = models.BooleanField(default=False)
    is_verified_user = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
    post = models.ManyToManyField(Post)
