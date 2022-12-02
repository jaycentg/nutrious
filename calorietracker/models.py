from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from home.models import AppUser



class Calorie(models.Model):
    description = models.TextField()
    category = models.CharField(max_length = 300, default='')
    user = models.ForeignKey(AppUser, on_delete= models.CASCADE)
    calorie= models.IntegerField(default=0,null=True,blank=True)
    date = models.DateTimeField(auto_now_add = True)
    time = models.CharField(max_length = 300, default='')
    is_increasing = models.BooleanField()
    class Meta:
        ordering = ['-date']
    
