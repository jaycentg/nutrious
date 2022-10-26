from recipe.models import FoodRecipe
from django.forms import ModelForm

class CreateRecipe(ModelForm):
    class Meta:
        model = FoodRecipe
        fields = ('food_name', 'author', 'ingredients', 'method', 'created_on')
        exclude = ['author', 'created_on']
