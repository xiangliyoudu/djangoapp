from django.conf.urls import include, url
from django.contrib import admin
# 导入backend_app 子路由
from backend_app import backend_urls as bu
from common_app import common_urls as cu

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangoapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #平台首页请求
    url(r'^index/$', include(cu)),

    # 子路由backend处理请求
    url(r'^backend/', include(bu)),

]
