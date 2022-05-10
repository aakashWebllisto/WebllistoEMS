from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import User
# Create your views here.


def Homepage(request):
    return render(request,'users/login.html')