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
            return HttpResponse('dev logining ...')
        else:
            error = '密码错误'
    except Exception as e:
        error = '用户不存在'
    # 登录失败
    cx = dict()
    cx['error'] = error
    return render(req, 'dev_login.html', context=cx)