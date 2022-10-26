from django.db import models
from django.contrib.auth.models import AbstractUser
from blog.models import Post
from django.db import models

# Create your models here.
class AppUser(AbstractUser):
    nickname = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    profile_pict_url = models.URLField(blank=True)
    is_admin = models.BooleanField(default=False)
    is_verified_user = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
    post = models.ManyToManyField(Post)

class Message(models.Model):
    user = models.ForeignKey(AppUser, on_delete= models.CASCADE)
    message = models.TextField()
    time_sent = models.DateTimeField(auto_now_add=True)
    
    def get_user(self):
        return self.user.username