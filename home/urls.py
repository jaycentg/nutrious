from django.urls import path
from home.views import change_status_user, delete_ajax, json_user, logout_user, register, show_index, login_user, show_profile

app_name = 'home'

urlpatterns = [
    path('', show_index, name='show_index'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('json-user/', json_user, name='json_user'),
    path('change/<int:id>', change_status_user, name='change_status_user'),
    path('delete/<int:id>', delete_ajax, name='delete_user'),
    path('profile/', show_profile, name='profile')
]