from django.db import models
from home.models import AppUser

# Create your models here.
class Donatee(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(AppUser, on_delete= models.CASCADE)
    description = models.TextField()
    amountNeeded = models.IntegerField(default=0)
    collectedFunds = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)

    def getAuthorName(self):
        return self.author.username