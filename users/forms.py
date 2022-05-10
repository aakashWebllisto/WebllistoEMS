from django.contrib.auth.models import User
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password','email','phn_number','image','residential_address','current_address']
