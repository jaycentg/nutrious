from django.urls import path
from foodsharing.views import show_location, location_detail, add_location, show_json

app_name = 'foodsharing'

urlpatterns = [
    path('', show_location, name='show_location'),
    path('details/<int:id>', location_detail, name='location_detail'),
    path('add_location/', add_location, name='add_location'),
    path('json/', show_json, name='show_json'),
    
]