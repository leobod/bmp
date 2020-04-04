
from bmpentry.BMPModel.DataModel import Account

class AccountService:

    def __init__(self):
        pass

    def createAccount(self, account, password):
        try:
            a0 = Account()
            a0.phone = str(account)
            a0.password = str(password)
            a0.astatus = "1"
            a0.save()
        except Exception as e:
            print("createAccount Exception: " + str(e))
            return False
        return True

    def queryPassword(self, account, password):
        a0 = Account.objects.filter(phone=account)[:1]
        for a in a0:
            if a.password == password:
                return a.aid
        return None

    def updateAccount(self, account, password):
        try:
            a0 = Account.objects.filter(phone=str(account))
            a1 = a0.get(phone=str(account))
            a1.phone = str(account)
            a1.password = str(password)
            a1.astatus = "1"
            a1.save()
        except Exception as e:
            print("updateAccount Exception: " + str(e))
            return False
        return True


