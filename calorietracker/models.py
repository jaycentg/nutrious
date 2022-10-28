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
    
# from django.db import models
# from django.contrib.auth.models import User
# from home.models import AppUser
# # Create your models here.


# class Food(models.Model):

#     def __str__(self):
#         return self.name

#     name = models.CharField(max_length=100)
#     carbs = models.FloatField()
#     protein = models.FloatField()
#     fats = models.FloatField()
#     calories = models.IntegerField()


# class Consume(models.Model):
#     user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
#     food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)