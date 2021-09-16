from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
from myapp.models import *
from myapp.GM_init import *
import json
# Create your views here.


# 构造房源
def house(request):
    # 带入初始化的数据
    res = {}
    res['address'] = Init_house_get_address()
    return render(request, 'GM_tools/house.html', res)


# 验证用户名密码
def house_check_user(request):
    username = request.GET['username']
    userpwd = request.GET['userpwd']
    res = Init_house_check_user(username, userpwd)
    return HttpResponse(json.dumps(res), content_type='application/json')
