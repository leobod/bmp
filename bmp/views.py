from django.shortcuts import render
from django.http import HttpResponse

# 全局403、404、500错误自定义页面显示
def page_not_found(request, exception):
    return render(request, 'common/404.html', {"error_tips": "404 Page Not found", "error_code": "404"})

def page_error(request):
    return render(request, 'common/404.html', {"error_tips": "500 Page Error", "error_code": "500"})


def permission_denied(request, exception):
    return render(request, 'common/404.html', {"error_tips": "403 Permission_denied", "error_code": "403"})
