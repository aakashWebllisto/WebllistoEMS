from django.contrib.auth.models import User
from django import forms
from .models import User

class UserForm(forms.Form):
    
    name = forms.CharField(max_length = 200)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    phn_number = forms.IntegerField()
    ResidentialAddress = forms.CharField(widget=forms.Textarea())
    CurrentAddress = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField()

        
        
