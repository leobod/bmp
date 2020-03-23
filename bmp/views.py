"""
    @File: views.py
    @Type: viewer -> (views)
    @Description: 通用的的视图

    @Author: Leobod
    @Version: 1.0.0
    @Modify Time: 2020-02-22

    @Contract: leobod@eside.cn
    @License: ©2019-2020 leobod 苏ICP备17004905号
"""

# # Code Start
# 视图相关的基本模块
from django.shortcuts import render
from django.http import HttpResponse
# 重置静态文件加载需要用到的模块
from django.contrib.staticfiles.views import serve

# 使用insecure=True来解决部署环境中静态文件加载问题
def return_static(request, path, insecure=True, **kwargs):
  return serve(request, path, insecure, **kwargs)

# 全局404 page not found 错误自定义页面显示
def page_not_found(request, exception):
    return render(request, 'common/404.html', {"error_tips": "404 Page Not found", "error_code": "404"})

# 全局405 page error 错误自定义页面显示
def page_error(request):
    return render(request, 'common/404.html', {"error_tips": "500 Page Error", "error_code": "500"})

# 全局403 permission denied 错误自定义页面显示
def permission_denied(request, exception):
    return render(request, 'common/404.html', {"error_tips": "403 Permission_denied", "error_code": "403"})
