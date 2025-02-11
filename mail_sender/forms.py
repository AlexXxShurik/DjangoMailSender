from django import forms
from .models import Mailing, Subscriber


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['subject', 'body']


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ["first_name", "last_name", "email", "birthday"]

