"""
    @File: AccountUrl.py
    @Type: controller -> (urls)
    @Description: /account/路径下对应的匹配项

    @Author: Leobod
    @Version: 1.0.0
    @Modify Time: 2020-02-19

    @Contract: leobod@eside.cn
    @License: ©2019-2020 leobod 苏ICP备17004905号
"""
from django.urls import path
from django.conf.urls import include, url

from bmpentry.BMPView import TestView

urlpatterns = [
    path('', TestView.index),
    # url(r'^index', TestView.index),
]
