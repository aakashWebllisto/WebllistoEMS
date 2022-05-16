import datetime

from django.http import HttpResponse
from django.shortcuts import render
from users.models import User
from .models import Attendance
from .forms import SessionForm

# Create your views here.


def attendance(request):
    if request.user:

        user = User.objects.filter(email=request.user)

        # rm = User.objects.get(reporting_manager=user)
        form = SessionForm()
        return render(request, 'attendance/attendance.html', {'user': user,'form':form ,'signin':False})


def signin_view(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data['location'])
            user = User.objects.get(email=request.user)
            # rm = user.rm
            attendance = Attendance()
            attendance.email = request.user
            attendance.date = datetime.date.today()
            attendance.timestamp_in = datetime.time()
            # attendance.location = str(form.cleaned_data['location'])
            attendance.save()
            # return HttpResponse("Form sent")
            return render(request, 'attendance/attendance.html', {'user': user, 'form': form, 'signin': True})


def signout_view(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data['location'])
            attendance = Attendance.objects.filter(email=request.user,date = datetime.date.today()).update(timestamp_out = datetime.time())
            # attendance.timestamp_out = datetime.time()
            # attendance.location = str(form.cleaned_data['location'])
            attendance.save()
            # return HttpResponse("Form sent")
            return render(request, 'attendance/attendance.html', {'user': user, 'form': form, 'signin': False})

