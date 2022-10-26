from django.db import models

from home.models import AppUser

class FoodRecipe(models.Model):
    food_name= models.CharField(max_length=100)
    author = models.ForeignKey(AppUser, on_delete= models.CASCADE)
    ingredients = models.TextField()
    method = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']