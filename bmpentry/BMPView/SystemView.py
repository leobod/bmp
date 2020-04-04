from django.shortcuts import render
from django.http import HttpResponse

from bmpentry.BMPModel.DataModel import Account, User

def pageSystem(request):
    aid = request.session.get('BMP_id')
    print(aid)
    if aid == None:
        return render(request, "login.html")
    else:
        users = User.objects.filter(aid=str(aid))[0:1]
        for user in users:
            user_name = user.uname

        return render(request, "./system.html", {"user_name": user_name})


def pageUpload(request):
    return render(request, "./upload.html")

def doExit(request):
    del request.session['BMP_id']
    return HttpResponse(True)

def doUpload(request):
    print(request)
    print(request.POST.get('img'))
    print(request.FILES)
    print(request.FILES.get('img'))
