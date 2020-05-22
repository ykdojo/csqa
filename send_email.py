# This is just a script for testing email sending.
# Run this with:
# ./manage.py shell < send_email.py
from django.core.mail import send_mail
from django.conf import settings
subject = 'Testing subject'
message = 'body'
email_from = settings.EMAIL_HOST_USER
recipient_list = ['csqa@csdojo.io',]
send_mail(subject, message, email_from, recipient_list)