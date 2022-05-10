from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from .models import User
from .forms import UserForm
# Create your views here.


def Homepage(request):
    if request.method == "POST":
        
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Form Submitted')  
        print(form.errors.as_data())  
        return render(request,'users/login.html',{'form':UserForm()})
            
    else:
        form = UserForm()
        return render(request,'users/login.html',{'form':form})