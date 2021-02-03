from django import forms
from django.forms import ModelForm
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model= Client
        fields = ('type', 'price', 'status', 'issues')
