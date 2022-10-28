from django.db import models

# Create your models here.
from home.models import AppUser

class Sharing(models.Model):
    author = models.ForeignKey(AppUser, on_delete= models.CASCADE, related_name='foodsharing_posts')
    location = models.TextField()
    description = models.TextField()
    date = models.TextField()
    update_date = models.TextField()
    img = models.TextField()

    class Meta:
        # descending order
        ordering = ['-date']