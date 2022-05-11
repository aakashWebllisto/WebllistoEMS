from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('users/home', views.Homepage),
    path("users/login", views.login_view)
    
    ]
