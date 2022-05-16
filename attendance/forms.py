# from django.contrib.auth.models import User
from django import forms
from .models import Attendance


class SessionForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['location']
