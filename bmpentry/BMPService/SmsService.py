

# Create your tests here.
# import os,django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bmp.settings")# project_name 项目名称
# django.setup()

import random

from bmpentry.BMPModel.Message import SmsByAli

from bmpentry.BMPModel.DataModel import Smscode

class SmsService:
    def randomCode(self):
        str = ""
        for i in range(6):
            ch = chr(random.randrange(ord('0'), ord('9') + 1))
            str += ch
        return str


    def __init__(self):
        pass

    def sendSms(self, phone):
        code = self.randomCode()
        res = self.sendSmsByAli(phone, code)
        print(res)
        if res["Code"] == "OK":
            bizcode = res['BizId']
            self.saveSmscode(phone, code, bizcode)
            return True
        else:
            return False

    def sendSmsByAli(self, phone, code):
        res = SmsByAli.actionSendSms(phone, code)
        return res

    def saveSmscode(self, phone, code, bizcode):
        smscode = Smscode()
        smscode.phone = phone
        smscode.code = code
        smscode.bizcode = bizcode
        smscode.save()



    def matchSms(self, phone, code):
        a0 = Smscode.objects.filter(phone=str(phone)).order_by("-effective_time")[:1]
        for a in a0:
            # print(a.code)
            if a.code == code:
                return True
        return False


# smss = SmsService()


# res = smss.sendSms("13952348337")
# print(res)


# res = smss.matchSms("13952348337", "737680")
# print(res)


