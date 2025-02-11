from django.conf.urls import url
from .views import mailing_list, create_mailing, subscribers_list, get_subscribers, add_subscriber

urlpatterns = [
    url(r'^$', mailing_list, name='mailing_list'),
    url(r'^subscribers$', subscribers_list, name='subscribers_list'),
    url(r'^create/$', create_mailing, name='create_mailing'),
    url(r'^subscribers/add$', add_subscriber, name='add_subscriber'),
    url(r'^subscribers/list$', get_subscribers, name='get_subscribers'),
]
