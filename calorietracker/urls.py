from django.urls import path
from calorietracker.views import show_caloriepage, add_calorie, show_json
from calorietracker.views import reduce_calorie,edit_add,edit_reduce,edit_reduce_save, edit_add_save,delete, add_calorief
app_name = 'calorietracker'

urlpatterns = [
    path('', show_caloriepage, name='show_caloriepage'),
    path('add_calorie/', add_calorie, name='add_calorie'),
    path('reduce_calorie/', reduce_calorie, name='reduce_calorie'),
    path('json/', show_json, name='show_json'),
    path('edit_add/<int:id>', edit_add, name='edit_add'),
    path('edit_reduce/<int:id>', edit_reduce, name='edit_reduce'),
    path('edit_reduce_save/<int:id>', edit_reduce_save, name='edit_reduce_save'),
    path('edit_add_save/<int:id>', edit_add_save, name='edit_add_save'),
    path('delete/<int:id>', delete, name='delete'),
    path('add-calorie/', add_calorief, name='add-calorie'),
]