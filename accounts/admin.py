from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    
    # Update list_display, search_fields, and ordering
    list_display = ['username', 'is_staff', 'is_active']  # No email here
    list_filter = ['is_staff', 'is_active']
    search_fields = ['username']  # Search by username only
    ordering = ['username']  # Order by username

    fieldsets = (
        (None, {'fields': ('username', 'password', 'is_artist')}),
        ('Personal info', {'fields': ('profile_picture', 'bio')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
