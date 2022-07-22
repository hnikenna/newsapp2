from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Profile
from PIL import Image
from django.core.files import File


class CustomUserCreationForm(UserCreationForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "email",)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email",)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'phone', 'bio']


class AvatarEditForm(forms.ModelForm):
    # avatar = forms.FileField(upload_to='avatars')

    class Meta:
        model = Profile
        fields = ['avatar']


class SocialsEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['website', 'tiktok', 'twitter', 'instagram', 'facebook']

