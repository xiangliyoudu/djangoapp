from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.core import serializers
from . import models
import json

# Create your views here.

# 处理首页请求
def loginMain(req):
    #return HttpResponse('main page')
    return render(req, 'main.html')

# app管理请求
def listApp(req):
    # return HttpResponse('applist page')
    cx = dict()
    # 查询app所有平台记录
    flatFormList = models.DataDictionary.objects.filter(typecode='APP_FLATFORM')
    # 查询一级分类记录
    categoryLevel1List = models.AppCategory.objects.filter(parentid=None)
    # 查询所有 appinfo
    appInfoList = models.AppInfo.objects.all()

    cx['appInfoList'] = appInfoList
    cx['flatFormList'] = flatFormList
    cx['categoryLevel1List'] = categoryLevel1List

    return render(req, 'appList.html', context=cx)

# 二三级分类ajax查询
def categorylevellistJson(req):
    # 根据一级、二级分类查询二、三级分类记录
    pid = req.GET.get('pid')
    # 获取queryset
    level23Set = models.AppCategory.objects.filter(parentid=pid)
    # 序列化为json
    level23Set = serializers.serialize('json', level23Set, ensure_ascii=False)
    # 参数字典
    # jsondata = dict()
    # jsondata['categoryLevel2List'] = level23Set
    return JsonResponse(level23Set, safe=False)
