from django.shortcuts import render
from django.http import HttpResponse


def pageSystem(request):

    uid = request.session.get('BMP_id')

    return HttpResponse(uid)