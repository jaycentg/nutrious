from django.urls import path
from home.views import change_status_user, delete_user, json_user, logout_user, show_index, Register, login_user

app_name = 'home'

urlpatterns = [
    path('', show_index, name='show_index'),
    path('register/', Register.as_view(), name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('json-user/', json_user, name='json_user'),
    path('change/<int:id>', change_status_user, name='change_status_user'),
    path('delete/<int:id>', delete_user, name='delete_user'),
]