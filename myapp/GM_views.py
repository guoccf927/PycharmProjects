from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
from myapp.models import *
from myapp.GM_init import *
from myapp.GM_getSteps import *
from myapp.GM_build import *
import json
# Create your views here.


# 房源-进入页面
def house(request):
    # 带入初始化的数据
    res = {}
    res['address'] = Init_house_get_address()
    res['steps'] = DB_GM_steps.objects.filter(tool_id=1).order_by('order')
    return render(request, 'GM_tools/house.html', res)


# 房源-验证用户名密码
def house_check_user(request):
    username = request.GET['username']
    userpwd = request.GET['userpwd']
    res = Init_house_check_user(username, userpwd)
    return HttpResponse(json.dumps(res), content_type='application/json')


# 房源-构造
def house_run(request):
    # 把所有数据拿出来
    user_data = {}
    user_data["input_username"] = request.GET['input_username']
    user_data["input_userpwd"] = request.GET['input_userpwd']
    user_data["house_name"] = request.GET['house_name']
    user_data["house_price"] = request.GET['house_price']
    user_data["people_counts"] = request.GET['people_counts']
    user_data["furniture"] = request.GET['furniture']
    user_data["city"] = request.GET['city']
    user_data["country"] = request.GET['country']
    # 规范数据
    del_filter = []  # 需要删除的步骤过滤标记
    user_data["country"] = user_data["country"].lower()
    if user_data["country"] == 'china':
        del_filter.append('del_country')
    if user_data["city"] == '北京':
        del_filter.append('del_city')
    # 获取步骤
    steps = get_steps(tool_id=1, del_filter=del_filter)
    # 调用业务层真实构造
    res = build(user_data, steps)
    # 返回结果
    return HttpResponse(json.dumps(res), content_type='application/json')