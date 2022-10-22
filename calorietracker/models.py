from django.db import models
from django.contrib.auth.models import User
from home.models import AppUser


class CalorieTracker(models.Model):
    calorie = models.IntegerField()
    description = models.TimeField()
    user =  models.ForeignKey(AppUser, on_delete= models.CASCADE)