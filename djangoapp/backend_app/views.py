from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.core import serializers
from . import models
from django.core.paginator import Paginator

# Create your views here.

# 处理首页请求
def loginMain(req):
    #return HttpResponse('main page')
    return render(req, 'main.html')

# app管理请求
def listApp(req):
    PAGE_NUM = 2
    # current page num
    # 当前页码
    currentPageNo = 1
    # ‘查询’参数
    querySoftwareName = None
    queryFlatformId = None
    queryCategoryLevel1 = None
    queryCategoryLevel2 = None
    queryCategoryLevel3 = None
    # filter参数字典
    queryParmsDict = dict()

    if req.POST:
        # 获取当前页面
        currentPageNo = req.POST['pageIndex']
        # 获取‘查询’表单参数，过滤None值，添加到queryParmsdict
        querySoftwareName = req.POST['querySoftwareName']
        queryParmsDict = filterNoneValue(queryParmsDict, 'softwarename', querySoftwareName)
        queryFlatformId = req.POST['queryFlatformId']
        queryParmsDict = filterNoneValue(queryParmsDict, 'flatformid', queryFlatformId)
        queryCategoryLevel1 = req.POST['queryCategoryLevel1']
        queryParmsDict = filterNoneValue(queryParmsDict, 'categorylevel1', queryCategoryLevel1)
        queryCategoryLevel2 = req.POST['queryCategoryLevel2']
        queryParmsDict = filterNoneValue(queryParmsDict, 'categorylevel2', queryCategoryLevel2)
        queryCategoryLevel3 = req.POST['queryCategoryLevel3']
        queryParmsDict = filterNoneValue(queryParmsDict, 'categorylevel3', queryCategoryLevel3)


    # context dict
    cx = dict()
    # 查询app所有平台记录
    flatFormList = models.DataDictionary.objects.filter(typecode='APP_FLATFORM')
    # 查询一级分类记录
    categoryLevel1List = models.AppCategory.objects.filter(parentid=None)
    # 根据queryParmsDict，查询所有 appinfo
    appInfoList = models.AppInfo.objects.complex_filter(queryParmsDict)


    # AppInfoList关联查询
    for appInfo in appInfoList:
        # 查询数据字典，获取平台名称
        valueId = appInfo.flatformid
        dataDictionary = models.DataDictionary.objects.filter(typecode='APP_FLATFORM').get(valueid=valueId)
        appInfo.flatformid = dataDictionary
        # 查询一级分类，获取分类名称
        level1Id = appInfo.categorylevel1
        appCategory1 = models.AppCategory.objects.get(id=level1Id)
        appInfo.categorylevel1 = appCategory1
        # 查询二级分类，获取分类名称
        level2Id = appInfo.categorylevel2
        appCategory2 = models.AppCategory.objects.get(id=level2Id)
        appInfo.categorylevel2 = appCategory2
        # 查询三级分类，获取分类名称
        level3Id = appInfo.categorylevel3
        appCategory3 = models.AppCategory.objects.get(id=level3Id)
        appInfo.categorylevel3 = appCategory3
        # 查询数据字典，获取app状态
        valueId = appInfo.status
        dataDictionary = models.DataDictionary.objects.filter(typecode='APP_STATUS').get(valueid=valueId)
        appInfo.status = dataDictionary
        # 查询app版本，获取最新版本信息
        versionId = appInfo.versionid
        try:
            appVersion = models.AppVersion.objects.get(id=versionId)
        except Exception as e:
            appVersion = '无'
        appInfo.versionid = appVersion

    # 分页信息
    paginator = Paginator(appInfoList, PAGE_NUM)
    currentPage = paginator

    cx['appInfoList'] = paginator.page(currentPageNo)
    cx['flatFormList'] = flatFormList
    cx['categoryLevel1List'] = categoryLevel1List
    cx['page'] = currentPage
    cx['currentPageNo'] = currentPageNo

    return render(req, 'appList.html', context=cx)

# 二 三级分类ajax查询
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

# 过滤dict中的None值
def filterNoneValue(dict, key, value):
    queryDict = dict

    if value:
        if not key == 'softwarename':
            value = int(value)
        dict[key] = value
    return queryDict