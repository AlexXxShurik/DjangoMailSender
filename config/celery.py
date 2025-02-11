from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config', broker=os.getenv('CELERY_BROKER_URL'))

app.config_from_object('django.conf:settings')

app.autodiscover_tasks(['mail_sender'])
