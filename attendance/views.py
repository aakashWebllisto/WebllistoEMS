import datetime
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, redirect
from users.models import User
from .models import Attendance
from .forms import SessionForm


# Create your views here.


def attendance(request):
    if request.user.is_authenticated:
        user = User.objects.get(email=request.user.email)
        print((user.reporting_manager.all()))
        print(user)
        # for e in user.reporting_manager.all():
        #     print(e)
        # rm = User.objects.get(reporting_manager=user)
        form = SessionForm()
        return render(request, 'attendance/attendance.html', {'user': user, 'form': form, 'signin': False})
    else:
        return redirect('/users/login')



def signin_view(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():

            user = User.objects.get(email=request.user.email)

            attendance = Attendance()
            attendance.email = str(request.user)
            attendance.date = str(datetime.date.today())
            attendance.timestamp_in = str(datetime.datetime.now())
            attendance.location = str(form.cleaned_data['location'])
            attendance.rm = user.reporting_manager.first()
            attendance.save()



            return render(request, 'attendance/attendance.html', {'user': user, 'form': form, 'signin': True})


def signout_view(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            Attendance.objects.filter(email=request.user, date=datetime.date.today()).update(
                timestamp_out=str(datetime.datetime.now()), location=str(form.cleaned_data['location']))
            Attendance.objects.filter(email=request.user, date=datetime.date.today())\
                .update(timing_duration=F('timestamp_out')-F('timestamp_in'))

        return redirect('/users/home')

    # return render(request, 'attendance/attendance.html', {'form': SessionForm()})
