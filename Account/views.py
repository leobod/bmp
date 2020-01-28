from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,World!")

def calculate(request):
    a = request.GET["a"]
    b = request.GET["b"]

    c = int(a) + int(b)
    return HttpResponse(str(a) + "+" + str(b) + "=" + str(c))

def add(request, a:int, b:int):
    c = int(a) + int(b)
    return HttpResponse(str(a) + "+" + str(b) + "=" + str(c))

def home(request):
    return render(request, "Account/home.html", {"re_loc" : "http://localhost:8000/Account/add/"})


