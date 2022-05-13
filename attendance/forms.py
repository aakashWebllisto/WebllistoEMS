# from django.contrib.auth.models import User
from django import forms
from .models import Attendance


class AttendanceFormSignIn(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Attendance
        fields = ['timestamp_in']


class AttendanceFormSignOut(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Attendance
        fields = ['timestamp_out']


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
