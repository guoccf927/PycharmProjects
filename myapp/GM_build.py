from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
from myapp.models import *
from myapp.ALL_VAR import *

# Create your views here.


def build(user_data, steps):
    # 声明最终返回值
    res = {}
    # 检查数据或打补丁
    if not user_data or steps == []:
        res['code'] = -1
        res['msg'] = '数据或步骤丢失'
        return res
    # 替换全局变量
    user_data = replace_user_data(user_data)

    # 把步骤骨架steps和用户数据user_data进行融合成可执行步骤
    


    # 返回最终结果
    res['code'] = 0
    res['msg'] = '构造成功'
    return res
