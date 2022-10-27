from django.urls import path
from foodsharing.views import delete, show_location, location_detail, add_location, show_json
from foodsharing.views import edit_add, edit_add_save, delete
app_name = 'foodsharing'

urlpatterns = [
    path('', show_location, name='show_location'),
    path('details/<int:id>', location_detail, name='location_detail'),
    path('add_location/', add_location, name='add_location'),
    path('json/', show_json, name='show_json'),
    path('edit_add/<int:id>', edit_add, name='edit_add'),
    path('edit_add_save/<int:id>', edit_add_save, name='edit_add_save'),
    path('delete/<int:id>', delete, name='delete'),
]