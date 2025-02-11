# -*- coding: utf-8 -*-
import os

from django.http import JsonResponse
from django.shortcuts import render

from .tasks import send_mass_email
from .models import Subscriber
from .forms import MailingForm, SubscriberForm
from dotenv import load_dotenv

load_dotenv()


def mailing_list(request):
    return render(request, 'mailing_list.html')


def create_mailing(request):
    if request.method == "POST":
        form = MailingForm(request.POST)
        if form.is_valid():
            mailing = form.save()

            send_mass_email.apply_async(
                kwargs={
                    "subject": mailing.subject,
                    "message": mailing.body,
                    "sender_email": os.getenv('EMAIL_HOST_USER'),
                },
                serializer="json"
            )

            return JsonResponse({"status": "success", "message": "Рассылка запущена!"})
        else:
            return JsonResponse({"status": "error", "errors": form.errors})

    return JsonResponse({"status": "error", "message": "Используйте POST-запрос"})


def subscribers_list(request):
    return render(request, 'subscribers_list.html')


def get_subscribers(request):
    subscribers = Subscriber.objects.all().values("first_name", "last_name", "email", "birthday")
    data = [
        {
            "first_name": sub["first_name"] or "",
            "last_name": sub["last_name"] or "",
            "email": sub["email"],
            "birthday": sub["birthday"].strftime("%Y-%m-%d") if sub["birthday"] else None
        }
        for sub in subscribers
    ]
    return JsonResponse(data, safe=False)


def add_subscriber(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success", "message": "Подписчик добавлен!"})
        return JsonResponse({"status": "error", "errors": form.errors})

    return JsonResponse({"status": "error", "message": "Используйте POST-запрос"})