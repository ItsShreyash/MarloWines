from django.core.mail import send_mail
from django.conf import settings

def send_email_to_client(usermail):
    subject = "Thanks for Signing Up to MAARLOWINES"
    message = "We would love to provide you our service"
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject , message , from_email, usermail)