"""
    @File: TestView.py
    @Type: viewer -> (views)
    @Description:  用于练习与测试效果的视图

    @Author: Leobod
    @Version: 1.0.0
    @Modify Time: 2020-02-19

    @Contract: leobod@eside.cn
    @License: ©2019-2020 leobod 苏ICP备17004905号
"""
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,World!")

def calculate(request):
    a = request.GET["a"]
    b = request.GET["b"]

    c = int(a) + int(b)
    return HttpResponse(str(a) + "+" + str(b) + "=" + str(c))

def add(request, a:int, b:int):
    c = int(a) + int(b)
    return HttpResponse(str(a) + "+" + str(b) + "=" + str(c))



