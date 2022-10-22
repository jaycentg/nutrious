
# Create your models here.
from django.db import models

from home.models import AppUser



class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(AppUser, on_delete= models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_on']