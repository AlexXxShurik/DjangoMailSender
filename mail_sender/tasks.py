from celery import shared_task
from django.core.mail import send_mail
from .models import Subscriber


@shared_task
def send_mass_email(subject, message, sender_email):
    subscribers = Subscriber.objects.all()
    recipient_list = [s.email for s in subscribers]

    send_mail(
        subject=subject,
        message=message,
        from_email=sender_email,
        recipient_list=recipient_list,
        fail_silently=False,
    )
