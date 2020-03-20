from django.urls import path
from django.conf.urls import include, url

from bmpentry.BMPView import TestView

urlpatterns = [
    url(r'^index', TestView.index),
]
