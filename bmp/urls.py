"""bmp URL Configuration

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
"""
# from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from .views import page_error, page_not_found, permission_denied
from bmpentry.BMPView import HomeView

urlpatterns = [
    # path('admin/', admin.site.urls),                              # 注销admin管理界面
    path('', HomeView.index),
    path('account/', include('bmpentry.BMPUrl.AccountUrl')),

    # url(r'^500', page_error),
    # url(r'^404', page_not_found),
    # url(r'^403', permission_denied),
]

# 定义错误跳转页面
# handler403 = permission_denied
# handler404 = page_not_found
# handler500 = page_error