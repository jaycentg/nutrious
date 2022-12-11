from django.urls import path
from recipe.views import show_recipe, add_recipe, show_json, delete, add_recipe_flutter

app_name = 'recipe'

urlpatterns = [
    path('', show_recipe, name='show_recipe'),
    path('add/', add_recipe, name='add_recipe'),
    path('add-flutter/', add_recipe_flutter, name='add_recipe_flutter'),
    path('delete/<int:id>', delete, name='delete'),
    path('json/', show_json, name='show_json'),
]
