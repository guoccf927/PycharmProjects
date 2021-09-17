from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
from myapp.models import *

# Create your views here.


# 获取构造步骤
def get_steps(tool_id, del_filter):
    # 获取全部步骤
    all_steps = DB_GM_steps.objects.filter(tool_id=tool_id)
    # 筛选步骤
    res_steps = []
    for i in all_steps:
        if i.filter_id not in del_filter:
            res_steps.append(i)
    return res_steps
