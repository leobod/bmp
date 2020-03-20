from django.urls import path
from django.conf.urls import include, url

from bmpentry.BMPView import TestView

urlpatterns = [
    path('', TestView.index),
    # url(r'^index', TestView.index),
]
