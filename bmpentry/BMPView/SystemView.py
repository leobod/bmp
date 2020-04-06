from django.shortcuts import render
from django.http import HttpResponse

from bmpentry.BMPModel.DataModel import Account, User

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

        return render(request, "./history.html", {"user_name": user_name})

def pageResult(request):
    aid = request.session.get('BMP_id')
    if aid == None:
        return render(request, "login.html")
    else:
        user_name = request.session.get('BMP_user')

        return render(request, "./result.html", {"user_name": user_name})

def doExit(request):
    del request.session['BMP_id']
    del request.session['BMP_user']
    return HttpResponse(True)

def doUpload(request):
    if request.method == "POST":
        imgfile = request.FILES.get('img')
        print(imgfile)
        print(imgfile.size)
        print(imgfile.content_type)
        fobj = open("./test.jpg", 'wb');
        for chrunk in imgfile.chunks():
            fobj.write(chrunk);
        fobj.close();

        # imgfile.name 文件名称
    # print(request)
    # print(request.POST.get('img'))
    # print(request.FILES)
    # print(request.FILES.get('img'))
