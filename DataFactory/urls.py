"""DataFactory URL Configuration

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
from django.contrib import admin
from django.urls import path
from myapp.views import *
from myapp.GM_views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', into_home),  # 进入首页
    path('accounts/login/', into_login),  # 进入登录页面
    path('login_act/', login_act),  # 登录
    path('logout/', logout),  # 注销
    path('register_act/', register_act),  # 注册
    path('add_href/', add_href),  # 首页添加超链接

    # 官方工具构造-房源构造-url
    path('GM_tools/house/', house),  # 进入房源构造
    path('GM_tools/house_check_user/', house_check_user),  # 验证用户名密码
    path('GM_tools/house_run/', house_run),  # 验证用户名密码
]
