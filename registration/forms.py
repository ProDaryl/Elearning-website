from .models import Profile
from django import forms
from django.contrib.auth.models import User

# class UserUpdateForm(forms.ModelForm):
#     email = forms.TextInput

#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name']

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['profile_picture']