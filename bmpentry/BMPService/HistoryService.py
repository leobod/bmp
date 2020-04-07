
from bmpentry.BMPModel.DataModel import Order

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

