from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Profile


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # list_display = ["email", "username", "image", "is_verified",]
    # fields = ["__all__"]


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Profile)
