from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^subscribers/$', views.SubscriberApi.as_view(), name='subscribers'),
]
