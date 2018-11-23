from django.shortcuts import render, HttpResponse

from backend_app.models import *

# Create your views here.

# dev登录页面
def getIndex(req):
    return render(req, 'dev_login.html')

# 处理登录信息
def dologin(req):
    devName = req.POST.get('devCode')
    devPassword = req.POST.get('devPassword')
    # 验证登录信息
    error = None
    try:
        devUser = DevUser.objects.get(devcode=devName)
        if devUser.devpassword == devPassword:
            # 登录成功
            # 查询用户角色信息
            # 将username userrolename存入session
            req.session['devName'] = devUser.devname
            req.session['devCode'] = devUser.devcode
            return render(req, 'dev_main.html')
        else:
            error = '密码错误'
    except Exception as e:
        error = '用户不存在'
    # 登录失败
    cx = dict()
    cx['error'] = error
    return render(req, 'dev_login.html', context=cx)