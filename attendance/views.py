import datetime

from django.http import HttpResponse
from.forms import AttendanceFormSignIn,AttendanceFormSignOut
from django.shortcuts import render
from users.models import User
from .models import Attendance
# Create your views here.



def attendance(request):
    if request.user:
        user = User.objects.filter(reporting_manager=request.user)


        return render(request, 'attendance/attendance.html', {'user': user})

def signin_view(request):
    user = User.objects.get(email=request.user)
    attendance = Attendance()
    attendance.email= request.user
    attendance.date = datetime.date.today()
    attendance.timestamp_in = datetime.time()
    return HttpResponse("SignOut")


def signout_view(request):
    return HttpResponse("SignIn")


