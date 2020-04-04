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
from django.http import HttpResponse, HttpResponseRedirect

from bmpentry.BMPService import SmsService, AccountService

def isLogin(request):
    uid = request.session.get('BMP_id')
    print(uid)
    if uid == None:
        return render(request, "login.html")
    else:
        return HttpResponseRedirect('/system/')




def pageLogin(request):
    return render(request, "login.html")

def pageRegister(request):
    return render(request, "register.html")

def pageForget(request):
    return render(request, "forget.html")





def doLogin(request):
    if request.method == 'POST':  # 当提交表单时
        accountservice = AccountService()

        account = request.POST.get('account')
        password = request.POST.get('password')
        account_id = accountservice.queryPassword(account, password)
        if account_id != None:
            request.session['BMP_id'] = account_id
            return HttpResponse(True)
        else:
            return HttpResponse(False)
    else:
        return HttpResponse("NotSupport")

def doRegister(request):
    if request.method == 'POST':  # 当提交表单时
        smsservice = SmsService()
        accountservice = AccountService()

        account = request.POST.get('account')
        code = request.POST.get('code')
        password = request.POST.get('password')
        res = smsservice.matchSms(account, code)
        if res:
            res2  = accountservice.createAccount(account, password)
            return HttpResponse(res2)
    else:
        return HttpResponse("NotSupport")


def doSms(request):
    if request.method == 'POST':  # 当提交表单时
        account = request.POST.get('account')
        smsservice = SmsService()
        res = smsservice.sendSms(account)
        return HttpResponse(res)
    else:
        return HttpResponse("NotSupport")

def doForget(request):
    if request.method == 'POST':  # 当提交表单时
        smsservice = SmsService()
        accountservice = AccountService()

        account = request.POST.get('account')
        code = request.POST.get('code')
        password = request.POST.get('password')
        res = smsservice.matchSms(account, code)
        if res:
            res2  = accountservice.updateAccount(account, password)
            return HttpResponse(res2)
    else:
        return HttpResponse("NotSupport")


