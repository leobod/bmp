# Create your tests here.
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bmp.settings")# project_name 项目名称
django.setup()

from bmpentry.BMPModel.DataModel import Account, Order, User
from django.core import serializers

from json import dumps, loads

from bmpentry.BMPService import HistoryService

def createAccount():
    account = Account()
    account.phone = "13952348340"
    account.password = "Aa12345678"
    account.astatus = "1"
    res = account.save()
    print(res)

def getAllAccount():
    res = Account.objects.all()
    for a in res:
        print(a.phone)

def getAccount():
    a0 = Account.objects.filter(phone="13952348337")
    a1 = a0.get(phone="13952348337")
    a1.password = "Aa123123"
    a1.save()


def createOrder():
    a0 = Account.objects.filter(phone="15651666029")
    a1 = a0.get(phone="15651666029")
    order = Order()
    order.aid = a1
    order.ostatus = "1"
    order.odir = "/static/data/10/"

    order.save()

    order.odir ="/static/data/"+ str(a1.aid) + "/" +str(order.oid)
    print(order.odir)
    order.save()

def queryOrder():
    D = Order.objects.filter(aid="16")
    print(len(D))
    data = serializers.serialize("json", Order.objects.filter(aid="16"))
    print(len(data))
    print(data)

    # orders = Order.objects.filter(aid="16")
    # for order in orders:
    #     print(order.toJSON())


if __name__ == "__main__":
    # queryOrder()
    # a = list(range(0, 9, 1))
    # print(a[2:3])

    h = HistoryService()
    print(h.queryRatio("10"))


