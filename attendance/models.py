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
    timestamp_in = models.DateTimeField(default=datetime.time(), blank=False, null=False)
    timestamp_out = models.DateTimeField(blank=True, null=True)
    timing_duration = models.CharField(max_length=200, blank=True, null=True)
    rm = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=20, choices=LOCALE_CHOICES, default='office')
    signin = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.timestamp_out:
            self.timing_duration = self.timestamp_out - self.timestamp_in
            super(Attendance, self).save(*args, **kwargs)
        else:
            super(Attendance, self).save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return (self.email + ":" + str(self.date))


LEAVE_CHOICES = (
    ('loss of pay', 'LOSS OF PAY'),
    ('comp - off', 'COMP - OFF'),
)
SESSION_CHOICES = (
    ('session1', 'SESSION1'),
    ('session2', 'SESSION2'),
)


class LeaveApplcation(models.Model):
    email = models.EmailField(blank=True, null=True)
    leave_type = models.CharField(max_length=20, choices=LEAVE_CHOICES, default='loss of pay')
    from_date = models.DateTimeField(default=datetime.date.today(), null=False, blank=False)
    to_date = models.DateTimeField(null=False, blank=False)
    from_session = models.CharField(max_length=20, choices=SESSION_CHOICES, default='session1')
    to_session = models.CharField(max_length=20, choices=SESSION_CHOICES, default='session2')
    applying_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applyingTo_leave_user')
    cc_to = models.EmailField()  # reason,mail to hr, cc to rm,to user as well
    contact_details = models.CharField(max_length=200, blank=False, null=False)
    reason = models.TextField(blank=False, null=False)
    total_leaves = models.IntegerField(default=10, blank=True, null=True)
    leaves_taken = models.IntegerField(blank=True, null=True)
    rm = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rm_leave_user', null=True)
    rm_approval = models.BooleanField(default=False)

    def __str__(self):
        return (self.email + ":" + str(self.applying_to))

    # def save(self, *args, **kwargs):
    #     if self.timestamp_out:
    #         self.timing_duration = self.timestamp_out - self.timestamp_in
    #         super(Attendance, self).save(*args, **kwargs)
    #     else:
    #         super(Attendance, self).save(*args, **kwargs)  # Call the "real" save() method.
    #
