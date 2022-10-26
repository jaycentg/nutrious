from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from home.forms import *
from home.models import *

# Register your models here.
class AppUserAdmin(UserAdmin):
    add_form = AppUserCreationForm
    form = AppUserChangeForm
    model = AppUser
    list_display = ['username', 'nickname', 'description', 'profile_pict_url']
    # Untuk menyetel user yang bisa menjadi admin
    fieldsets = ((None, {'fields': ('nickname', 'description', 'profile_pict_url', 'is_user', 'is_verified_user', 'is_admin')}),
    )

class MessageAdmin(admin.ModelAdmin):
    form = MessageForm
    list_display = ['get_user', 'message', 'time_sent']

admin.site.register(AppUser, AppUserAdmin)
admin.site.register(Message, MessageAdmin)