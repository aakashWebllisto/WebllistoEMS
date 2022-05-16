import datetime
# from .users.models import User
from django.db import models
from users.models import User
from django.utils.timezone import now


class Attendance(models.Model):
    email = models.EmailField(blank=False,null=False)
    date = models.DateTimeField(default=now(), blank=False,null = False)
    timestamp_in = models.TimeField(blank=False)
    timestamp_out = models.TimeField(blank=True)
    timing_duration = models.TimeField(blank=True, null=True)
    rm = models.OneToOneField(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.timestamp_out:
            self.timing_duration = self.timestamp_out - self.timestamp_in

        super(Attendance, self).save(*args, **kwargs)  # Call the "real" save() method.

# class Leaves(models.model):
#     rm_approval = models.BooleanField(default=False)
#     leave_application = models.BooleanField(default=False)
#     leave_application_approval = models.BooleanField(default=False)  # initial pending
#     # reason,mail to hr, cc to rm,to user as well
#     timing_duration = models.TimeField()
