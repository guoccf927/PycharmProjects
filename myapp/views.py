from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
from myapp.models import *

# Create your views here.


@login_required
def into_home(request):
    res = {}
    res['username'] = request.user.username
    res['hrefs'] = DB_href.objects.all()
    res['notices'] = DB_notice.objects.all()
    return render(request, 'home.html', res)


def into_login(request):
    return render(request, 'login.html', {})


def login_act(request):
    # 获取用户名 密码
    Uname = request.POST.get('Uname', None)
    Pwd = request.POST.get('Pwd', None)
    # 去用户表中查询这个用户名和密码 能找到的用户
    user = auth.authenticate(username=Uname, password=Pwd)
    if user is not None:
        # 登录成功
        auth.login(request, user)
        request.session['user'] = Uname
        return HttpResponseRedirect('/home')
    else:
        # 登录失败
        return HttpResponseRedirect('/accounts/login')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login')


def register_act(request):
    # 获取用户名 密码
    Uname = request.POST.get('Uname', None)
    Pwd = request.POST.get('Pwd', None)
    # 注册
    try:
        user = User.objects.create_user(username=Uname, password=Pwd)
        user.save()
        # 登录
        auth.login(request, user)
        request.session['user'] = Uname
        # 跳转到home页
        return HttpResponseRedirect('/home')
    except:
        for i in User.objects.all():
            if Uname in str(i):
                return HttpResponse(f'注册失败，{Uname} 用户名已经存在')
        else:
            return HttpResponse('注册失败，请重试')
