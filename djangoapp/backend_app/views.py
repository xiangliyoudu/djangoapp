from django.shortcuts import render, HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.

# 处理首页请求
def loginMain(req):
    #return HttpResponse('main page')
    return render(req, 'main.html')


