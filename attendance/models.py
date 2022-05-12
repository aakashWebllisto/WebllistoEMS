import datetime

from django.db import models
# from users.apps.UsersConfig import models.User


class Attendance(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(default=datetime.date.today(),blank=False,null=False)
    timestamp_in = models.TimeField(default=datetime.time(),blank=False,null=False)
    timestamp_out = models.TimeField(blank=False,null=False)
    timing_duration = models.TimeField()
    # user = models.ForeignKey(User)

    def save(self, *args, **kwargs):
        self.timing_duration = self.timestamp_out - self.timestamp_in
        super(Attendance, self).save(*args, **kwargs)  # Call the "real" save() method.


# class Leaves(models.model):
#     rm_approval = models.BooleanField(default=False)
#     leave_application = models.BooleanField(default=False)
#     leave_application_approval = models.BooleanField(default=False)  # initial pending
#     # reason,mail to hr, cc to rm,to user as well
#     timing_duration = models.TimeField()
