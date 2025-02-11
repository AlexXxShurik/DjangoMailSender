# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail

from .models import Subscriber
from .forms import MailingForm, SubscriberForm


def mailing_list(request):
    return render(request, 'mailing_list.html')


def create_mailing(request):
    if request.method == "POST":
        form = MailingForm(request.POST)
        if form.is_valid():
            mailing = form.save()

            subscribers = Subscriber.objects.all()
            recipient_list = [s.email for s in subscribers]

            send_mail(
                subject=mailing.subject,
                message=mailing.body,
                from_email='email@gmail.com',
                recipient_list=recipient_list,
                fail_silently=False,
            )

            return JsonResponse({"status": "success", "message": "Рассылка отправлена!"})
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