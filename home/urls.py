from django.urls import path
from home.views import show_index

app_name = 'index'

urlpatterns = [
    path('', show_index, name='show_index')
]