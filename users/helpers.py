# Helpers for the users app
import smtplib
from django.conf import settings
from django.core.mail import send_mail

def mailer(subject,message,recipient_list):

    subject = 'welcome'
    message = 'Hi, thank you for registering'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["user.email"]
    send_mail( subject, message, email_from, recipient_list )