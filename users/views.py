from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from .models import User
from .forms import UserForm
# Create your views here.


def Homepage(request):
    if request.method == "GET":
        
        form = UserForm()
        return render(request,'users/login.html',{'form':form})
    else:
        form = request.POST
        if form.is_valid():
            cd = form.cleaned_data
            name = cd.get('name')
            email = cd.get('email')
            password = cd.get('password')
            phn = cd.get('phn')
            resAdd = cd.get('resAdd')
            curAdd = cd.get('curAdd')
            img = cd.get('img[]')
            print(name)
            