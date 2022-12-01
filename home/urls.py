from django.urls import path
from home.views import *

app_name = 'home'

urlpatterns = [
    path('', show_index, name='show_index'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('json-user/', json_user, name='json_user'),
    path('change/<int:id>', change_status_user, name='change_status_user'),
    path('delete/<int:id>', delete_user, name='delete_user'),
    path('profile/', show_profile, name='profile'),
    path('add-message/', add_message, name='add_message'),
    path('json-message/', show_json_message, name='show_json_message'),
    path('delete-msg/<int:id>', delete_message, name='delete_message'),
    path('json-message-name/', show_json_message_with_sender, name='show_json_message_with_sender')
]