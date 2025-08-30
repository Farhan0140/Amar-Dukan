from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


class CustomUserAdmin( UserAdmin ):
    model = User
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'address', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ("Important Date's", {'fields': ('last_login', 'date_joined')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active'
    )

    search_fields = (
        'email',
        'first_name',
        'last_name',
        'phone'
    )

    ordering = (
        'email',
    )

admin.site.register(User, CustomUserAdmin)