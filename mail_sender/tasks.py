# -*- coding: utf-8 -*-
import os

from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import Subscriber
from dotenv import load_dotenv

load_dotenv()

EMAIL_TRACKER_SERVER = os.getenv("EMAIL_TRACKER_SERVER")


@shared_task
def send_mass_email(subject, message, sender_email):
    subscribers = Subscriber.objects.all()

    for subscriber in subscribers:
        context = {
            "first_name": subscriber.first_name or "дорогой подписчик",
            "last_name": subscriber.last_name or "",
            "birthday": subscriber.birthday.strftime("%d.%m.%Y") if subscriber.birthday else "",
            "message": message,
            "tracker_url": EMAIL_TRACKER_SERVER + "/tracker/?email=" + subscriber.email
        }
        html_message = render_to_string("email_template.html", context)
        plain_message = strip_tags(html_message)

        send_mail(
            subject=subject,
            message=plain_message,
            from_email=sender_email,
            recipient_list=[subscriber.email],
            fail_silently=False,
            html_message=html_message,
        )

