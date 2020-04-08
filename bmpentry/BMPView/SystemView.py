from django.shortcuts import render
from django.http import HttpResponse

from bmpentry.BMPModel.DataModel import Account, User
from bmpentry.BMPService import HistoryService, PicService

def pageSystem(request):
    aid = request.session.get('BMP_id')
    if aid == None:
        return render(request, "login.html")
    else:
        user_name = request.session.get('BMP_user')

        return render(request, "./system.html", {"user_name": user_name})


def pageUpload(request):
    aid = request.session.get('BMP_id')
    if aid == None:
        return render(request, "login.html")
    else:
        user_name = request.session.get('BMP_user')

        return render(request, "./upload.html", {"user_name": user_name})

def pageHistory(request):
    aid = request.session.get('BMP_id')
    if aid == None:
        return render(request, "login.html")
    else:
        user_name = request.session.get('BMP_user')
        history_obj = HistoryService()
        querydata = history_obj.queryData(aid,0)
        return render(request, "./history.html", {"user_name": user_name, "querydata": querydata, "currentpage": "1"})

# def pageResult(request):
#     aid = request.session.get('BMP_id')
#     if aid == None:
#         return render(request, "login.html")
#     else:
#         user_name = request.session.get('BMP_user')
#
#
#         return render(request, "./result.html", {"user_name": user_name})

def doExit(request):
    del request.session['BMP_id']
    del request.session['BMP_user']
    return HttpResponse(True)

def doUpload(request):
    if request.method == "POST":
        aid = request.session.get('BMP_id')
        user_name = request.session.get('BMP_user')

        imgfile = request.FILES.get('img')

        picprocess = PicService()
        picprocess.doChain(aid, imgfile)

        history_obj = HistoryService()
        querydata = history_obj.queryData(aid,0)
        return render(request, "./history.html", {"user_name": user_name, "querydata": querydata})
    else:
        return HttpResponse("NotSupport")

def doResult(request):
    if request.method == "POST":
        aid = request.session.get('BMP_id')
        if aid == None:
            return render(request, "login.html")
        else:
            oid = request.POST.get("oid")
            print(oid)
            user_name = request.session.get('BMP_user')
            history_obj = HistoryService()
            resulta, resultb, resultall = history_obj.queryResult(oid)
            return render(request, "./result.html", {"user_name": user_name, "aid": aid, "oid": oid , 'resulta': resulta, 'resultall': resultall})


    else:
        return HttpResponse("NotSupport")

def doHistory(request):
    if request.method == "POST":
        aid = request.session.get('BMP_id')
        if aid == None:
            return render(request, "login.html")
        else:
            user_name = request.session.get('BMP_user')
            history_obj = HistoryService()

            currentpage = request.POST.get("currentpage")
            nextpage = request.POST.get("nextpage")
            if currentpage == "1":
                if nextpage == "-1":
                    querydata = history_obj.queryData(aid, 0)
                    return render(request, "./history.html",
                                  {"user_name": user_name, "querydata": querydata, "currentpage": "1"})
                else:
                    querydata = history_obj.queryData(aid, int(currentpage)*10)
                    return render(request, "./history.html",
                                  {"user_name": user_name, "querydata": querydata, "currentpage": int(currentpage) + int(nextpage)})
            else:
                if nextpage == "-1":
                    querydata = history_obj.queryData(aid, (int(currentpage)-2)*10)
                    return render(request, "./history.html",
                                  {"user_name": user_name, "querydata": querydata, "currentpage": int(currentpage) + int(nextpage)})
                else:
                    querydata = history_obj.queryData(aid, int(currentpage)*10)
                    return render(request, "./history.html", {"user_name": user_name, "querydata": querydata, "currentpage": int(currentpage) + int(nextpage)})
    else:
        return HttpResponse("NotSupport")