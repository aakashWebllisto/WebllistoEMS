from django.contrib.auth.models import User
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    

    class Meta:

        model = User
        fields = ['email','password','name','phn_number','residential_address','current_address','image']

        
        
