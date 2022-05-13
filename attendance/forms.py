# from django.contrib.auth.models import User
from django import forms
from .models import Attendance


class AttendanceFormSignIn(forms.Form):
    pass


class AttendanceFormSignOut(forms.ModelForm):
    pass


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
