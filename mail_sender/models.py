from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    birthday = models.DateField(null=True, blank=True)
    last_opened = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.email


class Mailing(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject
