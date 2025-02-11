from django.conf.urls import url
from .views import mailing_list, create_mailing

urlpatterns = [
    url(r'^$', mailing_list, name='mailing_list'),
    url(r'^create/$', create_mailing, name='create_mailing'),
]
