from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from .forms import UserForm,LoginForm
from .models import User
from django.conf  import settings 
from django.core.mail import send_mail,EmailMultiAlternatives
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# Create your views here.


def Homepage(request):
    if request.method == "POST":
        
        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            # rm = User.objects.get(email=request.reporting_manager)
            # form.cleaned_data['reporting_manager'] = rm
            form2 = form.save()
            form2.set_password(form.cleaned_data['password'])
            form2.save()
            subject = "Webllisto EMS User Registration"
            from_email = settings.EMAIL_HOST_USER
            to = form.cleaned_data['email']
            text_content = 'You have been registered at Webllisto'
            html_content = '<p><strong>HTML Templated </strong>Message</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return HttpResponse('Form Submitted')
        print(form.errors.as_data())  
        return render(request,'users/home.html',{'form':UserForm()})
            
    else:
        form = UserForm()
        return render(request,'users/home.html',{'form':form})





def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        user = authenticate(email=email, password=password)
        
        print(user)
        if user is not None:
            login(request, user)
            # data = User.objects.get(id=user.id)
            # Redirect to a success page.
            return render(request,'users/home.html')
        return render(request,'users/login_error.html')
    login_form = LoginForm()
    return render(request,'users/login.html',{'login_form':login_form})
        



def logout_view(request):
    logout(request)
    return render(request,'users/home.html')