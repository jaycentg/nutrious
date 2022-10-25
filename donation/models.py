from django.db import models
from home.models import AppUser
from django.core.validators import MinValueValidator

# Create your models here.
class Donatee(models.Model):
    name = models.CharField(max_length=200)
    opener = models.ForeignKey(AppUser, on_delete= models.CASCADE, blank=True, null=True)
    description = models.TextField()
    amountNeeded = models.IntegerField(default=100000, validators=[MinValueValidator(100000)])
    collectedFunds = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)

    def getAuthorName(self):
        return self.opener.username