from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .forms import AppUserCreationForm, AppUserChangeForm
from .models import AppUser

class AppUserAdmin(UserAdmin):
    add_form = AppUserCreationForm
    form = AppUserChangeForm
    model = AppUser
    list_display = ['username', 'nickname', 'description', 'profile_pict_url']
    # Untuk menyetel user yang bisa menjadi admin
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('nickname', 'description', 'profile_pict_url', 'is_user', 'is_verified_user', 'is_admin')}),
    )


admin.site.register(AppUser, AppUserAdmin)