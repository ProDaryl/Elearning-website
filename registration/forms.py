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
# forms.py

from django import forms

class MyContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, error_messages={'required': 'Name is required.'})
    email = forms.EmailField(required=True, error_messages={'required': 'Email is required.', 'invalid': 'Enter a valid email address.'})
    message = forms.CharField(widget=forms.Textarea, required=True, error_messages={'required': 'Message is required.'})
