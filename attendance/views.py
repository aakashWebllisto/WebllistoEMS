import datetime
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, redirect
from users.models import User
from .models import Attendance,LeaveApplcation
from .forms import SessionForm, ApplyLeavesForm
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings


# Create your views here.


def attendance(request):
    if request.user.is_authenticated:
        user = User.objects.get(email=request.user.email)
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
            Attendance.objects.filter(email=request.user, date=datetime.date.today()) \
                .update(timing_duration=F('timestamp_out') - F('timestamp_in'))

        return redirect('/users/home')

    # return render(request, 'attendance/attendance.html', {'form': SessionForm()})


def leaves(request):
    if request.user.is_authenticated:
        # user = User.objects.get(email=request.user.email)
        form = ApplyLeavesForm()
        return render(request, 'attendance/leaves.html', {'form': form})
    else:
        return redirect('/users/login')


def apply_leaves(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            user = User.objects.get(email=request.user.email)
            model_obj = LeaveApplcation(email=request.user.email, rm=user.reporting_manager.first())
            form2 = ApplyLeavesForm(request.POST)
            # form2 = ApplyLeavesForm(request.POST)
            if form2.is_valid():
                # form.cleaned_data['email'] = request.user.email
                model_obj.applying_to = form2.cleaned_data.get('applying_to')
                model_obj.leave_type = form2.cleaned_data.get('leave_type')
                model_obj.from_date = form2.cleaned_data.get('from_date')
                model_obj.to_date = form2.cleaned_data.get('to_date')
                model_obj.from_session = form2.cleaned_data.get('from_session')
                model_obj.to_session = form2.cleaned_data.get('to_session')
                model_obj.cc_to = form2.cleaned_data.get('cc_to')
                model_obj.contact_details = form2.cleaned_data.get('contact_details')
                model_obj.reason = form2.cleaned_data.get('reason')
                model_obj.leaves_taken = (form2.cleaned_data.get('to_date')-form2.cleaned_data.get('from_date')).days+1
                model_obj.save()


                # Send respective mails
                subject = "Webllisto EMS Leave Application"
                from_email = settings.EMAIL_HOST_USER
                to = form2.cleaned_data['applying_to']
                cc_to = [form2.cleaned_data['cc_to'],user.reporting_manager.first()]
                text_content = 'You have applied for leave at Webllisto'
                html_content = '<p><strong>Leaves Applied</strong> for <strong>'+str(form2.cleaned_data['from_date'])+' to '+str(form2.cleaned_data['to_date'])+'</strong></p>'
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to],cc=cc_to)
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                return render(request,'attendance/leave_applied_success.html',{'msg':'Leave applied successfully'})

            else:
                return HttpResponse('Form invalid')

        else:     # For GET request method
            form = ApplyLeavesForm()
            # unique_rm = User.objects.order_by('reporting_manager')#.values('reporting_manager').distinct()
            # print(unique_rm)
            # is_rm = False
            # if request.user.email in unique_rm:
            #     is_rm = True
            return render(request,'attendance/leaves.html',{'form':form})

    else:
        return redirect('/users/home')


def approve_leaves(request):
    user = User.objects.filter(reporting_manager=User.objects.get(email=request.user.email)).first()
    leaves_applied = LeaveApplcation.objects.filter(email=user).first()
    if leaves_applied:
        LeaveApplcation.objects.filter(email=user).update()
    print(leaves_applied)
    return render(request,'attendance/approve_leaves.html')

