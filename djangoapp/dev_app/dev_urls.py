from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangoapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # 首页
    url(r'^login/$', views.getIndex, name='getIndex'),
    # 登录页面
    url(r'^dologin/$', views.dologin, name='dologin'),

    url(r'^app/list/$', views.appList, name='appList'),

    url(r'^app/appinfoadd/$', views.appInfoaAdd, name='appInfoaAdd'),
    # ajax get dataDictionaryList
    url(r'^datadictionarylist.json/$', views.dataDictionaryListJson, name='dataDictionaryListJson'),
    # check apk name if unique
    url(r'^apkexist.json/$', views.apkExistJson, name='apkExistJson'),
    # appinfo add save
    url(r'appinfoaddsave/$', views.appInfoAddSave, name='appInfoAddSave'),

]
