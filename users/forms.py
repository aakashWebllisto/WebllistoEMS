from django.contrib.auth.models import User
from django import forms
from .models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['email','password','name','phn_number','residential_address','current_address','image']

        
class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
