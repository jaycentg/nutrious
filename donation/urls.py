from django.urls import path
from donation.views import *

app_name = 'blog'

urlpatterns = [
    path('', show_donation, name='show_donation'),
    path('details/<int:id>', donation_detail, name='donation_detail'),
    path('add-donation/', create_donation, name='create_donation'),
    path('json/', show_json, name='show_json'),
    path('details/donate/<int:id>', donate, name='donate'),
]