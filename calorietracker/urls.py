from django.urls import path
from calorietracker.views import show_caloriepage, add_calorie, show_json, reduce_calorie, edit

app_name = 'calorietracker'

urlpatterns = [
    path('', show_caloriepage, name='show_caloriepage'),
    path('add_calorie/', add_calorie, name='add_calorie'),
     path('reduce_calorie/', reduce_calorie, name='reduce_calorie'),
    path('json/', show_json, name='show_json'),
    path('edit/<int:id>', edit, name='edit'),
]