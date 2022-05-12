# from django.contrib.auth.models import User
from django import forms
from .models import Attendance


class AttendanceForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Attendance
        fields = ['email', 'date', 'timestamp_in', 'timestamp_out']


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)