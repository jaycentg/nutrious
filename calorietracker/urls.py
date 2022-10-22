from django.urls import path
from calorietracker.views import show_caloriepage, add_calorie, show_json

app_name = 'calorietracker'

urlpatterns = [
    path('', show_caloriepage, name='show_caloriepage'),
    path('add_calorie/', add_calorie, name='add_calorie'),
    path('json/', show_json, name='show_json'),
]