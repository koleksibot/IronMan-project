from django.contrib.auth import get_user_model
from django.contrib import admin
User = get_user_model()

from .models import User, UserOTP
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    model = User
    list_display = ('username', 'full_name', 'email', 'phone', 'data_joined', 'last_login', 'is_staff', 'is_active', 'is_superuser', 'is_seller')
    list_filter = ('username', 'full_name', 'email', 'phone', 'is_staff', 'is_active', 'is_superuser', 'is_seller')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'is_seller')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'full_name', 'email', 'phone', 'password', 'is_staff', 'is_active', 'is_superuser', 'is_seller')
        }),
    )
    search_fields = ('username', 'full_name', 'email', 'phone',)
    ordering = ('email',)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserOTP)


