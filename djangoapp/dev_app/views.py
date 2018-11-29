from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core import serializers
import os
from datetime import datetime

from djangoapp.backend_app.models import *

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

# appinfo list
def appList(req):
    PAGE_NUM = 5
    # 当前页码
    currentPageNo = 1
    # filter参数字典
    queryParmsDict = dict()
    # post 请求处理
    if req.POST:
        currentPageNo, queryParmsDict = listAppPost(req, currentPageNo, queryParmsDict)
    #查询app状态信息
    statusList = DataDictionary.objects.filter(typecode='APP_STATUS')
    # 查询app所有平台记录
    flatFormList = DataDictionary.objects.filter(typecode='APP_FLATFORM')
    # 查询一级分类记录
    categoryLevel1List = AppCategory.objects.filter(parentid=None)
    # 根据queryParmsDict，查询所有 appinfo
    appInfoList = AppInfo.objects.complex_filter(queryParmsDict)
    # AppInfoList关联查询
    for appInfo in appInfoList:
        getAppInfoRelatedModels(appInfo)
    # 分页信息
    paginator = Paginator(appInfoList, PAGE_NUM)
    currentPage = paginator
    # context dict
    cx = dict()
    cx['statusList'] = statusList
    cx['appInfoList'] = paginator.page(currentPageNo)
    cx['flatFormList'] = flatFormList
    cx['categoryLevel1List'] = categoryLevel1List
    cx['page'] = currentPage
    cx['currentPageNo'] = currentPageNo

    return render(req, 'dev_appList.html', context=cx)

# appInfo add
def appInfoaAdd(req):
    return render(req, 'appInfo_add.html')


# appinfo关联查询
def getAppInfoRelatedModels(appInfo):
    # 查询数据字典，获取平台名称
    valueId = appInfo.flatformid
    dataDictionary = DataDictionary.objects.filter(typecode='APP_FLATFORM').get(valueid=valueId)
    appInfo.flatformid = dataDictionary
    # 查询一级分类，获取分类名称
    level1Id = appInfo.categorylevel1
    appCategory1 = AppCategory.objects.get(id=level1Id)
    appInfo.categorylevel1 = appCategory1
    # 查询二级分类，获取分类名称
    level2Id = appInfo.categorylevel2
    appCategory2 = AppCategory.objects.get(id=level2Id)
    appInfo.categorylevel2 = appCategory2
    # 查询三级分类，获取分类名称
    level3Id = appInfo.categorylevel3
    appCategory3 = AppCategory.objects.get(id=level3Id)
    appInfo.categorylevel3 = appCategory3
    # 查询数据字典，获取app状态
    valueId = appInfo.status
    dataDictionary = DataDictionary.objects.filter(typecode='APP_STATUS').get(valueid=valueId)
    appInfo.status = dataDictionary
    # 查询app版本，获取最新版本信息
    versionId = appInfo.versionid
    try:
        appVersion = AppVersion.objects.get(id=versionId)
    except Exception as e:
        appVersion = '无'
    appInfo.versionid = appVersion

# applist Post 请求处理方法
def listAppPost(req, currentPageNo, queryParmsDict):
    # 获取当前页面
    currentPageNo = int(req.POST.get('pageIndex'))
    # 获取‘查询’表单参数，过滤None值，添加到queryParmsdict
    querySoftwareName = req.POST.get('querySoftwareName')
    queryParmsDict = filterNoneValue(queryParmsDict, 'softwarename', querySoftwareName)
    queryFlatformId = req.POST.get('queryFlatformId')
    queryParmsDict = filterNoneValue(queryParmsDict, 'flatformid', queryFlatformId)
    queryCategoryLevel1 = req.POST.get('queryCategoryLevel1')
    queryParmsDict = filterNoneValue(queryParmsDict, 'categorylevel1', queryCategoryLevel1)
    queryCategoryLevel2 = req.POST.get('queryCategoryLevel2')
    queryParmsDict = filterNoneValue(queryParmsDict, 'categorylevel2', queryCategoryLevel2)
    queryCategoryLevel3 = req.POST.get('queryCategoryLevel3')
    queryParmsDict = filterNoneValue(queryParmsDict, 'categorylevel3', queryCategoryLevel3)

    return currentPageNo, queryParmsDict

# 过滤dict中的None值
def filterNoneValue(dict, key, value):
    queryDict = dict

    if value:
        if not key == 'softwarename':
            value = int(value)
        dict[key] = value
    return queryDict

# 查询flatformlist，返回JsonResponse
def dataDictionaryListJson(req):
    typeCode = req.GET.get('tcode')
    # 查询app所有平台记录
    flatFormList = DataDictionary.objects.filter(typecode=typeCode)
    flatFormList = serializers.serialize('json', flatFormList, ensure_ascii=False)

    return JsonResponse(flatFormList, safe=False)

# 查询apkname是否已经存在
def apkExistJson(req):
    APKName = req.GET.get('APKName')
    try:
        appInfo = AppInfo.objects.get(apkname=APKName)
        APKName = 'exist'
    except Exception as e:
        APKName = 'noexist'
    # str类型变量，可以直接由JsonResponse转换为json
    return JsonResponse(APKName, safe=False)

# 保存appInfo到数据库
def appInfoAddSave(req):
    if req.POST:
        formPost = req.POST
        newAppInfo = AppInfo()
        # 获取表单数据，并赋值给newAppInfo
        newAppInfo.softwarename = formPost.get('softwareName')
        newAppInfo.apkname = formPost.get('APKName')
        newAppInfo.supportrom = formPost.get('supportROM')
        newAppInfo.interfacelanguage = formPost.get('interfaceLanguage')
        newAppInfo.softwaresize = int(formPost.get('softwareSize'))
        newAppInfo.downloads = int(formPost.get('downloads'))
        newAppInfo.flatformid = int(formPost.get('flatformId'))
        newAppInfo.categorylevel1 = int(formPost.get('categoryLevel1'))
        newAppInfo.categorylevel2 = int(formPost.get('categoryLevel2'))
        newAppInfo.categorylevel3 = int(formPost.get('categoryLevel3'))
        newAppInfo.status = int(formPost.get('status'))
        newAppInfo.appinfo = formPost.get('appInfo')
        # 获取上传图片对象
        logopicFile = req.FILES.get('a_logoPicPath')
        if not logopicFile:
            return HttpResponse('没有可上传的文件')

        try:
            # 保存上传的文件
            with open(os.path.join('E:', logopicFile.name), 'wb') as f:
                # 文件大小是否大雨2.5M
                chunkSize = logopicFile.multiple_chunks()
                # 小文件直接写入 logopicFile.read()
                if not chunkSize:
                    f.write(logopicFile.read())
                else:
                    # 大文件分块写入 chunks()
                    for chunk in logopicFile.chunks():
                        f.write(chunk)
        except Exception as e:
            fileUploadError = '文件上传失败'
            return HttpResponse('文件上传失败')

        # 文件上传路径
        UPLOADPATH = '/static/uploadfiles/'
        newAppInfo.logopicpath = os.path.join(UPLOADPATH, logopicFile.name)
        newAppInfo.logolocpath = UPLOADPATH
        # appinfo创建时间
        newAppInfo.creationdate = datetime.now()
        # save appInfo到db
        newAppInfo.save()

    return HttpResponse('appinfo saving...')
