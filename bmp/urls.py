"""
    @File: urls.py
    @Type: controller -> (urls)
    @Description: 通用的的视图

    @Author: Leobod
    @Version: 1.0.0
    @Modify Time: 2020-02-22

    @Contract: leobod@eside.cn
    @License: ©2019-2020 leobod 苏ICP备17004905号
"""

# # Code Start
# 路径匹配需要的模块
from django.urls import path
from django.conf.urls import include, url
# 使用insecure=True来解决部署环境中静态文件加载问题
from django.urls import re_path
# 对应的一些基本视图
from .views import page_error, page_not_found, permission_denied, return_static
from bmpentry.BMPView import HomeView


urlpatterns = [
    path('', HomeView.index),
    path('account/', include('bmpentry.BMPUrl.AccountUrl')),
    re_path(r'^static/(?P<path>.*)$', return_static, name='static'),
]

# 重定义错误跳转页面
handler403 = permission_denied
handler404 = page_not_found
handler500 = page_error

"""URL 配置说明

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
Example
    # path('admin/', admin.site.urls),                              # 注销admin管理界面
    # path('account/', include('bmpentry.BMPUrl.AccountUrl')),
    # re_path(r'^static/(?P<path>.*)$', return_static, name='static'),
    # url(r'^403', permission_denied),
"""
