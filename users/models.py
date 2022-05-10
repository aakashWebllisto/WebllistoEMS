from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
# from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=100,blank=False,null=False)
    phn_number = models.IntegerField(blank=False,null=False,default=0000000000)
    image = models.ImageField(upload_to='images/')
    residential_address = models.TextField(max_length=600,blank=False,null=False)
    current_address = models.TextField(max_length=600,blank=False,null=False)
    reporting_manager = models.ManyToManyField("self", symmetrical=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email