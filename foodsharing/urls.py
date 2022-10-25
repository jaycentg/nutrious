from django.urls import path
from blog.views import show_location, post_detail, add_location, show_json

app_name = 'foodsharing'

urlpatterns = [
    path('', show_location, name='show_location'),
    path('details/<int:id>', post_detail, name='post_detail'),
    path('add-post/', add_location, name='add_location'),
    path('json/', show_json, name='show_json'),
    
]