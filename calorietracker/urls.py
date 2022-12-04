from django.urls import path
from calorietracker.views import show_caloriepage, add_calorie, show_json
from calorietracker.views import reduce_calorie,edit_add,edit_reduce,edit_reduce_save, edit_add_save,delete
from calorietracker.views import calorief, show_jsonf, deletef, edit_reduce_savef, edit_add_savef
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
    path('calorief/', calorief, name='show_jsonf'),
    path('show_jsonf/', show_jsonf, name='show_jsonf'),
    path('deletef/', deletef, name='deletef'),
    path('edit_reduce_savef/', edit_reduce_savef, name='edit_reduce_savef'),
    path('edit_add_savef/', edit_add_savef, name='edit_add_savef'),
]