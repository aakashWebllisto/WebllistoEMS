from django.http import HttpResponse
from.forms import AttendanceFormSignIn,AttendanceFormSignOut
# Create your views here.

def homepage(request):
    return HttpResponse("AttendancePage")

def signin_view(request):
    if request.method == "POST":
        form = AttendanceFormSignIn()
        if form.is_valid():
            pass
    return HttpResponse("SignIn ")

def signout_view(request):
    return HttpResponse("SinOut")


