from django.urls import path
from recipe.views import show_recipe, add_recipe, show_json

app_name = 'recipe'

urlpatterns = [
    path('', show_recipe, name='show_recipe'),
    path('add/', add_recipe, name='add_recipe'),
    path('json/', show_json, name='show_json'),
]