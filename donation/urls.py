from django.urls import path
from donation.views import *

app_name = 'blog'

urlpatterns = [
    path('', show_donation, name='show_donation'),
    path('opened-donatee', show_donation_user, name='show_donation_user'),
    path('details/<int:id>', donation_detail, name='donation_detail'),
    path('delete/<int:id>', donation_delete, name='donation_delete'),
    path('json/', show_json, name='show_json'),
    path('json-admin/', show_json_admin, name='show_json_admin'),
    path('json-user/', show_json_user, name='show_json_user'),
    path('details/donate/<int:id>', donate, name='donate'),
    path('delete-admin/<int:id>', delete_by_admin, name='delete_by_admin'),
    path('change-status/<int:id>', change_status_donatee, name='change_status_donatee'),
]