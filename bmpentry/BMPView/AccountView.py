"""
    @File: AccountView.py
    @Type: viewer -> (views)
    @Description: account的视图

    @Author: Leobod
    @Version: 1.0.0
    @Modify Time: 2020-02-19

    @Contract: leobod@eside.cn
    @License: ©2019-2020 leobod 苏ICP备17004905号
"""
from django.shortcuts import render
from django.http import HttpResponse

def pageLogin(request):
    return render(request, "login.html")

def doLogin(request):
    return HttpResponse("Hello")

