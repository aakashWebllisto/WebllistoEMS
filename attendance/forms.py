# from django.contrib.auth.models import User
from django import forms
from .models import Attendance,LeaveApplcation


class SessionForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['location']

class ApplyLeavesForm(forms.ModelForm):
    from_date = forms.DateField(widget=forms.SelectDateWidget)
    to_date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = LeaveApplcation
        fields = ['leave_type','from_date','to_date','from_session','to_session','applying_to','cc_to','contact_details','reason']
