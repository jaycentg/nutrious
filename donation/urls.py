from django.urls import path
from donation.views import *

app_name = 'blog'

urlpatterns = [
    path('', show_donation, name='show_donation'),
    path('opened-donatee', show_donation_user, name='show_donation_user'),
    path('details/<int:id>', donation_detail, name='donation_detail'),
    path('delete/<int:id>', donation_delete, name='donation_delete'),
    path('add-donation/', create_donation, name='create_donation'),
    path('add-donation-user/', create_donation_user, name='create_donation_user'),
    path('json/', show_json, name='show_json'),
    path('details/donate/<int:id>', donate, name='donate'),
]