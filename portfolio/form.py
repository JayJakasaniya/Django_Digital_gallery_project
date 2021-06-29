# forms.py
from django import forms
from .models import *


class uploadform(forms.ModelForm):

    class Meta:
        model = gallery
        fields = ['DrawingImage']
