from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Account import views as AccountViews



urlpatterns = [
    url(r'^index', AccountViews.index),
    url(r'^calculate', AccountViews.calculate),
    url(r'^add/(?P<a>[0-9]+)/(?P<b>[0-9]+)/', AccountViews.add),
    url(r'home/', AccountViews.home),
]