# Create your tests here.
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bmp.settings")# project_name 项目名称
django.setup()

from bmpentry.BMPModel.DataModel import Account


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

if __name__ == "__main__":
    createAccount()