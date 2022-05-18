from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('attendance/attendance', views.attendance),
    path("attendance/signin", views.signin_view),
    path("attendance/signout", views.signout_view),
    path("attendance/leaves", views.leaves),
    path("attendance/apply_leaves", views.apply_leaves),
    path("attendance/approve_leaves", views.approve_leaves),

]
