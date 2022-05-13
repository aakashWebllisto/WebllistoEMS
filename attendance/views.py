from django.http import HttpResponse
from.forms import AttendanceFormSignIn,AttendanceFormSignOut
from django.shortcuts import render
# Create your views here.

def attendance(request):
    return render(request, 'attendance/attendance.html')

def signin_view(request):
    pass


def signout_view(request):
    return HttpResponse("SinOut")


