from django.conf.urls import include, url
from django.contrib import admin
# 导入视图
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangoapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$', views.userLogin, {'error': None}, name='userLogin'),
    url(r'^dologin/$', views.doUserLogin, name='doUserLogin'),

    # backend 首页
    url(r'^main/$', views.loginMain, name='loginMain'),
    # appList 页面
    url(r'^app/list/$', views.listApp, name='listApp'),
    # ajax获取二三级分类信息
    url(r'^categorylevellist.json/$', views.categorylevellistJson, name='categorylevellistJson'),
    # appInfo check显示页面
    url(r'^app/list/check/$', views.checkAppInfo, name='checkAppInfo'),
    # appInfo check提交页面
    url(r'^app/checksave/$', views.checkSave, name='checkSave'),



]
