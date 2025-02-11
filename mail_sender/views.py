from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from .models import Subscriber
from .forms import MailingForm


def mailing_list(request):
    return render(request, 'mail_sender/mailing_list.html')


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
