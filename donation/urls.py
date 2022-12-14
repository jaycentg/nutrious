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
    path('json-with-name/', show_json_with_opener, name='show_json_with_opener'),
    path('json-verified/', show_json_verified, name='show_json_verified'),
    path('donate/', donate_flutter, name='donate_flutter'),
    path('add-donatee/', add_donatee, name='add_donatee'),
    path('json-by-user/', show_json_by_user, name='show_json_by_user'),
    path('close/', donation_close, name='donation_close'),
]