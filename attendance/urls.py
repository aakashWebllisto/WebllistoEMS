from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('attendance/attendance', views.attendance),
    path("attendance/signin", views.signin_view),
    path("attendance/signout", views.signout_view),

]
