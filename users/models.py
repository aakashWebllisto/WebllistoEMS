from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
# from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.contrib.auth.hashers import make_password, check_password


def upload_location(instance, filename):
    return "uploads/%s/img/%s" % (instance.email, filename)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=100,blank=False,null=False)
    phn_number = models.IntegerField(blank=False,null=False,default=9999999999)
    image = models.ImageField(upload_to=upload_location)
    residential_address = models.TextField(max_length=600,blank=False,null=False)
    current_address = models.TextField(max_length=600,blank=False,null=False)
    reporting_manager = models.ManyToManyField("self", symmetrical=False,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Attendance(models.Model):
    email = models.EmailField(('email address'))
    date = models.DateTimeField()
    timestamp_in = models.TimeField()
    timestamp_out = models.TimeField()
    rm_approval = models.BooleanField(default=False)
    leave_application = models.BooleanField(default=False)
    leave_application_approval = models.BooleanField(default=False)
    timing_duration = models.TimeField()


    def save(self, *args, **kwargs):
        self.timing_duration = self.timestamp_out - self.timestamp_in 
        super(Attendance, self).save(*args, **kwargs) # Call the "real" save() method.