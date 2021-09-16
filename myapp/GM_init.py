from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
from myapp.models import *
import requests
# Create your views here.

# 获取构造地址
def Init_house_get_address():
    # http请求
    return [{'name': '北京'}, {'name': '上海'}, {'name': '深圳'}]


# 房东账户验证
def Init_house_check_user(username, userpwd):
    # http请求
    # req = requests.get()
    if username == 'admin' and userpwd == '111111':
        return {'errCode': '0'}
    else:
        return {'errCode': '-1'}
