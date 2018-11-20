from django.conf.urls import include, url
from django.contrib import admin
# 导入视图
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangoapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^main/$', views.loginMain, name='loginMain'),

    url(r'^app/list/$', views.listApp, name='listApp'),

    url(r'^categorylevellist.json/$', views.categorylevellistJson, name='categorylevellistJson'),


]
