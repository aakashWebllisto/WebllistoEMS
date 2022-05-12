from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("AttendancePage")

def signin_view(request):
    return HttpResponse("SignIn ")

def signout_view(request):
    return HttpResponse("SinOut")


