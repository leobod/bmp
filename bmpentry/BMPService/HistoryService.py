
from bmpentry.BMPModel.DataModel import Order, Account
import os

class HistoryService:

    def __init__(self):
        pass

    def querySum(self, aid):
        Data = Order.objects.filter(aid=str(aid))
        return len(Data)

    def queryData(self, aid, start):
        length = self.querySum(str(aid))
        if length < 11:
            Data = Order.objects.filter(aid=str(aid)).order_by("-oid")[0:length]
        else:
            if start < length:
                if start + 10 <= length:
                    Data = Order.objects.filter(aid=str(aid)).order_by("-oid")[start:start+10]
                else:
                    Data = Order.objects.filter(aid=str(aid)).order_by("-oid")[start:length]
            else:
                pass
        QueryData = []
        i = 1
        for d in Data:
            if d.oratiored != None:
                d.oratiored = d.oratiored * 100
            if d.oratiogreen != None:
                d.oratiogreen = d.oratiogreen * 100
            if d.oratioother != None:
                d.oratioother = d.oratioother * 100
            if d.oresulta != None:
                if d.oresulta == 1:
                    d.oresulta = "A"
                else:
                    d.oresulta = "B"
            if d.oresultall != None:
                if d.oresultall == 1:
                    d.oresultall = "有妊娠"
                else:
                    d.oresultall = "无"
            history = {
                "oid": d.oid,
                "ostatus": d.ostatus,
                "oratiored": d.oratiored,
                "oratiogreen": d.oratiogreen,
                "oratioother": d.oratioother,
                "oresulta": d.oresulta,
                "oresultb": d.oresultb,
                "oresultall": d.oresultall,
                "odir": d.odir
            }
            QueryData.append((i,history))
            i = i+1
        return QueryData

    def createInitOrder(self, aid):
        a0 = Account.objects.filter(aid=aid)
        a1 = a0.get(aid=aid)
        order = Order()
        order.aid = a1
        order.ostatus = "0"
        order.odir = "static/data/"
        order.save()

        order.odir = "static/data/" + str(a1.aid) + "/" + str(order.oid) + "/"
        os.makedirs(order.odir)
        order.ostatus = "1"
        order.save()
        return order.oid, order.odir

    def changeStatus(self, oid, ostatus):
        order = Order.objects.get(oid=oid)
        order.ostatus = ostatus
        order.save()


    def updateRatio(self, oid, oratiored, oratiogreen):
        order = Order.objects.get(oid=oid)
        order.oratiored = oratiored
        order.oratiogreen = oratiogreen
        order.oratioother = 1-oratiored-oratiogreen
        order.ostatus = "3"
        order.save()

    def updateResult(self, oid, oresulta, oresultall):
        order = Order.objects.get(oid=oid)
        order.oresulta = oresulta
        order.oresultall = oresultall
        order.ostatus = "4"
        order.save()

    def queryRatio(self, oid):
        order = Order.objects.get(oid=oid)
        return order.oratiored, order.oratiogreen, order.oratioother


