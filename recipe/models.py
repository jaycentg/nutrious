from django.db import models

from home.models import AppUser

class FoodRecipe(models.Model):
    food_name= models.CharField(max_length=100)
    author = models.ForeignKey(AppUser, on_delete= models.CASCADE)
    author_name =models.CharField(max_length=100)
    ingredients = models.TextField()
    method = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    formatted_date = models.CharField(max_length=20)

    class Meta:
        ordering = ['-created_on']