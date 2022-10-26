from django.db import models

# Create your models here.
from home.models import AppUser

class Sharing(models.Model):
    author = models.ForeignKey(AppUser, on_delete= models.CASCADE, related_name='foodsharing_posts')
    location = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        # descending order
        ordering = ['-date']