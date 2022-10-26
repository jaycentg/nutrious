
# Create your models here.
from email.policy import default
from django.db import models

# from home.models import AppUser



class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=70, default='')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    vote_state = models.IntegerField(default=2)
    tag = models.CharField(max_length=50, default='')

    class Meta:
        ordering = ['-created_on']