from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
from myapp.models import *
import re
import time
# Create your views here.


def replace_user_data(user_data):
    for key in user_data.keys():
        # 根据#标志，找到目标替换文案
        if '#' in user_data[key]:
            # 通过正则表达式精确匹配到替换体
            pars = re.findall(r'#(.*?)#', user_data[key])
            for par in pars:
                code_par = DB_PAR.objects.filter(name=par)[0].code
                # 可执行文件，不可执行则打印出code源码
                try:
                    value = str(eval(code_par))
                except:
                    value = str(code_par)
                user_data[key] = user_data[key].replace(f"#{par}#", value)
    return user_data
