from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

# 平台首页
def getIndex(req):
    return render(req, 'index.html')

# user logout
def logout(req):
    # 获取session中的值
    sessionItems = {}
    devName = req.session.get('devName')
    sessionItems['devName'] = devName
    devCode = req.session.get('devCode')
    sessionItems['devCode'] = devCode
    userName = req.session.get('userName')
    sessionItems['userName'] = userName
    userRoleName = req.session.get('userRoleName')
    sessionItems['userRoleName'] = userRoleName
    print('logout ....')
    # 删除session中的值
    for k, v in sessionItems.items():
        if v:
            del req.session[k]
    # 重定向到首页
    return HttpResponseRedirect(reverse('getIndex'))

