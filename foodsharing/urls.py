from django.urls import path
from foodsharing.views import deletef, edit_add_savef, show_jsonf, show_json_by_user
from foodsharing.views import delete, foodsharingf, show_location, add_location, show_json
from foodsharing.views import edit_add, edit_add_save, delete
app_name = 'foodsharing'

urlpatterns = [
    path('', show_location, name='show_location'),
    path('add_location/', add_location, name='add_location'),
    path('json/', show_json, name='show_json'),
    path('edit_add/<int:id>', edit_add, name='edit_add'),
    path('edit_add_save/<int:id>', edit_add_save, name='edit_add_save'),
    path('delete/<int:id>', delete, name='delete'),
    path('foodsharingf', foodsharingf, name='foodsharingf'),
    path('show_jsonf',show_jsonf , name='show_jsonf'),
    path('deletef', deletef, name='deletef'),
    path('edit_add_savef', edit_add_savef, name='edit_add_savef'),
    path('show_json_by_user', show_json_by_user, name='show_json_by_user'),

]