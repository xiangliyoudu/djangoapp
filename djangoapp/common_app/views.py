from django.shortcuts import render

# Create your views here.

# 平台首页
def getIndex(req):
    return render(req, 'index.html')

