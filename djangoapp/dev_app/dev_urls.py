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

    url(r'^app/list/$', views.appList, name='appList')


]
