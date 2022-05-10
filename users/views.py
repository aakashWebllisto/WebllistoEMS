from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import UserForm
from django.conf  import settings 
from django.core.mail import send_mail
# Create your views here.


def Homepage(request):
    if request.method == "POST":
        
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            subject = "Webllisto EMS User Registration"
            message = "You have successfully registered to Webllisto"
            to = form.cleaned_data['email']
            send_mail(subject,message,settings.EMAIL_HOST_USER,[to])
            return HttpResponse('Form Submitted')  
        print(form.errors.as_data())  
        return render(request,'users/login.html',{'form':UserForm()})
            
    else:
        form = UserForm()
        return render(request,'users/login.html',{'form':form})