from django.conf.urls import include, url
from django.contrib import admin
# 导入backend_app 子路由
from backend_app import backend_urls as bu

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangoapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # 子路由backend处理请求
    url(r'^backend/', include(bu)),

]
