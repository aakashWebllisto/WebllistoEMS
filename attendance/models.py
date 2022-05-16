import datetime
# from .users.models import User
from django.db import models
from users.models import User
# from django.utils.timezone import now

LOCALE_CHOICES = (
    ('client location', 'CLIENT LOCATION'),
    ('office', 'OFFICE'),
    ('on duty', 'ON DUTY'),
    ('Work from home', 'WORK FROM HOME'),

)


class Attendance(models.Model):
    email = models.EmailField(blank=False, null=False)
    date = models.DateTimeField(default=datetime.date.today(), blank=False, null=False)
    timestamp_in = models.DateTimeField(blank=False, null=False)
    timestamp_out = models.DateTimeField(blank=True, null=True)
    timing_duration = models.CharField(max_length=200, blank=True, null=True)
    rm = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=20, choices=LOCALE_CHOICES, default='office')

    def save(self, *args, **kwargs):
        if self.timestamp_out:
            self.timing_duration = self.timestamp_out - self.timestamp_in
            super(Attendance, self).save(*args, **kwargs)
        else:
            super(Attendance, self).save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return (self.email + ":" + str(self.date))

# class Leaves(models.model):
#     rm_approval = models.BooleanField(default=False)
#     leave_application = models.BooleanField(default=False)
#     leave_application_approval = models.BooleanField(default=False)  # initial pending
#     # reason,mail to hr, cc to rm,to user as well
#     timing_duration = models.TimeField()
