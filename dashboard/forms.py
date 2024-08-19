from  django import forms
from . models import *


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']

class HomeWorkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['title', 'description', 'due']
        